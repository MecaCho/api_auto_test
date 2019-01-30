# -*-coding=UTF-8-*-
import requests
import json
import time
from base import BASE


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

    def get_tag_dict(self, num=1):
        return [{"key": "qwq_tag_key" + str(i), "value": "qwq_tag_value" + str(i)} for i in xrange(num)]

    def query_ins(self, resource_type, action, tags, limit=None, offset=None):
        data_post = {"action": action, "tags": tags}
        if limit is not None:
            data_post["limit"] = limit
        if offset is not None:
            data_post["offset"] = offset
        path = QUERY_INS.format(project_id=self.project_id, resource_type=resource_type)
        ret = self.req(method="post", path=path, body=data_post)
        return ret.status_code, json.loads(ret.content)




def test_batch_add_tags():
    iam_client = Client_()
    print "Start get user Token.\n"
    user_token = iam_client.get_user_token(name="",
                                           password="",
                                           domain_name="")
    print user_token
    client = TAG(project_id="", url=URL, port=PORT, token=user_token)
    node_id = None
    try:
        code, node = client.create_resource(resource_type="nodes")
        assert code == 201
        node_id = node["node"]["id"]
        print node_id
        # TC_TMS_BatchCreatDeleteResourceTags_001	带所有必选参数，创建一个资源标签成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=1), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=1), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_002	带所有必选参数，创建3个资源标签成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=3), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=3), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_003	带所有必选参数，创建5个资源标签成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=5), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=5), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_004	带所有必选参数，创建8个资源标签成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=8), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=8), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_005	带所有必选参数，创建10个资源标签成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=10), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=10), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_006	带所有必选参数，修改10个资源标签成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=1), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=1), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=1), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_007	带所有必选参数，创建11个资源标签失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(num=11), action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_008	创建一个资源标签，key值为null，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": None, "value": "value0"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_009	创建一个资源标签，key值为"null"，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "null", "value": "value0"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "null", "value": "value0"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_010	创建一个资源标签，key值为空，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "", "value": "value0"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_011	创建一个资源标签，key值为空格，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "null", " ": "value0"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_012	创建一个资源标签，key值长度为1，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value0"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value0"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_013	创建一个资源标签，key值长度为36，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"*36, "value": "value0"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"*36, "value": "value0"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_014	创建一个资源标签，key值长度为37(前面含有空格)，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": " "+"q"*36, "value": "value0"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value0"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_015	创建一个资源标签，key值长度为37(中间含有空格)，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"*16+" "+"q"*20, "value": "value0"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_016	创建一个资源标签，key值长度为37，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"*37, "value": "value0"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_017	创建一个资源标签，key值为西语，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_018	创建一个资源标签，key值为葡语，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_019	创建一个资源标签，key字段缺失，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"value": "value0"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_020	创建一个资源标签，key字段为“AAaa00-99_中”字符，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": u"AAaa00-99_中", "value": "value0"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_021	创建一个资源标签，key字段包含非打印字符ASCII（0~31），创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_022	创建一个资源标签，key字段包含特殊字符*，创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_023	创建一个资源标签，key字段包含特殊字符<，创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_024	创建一个资源标签，key字段包含特殊字符>，创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_025	创建一个资源标签，key字段包含特殊字符\，创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_026	创建一个资源标签，key字段包含特殊字符=，创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_027	创建一个资源标签，key字段包含特殊字符/，创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_028	创建一个资源标签，key字段包含特殊字符|，创建失败
    # TC_TMS_BatchCreatDeleteResourceTags_029	创建一个资源标签，key字段包含特殊字符","，创建失败
        for k in "*<>\=/|,$&%":
            code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "key"+k,"value": "value0"}], action="create")
            assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_030	创建一个资源标签，key字段包含特殊字符$，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_031	创建一个资源标签，key字段包含特殊字符&，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_032	创建一个资源标签，key字段包含特殊字符%，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_033	创建一个资源标签，value值为null，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": None}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_034	创建一个资源标签，value值为"null"，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "null"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "null"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_035	创建一个资源标签，value值为空，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": ""}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": ""}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_036	创建一个资源标签，value值为空格，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": " "}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": " "}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_037	创建一个资源标签，value值长度为1，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_038	创建一个资源标签，value值长度为43，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"*43}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"*43}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_039	创建一个资源标签，value值长度为44(前面含有空格)，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": " "+43*"q"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": " "+43*"q"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_040	创建一个资源标签，value值长度为44(中间含有空格)，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"*20+" "+23*"q"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_041	创建一个资源标签，value值长度为44，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": 44*"q"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_042	创建一个资源标签，value字段缺失，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_043	创建一个资源标签，value字段为“AAaa00-99_中”字符，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": u"AAaa00-99_中"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_044	创建一个资源标签，value字段包含非打印字符ASCII（0~31），创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_045	创建一个资源标签，value字段包含特殊字符*，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_046	创建一个资源标签，value字段包含特殊字符<，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_047	创建一个资源标签，value字段包含特殊字符>，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_048	创建一个资源标签，value字段包含特殊字符\，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_049	创建一个资源标签，value字段包含特殊字符=，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_050	创建一个资源标签，value字段包含特殊字符/，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_051	创建一个资源标签，value字段包含特殊字符|，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_052	创建一个资源标签，value字段包含特殊字符","，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_053	创建一个资源标签，value字段包含特殊字符$，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_054	创建一个资源标签，value字段包含特殊字符&，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_055	创建一个资源标签，value字段包含特殊字符%，创建成功
        for v in "*<>\=/|,$&%":
            code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"+v}], action="create")
            assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_056	创建一个资源标签，value的值为葡语，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_057	创建一个资源标签，value的值为西语，创建成功
        # TC_TMS_BatchCreatDeleteResourceTags_058	创建资源标签，参数tags列表中为空，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_059	创建资源标签，参数tags字段缺失，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=None, action="create")
        assert code == 400
        ################################################################################################################
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[None], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_060	创建资源标签，参数tags非列表格式，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags={}, action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_061	创建资源 标签，action值为CREATE，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}], action="CREATE")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_062	创建资源 标签，action值为Create，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}], action="CREATE")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_063	创建资源 标签，action值为creatE，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}], action="creatE")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_064	创建资源标签，resource_type和resource_id不一致，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_065	创建资源标签，project_id为其他租户的project_id，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_066	创建资源标签，project_id不存在，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_067	创建资源标签，请求中带无效token，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_068	创建资源标签，请求中不带token，创建失败
        # TC_TMS_BatchCreatDeleteResourceTags_069	创建资源标签，批量添加标签的时候key和value值均重复（key和value为一组），创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}, {"key": "q", "value": "value"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_070	创建资源标签，批量添加标签的时候key值重复，创建失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}, {"key": "q", "value": "value1"}], action="create")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_071	创建资源标签，批量添加标签的时候value值重复，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}, {"key": "q1", "value": "value"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}, {"key": "q1", "value": "value"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_072	创建资源标签，资源已存在标签，再次添加与之前key和value值相同的标签（key和value为一组），创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}, {"key": "q1", "value": "value"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}, {"key": "q1", "value": "value"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}, {"key": "q1", "value": "value"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_073	创建资源标签，资源已存在标签，再次添加与之前key值相同的标签，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value_new"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value_new"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_074	创建资源标签，资源已存在标签，再次添加与之前value值相同的标签，创建成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "value"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q_new", "value": "value"}], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q_new", "value": "value"}, {"key": "q1", "value": "value"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_075	创建资源标签，已存在3个，再次添加8个，添加失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(3), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(11)[3:], action="create")
        assert code == 400
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(3), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_076	创建资源标签，已存在3个，再次添加8个，其中有一组与之前添加的标签键值都相同，添加成功
        code, resp = client.get_tags_of_resource(resource_type="edge_node", resource_id=node_id)
        assert code == 200
        tags_resp = json.loads(resp)["tags"]
        print resp
        for tag in tags_resp:
            code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[tag], action="delete")
            assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(3), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(10)[2:], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(10), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_078	删除一个资源标签，key字段缺失，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"value": "value"}], action="delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_079	删除一个资源标签，key字段为null，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": None, "value": "value_new"}], action="delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_080	删除一个资源标签，key字段为“null”，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "null", "value": "value_new"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_081	删除一个资源标签，key字段为空，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"value": "value_new"}], action="delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_082	删除一个资源标签，key字段为空格，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": " ", "value": "value_new"}], action="delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_083	删除一个资源标签，key字段长度为37，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"*37, "value": "value_new"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_084	删除一个资源标签，key值长度为127，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"*127, "value": "value_new"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_085	删除一个资源标签，key值长度为128且前面含有空格，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": " "+"q"*127, "value": "value_new"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_086	删除一个资源标签，key值长度为128，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"*128, "value": "value_new"}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_087	删除一个资源标签，key字段为（AAaa00-99_中）字符，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_088	删除一个资源标签，key字段包含非打印字符ASCII（0~31），删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_089	删除一个资源标签，key字段包含特殊字符*，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_090	删除一个资源标签，key字段包含特殊字符<，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_091	删除一个资源标签，key字段包含特殊字符>，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_092	删除一个资源标签，key字段包含特殊字符\，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_093	删除一个资源标签，key字段包含特殊字符=，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_094	删除一个资源标签，key字段包含特殊字符\，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_095	删除一个资源标签，key字段包含特殊字符|，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_096	删除一个资源标签，key字段包含特殊字符,，删除成功
        for k in "*<>\=/|,":
            code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id,
                                           tags=[{"key": k, "value": "value_new"}], action="delete")
            assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_097	删除一个资源标签，value值为null，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": None}], action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_098	删除一个资源标签，value值为"null"，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "null"}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_099	删除一个资源标签，value值为空，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": ""}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_100	删除一个资源标签，value值为空格，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": " "}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_101	删除一个资源标签，value值长度为1，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_102	删除一个资源标签，value值长度为43，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"*43}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_103	删除一个资源标签，value值长度为44，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"*44}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_104	删除一个资源标签，value值长度为255，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"*255}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_105	删除一个资源标签，value值长度为256且前面含有空格，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": " "+"q"*256}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_106	删除一个资源标签，value值长度为256，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": "q"*256}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_107	删除一个资源标签，value字段缺失，删除成功
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"}],
                                       action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_108	删除一个资源标签，value字段为unicode字符（AAaa00-99_中），删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_109	删除一个资源标签，value字段包含非打印字符ASCII（0~31），删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_110	删除一个资源标签，value字段包含特殊字符*，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_111	删除一个资源标签，value字段包含特殊字符<，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_112	删除一个资源标签，value字段包含特殊字符>，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_113	删除一个资源标签，value字段包含特殊字符\，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_114	删除一个资源标签，value字段包含特殊字符=，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_115	删除一个资源标签，value字段包含特殊字符/，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_116	删除一个资源标签，value字段包含特殊字符|，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_117	删除一个资源标签，value字段包含特殊字符","，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_118	删除一个资源标签，value字段包含特殊字符"%"，删除成功
        for v in "*<>\=/|,%":
            code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q", "value": v}], action="delete")
            assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_119	删除资源标签，要删除的标签不存在，删除成功
        # TC_TMS_BatchCreatDeleteResourceTags_120	删除资源标签，参数tags列表中为空，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[],
                                       action="delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_121	删除资源标签，参数tags字段缺失，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=None,
                                       action="delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_122	删除资源标签，参数tags非列表格式，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags={},
                                       action="delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_123	删除资源 标签，action值为DELETE，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"}],
                                       action="Delete")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_124	删除资源 标签，action值为Delete，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"}],
                                       action="DELETE")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_125	删除资源 标签，action值为delEte，删除失败
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": "q"}],
                                       action="delEte")
        assert code == 400
        # TC_TMS_BatchCreatDeleteResourceTags_126	删除资源标签，resource_type和resource_id不一致，删除失败
        code, resp = client.batch_tags(resource_type="device", resource_id=node_id, tags=[{"key": "q"}],
                                       action="delete")
        assert code == 404
        # TC_TMS_BatchCreatDeleteResourceTags_127	删除资源标签，project_id为其他租户的[roject_id，删除失败
        # TC_TMS_BatchCreatDeleteResourceTags_128	删除资源标签，project_id不存在，删除失败
        # TC_TMS_BatchCreatDeleteResourceTags_129	删除资源标签，请求中带无效token，删除失败
        # TC_TMS_BatchCreatDeleteResourceTags_130	删除资源标签，请求中不带token，删除失败
        code, resp = client.get_tags_of_resource(resource_type="edge_node", resource_id=node_id)
        assert code == 200
        tags_num = len(json.loads(resp)["tags"])
        print resp
        if tags_num != 0:
            for tag in json.loads(resp)["tags"]:
                k, v = tag["key"], tag["value"]
                code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=[{"key": k, "value": v}], action="delete")
                assert code == 204
        # assert len(json.loads(resp)["tags"]) == 0
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(3), action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(10)[2:], action="create")
        assert code == 204
        code, resp = client.batch_tags(resource_type="edge_node", resource_id=node_id, tags=get_tag_dict(10), action="delete")
        assert code == 204
        # TC_TMS_BatchCreatDeleteResourceTags_077	删除资源标签，含有重复的key值，删除成功
        if node_id:
            code, resp = client.delete_resource(resource_type="nodes", id=node_id)
            assert code == 204
    except Exception:
        import traceback
        print traceback.print_exc()
        if node_id:
            code, resp = client.delete_resource(resource_type="nodes", id=node_id)
            assert code == 204
        raise Exception


