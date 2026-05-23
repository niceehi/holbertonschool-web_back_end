#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
  

    def operation(number: float) -> float:
        return number * multiplier
    return operation
