from datetime import datetime, timedelta, timezone
from factory import Factory, Faker, LazyAttribute, Sequence, SubFactory, fuzzy
from src.models import Ride, Schedule, ScheduleStop, ScheduleStopRide, User


WHEELCHAIR_CHOICES = (False, False, False, False, False, False, False, False, False, True)
STATUS_CHOICES = ('pending', 'in_progress')


def now():
    return datetime.utcnow().replace(tzinfo=timezone.utc)


class UserFactory(Factory):
    class Meta:
        model = User

    username = Sequence(lambda n: "user-{0}".format(n))
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = LazyAttribute(lambda a: '{0}.{1}@example.com'.format(a.first_name, a.last_name).lower())


class RideFactory(Factory):
    class Meta:
        model = Ride

    user = SubFactory(UserFactory)
    capacity = fuzzy.FuzzyInteger(1, 4)
    wheelchair = fuzzy.FuzzyChoice(WHEELCHAIR_CHOICES)
    status = fuzzy.FuzzyChoice(STATUS_CHOICES)


class ScheduleStopFactory(Factory):
    class Meta:
        model = ScheduleStop

    address = Faker('address')
    latitude = Faker('latitude')
    longitude = Faker('longitude')
    timestamp = fuzzy.FuzzyDateTime(now(), now() + timedelta(hours=1))
