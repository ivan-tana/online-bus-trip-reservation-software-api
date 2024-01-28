

def exception_message(exception: Exception, message: str = None):
    if  message and not exception.args[0]:
        return message
    try: 
        message = exception.args[0] 
    except IndexError:
        message = exception.message
    return message