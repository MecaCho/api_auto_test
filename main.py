import json
import os
import sys
import getpass
import logging
import time

from log.log import return_api_resp
from module import tag, node

# logging.basicConfig(level=logging.INFO,filename="report.html", format='<tr bordercolor="Blue" align="left"><td>%(message)s</td></tr>')
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
    t_case_name = sys.argv[1]
    for user_info in users:
        usr = user_info.get("user")
        pwd = getpass.getpass("please input user {} password : ".format(usr))
        regions = user_info.get("regions")
        for region in regions:
            project_id = region["project_id"]
            url = region["ief_url"]
            file_name = "-".join(url.split(".")[:2])
            # os.system("rm -rf report.html && touch report.html && chmod 777 report.html")
            with open("report.html", "w") as fp:
                fp.write("")
            api_version = region["api_version"]
            LOG.info('<h1 class="center"<nobr>IEF {} API Auto Test Result Report ({})</nobr></h1>'.format(t_case_name, url))
            LOG.info('<table bordercolor="Blue" width="1200" align="left" cellspacing="0" border="1">')
            LOG.info('<style>table { table-layout:fixed; word-wrap: break-word;}</style>')

            LOG.info(
                '<tr bordercolor="Blue" align="left"><td width="100">method</td><td width="300">path</td><td width="100">cost_time(s)</td><td width="100">resp_code</td><td width="100">expect_code</td><td width="100">Result</td><td width="400">body</td></tr>')
            client = node.Node(
                    usr=usr, pwd=pwd, project_id=project_id,
                    url=url, api_version=api_version)
            client.list_nodes()
            #LOG.info('<td colspan="7">{}</td>'.format("Created a node."))
            #code, node_json = client.create_node(name="qwq-test-node")
            #assert code == 201
            #with open("qwq-test-node1553566682.json", "r") as fp:
            #    node_json = json.load(fp)
            #print str(node_json)
            #LOG.info('<td colspan="7">{}</td>'.format("Installing a node."))
            #client.init_node(node_json)
            # client = tag.TAG(usr=usr, pwd=pwd, project_id=project_id, url=url, api_version=api_version)
            # client.query_ins(resource_type="edge_node", action="filter", tags=[{"key": "qwq", "values": []}])
            # print "0"*100
            # client.test_query_ins()
            # print "1"*100
            # client.test_batch_tags()
            LOG.info("</table><br></br>\n<br></br>\n<br></br>")
            LOG.info("</body></html>")
            now = str(int(time.time()))
            os.system("mv report.html {}_{}_report_{}.html".format(file_name, t_case_name, now))
