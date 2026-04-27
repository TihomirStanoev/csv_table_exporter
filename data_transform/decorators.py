def error_handler(method):
    def wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            raise ValueError(f"Error in '{method.__name__}': {e}") from e
    return wrapper