import http.client as http
import datetime
import speedtest

print("Checking internet status...")

timestamp = str(datetime.datetime.now())
wifi = speedtest.Speedtest()

def check_internet_status():
    try:
        conn = http.HTTPSConnection("8.8.8.8", timeout=5)
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        return False

def get_external_ip():
    try:
        conn = http.HTTPConnection("ipinfo.io", timeout=5)
        conn.request("GET", "/json")
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data.decode("utf-8")
    except:
        return "Error"


# if file doesn't exist, create it
try:
    with open("internet-status.log", "a") as f:
        f.write(timestamp + "\n")
        pass
except FileNotFoundError:
    with open("internet-status.log", "w") as f:
        f.write(timestamp + "\n")

if check_internet_status():
    print("Internet is up!")
    ip = get_external_ip()
    print("External IP: " + ip)
    down = wifi.download()
    print("Download speed: " + str(down) + " Mbps")
    up = wifi.upload()
    print("Upload speed: " + str(up) + " Mbps")
    with open("internet-status.log", "a") as f:
        f.write(ip + "\n")
        f.write("Download speed:" + str(down) + "\n")
        f.write("Upload speed:" + str(up) + "\n")
else:
    print("Internet is down!")
    with open("internet-status.log", "a") as f:
        f.write("Internet is down!\n")
