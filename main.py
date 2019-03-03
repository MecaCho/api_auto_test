import json
import os
import sys
import getpass
import logging

from log.log import return_api_resp
from module import tag, node

#logging.basicConfig(level=logging.INFO,filename="report.html", format='<tr bordercolor="Blue" align="left"><td>%(message)s</td></tr>')
logging.basicConfig(level=logging.INFO, filename="report.html", format="%(message)s")
LOG = logging.getLogger(__name__)

@return_api_resp()
def test_fun():
    return [i for i in xrange(100)]


def read_config():
    print os.path.abspath(__file__)
    file_c = os.getcwd() + "/config/configmap.json"
    with open(file_c) as fp:
        conf_dict = json.load(fp)
        return conf_dict

def gen_report():
    pass

def init_report():
    os.system("rm -rf report.html")
    os.system("cp tmp.html report.html")

if __name__ == '__main__':
    regions = read_config()
    users = read_config()
#    init_report()
    for user_info in users:
        usr = user_info.get("user")
        pwd = getpass.getpass("please input user {} password : ".format(usr))
        regions = user_info.get("regions")
        for region in regions:
            project_id = region["project_id"]
            url = region["ief_url"]
            api_version = region["api_version"]
            LOG.info('<h1 class="center"<nobr>IEF TMS API Auto Test Result Report ({})</nobr></h1>'.format(url))
            LOG.info('<table bordercolor="Blue" width="1200" align="left" cellspacing="0" border="1">')
            LOG.info('<tr bordercolor="Blue" align="left"><td>method</td><td>path</td><td>cost_time(s)</td><td>resp_code</td><td>expect_code</td><td>Result</td><td>body</td></tr>')
#            client = node.Node(
#                    usr=usr, pwd=pwd, project_id=project_id,
#                    url=url, api_version=api_version)
#            client.list_nodes()
            client = tag.TAG(usr=usr, pwd=pwd, project_id=project_id, url=url, api_version=api_version)
            client.query_ins(resource_type="edge_node", action="filter", tags=[{"key": "qwq", "values": []}])
            print "0"*100
            client.test_query_ins()
            print "1"*100
            client.test_batch_tags()
            LOG.info("</table><br></br>\n<br></br>\n<br></br>")
        LOG.info("</body></html>")
