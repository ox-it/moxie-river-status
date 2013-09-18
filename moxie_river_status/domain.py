STATUS_DESCRIPTIONS = {
    'green': 'No restrictions',
    'blue': 'No novice coxes',
    'yellow': 'Senior crews only',
    'red': 'No crews allowed out',
    'grey': 'Flag not currently being maintained',
    'black': 'No rowing for any crews. Isis on Environment Agency flood watch.'
}


class RiverStatus(object):
    def __init__(self, name, status):
        self.name = name
        self.status = status
