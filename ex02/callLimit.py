def callLimit(limit: int):
    """creation of callLimit decorator"""
    count = 0

    def callLimiter(function):
        """init count and call the function that as to be limited"""

        def limit_function(*args: any, **kwds: any):
            """Increments count and returns function \
if limit not out of bounds"""
            limit_function.count += 1
            if (limit_function.count > limit):
                print("Error:", function, "call too many times")
            else:
                return function(*args, **kwds)

        limit_function.count = count
        return (limit_function)

    return callLimiter
