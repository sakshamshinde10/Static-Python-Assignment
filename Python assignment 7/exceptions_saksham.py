class DataCleaningError(Exception):
    pass

class MissingColumnError(DataCleaningError):
    pass

class InconsistentTypeError(DataCleaningError):
    pass