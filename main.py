import subprocess
import os
from time import sleep
from multiprocessing import Process
from signal import SIGKILL
from os import kill

subprocess.Popen("vtex use testautomation", shell=True)
sleep(5)

currentDirectory = os.getcwd()

apps = open('read_file.txt','r')
appList = apps.readlines()

num = os.environ.get("INPUT_NUM")
print('check',num)
# def appLink():
#     cmd = "echo 'yes' |vtex link > output.txt"
#     subprocess.Popen(cmd, stdout= True, shell=True)


# for app in appList:
#     os.chdir(currentDirectory + '/' + app.replace("\n",""))
#     process = Process(target= appLink)
#     process.start()
#     var = True
#     sleep(3)
#     while var:
#         with open('output.txt', 'r', encoding='utf-8') as file:
#             sleep(5)
#             contents = file.read()
#             sentence = 'App linked successfully'
#             result = contents.find(sentence)
#             if result != -1:
#                 var = False
#                 print(app + " app link successful ... process will be killed")
#                 subprocess.Popen("rm output.txt", shell=True)
#                 try:
#                     kill(process.pid, SIGKILL)
#                 except: 
#                     print("something went wrong")
