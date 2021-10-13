import unittest
#from cpe import getCPEName
import cpe


class TestgetCPEName(unittest.TestCase):

    def test_getCPENameCisco01(self):
        sysDescr = "Cisco IOS Software, 2800 Software (C2800NM-ADVENTERPRISEK9-M), Version 15.1(4)M3, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2011 by Cisco Systems, Inc.\nCompiled Tue 06-Dec-11 16:21 by prod_rel_team"
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:cisco:ios:15.1\(4\)M3:*:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)
    
    def test_getCPENameCisco02(self):
        sysDescr = "Cisco IOS Software, C181X Software (C181X-ADVENTERPRISEK9-M), Version 15.1(4)M4, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2012 by Cisco Systems, Inc.\nCompiled Tue 20-Mar-12 23:34 by prod_rel_team"
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:cisco:ios:15.1\(4\)M4:*:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)

    def test_getCPENameCisco03(self):
        sysDescr = "Cisco Internetwork Operating System Software IOS (tm) s72033_rp Software (s72033_rp-JK9SV-M), Version 12.2(17d)SXB11, RELEASE SOFTWARE (fc1)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2005 by cisco Systems, Inc."
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:cisco:ios:12.2\(17d\)SXB11:*:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)

    def test_getCPENameCisco04(self):
        sysDescr = "Cisco IOS Software [Gibraltar], Catalyst L3 Switch Software (CAT9K_LITE_IOSXE), Version 16.12.4, RELEASE SOFTWARE (fc5)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2020 by Cisco Systems, Inc.\nCompiled Thu 09-Jul-20 19:31 by m"
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:cisco:ios_xe:16.12.4:*:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)

    def test_getCPENameCisco05(self):
        sysDescr = "Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500es8-UNIVERSALK9-M), Version 03.06.07.E RELEASE SOFTWARE (fc3)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2017 by Cisco Systems, Inc.\nCompiled Wed"
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:cisco:ios_xe:03.06.07.e:*:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)

    def test_getCPENameJuniper01(self):
        sysDescr = "Juniper Networks, Inc. mx240 internet router, kernel JUNOS 18.4R3-S7.2, Build date: 2021-02-03 13:31:24 UTC Copyright (c) 1996-2021 Juniper Networks, Inc."
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:juniper:junos:18.4:r3-s7.2:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)

    def test_getCPENameJuniper02(self):
        sysDescr = "Juniper Networks, Inc. ex4300-32f Ethernet Switch, kernel JUNOS 20.4R2-S2.2, Build date: 2021-08-12 00:07:44 UTC Copyright (c) 1996-2021 Juniper Networks, Inc."
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:juniper:junos:20.4:r2-s2.2:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)

    def test_getCPENameArista(self):
        sysDescr = "Arista Networks EOS version 4.23.0F running on an Arista Networks DCS-7050TX-64"
        ret = cpe.getCPEName(sysDescr)
        CPE = "cpe:2.3:o:arista:eos:4.23.0f:*:*:*:*:*:*:*"
        self.assertEqual(ret, CPE)
        
if __name__ == "__main__":
    unittest.main()
