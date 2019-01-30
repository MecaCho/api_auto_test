import json
import os
import sys
import getpass

from log.log import return_api_resp
from module import tag, node


@return_api_resp()
def test_fun():
    return [i for i in xrange(100)]


def read_config():
    print os.path.abspath(__file__)
    file_c = os.getcwd() + "/config/configmap.json"
    with open(file_c) as fp:
        conf_dict = json.load(fp)
        return conf_dict

if __name__ == '__main__':
    regions = read_config()
    users = read_config()
    for user_info in users:
        usr = user_info.get("user")
        pwd = getpass.getpass("please input user {} password : ".format(usr))
        regions = user_info.get("regions")
        for region in regions:
            project_id = region["project_id"]
            url = region["ief_url"]
            api_version = region["api_version"]
            client = node.Node(
                    usr=usr, pwd=pwd, project_id=project_id,
                    url=url, api_version=api_version)
            client.list_nodes()
            client = tag.TAG(usr=usr, pwd=pwd, project_id=project_id, url=url, api_version=api_version)
            client.query_ins(resource_type="edge_node", action="filter", tags=[{"key": "qwq", "values": []}])
            print "0"*100
            client.test_query_ins()
            print "1"*100
            client.test_batch_tags()
