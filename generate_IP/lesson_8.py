from functions import generate_list_ip_address, get_rand_0_255, get_ip

number = 1
mask = "xxx.xx.xx.x"
ip_list = generate_list_ip_address(number, repeat=False, sort=True)
print(ip_list)