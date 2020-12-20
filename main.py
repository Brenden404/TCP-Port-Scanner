import port_scanner


print("Please enter the IP address of the target host:")
HOST = input()

print("Please enter the lowest port number in the range you wish to scan:")
LOW_PORT = int(input())

print("Please enter the highest port number in the range you wish to scan:")
HIGH_PORT = int(input())

port_scanner.tcp_connect_scan(HOST, LOW_PORT, HIGH_PORT)
