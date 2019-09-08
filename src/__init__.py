import logging
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)
