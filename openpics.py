import urllib.request
import os
import tarfile 
import logging
from config import PICS_URL, PICS_DEST_PATH

def extract_file():
	"""
	this function downloads tar file and extracts it in the configured directory
	""" 
	try:
		logging.info("start downloading pictures...")
		picsfile = urllib.request.urlretrieve(PICS_URL)
		file = tarfile.open(picsfile[0], 'r:gz')
		logging.info("downloaded pictures completed!")
		cwd = os.getcwd()
		os.chdir(PICS_DEST_PATH)
		file.extractall()
		file.close()
		os.chdir(cwd)
		logging.info("pictures extracted in %s" % PICS_DEST_PATH)
	except urllib.error.HTTPError as e:
		logging.error("couldn't download file from URL specified. check if the URL is correct")
		logging.exception(e)
	except tarfile.CompressionError as e:
		logging.error("couldn't compress downloaded file - check file type")
	except Exception as e:
		logging.exception(e)
		



def check_dest_dir():
	"""
	this function checks if the configured directory exists, if not creates it
	"""
	if not os.path.exists(PICS_DEST_PATH):
		os.mkdir(PICS_DEST_PATH)
		logging.info("Directory created %s" % PICS_DEST_PATH)

def download_pics():
    check_dest_dir()
    extract_file()



	
	
	
	 
