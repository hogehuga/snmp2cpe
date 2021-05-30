import logging
import re

def getCPEName(sysDescr):
    # CPE 2.3 like "cpe:2.3:o:cisco:ios:14.1\(2\)s2:*:*:*:*:*:*:*""
    
    if re.match(r'Cisco IOS Software', sysDescr):
        # get version string "15.1(4)M3,"
        # Version A.B(C)D
        #   major release: A.B(Train:15.1)
        #   maintenance relerease: C(Throttle:4)
        #   Extended major release: D (or none) (Train+Rebuild:M(15.1M) + 3)
        sysDescr = sysDescr.replace('\n', '')
        verAll = sysDescr.split()[sysDescr.split().index("Version") + 1]
        verMajor = re.findall(r'^[0-9]*\.[0-9]*', verAll)[0]
        verMaint = re.findall(r'\(\w*\)', verAll)[0][1:-1]
        verExtRel = re.findall(r'\).*', verAll)[0][1:-1]
        ret = f"cpe:2.3:o:cisco:ios:{verMajor}\({verMaint}\){verExtRel}:*:*:*:*:*:*:*"
        return ret
    elif re.match(r'Cisco Internetwork Operating System Software IOS', sysDescr):
        sysDescr = sysDescr.replace('\n', '')
        verAll = sysDescr.split()[sysDescr.split().index("Version") + 1]
        verMajor = re.findall(r'^[0-9]*\.[0-9]*', verAll)[0]
        verMaint = re.findall(r'\(\w*\)', verAll)[0][1:-1]
        verExtRel = re.findall(r'\).*', verAll)[0][1:-1]
        ret = f"cpe:2.3:o:cisco:ios:{verMajor}\({verMaint}\){verExtRel}:*:*:*:*:*:*:*"
        return ret
    else:
        logging.info(
            "Can't match CPE regexp. Plz pull-request cpe.py and/or write snmpSysDescList.txt and/or Issue(welcome to issue only).")
        ret = "Can not match CPE."
        return ret
