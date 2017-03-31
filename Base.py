"""
The Base File For All Operations


"""
import os
class PathCrawler(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all(path):
        full_list = []
        first_list = os.listdir(path)
        for p in first_list:
            if os.path.isdir(path + "/" + p):
                full_list.extend(PathCrawler.get_all(path + "/" + p))
            else:
                full_list.append(path + "/" + p)
        return full_list
