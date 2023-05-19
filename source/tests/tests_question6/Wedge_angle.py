import math


class WedgeAngle:

    def __init__(self):
        self.__name = "Wedge Angle"

    def get_wedge_angle_in_degrees(self):
        angle = 0
        hyp = 2 * 0.005  # 10mm
        position1InSecond = 10e-6 / 2  # In HalfPath
        position2InSecond = 12e-6 / 2

        op = second_to_meter_converter(position2InSecond - position1InSecond)
        angleInRad = math.asin(op / hyp)
        angle = math.degrees(angleInRad)
        return angle


def second_to_meter_converter(position_in_second):
    return position_in_second * 2330
