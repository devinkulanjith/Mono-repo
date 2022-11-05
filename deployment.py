import os
import subprocess


# currentDirectory = os.getcwd()

# apps = open('president_order.txt','r')
# appListOrder = apps.readlines()

# vtexAppLinkOrder = []


 # Diff HEAD with the previous commit

          # Check if a file under docs/ or with the .md extension has changed (added, modified, deleted)

# cmd = "git diff --name-only HEAD^ HEAD"
# subprocess.Popen(cmd, stdout=True, shell=True)


# appListString = os.environ.get("CHANGED_DIRECTORIES")

# appList = appListString.split('[')[1].split(']')[0].split(',')

# if len(appList) != 0:
#     for app in appListOrder:
#        appName = app.replace('\n','')
#        if appName in appList:
#            vtexAppLinkOrder.append(appName)

#     for app in vtexAppLinkOrder:
#         os.chdir(currentDirectory + '/' + app)

p1 = subprocess.Popen("${{ steps.changed-files.outputs.all_changed_files }}", stdout=True, shell=True)