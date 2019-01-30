# -*-coding=UTF-8-*-
import time
import os
import requests
from req import common_request
from template.token import set_get_token_projectid_body
import json

BASEURL = "https://iam.cn-north-1.myhuaweicloud.com/v3/auth/tokens"
URI = BASEURL + ""


class Client_(object):
    def __init__(self, usr, pwd, project_id):
        self.usr = usr
        self.pwd = pwd
        self.project_id = project_id
        self.headers = {"Content-Type": "application/json"}

    def get_service_token(self):
        file_path = os.path.dirname(os.path.abspath(__file__))
        token_file = file_path + "/" + self.usr + ".cert"
        if os.path.exists(token_file):
            with open(token_file, "r") as fp:
                try:
                    read_token = json.load(fp)
                except Exception as err:
                    print "get restore token error", str(err)
                if read_token and read_token.get("token") and (
                    time.strftime("%Y-%m-%dT%H:%M:%S.000000Z") < read_token.get("expires_at")):
                    print "get restore token"
                    return read_token.get("token")
        else:
            post_body = set_get_token_projectid_body(usr=self.usr, pwd=self.pwd, project_id=self.project_id)
            ret = common_request(path=BASEURL, method="post", body=post_body)
            token = str(ret.headers["X-Subject-Token"])
        token_dict = dict()
        expires_at = json.loads(ret.content)["token"]["expires_at"]

        token_dict["expires_at"] = expires_at
        token_dict["token"] = token
        with open(token_file, "w") as fp:
            json.dump(token_dict, fp)
        return token


if __name__ == "__main__":
    test_client = Client_()
    print test_client.test_clienervice_token()