#--------------------------------------------------------------------------------------

#   USES Nmap to scan active port of TARGET HOST
#       And then carries out OS FINGRTPRINTING

#--------------------------------------------------------------------------------------


import nmap
import sys
import time

nm_scan = nmap.PortScanner()

print('\nRunning....\n')

nm_scanner = nm_scan.scan(sys.argv[1], '80' ,arguments='-O')
#The value returned to nm_scanner is in the form of a DICTIONARY.

#sys.argv : To take input and scan the "TARGET"
# 80 is port number
# -o argument is for fingerprinting

host_is_up = "The host is: "+nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"
port_open = "The port 80 is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"
method_scan = "The method of scanning is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"
guessed_os = "There is a %s percent chance that the host is running %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"

with open("%s.txt"%sys.argv[1],'w') as f:
    f.write(host_is_up+port_open+method_scan+guessed_os)
    f.write("\nReport generated "+time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))

print("\nFinished...")

