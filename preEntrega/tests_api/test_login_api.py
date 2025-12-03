import json
import logging

# This test verifies the login flow against DummyJSON and
# then fetches the authenticated profile using the access token.

def test_login_and_get_profile(api, caplog):
    caplog.set_level(logging.INFO)

    # Step 1: Login and obtain access token
    login_payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }
    logging.info("Login payload: %s", json.dumps(login_payload))

    # Send the login request to the API
    login_response = api.post("/auth/login", json=login_payload)
    logging.info("POST /auth/login status=%s", login_response.status_code)

    # Verify login was successful
    assert login_response.status_code == 200

    login_json = login_response.json()
    logging.info("LOGIN RESPONSE:\n%s", json.dumps(login_json, indent=4))

    # Basic assertions: token fields must be present
    assert "accessToken" in login_json
    assert "refreshToken" in login_json

    # Access token will be used to call /auth/me
    access_token = login_json["accessToken"]
    logging.info("Access token obtained: %s...", access_token[:12])

    # Step 2: Get profile using the access token
    # The APIClient sets Authorization header automatically after login
    profile_response = api.get("/auth/me")
    logging.info("GET /auth/me status=%s", profile_response.status_code)

    # Verify the profile endpoint was successful
    assert profile_response.status_code == 200

    profile_json = profile_response.json()
    logging.info("PROFILE RESPONSE:\n%s", json.dumps(profile_json, indent=4))

    # Validate profile fields match login response
    assert profile_json["id"] == login_json["id"]
    assert profile_json["username"] == "emilys"
    assert profile_json["email"] == login_json["email"]

    logging.info("TEST COMPLETED SUCCESSFULLY")
