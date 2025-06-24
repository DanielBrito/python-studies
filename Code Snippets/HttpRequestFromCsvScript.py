import requests
import time
import csv
from loguru import logger

def get_access_token(username, password):
    url = f"<AUTH_URL>"
    headers = {'Content-Type': 'application/json'}
    data = {
        "username": username,
        "password": password
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json().get('access_token')
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to get access token: {e}")
        return None
    

def process_request(id, name, index):
    url = f"<API_URL>"
    token = get_access_token("username", "password")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    with open('logs.txt', 'a') as file:
        try:
            response = requests.post(url, headers=headers, json={"id": id, "name": name})
            response.raise_for_status()
            
            logger.info(f"Successfull request for id {id}")
            file.write(f"Successfull request for id {id}\n")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed for id {id}: {e}")
            file.write(f"Request failed for id {id}: {e}\n")
            return None

def main():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)

    next(reader)
    
    data = [[row[0], row[1]] for row in reader]
    index = 1

    for id, name in data:
        process_request(id, name, index)
        index += 1
        time.sleep(1)

if __name__ == '__main__':
    main()
