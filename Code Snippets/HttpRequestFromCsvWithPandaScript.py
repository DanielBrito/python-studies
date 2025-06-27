from typing import List, Tuple
import requests
from loguru import logger
import pandas as pd

## This script process a CSV file with the following structure:

# id,name
# 1,Daniel

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

def get_values_from_csv(file: str) -> List[Tuple[str, str]]:
    data_frame = pd.read_csv(file)
    values = list(data_frame[['id', 'name']].itertuples(index=False, name=None))

    logger.info(f"There are {len(values)} registries to be processed")

    return values

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
            
            logger.info(f"{index}: Successfull request for id {id}")
            file.write(f"{index}: Successfull request for id {id}\n")
        except requests.exceptions.RequestException as e:
            logger.error(f"{index}: Request failed for id {id}: {e}")
            file.write(f"{index}: Request failed for id {id}: {e}\n")

            return None

def main():
  users = get_values_from_csv('users.csv')
  
  for index, (id, name) in enumerate(users):
    process_request(id, name, index + 1)

if __name__ == '__main__':
    main()
