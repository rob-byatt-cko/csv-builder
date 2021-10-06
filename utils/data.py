import random

def generate_random_float(len: int, decimal_places: int = 2):
    return round(random.random() * len, decimal_places)

def generate_random_int(len: int):
    return int(random.random() * len)