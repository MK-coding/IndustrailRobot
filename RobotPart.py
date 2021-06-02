from enum import Enum

class RobotPart(Enum):
    WAIST = "DJ 1,"
    SHOULDER = "DJ 2,"
    ELBOW = "DJ 3,"
    TWIST = "DJ 4,"
    PITCH = "DJ 5,"
    ROLL = "DJ 6,"


def robotPartToIncrement(robot_part: RobotPart):
    return robot_part.value


def robotPartToDecrement(robot_part: RobotPart):
    return robot_part.value + "-"

