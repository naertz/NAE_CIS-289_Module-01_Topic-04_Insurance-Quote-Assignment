"""
Program:               driver_exceptions.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-08-31

Driver exception classes
"""

from constants.coverages import AGE_0


class InvalidNameException(Exception):
    """InvalidNameException Class"""
    """Constructor"""
    def __init__(self, name, message='Name contains non-alpha characters'):
        self._name = name
        self._message = message
        super(InvalidNameException, self).__init__(self._message)

    """String Representation Functions"""
    def __str__(self):
        return f'{self._name} -> {self._message}'


class InvalidAgeException(Exception):
    """InvalidAgeException Class"""
    """Constructor"""
    def __init__(self, age, message='Age is not ' + str(AGE_0) + '+ range'):
        self._age = age
        self._message = message
        super(InvalidAgeException, self).__init__(self._message)

    """String Representation Functions"""
    def __str__(self):
        return f'{self._age} -> {self._message}'


class InvalidCoverageLevelException(Exception):
    """InvalidCoverageLevelException Class"""
    """Constructor"""
    def __init__(self, coverage_level, message='Coverage level is not \'sm\', \'l\', or \'f\'.'):
        self._coverage_level = coverage_level
        self._message = message
        super(InvalidCoverageLevelException, self).__init__(self._message)

    """String Representation Functions"""
    def __str__(self):
        return f'{self._coverage_level} -> {self._message}'
