from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    # ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        # assert that the response code of 'incidents/escalators returns a 200 code
        assert escalator_response == 200, "escalator_response api failed"

        elevator_response = app.test_client().get('/incidents/elevators').status_code
        # assert that the response code of 'incidents/elevators returns a 200 code
        assert elevator_response == 200, "elevator_response api failed"

################################################################################

    # ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())
        for response in json_response:
            assert "StationCode" in response, "StationCode field is missing"
            assert "StationName" in response, "StationName field is missing"
            assert "UnitType" in response, "UnitType field is missing"
            assert "UnitName" in response, "UnitName field is missing"

        # for each incident in the JSON response assert that each of the required fields
        # are present in the response


################################################################################

    # ensure all entries returned by the /escalators endpoint have a UnitType of "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())
        for response in json_response:
            assert response['UnitType'] == 'ESCALATOR', "UnitType field does not match for ESCALATOR"

        # for each incident in the JSON response, assert that the 'UnitType' is "ESCALATOR"

################################################################################

    # ensure all entries returned by the /elevators endpoint have a UnitType of "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # for each incident in the JSON response, assert that the 'UnitType' is "ELEVATOR"
        for response in json_response:
            assert response['UnitType'] == 'ELEVATOR', "UnitType field does not match for ELEVATOR"


################################################################################

if __name__ == "__main__":
    unittest.main()