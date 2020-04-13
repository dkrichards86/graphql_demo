from src import ma
from src.models import Ride


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name')


class RideSchema(ma.Schema):
    class Meta:
        fields = ('capacity', 'wheelchair', 'status', 'user')

    user = ma.Nested(UserSchema)


class ScheduleStopRideSchema(ma.Schema):
    class Meta:
        fields = ('ride', 'stop_type')

    ride = ma.Nested(RideSchema)


class ScheduleStopSchema(ma.Schema):
    class Meta:
        fields = ('address', 'latitude', 'longitude', 'timestamp', 'rides')

    latitude = ma.Decimal(as_string=True)
    longitude = ma.Decimal(as_string=True)
    rides = ma.Nested(ScheduleStopRideSchema, many=True)


class ScheduleSchema(ma.Schema):
    class Meta:
        fields = ('stops',)

    stops = ma.Nested(ScheduleStopSchema, many=True)


ride_schema = RideSchema()
rides_schema = RideSchema(many=True)
schedule_schema = ScheduleSchema()
user_schema = UserSchema()
users_schema = UserSchema(many=True)