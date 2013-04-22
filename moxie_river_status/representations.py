from flask import url_for, jsonify

from moxie.core.representations import Representation, HALRepresentation


class RiverStatusRepresentation(Representation):

    def __init__(self, river_status):
        self.river_status = river_status

    def as_dict(self):
        return {self.river_status.name: self.river_status.status}

    def as_json(self):
        return jsonify(self.as_dict())


class RiversStatusRepresentation(Representation):

    def __init__(self, rivers, last_updated):
        self.rivers = rivers
        self.last_updated = last_updated

    def as_dict(self):
        rivers = {'rivers': [RiverStatusRepresentation(river).as_dict()
            for river in self.rivers]}
        rivers['last_updated'] = self.last_updated
        return rivers

    def as_json(self):
        return jsonify(self.as_dict())


class HALRiversStatusRepresentation(RiversStatusRepresentation):

    def __init__(self, rivers, last_updated, endpoint):
        self.rivers = rivers
        self.last_updated = last_updated
        self.endpoint = endpoint

    def as_dict(self):
        rivers = RiversStatusRepresentation(self.rivers,
                self.last_updated).as_dict()
        representation = HALRepresentation(rivers)
        representation.add_link('self', url_for(self.endpoint))
        return representation.as_dict()

    def as_json(self):
        return jsonify(self.as_dict())
