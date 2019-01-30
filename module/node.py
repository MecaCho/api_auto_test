# -*-coding=UTF-8-*-
import requests
import json
import time
from base import BASE
from common.req import common_request


class Node(BASE):
    def __init__(self, project_id, url, api_version, pwd, usr):
        super(Node, self).__init__(project_id, url, api_version, pwd, usr)
        self.project_id = project_id
        self.url = url
        # self.port = port
        self.api_version = api_version
        self.pwd = pwd
        self.usr = usr

    def list_nodes(self):
        path = self.url_nodes.format(project_id=self.project_id)
        ret = self.req(method="get", path=path, body=None)
        return ret.status_code, json.loads(ret.content)

