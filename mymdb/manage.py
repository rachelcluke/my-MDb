"""
def deploy():
	from app import create_app,db
	from flask_migrate import upgrade,migrate,init,stamp
	from models import User

	app = create_app()
	app.app_context().push()
	db.create_all()

	#migrate db to latest revision
	init()
	stamp()
	migrate()
	upgrade()

#imports create_app from run.py	
deploy()
"""
