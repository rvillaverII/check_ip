import ipaddress

while True:
    input_ip = input("Enter IP address (Type x to End) ")
    try:
        if input_ip == "x":
            break
        elif type(ipaddress.ip_address(input_ip)) is ipaddress.IPv4Address:
            print("{} is a Valid IP address" .format(input_ip))
        elif type(ipaddress.ip_address(input_ip)) is ipaddress.IPv6Address:
            print("{} is a Valid IPv6 address" .format(input_ip))
    except:
        print("{} is not a Valid IP address" .format(input_ip))