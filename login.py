import requests
import json

def login(base_url, name, password):
    try:
        url = f'{base_url}/api/auth/login'
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        json_data = json.dumps({"username": name, "password": password})
        response = requests.post(url, headers=headers, data=json_data)


        if response.status_code == 200:
            return_data = response.json()  
            token = f'Bearer {return_data["token"]}'
            return token
        else:
            error_message = response.json().get("message", "Error desconocido")
            raise ValueError(f"Error al iniciar sesión: {error_message} (Código HTTP {response.status_code})")
    
    except Exception as e:
        raise RuntimeError(f"Ha ocurrido un error inesperado: {e}")


