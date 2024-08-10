import requests

def get_new_token():
    token_endpoint = 'https://api.angelcam.com/oauth/token/'
    client_id = 'XU0aXeP1299oS48KnZmxhqWUR928jsmFKosdrfMS'
    client_secret = 'your_client_secret'  # Substitua pelo seu client secret
    refresh_token = 'your_refresh_token'  # Substitua pelo seu refresh token

    payload = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }

    try:
        response = requests.post(token_endpoint, data=payload)
        response.raise_for_status()
        token_data = response.json()
        return token_data['access_token']
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining token: {e}")
        return None
