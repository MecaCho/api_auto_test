# -*-coding=UTF-8-*-
import json
import time
import uuid
import logging
from base import BASE
from template import volume
import threading
from log.log import assert_resp

TEST_CASE_SEQ = 0
TOTAL_TIME = 0
logging.basicConfig(level=logging.INFO, filename="report.html",
                    format='<tr bordercolor="Blue" align="left"><td colspan="7">%(asctime)s-%(message)s</td></tr>')
LOG = logging.getLogger(__name__)


class Deployment(BASE):
    def __init__(self, project_id, url, api_version, pwd, usr):
        super(Deployment, self).__init__(project_id, url, api_version, pwd, usr)
        self.project_id = project_id
        self.url = url
        self.api_version = api_version
        self.pwd = pwd
        self.usr = usr

    def assert_result(code=None, expect_code=None, comment=""):
        if code and expect_code:
            assert code == expect_code
        LOG.info('<td colspan="7">{}</td>'.format(comment))

    def get_deployment(self, id):
        path = self.deployment_url.format(
                project_id=self.project_id, deployment_id=id)
        ret = self.req(method="get", path=path, body=None)
        print ret.status_code, json.loads(ret.content) if ret.content else None
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def get_deployments(self):
        path = self.deployments_url.format(project_id=self.project_id)
        ret = self.req(method="get", path=path, body=None)
        print ret.status_code, json.loads(ret.content) if ret.content else None
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def put_deployment(self, id=None, description="qwq update", volumes=None, del_key=None):

        data_post = {
                    "description": description,
                    "deployment": {
                        "envs": [
                            {
                                "name": "PROJECT_ID",
                                "value": "c3b4a9da5ba24620bb8d3d67027db04c"
                            }
                        ],
                        "liveness_probe": None,
                        "configs": {
                            "host_network": True,
                            "restart_policy": "Always",
                            "privileged": False,
                            "ports": None
                        },
                        "image_url": "swr.cn-north-1.myhuaweicloud.com/qiuwenqi/sample:latest",
                        "resources": {
                            "requests": {
                                "cpu": 0.25,
                                "memory": 512
                            },
                            "limits": {
                                "cpu": 1,
                                "memory": 512
                            }
                        },
                        "volumes": [],
                        "readiness_probe": None
                    }
        }
        if volumes:
            data_post["deployment"]["volumes"] = volumes
        if del_key:
            data_post.pop(del_key, None)
        path = self.deployment_url.format(
                project_id=self.project_id, deployment_id=id)
        ret = self.req(method="put", path=path, body=data_post)
        print ret.status_code, json.loads(ret.content) if ret.content else None
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def put_deployment_with_configmap(self, id=None):
        return self.put_deployment(id=id, volumes=volume.configmaps)
