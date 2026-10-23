import socket
targets =(input("Enter The IP Adress."))
common_ports ={
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Proxy"
}
print(f"\n scanning {targets} for common ports..\n")
for port, service in common_ports.items():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1.0)
        result= s.connect_ex((targets,port))
        if result==0:
                    print(f"[+] Port {port} ({service}) is OPEN")
            
        s.close()
    except Exception as e:
        print(f"[!] Error checking port {port}: {e}")