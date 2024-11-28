import requests
import time
import csv

def process_request(id, name, index):
    url = f"<API_URL>"
    headers = {
        "Authorization": "Bearer <TOKEN>",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json={"id": id, "name": name})

    with open('logs.txt', 'a') as file:
        if response.status_code == 200:
            print(f'{index} Successfull request for id {id}')
            file.write(f"{index} Successfull request for id {id}\n")
        else:
            print(f'{index} Request failed for id {id}: {response.text}')
            file.write(f"{index} Request failed for id {id}: {response.text}\n")

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
