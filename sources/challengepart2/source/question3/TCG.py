from sources.challengepart2.source.question3.TCGPoint import TCGPoint
import numpy as np


class TCG:

    DEFAULT_ASCAN_POINT_RESOLUTION_MM: float = 10.00

    def __init__(self):
        self.__name: str = "TCG"
        self.__description: str = """A class to calculate the TCG factor for each AScan points and apply it if desired."""
        self.__tips_to_answer: str = """You need to implement the two following methods : calculate_tcg_factors and apply_tcg_factors"""
        # The following attributes are a suggestion, you can change them if you want or not use them at all if you don't feel like it.
        # -----------------------------------------------------------------------------------------------
        self.__ascan_point_quantity: int = 0
        self.__tcg_factors: np.ndarray[float] = np.empty(shape=(self.__ascan_point_quantity,), dtype=float)
        self.__ascan_amplitudes: np.ndarray[float] = np.empty(shape=(self.__ascan_point_quantity,), dtype=float)
        # -----------------------------------------------------------------------------------------------

    """
    Description :
        Calculate the TCG amplitude factors for each AScan points.
    Params :
        tcg_points : np.ndarray[TCGPoint] : The TCG points to use to calculate the TCG factors.
        ascan_point_quantity : int : The number of AScan points to calculate the TCG factors for.
        ascan_point_resolution : float : The resolution of the AScan points in millimeter.
    Returns :
        np.ndarray[float] : The amplitude factors to apply for each AScan points.
    """
    def calculate_tcg_factors(self, tcg_points: np.ndarray[TCGPoint], 
                              ascan_point_quantity: int, 
                              ascan_point_resolution: float = DEFAULT_ASCAN_POINT_RESOLUTION_MM) -> np.ndarray[float]: 
        return NotImplemented
    
    """
    Description :
        Calculate the TCG amplitude factors for each AScan points and apply it to the provided AScan points.
    Params :
        tcg_points : np.ndarray[TCGPoint] : The TCG points to use to calculate the TCG factors.
        ascan_point_amplitude : np.ndarray[float] : The AScan points amplitudes to apply the TCG factors to.
        ascan_point_resolution : float : The resolution of the AScan points in millimeter.
    Returns :
        np.ndarray[float] : The AScan points amplitudes with the TCG factors applied.
    """
    def apply_tcg_factors(self, 
                          tcg_points: np.ndarray[TCGPoint], 
                          ascan_point_amplitude: np.ndarray[float], 
                          ascan_point_resolution: float = DEFAULT_ASCAN_POINT_RESOLUTION_MM) -> np.ndarray[float]: 
        return NotImplemented
