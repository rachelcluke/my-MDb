import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "8080")
os.environ.setdefault("SECRET_KEY", "6119b7f9fe594a52ddd1240a674db4e8876f94819e23382b1b97b0195fe75b9f")
os.environ.setdefault("DEBUG", "True")
#os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgresql:///my_mdb")