import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/dev/python/wsgi/flaskapp/")
from main import app as application