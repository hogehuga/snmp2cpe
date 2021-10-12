#!/usr/bin/env python3

import argparse
import logging
from lib import scan, cpe

#logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

# option parse
parser = argparse.ArgumentParser(description='program description')
parser.add_argument("-ip", "--ipaddress", help="scan ip address", required=True)
parser.add_argument("-v", "--version", choices=['2c', '3c'], help="SNMP version", required=True)
parser.add_argument("-c", "--community", help="SNMP community name", required=True)
args = parser.parse_args()


# commandline arguments
logging.debug('Commandline arguments')
logging.debug('  Target IP     : %s', args.ipaddress)
logging.debug('  SNMP version  : %s', args.version)
logging.debug('  SNMP community: %s', args.community)

snmpString = scan.getSnmpString(args.ipaddress, args.version, args.community)
logging.debug("[return] getSnmpString")
logging.debug("  sysName : %s", snmpString[0])
logging.debug("  sysDescr: %s", snmpString[1])

cpeName = cpe.getCPEName(snmpString[0])
print(f"sysName  :{snmpString[0]}\ncpeName  :{cpeName}\nsysDescr :{snmpString[1]}")
