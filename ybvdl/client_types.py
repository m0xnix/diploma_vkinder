from enum import Enum


class SexEnum(Enum):
    """
    Possible user's sex variants
    """
    FEMALE = 1
    MALE = 2
    UNDEFINED = 0


class MaritalStatusEnum(Enum):
    """
    Possible user's marital status options
    """
    SINGLE = 1
    HAS_RELATIONSHIPS = 2
    IS_ENGAGED = 3
    MARRIED = 4
    ITS_COMPLICATED = 5
    ACTIVELY_SEEKING = 6
    IN_LOVE = 7
    HAS_CIVIL_MARRIAGE = 8
