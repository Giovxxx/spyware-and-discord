import time
import webbrowser
import subprocess
import platform
import sys
import os 
import psutil
def restart_computer():
    subprocess.call(["shutdown", "-r", "-t", "0"])

time.sleep(5)

#url = 'https://youtu.be/xvFZjo5PgG0?si=iJGfaVTDQ1fbqwe3'
num_of_times = 3

#f#or i in range(num_of_times):
 #   webbrowser.open_new(url)

print(r"hello World HAHAHAHAHHAHAHA you fool")


print(platform.system())


status = os.system('systemctl is-active --quiet service-name')
print(status)