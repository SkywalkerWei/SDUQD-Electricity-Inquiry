import json
import requests

BUILDINGS = eval("""
[
    {
         "buildingid":"1574231830",
         "building":"T1"
    },
    {
         "buildingid":"1574231833",
         "building":"T2"
    },
    {
         "buildingid":"1574231835",
         "building":"T3"
    },
    {
         "buildingid":"1503975832",
         "building":"S1"
    },
    {
         "buildingid":"1503975890",
         "building":"S2"
    },
    {
         "buildingid":"1503975967",
         "building":"S5"
    },
    {
         "buildingid":"1503975980",
         "building":"S6"
    },
    {
         "buildingid":"1503975988",
         "building":"S7"
    },
    {
         "buildingid":"1503975995",
         "building":"S8"
    },
    {
         "buildingid":"1503976004",
         "building":"S9"
    },
    {
         "buildingid":"1503976037",
         "building":"S10"
    },
    {
         "buildingid":"1599193777",
         "building":"S11-13"
    },
    {
         "buildingid":"1661835249",
         "building":"B1"
    },
    {
         "buildingid":"1661835256",
         "building":"B2"
    },
     {
         "buildingid":"1661835273",
         "building":"B5"
    },
    {
         "buildingid":"1693031698",
         "building":"B9"
    },
    {
         "buildingid":"1693031710",
         "building":"B10"
    }
]
""")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 14; 23013RK75C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/131.0.6778.39 Mobile Safari/537.36/Synjones-E-Campus/2.3.24/&cn&/53",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://mcard.sdu.edu.cn",
    "Referer": "https://mcard.sdu.edu.cn/charge-app/",
    # "Synjones-Auth": , # 此处需要登录认证信息填充
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Sec-Ch-Ua-Platform": "Android",
    "Sec-Ch-Ua": '"Android WebView";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?1",
    "Accept": "application/json, text/plain, */*"
}

def building_to_id(building):
    for _building in BUILDINGS:
        if _building['building'] == building:
            return _building['buildingid']
    print('ERROR: Wrong building number')
    input()
    exit(-1)

def query(account, building, room):
    data=f"feeitemid=410&type=IEC&level=3&campus=%E9%9D%92%E5%B2%9B%E6%A0%A1%E5%8C%BA%26%E9%9D%92%E5%B2%9B%E6%A0%A1%E5%8C%BA&building={building_to_id(building)}&room={room}"
    """
    :param account: 6位校园卡账号
    :param building: 宿舍楼名称, ['T1', 'T2', 'T3', 'S1', 'S2', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11-13', 'B1', 'B2', 'B5', 'B9', 'B10']
    :param room: 宿舍号
    :return: 电余量
    """
    try:
        response = requests.post('https://mcard.sdu.edu.cn/charge/feeitem/getThirdData', headers=HEADERS, data=data)
        response.raise_for_status()
        return json.loads(response.text)['map']['showData']['信息'][8:]
    except Exception as e:
        print(e)
        exit(-1)
    '''
    data = {
        "jsondata": json.dumps({
            "query_elec_roominfo": {
                "aid": "0030000000002505",
                "account": str(account),
                 "room": {
                     "roomid": room,
                     "room": room
                 },
                "floor": {
                    "floorid": "",
                    "floor": ""
                },
                "area": {
                    "area": "青岛校区",
                    "areaname": "青岛校区"
                },
                "building": {
                     "buildingid": building_to_id(building),
                     "building": building
                }
            }
        }, ensure_ascii=False),"funname": "synjones.xuepay.sdu","json": "true"
    }
    '''
    '''
    try:
        # response = requests.post('http://10.100.1.24:8988/web/Common/Tsm.html', headers=HEADERS, data=data, timeout=3)
        # response = requests.post('http://10.100.1.24:8988/web/common/checkEle.html', headers=HEADERS, data=data, timeout=3)
        # response = requests.post('http://222.206.1.180', headers=HEADERS, data=data, timeout=3)
        # response = requests.post('https://222.206.1.213:8755/ppage/service', headers=HEADERS, data=data, timeout=3, verify=False)
        response = requests.post('https://mcard.sdu.edu.cn/charge/feeitem/getThirdData', headers=HEADERS, data=data, timeout=3)
        # print(response.text)
        # electricity = json.loads(response.text)['query_elec_roominfo']['errmsg']
        return json.loads(response.text)['map']['showdata']['信息'][8:]
    '''