import requests
import csv
import random
from datetime import datetime
import time

# Function to write aircraft data to CSV
def data_to_csv(data, filename, type):
    file_path = f"{filename}.csv"
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for datai in data:
            writer.writerow([f"{type}", *datai])
        if data == []:
            writer.writerow([f"{type}", "null", "null", "null", "null", "null", "null", "null"])  
    print(f"Les données ont été écrites dans {file_path}.")

# Function to fetch aircraft data
def get_data(lat, lon):  
    url = "https://flight-radar1.p.rapidapi.com/flights/list-in-boundary"
    querystring = {"bl_lat": "12.9278", "bl_lng": "-65.0011", "tr_lat": "19.6016", "tr_lng": "-58.0489", "limit": "300"}
    headers = {
        "x-rapidapi-key": "ed9a81357bmshc5c853403e14a94p1e1cb2jsn27465cfa38f3",
        "x-rapidapi-host": "flight-radar1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json().get("aircraft", [])
    if data is None:
        data = []
    return select_data(data)

# Function to select relevant data from the aircraft response
def select_data(data):
    data_selected = []
    for datai in data:
        for i in range(len(datai)):
            if datai[i] == "":
                datai[i] = "N/A"
        data_selected.append([datai[1], datai[10], datai[2], datai[3], datai[5], datai[6], datai[9], datai[11]])
    return data_selected

# Sensor definitions: fixed values for Start, Latitude, Longitude, and Code
sensors = [
    {"Start": "S", "Latitude": 16.2659, "Longitude": -60.924, "Code": "Z46MH"},
    {"Start": "S", "Latitude": 16.0186, "Longitude": -62.1204, "Code": "N12NY"},
    {"Start": "S", "Latitude": 15.8964, "Longitude": -60.5246, "Code": "L89CA"},
    {"Start": "S", "Latitude": 16.4265, "Longitude": -60.9873, "Code": "L56LD"},
    {"Start": "S", "Latitude": 16.3249, "Longitude": -60.412, "Code": "T78TK"},
    {"Start": "S", "Latitude": 16.5262, "Longitude": -61.5054, "Code": "A12BC"},
    {"Start": "S", "Latitude": 16.3482, "Longitude": -61.3523, "Code": "C34DE"},
    {"Start": "S", "Latitude": 16.028, "Longitude": -61.0179, "Code": "E56FG"},
    {"Start": "S", "Latitude": 15.8025, "Longitude": -61.2563, "Code": "G78HI"},
    {"Start": "S", "Latitude": 16.2786, "Longitude": -61.8247, "Code": "I90JK"},
    {"Start": "S", "Latitude": 16.421, "Longitude": -61.824, "Code": "K12LM"},
    {"Start": "S", "Latitude": 15.9038, "Longitude": -60.8042, "Code": "M34NO"},
    {"Start": "S", "Latitude": 16.642, "Longitude": -61.4425, "Code": "O56PQ"},
    {"Start": "S", "Latitude": 16.3736, "Longitude": -60.9356, "Code": "S90TU"},
    {"Start": "S", "Latitude": 15.7487, "Longitude": -61.154, "Code": "U12VW"},
    {"Start": "S", "Latitude": 16.7257, "Longitude": -61.6404, "Code": "W34XY"},
    {"Start": "S", "Latitude": 16.1626, "Longitude": -61.3536, "Code": "Y56ZA"},
    {"Start": "S", "Latitude": 16.0002, "Longitude": -61.2785, "Code": "B78CD"},
    {"Start": "S", "Latitude": 16.8156, "Longitude": -61.5402, "Code": "D90EF"}
]

# Function to generate a random number between 30 and 50
def generate_random_number():
    return random.randint(30, 50)

# Function to write the latest data for all sensors
def write_latest_data():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sensors.csv", mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for sensor in sensors:
            row = [
                sensor["Start"],
                sensor["Latitude"],
                sensor["Longitude"],
                sensor["Code"],
                generate_random_number(),
                timestamp
            ]
            writer.writerow(row)

# Main execution
if __name__ == "__main__":
    lat = "16.2647"
    lon = '-61.5250'
   
    # Generate aircraft data
    aircraft_data = get_data(lat, lon)
    data_to_csv(aircraft_data, "aircrafts", "A")
   
    # Generate sensor data
    write_latest_data()
    print("Latest sensor data written to sensors.csv.")