import os,sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
from service import make_app
application = make_app()
