# -*-coding=UTF-8-*-
import json
import os
import time
import logging
from base import BASE
# from common.req import common_request
from log.log import assert_resp

logging.basicConfig(level=logging.INFO,
                    format='<tr bordercolor="Blue" align="left"><td colspan="7">%(asctime)s-%(message)s</td></tr>')
'''
logging.basicConfig(level=logging.INFO, filename="node.html", 
format='<tr bordercolor="Blue" align="left"><td colspan="7">%(asctime)s-%(message)s</td></tr>')
logging.basicConfig(level=logging.INFO, 
format='<tr bordercolor="Blue" align="left"><td colspan="7">%(asctime)s-%(message)s</td></tr>')

'''
LOG = logging.getLogger(__name__)


class Node(BASE):
    def __init__(self, project_id, url, api_version, pwd, usr):
        super(Node, self).__init__(project_id, url, api_version, pwd, usr)
        self.project_id = project_id
        self.url = url
        # self.port = port
        self.api_version = api_version
        self.pwd = pwd
        self.usr = usr

    def init_node(self, node_json=None):
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
        if not node_json:
            with open("node.json", "r") as fp:
                node_json = json.load(fp)
        node_json = node_json.get("node")
        node_id = node_json.get("id")
        project_id = node_json.get("project_id")
        package = node_json.get("package")
        import base64
        data = base64.b64decode(package)
        print data
        os.system("rm -rf node.tar.gz;echo {}| base64 -d >> node.tar.gz".format(package))
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
            #self.assert_result(comment=u"# IEF_NODE_QuerryNode 查询节点状态")
            code, resp = self.get_node(node_id)
            node_json = resp.get("node")
            # if node_json.get("state") != state:
            state = node_json.get("state")
            comment = "project_id: {}, node_id: {}, state: {}".format(project_id, node_id, state)
            LOG.info('<td colspan="7">{}</td>'.format(comment))
            time.sleep(1)
            num += 1
        comment = "Init node successfull."
        LOG.info('<td colspan="7">{}</td>'.format(comment))


if __name__ == "__main__":
    node = Node("project_id", "url.url", "api_version", "pwd", "usr")
    node.init_node()
