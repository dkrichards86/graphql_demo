from flask import Blueprint, jsonify
from flask_restful import Resource, Api

from src.models import Ride, Schedule, ScheduleStop, ScheduleStopRide, User
from src.api.schemas import ride_schema, rides_schema, schedule_schema, user_schema, users_schema

api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)


def as_response(content):
    return dict(data=content), 200


class RideView(Resource):
    def get(self, ride_id):
        rides = Ride.query.get(ride_id)
        return as_response(dict(rides=ride_schema.dump(rides)))


class RidesListView(Resource):
    def get(self):
        rides = Ride.query.all()
        return as_response(dict(rides=rides_schema.dump(rides)))


class ScheduleView(Resource):
    def get(self):
        schedule = Schedule.query.join(ScheduleStop).join(ScheduleStopRide).first()
        return as_response(dict(schedule=schedule_schema.dump(schedule)))


class UserView(Resource):
    def get(self, user_id):
        users = User.query.get(user_id)
        return as_response(dict(users=user_schema.dump(users)))


class UsersListView(Resource):
    def get(self):
        users = User.query.all()
        return as_response(dict(users=users_schema.dump(users)))


api.add_resource(RideView, '/ride/<ride_id>')
api.add_resource(RidesListView, '/rides')
api.add_resource(ScheduleView, '/schedule')
api.add_resource(UserView, '/user/<user_id>')
api.add_resource(UsersListView, '/users')
