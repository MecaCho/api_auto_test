
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


def set_get_aksk_by_service_token_body(project_id, domain_id):
    post_dict = {
                "auth": {
                    "identity": {
                        "method": [
                            "assume_role"
                        ],
                        "assume_role": {
                            "domain_id": domain_id,
                            "xrole_name": "ief_admin_trust",
                            "duration-seconds": 600
                        }
                    },
                    "scope": {
                        "project": {
                            "id": project_id
                        }
                    }
                }
            }
    return post_dict

