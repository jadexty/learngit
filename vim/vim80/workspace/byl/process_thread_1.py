import subprocess
child = subprocess.Popen(["ping","-t","www.google.com"])
print("parent process")
