import requests
import json

def get_customer_by_name(ip_puerto, token, name):
    try:
        url = f'{ip_puerto}/api/tenant/customers?customerTitle={name}'
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Authorization": f"{token}"
        }
        response = requests.get(url, headers=headers)
        response_data = response.json()

        if response.status_code == 200 and "id" in response_data:
            return response_data["id"]["id"]
        elif response.status_code == 404:
            print(f"Customer not found: {response_data.get('message', 'Unknown error')}")
            return "13814000-1dd2-11b2-8080-808080808080"
    except Exception:
        return "13814000-1dd2-11b2-8080-808080808080"
    

    
     
