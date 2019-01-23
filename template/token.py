
def set_get_token_projectid_body(usr, pwd, project_id):
    user_token = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": usr,
                        "password": pwd,
                        "domain": {
                            "name": usr
                        }
                    }
                }
            },
            "scope": {
                "project": {
                    "id": project_id
                }
            }
        }
    }
    return user_token
