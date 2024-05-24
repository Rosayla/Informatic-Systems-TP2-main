import uuid
from datetime import datetime


class Time:
    def __init__(self, departure, arrival, id=None, created_on=None, updated_on=None):
        self.id = id or uuid.uuid4()
        self.departure = departure
        self.arrival = arrival
        self.created_on = created_on or datetime.now()
        self.updated_on = updated_on or datetime.now()