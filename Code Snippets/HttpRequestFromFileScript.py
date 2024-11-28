import requests
import time

def process_request(id, index):
    url = f"<API_URL>"
    headers = {
        "Authorization": "Bearer <TOKEN>",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json={"id": id})

    with open('logs.txt', 'a') as file:
        if response.status_code == 200:
            print(f'{index} Successfull request for id {id}')
            file.write(f"{index} Successfull request for id {id}\n")
        else:
            print(f'{index} Request failed for id {id}: {response.text}')
            file.write(f"{index} Request failed for id {id}: {response.text}\n")

def main():
    with open('ids.txt', 'r') as file:
        ids = file.readlines()

    ids = [id.strip() for id in ids]

    for index, id in enumerate(ids):
        process_request(id, index + 1)
        time.sleep(1)

if __name__ == '__main__':
    main()
