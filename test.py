from datetime import datetime
from re import S
import time
import http.client

TESTER_NUM=30

class Request:
    def __init__(self):
        self.address = "192.168.1.37:81"
        self.header = {
            "Content-Type": "application/json"
        }
        self.method = "POST"
        self.url = ""
        self.data = ""
        self.c_times = 0
        self.name = ""

    def s_data(self, data):
        self.data = data
        return self

    def s_url(self, url):
        self.url = url
        return self

    def s_c_times(self, c_times):
        self.c_times = c_times
        return self

    def s_name(self, name):
        self.name = name
        return self

    def exec(self):
        conn = http.client.HTTPConnection("192.168.1.46:8087")
        conn.request(method=self.method, url=self.url, body=self.data, header=self.header)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")


TESTLIST = [
    Request().s_url("/bank-kpi/system/psmApi/upPsmSysMonitorItems").s_data([{
        "bankCode": "72712",
        "psmIp": "192.168.1.84",
        "itemKey": "PSM.memory.status",
        "itemValue": "31.2 ",
        "itemUnit": "GiB",
        "itemText": "Network Interfaces:\n Name: eth0 (eth0)\n  MAC Address: 48:b0:2d:3c:87:c7\n  MTU: 1500, Speed: 104857600\n  IPv4: [192.168.1.84/24]\n  IPv6: [fe80:0:0:0:969b:a846:3cea:fa17/64]\n  Traffic: received 139765218 packets/156.8 GiB (0 err, 18092 drop); transmitted 71455587 packets/61.3 GiB (0 err, 0 coll);\nPhysical Memory: \n Available: 17.9 GiB/31.2 GiB\nVirtual Memory: \n Swap Used/Avail: 28.8 MiB/15.6 GiB, Virtual Memory In Use/Max=13.3 GiB/31.2 GiB\n",
        "delFlag": "0",
        "createTime": "2021-08-28 15:54:10"
    }]).s_c_times(10),
    Request().s_url("/bank-kpi/system/psmApi/upPsmManagerLog ").s_data([
        {
            "bankCode": "72712",
            "psmIp": "192.168.1.84",
            "itemKey": "PSM.memory.status",
            "itemValue": "31.2 ",
            "itemUnit": "GiB",
            "itemText": "Network Interfaces:\n Name: eth0 (eth0)\n  MAC Address: 48:b0:2d:3c:87:c7\n  MTU: 1500, Speed: 104857600\n  IPv4: [192.168.1.84/24]\n  IPv6: [fe80:0:0:0:969b:a846:3cea:fa17/64]\n  Traffic: received 139765218 packets/156.8 GiB (0 err, 18092 drop); transmitted 71455587 packets/61.3 GiB (0 err, 0 coll);\nPhysical Memory: \n Available: 17.9 GiB/31.2 GiB\nVirtual Memory: \n Swap Used/Avail: 28.8 MiB/15.6 GiB, Virtual Memory In Use/Max=13.3 GiB/31.2 GiB\n",
            "delFlag": "0",
            "createTime": "2021-08-28 15:54:10"
        }]).s_c_times(10),
    Request().s_url("/bank-kpi/system/psmApi/getDeviceList?bankCode=72712&key=").s_c_times(3)]


def testMain():
    for t in TESTLIST:
        for i in range(t.c_times*TESTER_NUM):
            print(t.url," 开始测试|第【",i+1,"】次|结果",end="")
            try:
                res=t.exec()
                print("【成功】:",res)
            except Exception as e:
                print("【失败】:",str(e))




def timer(n):
    timeCounter=1;
    while True:
        print(timeCounter," times test=======================")
        testMain()
        print(timeCounter," times test end=======================")
        timeCounter+=1
        time.sleep(n)


if __name__ == '__main__':
    # timer(5)

     for t in TESTLIST:
            for i in range(t.c_times*TESTER_NUM):
                print(t.url," 开始测试|第【",i+1,"】次|结果",end="")
            try:
                res=t.exec()
                print("【成功】:",res)
            except Exception as e:
                print("【失败】:",str(e))
