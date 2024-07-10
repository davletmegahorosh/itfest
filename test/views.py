from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Members
import httplib2
from googleapiclient.discovery import build
from .serializers import MembersSerializer, MembersActivationSerializer, ActiveMembersSerializer

from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1xcZlQmnifvOg-kf-BSqwH401HmY5p1oATPiH18U2bfM'
range_name = 'A:K'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http = httpAuth)

result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range=range_name
).execute()

values = result.get('values', [])

row_index = len(values) + 1
class MembersRegistrationAPIView(APIView):
    serializer_class = MembersSerializer


    def post(self, request, *args, **kwargs):
        serializer = MembersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(request.data)
            member = serializer.save()

            # member = Members.objects.get(id=1)  # Получаем экземпляр модели
            # json_data = member.to_json()  # Преобразуем в JSON
            # print(json_data)


            range_ = "A1:G1"
            new_range = f'A{row_index}:G{row_index}'
            response = service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=new_range,
                valueInputOption="USER_ENTERED",
                body={
                    "values": [[request.data['name'], request.data['surname'], request.data['age'],request.data['email'],request.data['profession'],request.data['section']]]
                }
            ).execute()

            if 'updatedCells' in response:
                # send_activation_email(member.email, member.confirmation_code)
                response_serializer = MembersSerializer(member)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MembersActivationAPIView(APIView):
    serializer_class = MembersActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = MembersActivationSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.validated_data['member']
            member.accepted = True
            member.save()
            return Response({"detail": "Account activated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        email = request.GET.get('email')

        user = get_object_or_404(Members, email=email, confirmation_code=code)

        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response({"detail": "Account activated successfully."}, status=status.HTTP_200_OK)


class ActiveMembersListView(generics.ListAPIView):
    queryset = Members.objects.filter(is_active=True)
    serializer_class = ActiveMembersSerializer