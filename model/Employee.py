from app import db

# tạo ra model tương ứng với 1 bảng trong database

# flask db init 
# => khởi tạo 
# flask db migrate -m "init db"
# flask db upgrade

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.String(255))
    file_name = db.Column(db.String(255))

    def __init__(self,name, email, address, file_name) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.file_name = file_name

    def obj_person(self):
        obj = dict(id = self.id, name = self.name, address = self.address,email = self.email,  file_name = self.file_name)
        return obj         