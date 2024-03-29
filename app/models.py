from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Users(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  is_active = db.Column(db.Boolean, default=True)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)


class Groups(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=True, unique=True)
  description = db.Column(db.String(128))
  private = db.Column(db.Boolean, default=True)
  admins = db.Column(db.PickleType)
  members = db.Column(db.PickleType, default=[]) 
  is_active = db.Column(db.Boolean, default=True)