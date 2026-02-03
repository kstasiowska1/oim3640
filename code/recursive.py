#creating a recursive function that calls itself indefinitely
def groundhog_day():
    """A function that prints 'groundhog' day indefinitely."""""
    import time
    print('Did you mean: groundhog day?')

    time.sleep(1)
    groundhog_day()

groundhog_day