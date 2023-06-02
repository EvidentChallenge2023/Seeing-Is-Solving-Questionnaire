import numpy as np

from sources.challengepart2.source.question3.TCGPoint import TCGPoint

EMPTY = np.array([])

BASIC = np.array([TCGPoint(0.0, 0.0),
                  TCGPoint(20.0, 6.0),
                  TCGPoint(40.0, 3.0),
                  TCGPoint(100.0, 20.0),
                  TCGPoint(150.0, 1.0)])

NOT_ON_DEFAULT_RESOLUTION = np.array([TCGPoint(0.0, 0.0),
                                      TCGPoint(25.40, 6.0),
                                      TCGPoint(58.95, 3.0),
                                      TCGPoint(108.80, 20.0),
                                      TCGPoint(148.32, 1.0)])

WITHOUT_ZERO_POINT = np.array([TCGPoint(20.0, 6.0),
                               TCGPoint(40.0, 3.0),
                               TCGPoint(100.0, 20.0),
                               TCGPoint(150.0, 1.0)])

WITH_AMPLIFIED_ZERO = np.array([TCGPoint(0.0, 4.0),
                                TCGPoint(20.0, 6.0),
                                TCGPoint(100.0, 20.0)])

WITH_NEGATIVE_POSITION = np.array([TCGPoint(-20.0, 6.0),
                                   TCGPoint(40.0, 3.0),
                                   TCGPoint(100.0, 40.0),
                                   TCGPoint(150.0, 30.0)])

WITH_NEGATIVE_POINT = np.array([TCGPoint(0.0, 0.0),
                                TCGPoint(20.0, 6.50),
                                TCGPoint(40.0, -6.0),
                                TCGPoint(100.0, 18.45),
                                TCGPoint(150.0, 2.09)])
