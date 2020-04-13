from flask import Blueprint
from flask_graphql import GraphQLView

from src.models import Ride, Schedule, ScheduleStop, ScheduleStopRide
from src.graphql.schemas import graphql_schema

graphql_bp = Blueprint("graphql", __name__, url_prefix="/graphql")

view = GraphQLView.as_view('graphql', schema=graphql_schema, graphiql=True)
graphql_bp.add_url_rule('/', view_func=view)