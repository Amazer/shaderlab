import subprocess
filename='debug.log'
command='tail -f '+filename+' '
popen=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
while True:
    line=popen.stdout.readline().strip()
    print line
