import os

shutdown = input("Shutdown your PC ?(yes/no): ")

if shutdown == 'no':
  exit()
else:
  os.system("Shutdown /s /t 1")
