import requests
import json
from requests.exceptions import ConnectionError


def api_get_request(referral_id):
    """function to make GET request"""
    try:
        response = requests.get(f'http://127.0.0.1:8000/'
                                f'refferal_link/{referral_id}/')
    except ConnectionError:
        return False

    if response.status_code == 200:  # checking if instance exists
        data = response.content.decode('utf-8')
        refferal_data = json.loads(data)
        return refferal_data
    return False


def api_delete_request(referral_id):
    """function to make DELETE request"""
    try:
        delete_response = requests.delete(f'http://127.0.0.1:8000/'
                                          f'refferal_link/{referral_id}/')
    except ConnectionError:
        return False

    if not delete_response.status_code == 204:  # checking for eny errors
        return False

    return True
