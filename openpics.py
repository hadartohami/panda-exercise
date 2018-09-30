import urllib.request
import os
import tarfile 
from config import PICS_URL, PICS_DEST_PATH

def extract_file():
	"""
	this function downloads tar file and extracts it in the configured directory
	""" 
	picsfile = urllib.request.urlretrieve(PICS_URL)
	file = tarfile.open(picsfile[0], 'r:gz')
	cwd = os.getcwd()
	os.chdir(PICS_DEST_PATH)
	file.extractall()
	file.close()
	os.chdir(cwd)



def check_dest_dir():
	"""
	this function checks if the configured directory exists, if not creates it
	"""
	if not os.path.exists(PICS_DEST_PATH):
		os.mkdir(PICS_DEST_PATH)

def download_pics():
    check_dest_dir()
    extract_file()



	
	
	
	 
