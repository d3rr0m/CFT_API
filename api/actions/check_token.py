def check_is_valid_token(token: str)-> bool:
    if len(token) > 5:
        return True
    else:
        return False