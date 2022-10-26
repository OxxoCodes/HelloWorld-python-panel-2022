def checkIpBlacklisted(ip, blacklisted):
    if ip in blacklisted:
        print("IP " + ip + " is blacklisted.")
        return True
    else:
        print("IP " + ip + " is not blacklisted.")


blackListedIPs = ["192.168.12.43", "10.3.147.243", "18.49.43.254"]

print("What is your IP?")
userIP = input()
userIPIsBlackListed = checkIpBlacklisted(userIP, blackListedIPs)

if not userIPIsBlackListed:
    print("Access Granted")
else:
    print("Access denied")