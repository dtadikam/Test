
import subprocess

out = subprocess.Popen(['git', 'clone', 'https://github.com/dtadikam/Test.git'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
print(stdout)
print(stderr)

f = open("D://Users//tadikama//Desktop//Test//sample.txt", "r").readlines()
for x in f:
  print(x)
