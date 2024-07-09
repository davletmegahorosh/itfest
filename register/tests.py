import phonenumbers
import requests



def phone_number_check(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        return is_valid
    except phonenumbers.NumberParseException:
        return False



def check_email_existence(email):
    api_key = '498396a888e7f9bc2fb07092fb7615d724b15bd9'
    url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['data']['result'] == 'deliverable':
            return True
        else:
            return False
    else:
        return False
