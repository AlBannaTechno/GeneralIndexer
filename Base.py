"""
The Base File For All Operations


"""
import os
class PathCrawler(object):
    def __init__(self,path):
        self.path=path
        self.__fileList=[]
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
    def do_evry_thing(self):
        self.__fileList=PathCrawler.get_all(self.path)
