import os


def create_dir_if_none_exists(dirname):
    isdir = os.path.isdir(dirname)
    if not isdir:
        os.mkdir(dirname)
