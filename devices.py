import json
import requests
import customers


def create_devices(ip_puerto, token, datos):
    for index, row in datos.iterrows():
       cliente_id = customers.get_customer_by_name(ip_puerto, token, row["cliente"])
       print(ip_puerto)
       create_device(ip_puerto, row["nombre"], token, row["type"], cliente_id, row["accessToken"], row["label"])


def create_device(ip_puerto, name, token, type_profile, id_client, accessToken, label):
    try:
        url = f'{ip_puerto}/api/device?accessToken={accessToken}'

        post_data = {
            "customerId": {
                "id": id_client,
                "entityType": "CUSTOMER"
            },
            "name": name,
            "type": type_profile,
            "label": label,
            "additionalInfo": {}
        }
        post_data_json = json.dumps(post_data)

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Authorization": f"{token}"
        }
        response = requests.post(url, headers=headers, data=post_data_json)
        response_data = response.json()

    
        if response.status_code in range(200, 300):
            print(f"El dispositivo {name} se creo correctamente")
            return response_data
        
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")