# SubscriptionModel.py
from .. import db

class SubscriptionModel(db.Model):
    __tablename__ = 'subscriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    plan_name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime, server_default=db.func.now())
    end_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, plan_name, end_date=None):
        self.user_id = user_id
        self.plan_name = plan_name
        self.end_date = end_date

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "plan_name": self.plan_name,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
