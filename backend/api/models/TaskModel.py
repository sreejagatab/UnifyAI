# TaskModel.py
from .. import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    task_type = db.Column(db.String(50), nullable=False)
    input_data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, user_id, task_type, input_data):
        self.user_id = user_id
        self.task_type = task_type
        self.input_data = input_data

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "task_type": self.task_type,
            "input_data": self.input_data,
            "created_at": self.created_at
        }
