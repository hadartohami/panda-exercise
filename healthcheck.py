import requests
import logging
from config import HEALTHCHECK_URL

def healthcheck():
	"""
	this function checks status code of http get request
	"""
	try:
		logging.info("healthcheck: check status code")
		status = requests.get(HEALTHCHECK_URL, timeout=10)
		if status.status_code == 200:
			logging.info("Healthcheck is OK!")
			return True
		logging.error("Application is not healthy - check DB or Disk connectivity")
		return False
	except requests.exceptions.RequestException as e:		
		logging.error("Application is not healthy - couldn't connect to Website")
		logging.exception(e)
		return False

