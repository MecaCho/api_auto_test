import json

from common.req import common_request
from template import token
from common import iam_client

BASE_URL = "https://{url}/{api_version}"
NODES = "/{project_id}/edgemgr/nodes"
NODE = "/{project_id}/edgemgr/nodes/{node_id}"

QUERY_INS = "/{project_id}/ief-{resource_type}/resource_instances/action"
ADD_TAG = "/{project_id}/ief-{resource_type}/{resource_id}/tags"
DEL_TAG = "/{project_id}/ief-{resource_type}/{resource_id}/tags/{key}"
ADD_TAGS = "/{project_id}/ief-{resource_type}/{resource_id}/tags/action"
RESS_TAGS = "/{project_id}/ief-{resource_type}/tags"
RES_URL = "/{project_id}/edgemgr/{resource_type}"


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
        self.url_nodes = NODES
        self.url_node = NODE
        self.url_query_ins_by_tag = QUERY_INS
        self.url_add_tag = ADD_TAG
        self.url_tags = ADD_TAG
        self.url_ress_tags = RESS_TAGS
        self.url_batch_tags = ADD_TAGS
        self.url_res = RES_URL
        self.url_del_tag = DEL_TAG

    def get_res_type(self, resource_type):
        res_dict = {"edge_node": "nodes"}
        return res_dict[resource_type]

    def get_token(self):
        iam = iam_client.Client_(usr=self.usr, pwd=self.pwd, project_id=self.project_id)
        self.token = iam.get_service_token()

    def req(self, path, method, body):
        if not self.token:
            self.get_token()
        self.headers = {"X-Auth-Token": self.token, "Content-Type": "application/json"}
        path = self.base_url + path
        return common_request(path=path, method=method, body=body, headers=self.headers)

    def list_ress(self, resource_type):
        path = self.url_res.format(project_id=self.project_id, resource_type=resource_type)
        ret = self.req(method="get", path=path, body=None)
        return ret.status_code, json.loads(ret.content)
