# GraphQL Demo
This is a simple application to demo the flexibility of GraphQL compared to a RESTful API. The
database schemas are intended to represent a vehicle routing schedule with stops and riders.

All data was generated using FactoryBoy and Faker.

## See it in action
A demo of this site is available on Heroku. https://nameless-everglades-44291.herokuapp.com/

### REST API
The REST API exposes a few endpoints available via GET requests. All payloads are defined by
serializers created using Marshmallow. Modifications to these schema require updating code.

#### Get the full schedule
The users REST endpoint is available at `/api/schedules`.

#### Get a list of rides
The rides endpoint is available at `/api/rides`.

#### Get a single ride by id
The ride endpoint is available at `/api/ride/<ride_id>`.

#### Get a list of users
The users REST endpoint is available at `/api/users`.

#### Get a single user by id
The users REST endpoint is available at `/api/user/<user_id>`.

### GraphQL
GraphQL endpoints can be queried by POSTing payloads to the `/graphql` endpoint. For ease of
demonstration, a graphiQL viewer is enabled at the endpoint. Simply paste the queries into the
query box and GraphiQL will handle the rest.  Modifications to the payloads require updating the
query.

#### Get the full schedule
Schedules can be queried with:
```
{
  schedule {
    stops {
      timestamp
      address
      latitude
      longitude
      rides {
        ride {
          status
          capacity
          wheelchair
          user {
            username
            firstName
            lastName
          }
        }
        stopType
      }
    }
  }
}
```

#### Get a list of rides
Rides can be queried with:
```
{
    rides {
        status
        capacity
        wheelchair
        user {
            username
            firstName
            lastName
        }
    }
}
```

#### Get a single ride by id
```
{
    ride (rideId: <ride_id) {
        status
        capacity
        wheelchair
        user {
            username
            firstName
            lastName
        }
    }
}
```

#### Get a list of users
Users can be queried with:
```
{
  users {
    username
    firstName
    lastName
  }
}
```

#### Get a single user by id
```
{
    user(userId: <user_id>) {
        username
        firstName
        lastName
        email
    }
}
```

## Local usage
1. Install requirements `pip install -r requirements.txt`
2. Copy `.env.example` into `.env`, changing database URL as desired.
3. Set up your local database.
    1. `flask db upgrade`
    2. `flask seed`
4. Run the development server `flask run`