class Column:
    def __init__(self, *args, **kwargs):
        pass

class DateTime:
    def __init__(self, timezone=False):
        self.timezone = timezone

class String:
    def __init__(self, *args, **kwargs):
        pass

class Integer:
    pass

class Float:
    pass

class ForeignKey:
    def __init__(self, target):
        self.target = target

__all__ = [
    'Column', 'DateTime', 'String', 'Integer', 'Float', 'ForeignKey'
]
