import requests
from config import HEALTHCHECK_URL

def healthcheck():
	"""
	this function checks status code of http get request
	"""
	try:
		status = requests.get(HEALTHCHECK_URL, timeout=10)
		if status.status_code == 200:
			return True
		return False
	except:		
		return False


