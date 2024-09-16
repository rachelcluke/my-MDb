import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "8080")
os.environ.setdefault("SECRET_KEY", "7even")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgresql:///my_mdb")