import argparse
import nmap

# Parse arguments
parser = argparse.ArgumentParser(description='Scan hosts with nmap')
parser.add_argument('host', help='Host to scan')
parser.add_argument('-p', '--port', help='Port')
parser.add_argument('-a', '--args', help='Aditional Args')
parser.add_argument('-r', '--root', action='store_true', help='Run queries as super user.')
args = parser.parse_args()

print("Scanning host: ", args.host)
if args.port is not None:
    print("Scanning port: ", args.port)
# Execute scan.
nm = nmap.PortScanner()
nm.scan(
    args.host, 
    args.port,
    # Si vienen argumentos los mandamos, si no, mandamos el valor por defecto de la librería
    arguments=args.args if args.args is not None else "-sV" ,
    sudo=args.root
)

# Print results.
print(nm.command_line())
print(nm.scaninfo())
all_hosts = nm.all_hosts()
print(all_hosts)

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))