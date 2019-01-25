# -*-coding=UTF-8-*-
import requests
import json
import time
from base import BASE
from common.req import _request


QUERY_INS = "/{project_id}/ief-{resource_type}/resource_instances/action"
ADD_TAG = "/{project_id}/ief-{resource_type}/{resource_id}/tags"
ADD_TAGS = "/{project_id}/ief-{resource_type}/{resource_id}/tags/action"
RES_URL = "/v1/{project_id}/edgemgr/{resource_type}"
TEST_CASE_SEQ = 0
TOTAL_TIME = 0


class TAG(BASE):
    
    def __init__(self, project_id, url, api_version, pwd, usr):
        super(TAG, self).__init__(project_id, url, api_version, pwd, usr)
        self.project_id = project_id
        self.url = url
        # self.port = port
        self.api_version = api_version
        self.pwd = pwd
        self.usr = usr

    def query_ins(self, resource_type, action, tags, limit=None, offset=None):
        data_post = {"action": action, "tags": tags}
        if limit is not None:
            data_post["limit"] = limit
        if offset is not None:
            data_post["offset"] = offset
        path = QUERY_INS.format(project_id=self.project_id, resource_type=resource_type)
        ret = self.req(method="post", path=path, body=data_post)
        return ret.status_code, json.loads(ret.content)

