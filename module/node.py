# -*-coding=UTF-8-*-
import requests
import json
import os
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
#     在您的设备上链接华为边缘计算服务，需要执行以下步骤：
#        1) 请在安装installer之前先安装docker
#        2) 解压installer
#        sudo tar -zxvf edge-installer_1.0.2_x86_64.tar.gz -C /opt
#        3) 解压证书到/opt/IEF/Cert
#        sudo mkdir -p /opt/IEF/Cert; sudo tar -zxvf qwq-node-0320.tar.gz -C /opt/IEF/Cert
#        4) 执行安装命令
#        cd /opt/edge-installer; sudo ./installer -op=install

    def init_node(self, node=None):
        #     在您的设备上链接华为边缘计算服务，需要执行以下步骤：
        #        1) 请在安装installer之前先安装docker
        #        2) 解压installer
        #        sudo tar -zxvf edge-installer_1.0.2_x86_64.tar.gz -C /opt
        #        3) 解压证书到/opt/IEF/Cert
        #        sudo mkdir -p /opt/IEF/Cert; sudo tar -zxvf qwq-node-0320.tar.gz -C /opt/IEF/Cert
        #        4) 执行安装命令
        #        cd /opt/edge-installer; sudo ./installer -op=install:

        # delete node
        os.system("cd /opt/edge-installer; sudo ./installer -op=uninstall")
        # create node and get package
        with open("node.json", "r") as fp:
            node = json.load(fp)
            node = node.get("node")
            node_id = node.get("id")
            project_id = node.get("project_id")
            package = node.get("package")
            import base64
            data = base64.b64decode(package)
            import os
            os.system("echo {}| base64 -d >> node.tar.gz".format(package))
            os.system("tar -xzvf node.tar.gz -C /opt/IEF/Cert/")
        # precheck install node
        with open("/opt/IEF/Cert/user_config", "r") as c_fp:
            user_config = json.load(c_fp)
            print json.dumps(user_config)
            print node_id, project_id
            user_config = user_config.get("node")
            print user_config.get("NODE_ID"), user_config.get("PROJECT_ID")
            assert user_config.get("NODE_ID") == node_id
            assert user_config.get("PROJECT_ID") == project_id
        # install node
        os.system("cd /opt/edge-installer; sudo ./installer -op=install")
        state = None
        num = 0
        while state != "RUNNING" and num < 610:
            code, resp = get_node(node_id)
            node_json = resp.get("node")
            if node_json.get("state") != state:
                state = node_json.get("state")
                comment = "project_id: {}, node_id: {}, state: {}".format(project_id, node_id, state)
                LOG.info('<td colspan="7">{}</td>'.format(comment))
            time.sleep(1)
            num += 1
        comment = "Init node successfull."
        LOG.info('<td colspan="7">{}</td>'.format(comment))

