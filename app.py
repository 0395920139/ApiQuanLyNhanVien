from flask import Flask
from controller.FlaskAppWrapper import FlaskAppWrapper
from flask_login import LoginManager


flask_app = Flask(__name__)
login_manager = LoginManager()
# login_manager.unauthorized()
login_manager.init_app(flask_app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"status":"fail","message":"Please login"})


def process_data(results):
    list_result = []
    for item in results:
        list_result.append(item.obj_person())
    return list_result


# SQLALCHEMY_DATABASE_URI': 'mysql://root:Minh123456@127.0.0.1:3306/flask_app
obj = {
    'SECRET_KEY':'secret-key-goes-here',
    'SQLALCHEMY_DATABASE_URI':'mysql://root:Minh191000@127.0.0.1:3306/flask_employee',
    "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    "MAX_CONTENT_LENGTH":500*1000*1000,
}

app = FlaskAppWrapper(flask_app,obj)

db = app.db
# jwt = JWT(app, self.authenticate, self.identity)

# import controller 
from controller.TestController import *
from controller.UserController import *
from controller.Auth import *
from controller.EmpController import *



# import model

from model.Employee import *
from model.User import *
# test = ViewController()

# app.add_enpoint("/","test",test.index)





if __name__ == "__main__":
    app.run(host="127.0.0.1",debug=True,port=8080)