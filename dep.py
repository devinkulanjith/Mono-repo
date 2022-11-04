import subprocess


cmd = "git diff --name-only HEAD^ HEAD"
subprocess.Popen(cmd, stdout=True, shell=True)