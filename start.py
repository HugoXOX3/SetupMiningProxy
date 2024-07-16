import time
import subprocess

pool1_command = "./xmrig-proxy -o pool.hashvault.pro:80 -u 87f29B57sn4N4G1cM1LtXga2REhxg7aV9XyX7PprrJHManB1wB1indnRQhmCpK8AjmNVhoiZgnbgbeTCqBt3JDMyT6U9q9Z -p x --bind 0.0.0.0:4444 --http-enabled --http-host 0.0.0.0 --restricted"
pool2_command = "./xmrig-proxy -o pool.hashvault.pro:80 -u solo:87f29B57sn4N4G1cM1LtXga2REhxg7aV9XyX7PprrJHManB1wB1indnRQhmCpK8AjmNVhoiZgnbgbeTCqBt3JDMyT6U9q9Z -p x --bind 0.0.0.0:5555 --http-enabled --http-host 0.0.0.0 --restricted"

switch_interval_minutes_1 = 55
switch_interval_minutes_2 = 5

while True:
    subprocess.Popen(pool1_command, shell=True)
    time.sleep(switch_interval_minutes_1*60)
    subprocess.Popen("taskkill /IM xmrig-proxy.exe /F", shell=True)
    subprocess.Popen(pool2_command, shell=True)
    time.sleep(switch_interval_minutes_2*60)
    subprocess.Popen("taskkill /IM xmrig-proxy.exe /F", shell=True)
