def hhtp_status(status):
    match status:
        case 200:
            return "OK " 
        case 404:
            return "Not Found  " 
        case 500:
            return "Internal Server Error" 
        case _:
            return " Unkown Status "
        