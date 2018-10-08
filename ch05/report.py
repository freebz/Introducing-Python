def get_description():  # 바로 아래에 docstring이 있다.
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who known']
    return choice(possibilities)
