import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "c3c11c825b254ed5adeb8321b2c05c4a"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_ty>", methods=["GET"])

def get_incidents(unit_ty):
  # create an empty list called 'incidents'
    incidents = []
    if unit_ty.upper() not in ["ESCALATORS", "ELEVATORS"]:
        print(f"Error: Invalid unit type: {unit_ty}")
        return "{}"
  # use 'requests' to do a GET request to the WMATA Incidents API
    response = requests.get(INCIDENTS_URL, headers=headers)

  # retrieve the JSON from the response
    if response.status_code == 200:
        response_json = response.json()
        StationIncidents = response_json["ElevatorIncidents"]

        # iterate through the JSON response and retrieve all incidents matching 'unit_type'
        for incident in StationIncidents:
            if incident["UnitType"].upper()+"S" == unit_ty.upper():
                incidents.append({"UnitType": incident["UnitType"], "UnitName": incident["UnitName"],
                "StationName": incident["StationName"], "StationCode": incident["StationCode"]})
        return json.dumps(incidents)
    else:
        print(f"Error: {response.status_code}")

#
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition


  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list

  # return the list of incident dictionaries using json.dumps()


if __name__ == '__main__':
    app.run(debug=True)

