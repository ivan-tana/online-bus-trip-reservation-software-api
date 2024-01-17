

def exception_message(exception: Exception, message: str = None):
    if  message:
        return message
    try: 
        message = exception.args[0] 
    except IndexError:
        message = "agency already exist"
    return message