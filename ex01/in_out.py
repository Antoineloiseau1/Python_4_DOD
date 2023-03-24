def square(x: int | float) -> int | float:
    """returns the x squared"""
    result = x ** 2
    return result


def pow(x: int | float) -> int | float:
    """returns x pow x"""
    result = x ** x
    return result


def outer(x: int | float, function) -> object:
    """declare an inner function and returns its return"""
    def inner() -> float:
        """apply function(x) on x"""
        nonlocal x
        x = function(x)
        return (x)
    return (inner)
