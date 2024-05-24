import uuid
from datetime import datetime


class Time_Flight:
    def __init__(self, name, duration, days, id_fligths=None, id_times=None, id=None, created_on=None, updated_on=None):
        self.id = id or uuid.uuid4()
        self.name = name
        self.id_fligths = id_fligths if id_fligths is not None else None,
        self.id_times = id_times if id_times is not None else None,
        self.duration = duration
        self.days = days
        self.created_on = created_on or datetime.now()
        self.updated_on = updated_on or datetime.now()