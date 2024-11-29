import json
import requests
import customers

def create_assets(ip_puerto, token, datos):
    for index, row in datos.iterrows():
       print(row)
       cliente_id = customers.get_customer_by_name(ip_puerto, token, row["cliente"])
       create_asset(ip_puerto, row["nombre"], token, row["type"], cliente_id, row["label"])

def create_asset(base_url, name, token, type_profile, id_client, label):
    try:
        url = f'{base_url}/api/asset'

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
            print(f"El activo {name} se creo correctamente")
            return response_data
        else:
            print(response_data)
        
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")