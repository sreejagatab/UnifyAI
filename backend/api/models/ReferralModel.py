# ReferralModel.py
from .. import db

class ReferralModel(db.Model):
    __tablename__ = 'referrals'
    
    id = db.Column(db.Integer, primary_key=True)
    referrer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    referred_email = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(20), default='pending')

    def __init__(self, referrer_id, referred_email):
        self.referrer_id = referrer_id
        self.referred_email = referred_email

    def to_dict(self):
        return {
            "id": self.id,
            "referrer_id": self.referrer_id,
            "referred_email": self.referred_email,
            "status": self.status
        }
