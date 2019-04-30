from inspect import signature
from functools import wraps


def typeassert(*type_args, rtype=None, **type_kwargs):
    def decorate(func):
        sig = signature(func)
        bound_types = sig.bind_partial(*type_args, **type_kwargs).arguments
        func.paramTypes = bound_types
        func.rtype = rtype

        @wraps(func)
        def wrapper(*args,  **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            v = func(*args, **kwargs)
            if not isinstance(v, rtype):
                raise TypeError('return {} must be {}'.format(v, rtype))
            return v

        return wrapper

    return decorate
