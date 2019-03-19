# -*-coding=UTF-8-*-
import requests
import json
import time
from base import BASE
from common.req import common_request
from log.log import assert_resp


class Node(BASE):
    def __init__(self, project_id, url, api_version, pwd, usr):
        super(Node, self).__init__(project_id, url, api_version, pwd, usr)
        self.project_id = project_id
        self.url = url
        # self.port = port
        self.api_version = api_version
        self.pwd = pwd
        self.usr = usr

    @assert_resp(True, expection_code=200)
    def list_nodes(self):
        path = self.url_nodes.format(project_id=self.project_id)
        ret = self.req(method="get", path=path, body=None)
        return ret.status_code, json.loads(ret.content)

    @assert_resp(True, expection_code=200)
    def get_node(self, node_id):
        path = self.url_node.format(project_id=self.project_id, node_id=node_id)
        ret = self.req(method="get", path=path, body=None)
        return ret.status_code, json.loads(ret.content)

    @assert_resp(True, expection_code=204)
    def delete_node(self, node_id):
        path = self.url_node.format(project_id=self.project_id, node_id=node_id)
        ret = self.req(method="delete", path=path, body=None)
        return ret.status_code, json.loads(ret.content)

    @assert_resp(True, expection_code=201)
    def create_node(self, name=None):
        path = self.url_nodes.format(project_id=self.project_id)
        if not name:
            name = str(int(time.time()))
        node_post = {
            "name": name,
            "description": "This is a test node."
        }
        ret = self.req(method="post", path=path, body=node_post)
        return ret.status_code, json.loads(ret.content)
    
    @assert_resp(True, expection_code=201)
    def init_node(self, name=None):
        path = self.url_nodes.format(project_id=self.project_id)
        if not name:
            name = str(int(time.time()))
        node_post = {
            "name": name,
            "description": "This is a test node."
        }
        ret = self.req(method="post", path=path, body=node_post)
        return ret.status_code, json.loads(ret.content)

