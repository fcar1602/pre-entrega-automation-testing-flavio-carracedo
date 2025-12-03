import json
import logging

# This test covers a full user lifecycle against DummyJSON:
# create a user, update the user's last name, and delete the user.
# Note: Some DummyJSON endpoints are mocked and may not persist created IDs
# across update/delete operations. We log all steps for debugging.

def test_full_user_flow(api, fake, caplog):
    caplog.set_level(logging.INFO)

    # Step 1: Create a new user
    user = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "age": fake.random_int(min=18, max=70)
    }
    logging.info("Creating user payload: %s", json.dumps(user))

    # Send POST to create the user
    create_res = api.add_user(user)
    logging.info("POST /users status=%s", create_res.status_code)
    assert create_res.status_code == 201
    created = create_res.json()
    logging.info("USER CREATED:\n%s", json.dumps(created, indent=4))

    # Use a known ID compatible with update/delete endpoints
    # (DummyJSON may not allow updating freshly created IDs)
    real_user_id = 5
    logging.info("Using user id=%s for update/delete", real_user_id)

    # Step 2: Update user's lastName
    new_lastname = fake.last_name()
    logging.info("Updating lastName -> %s", new_lastname)
    update_res = api.update_user(real_user_id, {"lastName": new_lastname})
    logging.info("PUT /users/%s status=%s", real_user_id, update_res.status_code)

    # Verify update succeeded
    assert update_res.status_code == 200
    updated = update_res.json()
    logging.info("USER UPDATED:\n%s", json.dumps(updated, indent=4))

    # Validate lastName change took effect
    assert updated["lastName"] == new_lastname

    # Step 3: Delete the user
    delete_res = api.delete_user(real_user_id)
    logging.info("DELETE /users/%s status=%s", real_user_id, delete_res.status_code)
    assert delete_res.status_code == 200

    # Log delete response body for completeness
    logging.info("USER DELETED:\n%s", json.dumps(delete_res.json(), indent=4))
