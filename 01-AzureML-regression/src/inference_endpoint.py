import urllib.request
import json

# Request data must match the MLmodel signature
# Based on the model signature, all 13 fields are required:
# Path, name, year, km_driven, fuel, seller_type, transmission, owner,
# mileage, engine, max_power, torque, seats
data = {
    "input_data": {
        "columns": [
            "Path", "name", "year", "km_driven", "fuel", "seller_type",
            "transmission", "owner", "mileage", "engine", "max_power",
            "torque", "seats"
        ],
        "index": [0, 1],
        "data": [
            [
                "path/to/car1", "Maruti Swift", 2015, 50000, "Petrol",
                "Individual", "Manual", "First Owner", "19.1 kmpl",
                "1197 CC", "81.80 bhp", "113Nm@ 4200rpm", 5.0
            ],
            [
                "path/to/car2", "Hyundai Creta", 2020, 15000, "Diesel",
                "Dealer", "Automatic", "First Owner", "21.4 kmpl",
                "1493 CC", "113.4 bhp", "250Nm@ 1500-2750rpm", 5.0
            ]
        ]
    }
}

body = str.encode(json.dumps(data))

url = 'https://tech901-workspace-zujbb.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = '9oiDdkeEGfvtOy70zt3oYa0KWPHIrYLyufPycKy4TlWHrTYEvhMNJQQJ99CAAAAAAAAAAAAAINFRAZML11i1'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Accept': 'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))