data_login = [
    ("standard_user", "secret_sauce", True),            # valid
    ("locked_out_user", "secret_sauce", False),          # locked user
    ("invalid_user", "secret_sauce", False),             # non-existent user
    ("standard_user", "wrong_pass", False),              # wrong password
]

valid_login = [(u, p) for (u, p, ok) in data_login if ok]
invalid_login = [(u, p) for (u, p, ok) in data_login if not ok]