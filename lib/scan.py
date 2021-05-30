import logging
import traceback

def getSnmpString(addr, ver, comm):
    from ipaddress import IPv4Address
    import subprocess, ipaddress, re

    logging.debug("[call] scan/getCPE")
    logging.debug("  addr is: %s", addr)
    logging.debug("  ver  is: %s", ver)
    logging.debug("  comm is: %s", comm)

    snmpSysDescr = ".1.3.6.1.2.1.1.1.0"
    snmpSysName = ".1.3.6.1.2.1.1.5.0"

    # check ipaddress data
    try:
        chkaddr = ipaddress.IPv4Address(addr)
    except:
        logging.error(" Incorrect IP Address: %s", addr)
        exit(1)

    if chkaddr.is_multicast or chkaddr.is_global or chkaddr.is_loopback or chkaddr.is_unspecified or chkaddr.is_reserved:
        logging.error("Bad IP Address: %s", addr)
        logging.error("  is_multicast: %s", chkaddr.is_multicast)
        logging.error("  is_global: %s", chkaddr.is_global)
        logging.error("  is_loopback: %s", chkaddr.is_loopback)
        logging.error("  is_unspecified: %s", chkaddr.is_unspecified)
        logging.error("  is_reserved: %s", chkaddr.is_reserved)
        exit(1)

    logging.debug("IPAddress check is ok")

    walkstring = 'snmpget -v ' + str(ver) + ' -c ' + comm + ' ' + addr
    logging.debug("snmpgetting: %s", walkstring)

    try:
        #       resSysName =subprocess.run("snmpwalk -v 2c -c public 192.168.1.26 .1.3.6.1.2.1.1.5.0", shell=True, stdout=subprocess.PIPE)
        resSysName = subprocess.run(
            walkstring + ' .1.3.6.1.2.1.1.5.0', shell=True, stdout=subprocess.PIPE)
        resSysDescr = subprocess.run(
            walkstring + ' .1.3.6.1.2.1.1.1.0', shell=True, stdout=subprocess.PIPE)
    except OSError as e:
        logging.error("catch OSError:", e)
    except subprocess.CalledProcessError as e:
        logging.error("catch subprocess.CalledProcessError\n:", e)
    except:
        traceback.format_exc()
        logging.error("catch subprocess err")

    logging.debug("snmpget results")
    logging.debug("  sysName : %s", resSysName.stdout.strip().decode())
    logging.debug("  sysDescr: %s", resSysDescr.stdout.strip().decode())

    return re.sub(r'^.*STRING:\ ', '', resSysName.stdout.strip().decode()), re.sub(r'^.*STRING:\ ', '', resSysDescr.stdout.strip().decode())
