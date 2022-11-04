import os
# import subprocess


# currentDirectory = os.getcwd()

# apps = open('president_order.txt','r')
# appListOrder = apps.readlines()

# vtexAppLinkOrder = []

# subprocess.Popen("vtex use testautomation", shell=True)


# appListString = os.environ.get("CHANGED_DIRECTORIES")

# appList = appListString.split('[')[1].split(']')[0].split(',')

# if len(appList) != 0:
#     for app in appListOrder:
#        appName = app.replace('\n','')
#        if appName in appList:
#            vtexAppLinkOrder.append(appName)

#     for app in vtexAppLinkOrder:
#         os.chdir(currentDirectory + '/' + app)
appListString = os.environ.get("CHANGED_FILES")
print('applist', appListString)