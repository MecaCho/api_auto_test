from log.log import return_api_resp
from module import tag, node
import json
import os

@return_api_resp()
def test_fun():
    return [i for i in xrange(100)]

from common.req import _request

def read_config():
    print os.path.abspath(__file__)
    file_c = os.getcwd() + "/config/configmap.json"
    with open(file_c) as fp:
        conf_dict = json.load(fp)
        return conf_dict

if __name__ == '__main__':
    regions = read_config()
    import sys,getpass
    usr = sys.argv[1]
    pwd = getpass.getpass()
    users = read_config()
    usr = users[0].get("user")
    regions = users[0].get("regions")
    region = regions[0]
    project_id = region["project_id"]
    url = region["ief_url"]
    api_version = region["api_version"]
    client = node.Node(
            usr=usr, pwd=pwd, project_id=project_id,
            url=url, api_version=api_version)
    client.list_nodes()

    client = tag.TAG(usr=usr, pwd=pwd, project_id=project_id,url=url, api_version=api_version)
    client.query_ins(resource_type="edge_node", action="filter", tags=[{"key": "qwq", "values": []}])

