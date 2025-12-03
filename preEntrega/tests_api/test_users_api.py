import json
import logging

# This test logs in first to obtain a Bearer token and
# then calls the authenticated endpoint /user/me to verify user details.

def test_get_user_me(api, caplog):
    caplog.set_level(logging.INFO)

    # Step 1: Login first (APIClient stores the Bearer token)
    login_data = api.login("emilys", "emilyspass")
    logging.info("LOGIN RESPONSE:\n%s", json.dumps(login_data, indent=4))

    # Step 2: Call /user/me with Bearer Token automatically set in headers
    response = api.get_me()
    logging.info("GET /auth/me status=%s", response.status_code)

    assert response.status_code == 200

    user_data = response.json()
    logging.info("USER/ME RESPONSE:\n%s", json.dumps(user_data, indent=4))

    # Step 3: Validations - the returned profile must match login data
    logging.info(
        "Validating user matches: id=%s username=%s email=%s",
        login_data.get("id"), login_data.get("username"), login_data.get("email")
    )
    assert user_data["id"] == login_data["id"]
    assert user_data["username"] == login_data["username"]
    assert user_data["email"] == login_data["email"]

    logging.info("TEST COMPLETED SUCCESSFULLY")
