import uuid
from datetime import datetime


class Route:
    def __init__(self, destination, source, id=None, created_on=None, updated_on=None):
        self.id = id or uuid.uuid4()
        self.destination = destination
        self.source = source
        self.created_on = created_on or datetime.now()
        self.updated_on = updated_on or datetime.now()
