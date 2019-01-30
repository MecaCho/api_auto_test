from common.req import common_request
from template import token
from common import iam_client

BASE_URL = "https://{url}/{api_version}"


class BASE(object):
    def __init__(self, project_id, url, api_version, pwd, usr):
        self.project_id = project_id
        self.url = url
        # self.port = port
        self.pwd = pwd
        self.usr = usr
        self.token = None
        self.base_url = BASE_URL.format(url=url, api_version=api_version)
        self.headers = None

    def get_token(self):
        iam = iam_client.Client_(usr=self.usr, pwd=self.pwd, project_id=self.project_id)
        self.token = iam.get_service_token()

    def req(self, path, method, body):
        self.get_token()
        self.headers = {"X-Auth-Token": self.token, "Content-Type": "application/json"}
        path = self.base_url + path
        return common_request(path=path, method=method, body=body, headers=self.headers)


