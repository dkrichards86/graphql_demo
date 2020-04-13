import click
import random
from flask import current_app
from flask.cli import with_appcontext

from src.factories import RideFactory, ScheduleStopFactory
from src.models import Ride, Schedule, ScheduleStop, ScheduleStopRide, User

STOP_TYPE_CHOICES = ('pickup', 'dropoff')


@click.command()
@with_appcontext
def seed():
    NUM_RIDERS = 12
    NUM_STOPS = 8

    schedule = Schedule.create()
    schedule_stops = []

    for ss in ScheduleStopFactory.create_batch(NUM_STOPS):
        instance = ScheduleStop.create(address=ss.address, latitude=ss.latitude,
                                       longitude=ss.longitude, timestamp=ss.timestamp,
                                       schedule=schedule)
        schedule_stops.append(instance)

    for i, r in enumerate(RideFactory.create_batch(NUM_RIDERS)):
        user = User.create(username=r.user.username, first_name=r.user.first_name,
                           last_name=r.user.last_name, email=r.user.email)
        ride = Ride.create(user=user, capacity=r.capacity, wheelchair=r.wheelchair, status=r.status)

        # Pick a stop for this rider. Once we fill all stops, randomize the remaining rides
        if i < NUM_STOPS:
            schedule_stop = schedule_stops[i]
        else:
            schedule_stop = random.choice(schedule_stops)

        ScheduleStopRide.create(stop=schedule_stop, ride=ride,
                                stop_type=random.choice(STOP_TYPE_CHOICES))
