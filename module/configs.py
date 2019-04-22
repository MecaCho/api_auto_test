# -*-coding=UTF-8-*-
import json
import time
import uuid
import logging
from base import BASE
import threading
from log.log import assert_resp

TEST_CASE_SEQ = 0
TOTAL_TIME = 0
logging.basicConfig(level=logging.INFO, filename="report.html",
                    format='<tr bordercolor="Blue" align="left"><td colspan="7">%(asctime)s-%(message)s</td></tr>')
LOG = logging.getLogger(__name__)


class ConfigMap(BASE):
    def __init__(self, project_id, url, api_version, pwd, usr):
        super(ConfigMap, self).__init__(project_id, url, api_version, pwd, usr)
        self.project_id = project_id
        self.url = url
        self.api_version = api_version
        self.pwd = pwd
        self.usr = usr

    def assert_result(code=None, expect_code=None, comment=""):
        if code and expect_code:
            assert code == expect_code
        LOG.info('<td colspan="7">{}</td>'.format(comment))

    def create_configmap(self, name=None, description="edge_node_value0", del_key=None):

        data_post = {
            "configmap": {
                "name": name,
                "description": "description test",
                "configs": {
                    "key1": "value1"
                }

            }
        }
        if del_key:
            data_post.pop(del_key, None)
        path = self.configmaps_url.format(
                project_id=self.project_id)
        ret = self.req(method="post", path=path, body=data_post)
        print ret.status_code, json.loads(ret.content) if ret.content else None
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def delete_configmap(self, id=None):
        path = self.configmap_url.format(
                project_id=self.project_id, configmap_id=id)
        ret = self.req(method="delete", path=path, body=None)
        
        print ret.status_code, json.loads(ret.content) if ret.content else None
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def list_configmaps(self):
        path = self.configmaps_url.format(
                project_id=self.project_id)
        ret = self.req(method="get", path=path, body=None)
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def multi_post(self):
        for i in xrange(10):
            name = "qwq-0422-{}".format(str(i))
            t = threading.Thread(target=self.create_configmap, args=(name,))
            t.start()

    def multi_delete(self):
        code, config_maps = self.list_configmaps()
        assert code == 200
        id_list = [configmap["id"] for configmap in config_maps["configmaps"] if "qwq-0422" in configmap["name"]]
        for id in id_list:
            t = threading.Thread(target=self.delete_configmap, args=(id,))
            t.start()
            time.sleep(0.3)
            t.join(timeout=5)


if __name__ == '__main__':
    config_map = ConfigMap(usr="", pwd="", project_id="988a1af23ff942879d4844f233ba7b23", url="ief2.cn-north-1.myhuaweicloud.com", api_version="v2")
    config_map.create_configmap(name="test_12345")

