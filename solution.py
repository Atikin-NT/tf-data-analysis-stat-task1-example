import pandas as pd
import numpy as np


chat_id = 708133213 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    alpha = -45
    r = math.exp(1)
    a = np.array([])
    for el in x:
        a = np.append(a, 1 / (math.sqrt(2*math.pi) * r) * math.exp(-(el - alpha) / 2*r**2))
    return np.sum(a)/len(a)
