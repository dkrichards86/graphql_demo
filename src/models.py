from flask import current_app, url_for
from flask_sqlalchemy import BaseQuery
from sqlalchemy.dialects import postgresql

from src import db


class PKMixin:
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)


class CRUDMixin:

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        return db.session.commit()


class BaseModel(PKMixin, CRUDMixin, db.Model):
    __abstract__ = True


class User(BaseModel):
    __tablename__ = "users"
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)


class Ride(BaseModel):
    __tablename__ = "rides"
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    capacity = db.Column(db.Integer)
    wheelchair = db.Column(db.Boolean)
    status = db.Column(db.String)

    # ORM Relationship
    user = db.relationship("User", uselist=False, backref="ride")


class Schedule(BaseModel):
    __tablename__ = "schedules"


class ScheduleStop(BaseModel):
    __tablename__ = "schedule_stops"
    schedule_id = db.Column(db.Integer, db.ForeignKey("schedules.id"))
    address = db.Column(db.String)
    latitude = db.Column(db.Numeric(8, 5))
    longitude = db.Column(db.Numeric(8, 5))
    timestamp = db.Column(db.DateTime, nullable=False)

    # ORM Relationship
    schedule = db.relationship("Schedule", backref="stops", order_by="ScheduleStop.timestamp")


class ScheduleStopRide(BaseModel):
    __tablename__ = "schedule_stop_rides"
    schedule_stop_id = db.Column(db.Integer, db.ForeignKey("schedule_stops.id"))
    ride_id = db.Column(db.Integer, db.ForeignKey("rides.id"))
    stop_type = db.Column(db.String)

    # ORM Relationship
    stop = db.relationship("ScheduleStop", backref="rides")
    ride = db.relationship("Ride", backref="stops")
