# -*-coding=UTF-8-*-
import requests
import json
import time
from iam_client import Client_

URL = "xxx"
PORT = 443

QUERY_INS = "https://{url}:{port}/v1/{project_id}/ief-{resource_type}/resource_instances/action"
ADD_TAG = "https://{url}:{port}/v1/{project_id}/ief-{resource_type}/{resource_id}/tags"
ADD_TAGS = "https://{url}:{port}/v1/{project_id}/ief-{resource_type}/{resource_id}/tags/action"
RES_URL = "https://{url}:{port}/v1/{project_id}/edgemgr/{resource_type}"
TEST_CASE_SEQ = 0
TOTAL_TIME = 0


class TAG(object):
    def __init__(self, project_id, url, port, token):
        self.project_id = project_id
        self.url = url
        self.port = port
        self.token = token
        self.headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    def _request(self, path, method, body=None):
        global TEST_CASE_SEQ, TOTAL_TIME
        ret = None
        time_s = time.time()
        if method == "post":
            ret = requests.post(path, headers=self.headers, verify=False, timeout=5, data=json.dumps(body))
        elif method == "get":
            ret = requests.get(path, headers=self.headers, verify=False, timeout=5)
        elif method == "put":
            ret = requests.put(path, headers=self.headers, verify=False, timeout=5, data=json.dumps(body))
        elif method == "delete":
            ret = requests.delete(path, headers=self.headers, verify=False, timeout=5, data=None)
        time_cost = time.time() - time_s
        print "Cost time: {0}".format(time_cost)
        TEST_CASE_SEQ += 1
        TOTAL_TIME += time_cost
        return ret

    def query_ins(self, resource_type, action, tags, limit=None, offset=None):
        data_post = {"action": action, "tags": tags}
        if limit is not None:
            data_post["limit"] = limit
        if offset is not None:
            data_post["offset"] = offset
        path = QUERY_INS.format(url=self.url, port=self.port, project_id=self.project_id, resource_type=resource_type)
        print path
        print json.dumps(data_post)
        ret = self._request(method="post", path=path, body=data_post)
        print ret.status_code, ret.content
        return ret.status_code, json.loads(ret.content)