def test_query_rsource_by_tags():
    iam_client = Client_()
    print "Start get user Token.\n"
    user_token = iam_client.get_user_token(name="",
                                           password="!",
                                           domain_name="")
    print user_token
    client = TAG(project_id="", url=URL, port=PORT, token=user_token)
    client.delete_nodes()
    node_id = None
    try:
        for action in ["filter", "count"]:
            # TC_TMS_QuerryResourceInstanceFilter_001	请求体中带所有必选参数，查询实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "key0", "values": ["value0"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_002	带必选参数tags（含有一组key和value），查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "key0", "values": ["value0"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_003	tags含有9组key和value，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": str(i), "values": [str(i)]} for i in xrange(9)])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_004	tags含有10组key和value，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": str(i), "values": [str(i)]} for i in xrange(10)])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_005	tags含有11组key和value，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": str(i), "values": [str(i)]} for i in xrange(11)])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_006	tags一个key对应2个value,且这两个value在不同的资源上，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0", "dp_value0"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_007	tags一个key对应9个value，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": [str(i) for i in xrange(9)]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_008	tags一个key对应10个value，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": [str(i) for i in xrange(10)]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_009	tags一个key对应11个value，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": [str(i) for i in xrange(11)]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_010	tags10个key对应10个value（即每个key里面有10个value），查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key" + str(j), "values": [str(i) for i in xrange(10)]}
                                               for j in xrange(10)])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_011	tags3个key对应4个value，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key" + str(j), "values": [str(i) for i in xrange(10)]}
                                               for j in xrange(10)])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_012	tags字段key缺失，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"values": ["value0"]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_013	tags字段key值为null，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": None, "values": ["value0"]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_014	tags字段key值为“null”，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "null", "values": ["value0"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_015	tags字段key的值为空，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "", "values": ["value0"]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_016	tags字段key的值为空格，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": " ", "values": ["value0"]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_017	tags字段key的值含有多个空格，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "  ", "values": ["value0"]}])
            assert code == 400

            code, node = client.create_resource(resource_type="nodes")
            assert code == 201
            node_id = node["node"]["id"]
            print node_id
            # assert node["node"]["name"]
            code, rep = client.add_tag(resource_type="edge_node", resource_id=node_id, key="edge_node_key0",
                                       value="edge_node_value0")
            assert code == 204

            # TC_TMS_QuerryResourceInstanceFilter_018	tags字段key的值前后均含有空格，查询资源实例成功（校验是否前后trim）
            code, response = client.query_ins("edge_node", action,
                                              [{"key": " edge_node_key0 ", "values": ["edge_node_value0"]}])
            assert code == 200
            assert response["total_count"] == 1

            # TC_TMS_QuerryResourceInstanceFilter_018	tags字段key的值前后均含有空格，查询资源实例成功（校验是否前后trim）
            code, response = client.query_ins("edge_node", action,
                                              [{"key": " edge_node_key0 ", "values": ["edge_node_value0", "abc"]}])
            assert code == 200
            assert response["total_count"] == 1

            # TC_TMS_QuerryResourceInstanceFilter_019	tags字段key的值前后均含有多个空格，查询资源实例成功（校验是否前后trim）
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "  edge_node_key0  ", "values": ["edge_node_value0"]}])
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_020	tags字段key的值前面含有多个空格，查询资源实例成功（校验是否前后trim）
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "  edge_node_key0", "values": ["edge_node_value0"]}])
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_021	tags字段key的值有重复，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": " edge_node_key0 ", "values": ["edge_node_value0"]},
                                               {"key": "edge_node_key0", "value": "null"}])
            assert code == 400

            # TC_TMS_QuerryResourceInstanceFilter_022	tags字段key的值长度为1，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "q", "values": ["edge_node_value0"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_023	tags字段key的值长度为127，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": ["edge_node_value0"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_024	tags字段key的值长度为128，中间含有空格，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "q" * 120 + " " + "q" * 7, "values": ["edge_node_value0"]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_025	tags字段key的值长度为128，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 128, "values": ["edge_node_value0"]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_026	tags字段key的值含有特殊字符*，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_027	tags字段key的值含有特殊字符<，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_028	tags字段key的值含有特殊字符>，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_029	tags字段key的值含有特殊字符\，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_030	tags字段key的值含有特殊字符=，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_031	tags字段key的值含有特殊字符/，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_032	tags字段key的值含有特殊字符|，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_033	tags字段key的值含有特殊字符","，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_034	tags字段key的值含有特殊字符$，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_035	tags字段key的值含有特殊字符%，查询资源实例成功
            for v in "*<>\=/|,$%":
                code, response = client.query_ins("edge_node", action, [{"key": v, "values": ["edge_node_value0"]}])
                assert code == 200
                assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_036	tags字段key的值为西语，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_037	tags字段key的值为葡语，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_038	tags字段values值有重复，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": ["value0", "value0"]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_039	tags字段values值为空，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": [""]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_040	tags字段values值为空格，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": [" "]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_041	tags字段values值为多个空格，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": ["  "]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_042	tags字段values值前后都含有空格，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": [" edge_node_value0 "]}])
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_043	tags字段values值前面含有多个空格，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["  edge_node_value0  "]}])
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_044	tags字段values值为null，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": [None]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_045	tags字段values值为"null"，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": ["null"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_046	tags字段values缺失，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_047	tags字段values为空列表，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "edge_node_key0", "values": []}])
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_048	tags字段value的值长度为1，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "q" * 127, "values": ["q"]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_049	tags字段value的值长度为255，查询资源实例成功
            code, response = client.query_ins("edge_node", action, [{"key": "edge_node_key0", "values": ["q" * 255]}])
            assert code == 200
            assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_050	tags字段value的值长度为256，且中间含有空格，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["q" * 250 + " " + "q" * 5]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_051	tags字段value的值长度为256，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "edge_node_key0", "values": ["q" * 256]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_052	tags字段value的值含有特殊字符*(*为开头)，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["*edge_node_value0"]}])
            assert code == 200
            assert response["total_count"] == 1
            # assert response["total_count"] == 0

            # TC_TMS_QuerryResourceInstanceFilter_053	tags字段value的值含有特殊字符<，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_054	tags字段value的值含有特殊字符>，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_055	tags字段value的值含有特殊字符\，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_056	tags字段value的值含有特殊字符=，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_057	tags字段value的值含有特殊字符/，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_058	tags字段value的值含有特殊字符|，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_059	tags字段value的值含有特殊字符","，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_060	tags字段value的值含有特殊字符$，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_061	tags字段value的值含有特殊字符%，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_062	tags字段value为西语，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_063	tags字段value的葡语，查询资源实例成功
            for v in "<>\=/|,$%":
                code, response = client.query_ins("edge_node", action, [{"key": "edge_node_key0", "values": [v]}])
                assert code == 200
                assert response["total_count"] == 0
            # TC_TMS_QuerryResourceInstanceFilter_064	tags字段values不是列表形式，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "edge_node_key0", "values": {}}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_065	tags为空列表，查询资源实例失败
            code, response = client.query_ins("edge_node", action, [{"key": "edge_node_key0", "values": [None]}])
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_066	tags为[null]，查询资源实例失败
            code, response = client.query_ins("edge_node", action, None)
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_067	带必选参数和可选参数limit，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="10",
                                              offset="0")
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_068	limit=1.5，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="1.5")
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_069	limit=1，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="1")
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_070	limit=-1，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="-1")
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_071	limit=0，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="0")
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_072	limit=999，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="999")
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_073	limit=1000，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="1000")
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_074	limit=1001，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_075	limit=*，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_076	limit=A，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_077	limit的值为空，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_078	limit的值为null，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_079	limit的值为“null”，查询资源实例失败
            for li in ["*", "A", "", "null", 1001]:
                code, response = client.query_ins("edge_node", action,
                                                  [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit=li)
                assert code == 400
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit=None)
            assert code == 200
            assert response["total_count"] == 1
            # TC_TMS_QuerryResourceInstanceFilter_080	带必选成参数和可选参数offset，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_081	offset=-1，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_082	offset=A，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_083	offset=#，查询资源实例失败
            for o in [-1, "A", "#"]:
                code, response = client.query_ins("edge_node", action,
                                                  [{"key": "edge_node_key0", "values": ["edge_node_value0"]}],
                                                  limit="10", offset=o)
                assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_084	offset=0，查询资源实例成功，校验查询结果
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="10",
                                              offset="0")
            assert code == 200
            assert response["total_count"] == 1
            # resources
            if action == "filter":
                assert len(response["resources"]) == 1
            # TC_TMS_QuerryResourceInstanceFilter_085	offset=5，查询资源实例成功，校验查询结果
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="10",
                                              offset="5")
            assert code == 200
            assert response["total_count"] == 1
            if action == "filter":
                assert len(response["resources"]) == 0
            # TC_TMS_QuerryResourceInstanceFilter_086	offset的值为空，查询资源实例失败
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="10",
                                              offset="")
            assert code == 400
            # TC_TMS_QuerryResourceInstanceFilter_087	offset的值为null，查询资源实例成功
            code, response = client.query_ins("edge_node", action,
                                              [{"key": "edge_node_key0", "values": ["edge_node_value0"]}], limit="10",
                                              offset=None)
            assert code == 200
            assert response["total_count"] == 1
            if action == "filter":
                assert len(response["resources"]) == 1
            # TC_TMS_QuerryResourceInstanceFilter_088	请求体为空，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_089	请求体只带必选参数action=FILTER，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_090	必选参数action=Av45*，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_091	带必选参数和可选参数matches,查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_092	matches不是列表形式,查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_093	matches列表为空，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_094	matches为[null]，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_095	matches字段key缺失，字段value存在，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_096	matches字段key的值不为限定的resource_name，为resource_id，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_097	matches字段key的值为Aa12_中*，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_098	matches字段key值为空，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_099	matches字段key值为空格，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_100	matches字段key值为null，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_101	matches字段中含有多个键值对（key值只有一个为resource_name，其余为任意字符串），查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_102	matches字段value缺失，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_103	matches字段value值为空，查询资源实例成功，为精确搜索
            # TC_TMS_QuerryResourceInstanceFilter_104	matches字段value值为空格，查询资源实例成功，为模糊搜索
            # TC_TMS_QuerryResourceInstanceFilter_105	matches字段value值为“null”，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_106	matches字段value值含有特殊字符，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_107	matches字段value值为null，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_108	matches字段value值为资源名称的前缀，全部大写，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_109	matches字段value值为资源名称的前缀，全部小写，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_110	matches字段value值为资源名称的前缀，大小写均存在，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_111	matches字段value值为资源名称的后缀，全部大写，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_112	matches字段value值为资源名称的后缀，全部小写，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_113	matches字段value值为资源名称的后缀，大小写均存在，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_114	matches字段value值为资源名称的中间部分，全部大写，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_115	matches字段value值为资源名称的中间部分，全部小写，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_116	matches字段value值为资源名称的中间部分，大小写均存在，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_117	matches字段value值长度为1，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_118	matches字段value值长度为255，查询资源实例成功
            # TC_TMS_QuerryResourceInstanceFilter_119	matches字段value值长度为256，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_120	matches字段value值长度为256，且前面含有多个空格查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_121	带必选参数和所有可选参数，查询成功
            # TC_TMS_QuerryResourceInstanceFilter_122	token无效，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_123	不带token，查看资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_124	resource_type不存在，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_125	resource_type缺失，查询资源实例失败
            # TC_TMS_QuerryResourceInstanceFilter_126	project_id缺失，查询资源失败
            # TC_TMS_QuerryResourceInstanceFilter_127	project_id不存在，查询资源失败
            # TC_TMS_QuerryResourceInstanceFilter_128	project_id为其他租户的project_id，查询资源失败
            code, rep = client.delete_resource(resource_type="nodes", id=node_id)
            assert code == 204
    except Exception:
        import traceback
        print traceback.print_exc()
        if node_id:
            code, resp = client.delete_resource(resource_type="nodes", id=node_id)
            assert code == 204
        raise Exception