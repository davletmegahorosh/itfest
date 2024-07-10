from rest_framework import serializers
from .models import Members
from section.models import Sections
from members.email import check_email_existence


class MembersSerializer(serializers.ModelSerializer):
    section = serializers.CharField(max_length=225)

    class Meta:
        model = Members
        fields = ['name', 'email', 'section', 'surname', 'age', 'profession', 'phone']

    def validate(self, data):
        errors = {}

        if Members.objects.filter(email=data['email']).exists():
            errors['email'] = "A member with this email already exists."

        elif not check_email_existence(data['email']):
            errors['email'] = "This email does not exists"

        section_name = data.get('section')
        try:
            Sections.objects.get(name=section_name)
        except Sections.DoesNotExist:
            errors['section'] = "Invalid section name."

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def create(self, validated_data):
        section_name = validated_data.pop('section', None)

        try:
            section = Sections.objects.get(name=section_name)
        except Sections.DoesNotExist:
            raise serializers.ValidationError("Invalid section name.")

        validated_data['section'] = section
        member = Members.objects.create(**validated_data)
        return member

    def to_representation(self, instance):
        return {
            'email': instance.email,
            'confirmation_code': instance.confirmation_code
        }

    def is_valid(self, raise_exception=False):
        try:
            super(MembersSerializer, self).is_valid(raise_exception=True)
        except serializers.ValidationError as exc:
            errors = exc.detail
            if len(errors) == 1:
                key = list(errors.keys())[0]
                detail = {key: errors[key]}
            else:
                detail = errors
            if raise_exception:
                raise serializers.ValidationError(detail)
            return False
        return True


class MembersActivationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.IntegerField()


    def validate(self, data):
        email = data.get('email')
        confirmation_code = data.get('confirmation_code')

        try:
            member = Members.objects.get(email=email, confirmation_code=confirmation_code)
        except Members.DoesNotExist:
            raise serializers.ValidationError("Invalid email or confirmation code.")

        data['member'] = member
        return data


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = ['name']


class ActiveMembersSerializer(serializers.ModelSerializer):
    section = SectionsSerializer()

    class Meta:
        model = Members
        fields = ['name', 'email', 'section']
