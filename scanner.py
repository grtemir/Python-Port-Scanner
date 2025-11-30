import socket # For network connections
import sys    # For system-specific parameters and functions
from datetime import datetime # for timestamping

#Get target ip from user
target = input("Enter target ip address: ") 

timeout=float(input("Enter timeout second: "))

startport=int(input("Starting port(include): "))

finishtport=int(input("Finishing port(include): "))


#Resolve hostname to Ip
target_ip=socket.gethostbyname(target)

print("-"*50)
print("Scannning target: " + target_ip)
print("Time started: " + str(datetime.now()))
print("-"*50)

with open("reports.txt","w",encoding="utf-8") as rep:
    rep.write(f"---Report: {datetime.now()}----\n")
    rep.write(f"Target: {target_ip}\n")
    print("-"*40)


try:
    #loop through port startport to finishtport
    for port in range(startport,finishtport+1):
        
        #create an socket object
        s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        #set timeout to timeout seconds
        s.settimeout(timeout)

        #Attempt to connect port
        result=s.connect_ex((target_ip,port))

        #if port open result is zero
        if result ==0:
            #f is important to apply { }
            print(f"Port {port}: OPEN")
            with open("reports.txt", "a", encoding="utf-8") as dosya:
                dosya.write(f"Port {port}: AÇIK\n")
            try:
                if port==80:
                    #port 80,443,53,1433 etc dont give message without payload
                    s.send(b'GET / HTTP/1.1\r\n\r\n')

                #read first 1024byte
                banner=s.recv(1024).decode()

                
                rows= banner.split('\n')
                #To eleminate rows except version info
                if port==80:
                    for row in rows:
                        if "Server:" in row:
                            print(f"-->Version: {row.strip()}")
                            with open("reports.txt","a",encoding="utf-8") as rep:
                                rep.write(f"-->Version: {row.strip()}\n")
                else:
                    print(f"-->Version: {rows[0].strip()}")
                    with open("reports.txt","a",encoding="utf-8") as rep:
                        rep.write(f"-->Version: {rows[0].strip()}\n")

            except socket.timeout:
                print("-->Timout-not found version info")
            except:
                print("--> data error")
        s.close()
except KeyboardInterrupt:
    print("User cancelled scan") 
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Could not connect to server...")
    sys.exit()
except ValueError:
    print("Please enter just number for port and timeout values")

