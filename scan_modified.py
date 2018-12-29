import subprocess
import sys
from subprocess import Popen, PIPE, STDOUT
import os

def _return_barcode (directory):
    p = subprocess.Popen(directory, stdout=subprocess.PIPE, stderr = subprocess.STDOUT, shell=True)
    while True:
        line = p.stdout.readline()
        if not line:
            break
        copy = (str)(line)
        temp1, temp2 = copy.split(':')
        temp2 = temp2.strip()
        if len(temp2) > 0:
            break
    subprocess.call(["taskkill","/F","/IM","zbarcam.exe"])
    return temp2

directory = "C://Program Files (x86)//ZBar//bin//zbarcam.exe"




