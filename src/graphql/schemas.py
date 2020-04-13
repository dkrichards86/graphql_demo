import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from src.models import (
    Ride as RideModel,
    Schedule as ScheduleModel,
    ScheduleStop as ScheduleStopModel,
    ScheduleStopRide as ScheduleStopRideModel,
    User as UserModel,
)


class Ride(SQLAlchemyObjectType):
    class Meta:
        model = RideModel


class Schedule(SQLAlchemyObjectType):
    class Meta:
        model = ScheduleModel


class ScheduleStop(SQLAlchemyObjectType):
    class Meta:
        model = ScheduleStopModel


class ScheduleStopRide(SQLAlchemyObjectType):
    class Meta:
        model = ScheduleStopRideModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    ride = graphene.Field(Ride, ride_id=graphene.Int(required=True))
    rides = graphene.List(Ride)
    schedule = graphene.Field(Schedule)
    users = graphene.List(User)
    user = graphene.Field(User, user_id=graphene.Int(required=True))

    def resolve_ride(self, info, ride_id):
        return Ride.get_query(info).get(ride_id)

    def resolve_rides(self, info):
        return Ride.get_query(info).all()

    def resolve_schedule(self, info):
        return Schedule.get_query(info).first()

    def resolve_user(self, info, user_id):
        return User.get_query(info).get(user_id)

    def resolve_users(self, info):
        return User.get_query(info).all()


graphql_schema = graphene.Schema(query=Query)
