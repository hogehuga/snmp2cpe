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

if __name__ == "__main__":
    unittest.main()
