from time import sleep


def follow(filename):
    """ Follow a file tail -f style

    This function is a generator, yielding the lines
    of the file to follow.

    Args:
        filename (str): The filename of the file to follow

    Yields:
        line (str): The next line of the file
    """
    with open(filename, 'r') as fileToFollow:
        fileToFollow.seek(0, 2)
        while True:
            line = fileToFollow.readline()
            if not line:
                sleep(0.1)
                continue
            yield line
