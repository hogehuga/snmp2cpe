import logging
import re

def getCPEName(sysDescr):
    # CPE 2.3 like "cpe:2.3:o:cisco:ios:14.1\(2\)s2:*:*:*:*:*:*:*""
    
    if re.match(r'Cisco IOS Software.*IOS-?XE', sysDescr):
        # IOS-XE regexp must evaluate before IOS
        sysDescr = sysDescr.replace('\n', '')
        verAll = sysDescr.split()[sysDescr.split().index("Version") + 1]
        verMajor = re.findall(r'^.*[^,]', verAll)[0]
        ret = f"cpe:2.3:o:cisco:ios_xe:{verMajor.lower()}:*:*:*:*:*:*:*"
        return ret
    elif re.match(r'Cisco IOS Software', sysDescr):
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
    elif re.match(r'Juniper Networks, Inc.', sysDescr):
        verAll = sysDescr.split()[sysDescr.split().index("JUNOS") + 1]
        verMajor = re.findall(r'^[0-9]*.*R', verAll)[0][0:-1]
        verMaint = re.findall(r'R[0-9]*.*,', verAll)[0][0:-1]
        ret = f"cpe:2.3:o:juniper:junos:{verMajor}:{verMaint.lower()}:*:*:*:*:*:*"
        return ret
    elif re.match(r'Arista Networks EOS', sysDescr):
        verAll = sysDescr.split()[sysDescr.split().index("version") + 1]
        verMajor = re.findall(r'^[0-9].*', verAll)[0]
        ret = f"cpe:2.3:o:arista:eos:{verMajor.lower()}:*:*:*:*:*:*:*"
        return ret
    else:
        logging.info(
            "Can't match CPE regexp. Plz pull-request cpe.py and/or write snmpSysDescList.txt and/or Issue(welcome to issue only).")
        ret = "Can not match CPE."
        return ret
