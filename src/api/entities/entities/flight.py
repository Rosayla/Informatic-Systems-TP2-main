import uuid
from datetime import datetime


class Flight:
    def __init__(self, name, price, stops, id_airline=None, id_routes=None, id_classes=None, id_times=None, id=None, created_on=None, updated_on=None):
        self.id = id or uuid.uuid4()
        self.name = name
        self.id_airline = id_airline if id_airline is not None else None,
        self.id_routes = id_routes if id_routes is not None else None,
        self.id_classes = id_classes if id_classes is not None else None,
        self.id_times = id_times if id_times is not None else None,
        self.price = price
        self.stops = stops
        self.created_on = created_on or datetime.now()
        self.updated_on = updated_on or datetime.now()