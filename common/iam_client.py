# -*-coding=UTF-8-*-
import time
import os
import requests
from req import common_request
from template.token import set_get_token_projectid_body
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s - %(name)s - %(message)s")
LOG = logging.getLogger(__name__)

BASEURL = "https://iam.cn-north-1.myhuaweicloud.com/v3/auth/tokens"
URI = BASEURL + ""


class ClientIAM(object):
    def __init__(self, usr, pwd, project_id, region):
        self.usr = usr
        self.pwd = pwd
        self.project_id = project_id
        self.region = region
        self.headers = {"Content-Type": "application/json"}

    def get_service_token(self):
        file_path = os.path.dirname(os.path.abspath(__file__))
        file_name = "-".join([self.usr, self.region, self.project_id]) + ".cert"
        token_file = file_path + "/" + file_name
        if os.path.exists(token_file):
            with open(token_file, "r") as fp:
                try:
                    read_token = json.load(fp)
                except Exception as err:
                    LOG.error("get restore token error", str(err))
                if read_token and read_token.get("token") and (
                    time.strftime("%Y-%m-%dT%H:%M:%S.000000Z") < read_token.get("expires_at")):
                    LOG.debug("get restore token from {}.".format(token_file))
                    return read_token.get("token")
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
    test_client = ClientIAM()
    print test_client.test_clienervice_token()
