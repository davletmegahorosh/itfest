from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .serializers import FoodZoneSerializer, ITExpoSerializer

CREDENTIALS_FILE = 'cred.json'
spreadsheet_design = '1egOuiTuxZPPXV4gVOgMpSVLX1fLbmn-N6gM8FLn1-Qo'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http=httpAuth)

class FoodZoneRegistrationAPIView(APIView):
    serializer_class = FoodZoneSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            logo = request.FILES.get('Logo')
            if logo:
                logo_path = default_storage.save(f'logos/{logo.name}', ContentFile(logo.read()))
                logo_url = request.build_absolute_uri(f'{settings.MEDIA_URL}{logo_path}')
            else:
                logo_url = None

            register_check = request.FILES.get('Register_check')
            if register_check:
                register_check_path = default_storage.save(f'register_checks/{register_check.name}', ContentFile(register_check.read()))
                register_check_url = request.build_absolute_uri(f'{settings.MEDIA_URL}{register_check_path}')
            else:
                register_check_url = None

            new_values = [[
                request.data.get('Brand_name'),
                request.data.get('Legal_name'),
                request.data.get('Legal_address'),
                request.data.get('INN'),
                request.data.get('Supervisor_Name'),
                request.data.get('Job_Title'),
                request.data.get('Company_Activity'),
                request.data.get('Web_Site'),
                request.data.get('Email'),
                request.data.get('Country'),
                request.data.get('Company_Product'),
                logo_url,
                register_check_url,
            ]]
            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='food', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:N'
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


class ITExpoRegistrationAPIView(APIView):
    serializer_class = ITExpoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            logo = request.FILES.get('Logo')
            if logo:
                logo_path = default_storage.save(f'logos/{logo.name}', ContentFile(logo.read()))
                logo_url = request.build_absolute_uri(f'{settings.MEDIA_URL}{logo_path}')
            else:
                logo_url = None

            register_check = request.FILES.get('Register_check')
            if register_check:
                register_check_path = default_storage.save(f'register_checks/{register_check.name}', ContentFile(register_check.read()))
                register_check_url = request.build_absolute_uri(f'{settings.MEDIA_URL}{register_check_path}')
            else:
                register_check_url = None

            new_values = [[
                request.data.get('Brand_name'),
                request.data.get('Legal_name'),
                request.data.get('Legal_address'),
                request.data.get('INN'),
                request.data.get('Supervisor_Name'),
                request.data.get('Job_Title'),
                request.data.get('Company_Activity'),
                request.data.get('Web_Site'),
                request.data.get('Email'),
                request.data.get('Country'),
                request.data.get('Theme'),
                request.data.get('Company_Product'),
                logo_url,
                register_check_url,
            ]]
            response = self.append_to_spreadsheet(spreadsheet_id=spreadsheet_design, sheet_name='expo', values=new_values)

            if 'updates' in response and 'updatedRows' in response['updates']:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Failed to add data to Google Sheets"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def append_to_spreadsheet(self, spreadsheet_id, sheet_name, values):
        range_name = f'{sheet_name}!A:N'
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
