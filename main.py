import subprocess
import os
from time import sleep
from multiprocessing import Process
from signal import SIGKILL
from os import kill

subprocess.Popen("vtex use testautomation", shell=True)
sleep(10)

currentDirectory = os.getcwd()

apps = open('read_file.txt','r')
appList = apps.readlines()

def appLink():
    subprocess.Popen("echo enter 4", shell=True)
    cmd = "vtex link > output.txt&"
    subprocess.Popen(cmd, stdout= True, shell=True)


for app in appList:
    os.chdir(currentDirectory + '/' + app.replace("\n",""))
    subprocess.Popen("echo enter 1", shell=True)
    subprocess.Popen("touch output.txt", shell=True)
    sleep(3)
    process = Process(target= appLink)
    process.start()
    var = True
    subprocess.Popen("echo enter 2", shell=True)
    while var:
        with open('output.txt', 'r', encoding='utf-8') as file:
            sleep(5)
            contents = file.read()
            sentence = 'App linked successfully'
            subprocess.Popen("echo enter 3", shell=True)
            result = contents.find(sentence)
            if result != -1:
                var = False
                print(app + " app link successful ... process will be killed")
                # subprocess.Popen("rm output.txt", shell=True)
                try:
                    kill(process.pid, SIGKILL)
                except: 
                    print("something went wrong")
