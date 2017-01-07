from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables(): #Runs the method below ONLY when we have the first request
    db.create_all() #This goes through our model .py files and creates a table based on
                    #__tablename__ and the Column representations. So importing the correct
                    #models/files is very important.
