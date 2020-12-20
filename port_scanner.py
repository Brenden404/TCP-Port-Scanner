import socket


def tcp_connect_scan(target_ip, low_port, high_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        port_range = range(low_port, high_port + 1)  # Adding the +1 allows the for loop to include the highest port.
        for n in port_range:  # This statement iterates through each port number in port_range starting with the lowest.
            if s.connect_ex((target_ip, n)) == 0:  # s.connect_ex returns a 0 if connections succeeds.
                print(f"***Port {n} is open***")

            else:
                print(f"Port {n} is closed")

# def syn_scan(target_ip, low_port, high_port):
