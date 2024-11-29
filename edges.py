import json
import requests
import uuid
import base64
import secrets
import customers

def create_edges(ip_puerto, token, datos):
    for index, row in datos.iterrows():
       cliente_id = customers.get_customer_by_name(ip_puerto, token, row["cliente"])
       create_edge(ip_puerto, row["nombre"], token, row["type"], cliente_id, row["label"])

def generate_secret_key(length=22):
    uuid_timestamp = uuid.uuid1()
    random_bytes = secrets.token_bytes(length)
    base32_key = base64.b32encode(random_bytes).decode('utf-8').rstrip('=')
    return str(uuid_timestamp), base32_key[:length]

def create_edge(base_url, name, token, type_profile, id_customer, label):
    url = f'{base_url}/api/edge'
    secret, key = generate_secret_key()
    post_data = f'''{{
                    "customerId": {{
                        "id": "{id_customer}",
                        "entityType": "CUSTOMER"
                    }},
                    "name": "{name}",
                    "type": "{type_profile}",
                    "label": "{label}",
                    "routingKey": "{key}",
                    "secret": "{secret}"
                }}
    '''
    headers = {"Content-Type": "application/json", "Accept": "application/json", "X-Authorization": f"{token}"}
    x = requests.post(url, headers=headers, data=post_data)
    return json.loads(x.text)