import os
from dotenv import load_dotenv

load_dotenv(".env")
BACKUP_DIR = os.getenv('BACKUP_DIR')
os.system('open "%s"' % BACKUP_DIR)
