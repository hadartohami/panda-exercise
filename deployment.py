import openpics
import os
import healthcheck
import subprocess
import time
from config import EXERCISE_DIR_PATH

# download tar file and extract in ./public/images
openpics.download_pics()

# change directory, start up docker-compose
os.chdir(EXERCISE_DIR_PATH)
os.system("sudo docker-compose up -d")

# wait until docker-compose finish 
time.sleep(20)

# app healthcheck, if fails docker compose goes down
status = healthcheck.healthcheck()
if status == False:
	print("App is unhealthy, going down :(")
	os.system("sudo docker-compose down")
else:
	print("Everything is great!")
