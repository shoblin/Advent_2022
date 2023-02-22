import os

PATH_DATA = os.path.dirname(__file__)


def read_file(file_name: str) -> list:
    '''

    :param file_name:
    :return:
    '''
    full_name = os.path.join(PATH_DATA, file_name)
    with open(full_name, "r") as file:
        line = file.read().splitlines()

    return line
