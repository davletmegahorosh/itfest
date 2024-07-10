from .tests import phone_number_check, check_email_existence
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'cred.json'
spreadsheet_design = '1egOuiTuxZPPXV4gVOgMpSVLX1fLbmn-N6gM8FLn1-Qo'
range_name = 'A:K'




credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http=httpAuth)


class CyberSportRegistrationAPIView(APIView):
    serializer_class = CyberSportSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            print(request.data.get('Name'))
            new_values = [[
                    request.data.get('Surname'),
                    request.data.get('Name'),
                    request.data.get('FatherName'),
                    request.data.get('Email'),
                    request.data.get('Country'),
                    request.data.get('City'),
                    request.data.get('DateOfBirth'),
                    request.data.get('PhoneNumber'),
                    request.data.get('Game'),
                    request.data.get('ParticipateFormat')]
            ]
            print(new_values)

            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='cyber', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = CyberSportSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response


class HackathonRegistrationAPIView(APIView):
    serializer_class = HackathonSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            new_values = [
                [
                    request.data.get('Name', ''),
                    request.data.get('Surname', ''),
                    request.data.get('FatherName', ''),
                    request.data.get('Email', ''),
                    request.data.get('Country', ''),
                    request.data.get('City', ''),
                    request.data.get('DateOfBirth', ''),
                    request.data.get('PhoneNumber', ''),
                    request.data.get('course', '')
                ]
            ]

            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='hackathon', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = HackathonSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response



class DesignRegistrationAPIView(APIView):
    serializer_class = DesignSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            new_values = [
                [
                    request.data.get('Name', ''),
                    request.data.get('Surname', ''),
                    request.data.get('FatherName', ''),
                    request.data.get('Email', ''),
                    request.data.get('Country', ''),
                    request.data.get('City', ''),
                    request.data.get('DateOfBirth', ''),
                    request.data.get('PhoneNumber', ''),
                    request.data.get('course', '')
                ]
            ]

            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='design', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = CyberSportSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response


class MobilographyRegistrationAPIView(APIView):
    serializer_class = MobilographySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            new_values = [
                [
                    request.data.get('Name', ''),
                    request.data.get('Surname', ''),
                    request.data.get('FatherName', ''),
                    request.data.get('Email', ''),
                    request.data.get('Country', ''),
                    request.data.get('City', ''),
                    request.data.get('DateOfBirth', ''),
                    request.data.get('PhoneNumber', ''),
                ]
            ]

            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='mobilography', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = CyberSportSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response

class RobotixRegistrationAPIView(APIView):
    serializer_class = RobotixSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            new_values = [
                [
                    request.data.get('Name', ''),
                    request.data.get('Surname', ''),
                    request.data.get('FatherName', ''),
                    request.data.get('Email', ''),
                    request.data.get('Country', ''),
                    request.data.get('City', ''),
                    request.data.get('DateOfBirth', ''),
                    request.data.get('PhoneNumber', ''),
                ]
            ]

            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='robotix', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = CyberSportSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response

class DroneRaceRegistrationAPIView(APIView):
    serializer_class = DroneRaceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            new_values = [
                [
                    request.data.get('Name', ''),
                    request.data.get('Surname', ''),
                    request.data.get('FatherName', ''),
                    request.data.get('Email', ''),
                    request.data.get('Country', ''),
                    request.data.get('City', ''),
                    request.data.get('DateOfBirth', ''),
                    request.data.get('PhoneNumber', ''),
                ]
            ]

            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='drone', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = CyberSportSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response

class SpeakerRegistrationAPIView(APIView):
    serializer_class = SpeakerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            new_values = [
                [
                    request.data.get('Name', ''),
                    request.data.get('Surname', ''),
                    request.data.get('FatherName', ''),
                    request.data.get('Email', ''),
                    request.data.get('Country', ''),
                    request.data.get('City', ''),
                    request.data.get('DateOfBirth', ''),
                    request.data.get('PhoneNumber', ''),
                    request.data.get('speech_theme', ''),
                ]
            ]

            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='speaker', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = CyberSportSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response

class MasterClassRegistrationAPIView(APIView):
    serializer_class = MasterClassSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            new_values = [
                [
                    request.data.get('Name', ''),
                    request.data.get('Surname', ''),
                    request.data.get('FatherName', ''),
                    request.data.get('Email', ''),
                    request.data.get('Country', ''),
                    request.data.get('City', ''),
                    request.data.get('DateOfBirth', ''),
                    request.data.get('PhoneNumber', ''),
                    request.data.get('speech_theme', ''),
                ]
            ]
            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='master_class', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                response_serializer = CyberSportSerializer(serializer.instance)
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:K'
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name
        ).execute()
        values_in_sheet = result.get('values', [])
        row_index = len(values_in_sheet) + 1  # Calculate the next available row index

        # Append new data
        response = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="USER_ENTERED",
            body={
                "values": values
            }
        ).execute()

        return response

class PhoneNumCheck(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')  # Assuming phone_number is passed in POST data

        if not phone_number:
            return Response({"error": "Phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        is_valid = phone_number_check(phone_number)

        if is_valid:
            return Response({"valid": True}, status=status.HTTP_200_OK)
        else:
            return Response({"valid": False}, status=status.HTTP_200_OK)


class EmailCheck(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        is_valid = check_email_existence(email)

        response_data = {
            "email": email,
            "valid": is_valid
        }

        return Response(response_data, status=status.HTTP_200_OK)