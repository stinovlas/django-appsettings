"""Basic set of setting validators."""
from django.core.exceptions import ValidationError


class TypeValidator(object):
    """Validator which checks type of the value."""

    message = "Value %(value)s is not of type %(type)s."

    def __init__(self, value_type, message=None):
        self.value_type = value_type
        if message:
            self.message = message

    def __call__(self, value):
        if not isinstance(value, self.value_type):
            params = {"value": value, "type": self.value_type.__name__}
            raise ValidationError(self.message, params=params)


class ValuesTypeValidator(object):
    """Validator which checks types of iterable values."""

    message = "Element %(value)s is not of type %(type)s."

    def __init__(self, value_type, message=None):
        self.value_type = value_type
        if message:
            self.message = message

    def __call__(self, value):
        for element in value:
            if not isinstance(element, self.value_type):
                params = {"value": element, "type": self.value_type.__name__}
                raise ValidationError(self.message, params=params)


class DictKeysTypeValidator(object):
    """Validator which checks types of dict keys."""

    message = "The key %(key)s is not of type %(type)s."

    def __init__(self, key_type, message=None):
        self.key_type = key_type
        if message:
            self.message = message

    def __call__(self, value):
        for key in value:
            if not isinstance(key, self.key_type):
                params = {"key": key, "type": self.key_type.__name__}
                raise ValidationError(self.message, params=params)


class DictValuesTypeValidator(object):
    """Validator which checks types of dict values."""

    message = "Item %(key)s's value %(value)s is not of type %(type)s."

    def __init__(self, value_type, message=None):
        self.value_type = value_type
        if message:
            self.message = message

    def __call__(self, value):
        for key, element in value.items():
            if not isinstance(element, self.value_type):
                params = {"key": key, "value": element, "type": self.value_type.__name__}
                raise ValidationError(self.message, params=params)
