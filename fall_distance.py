# Author: Krystal Palacios
# Date : April 22. 2020
# Description : Determine the distance an object falls due to the gravity in a specific time period.

def fall_distance(fallingTime):
    """
    fall_distance used to calculate the distance an objects falls due to gravity with the equation:
    d = (1/2)*gt(squared) and returns the result.
    """
    distance = (1 / 2) * 9.8 * (fallingTime ** 2)
    return distance
