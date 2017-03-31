"""
The Base File For All Operations


"""
import os
import peewee
class PathCrawler(object):
    def __init__(self,path):
        self.path=path
        self.__fileList=[]
        self.__pdfList=[]
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
        self.__pdfList=PathCrawler.get_pdf(self.__fileList)
    @staticmethod
    def get_pdf(path_list):
        tl = []
        for a in path_list:
            if os.path.isfile(a):
                name = os.path.basename(a)
                # fullPath,name,ext
                nt = [a, name[:len(name) - 4], name.split('.')[-1]]
                if nt[2] == 'pdf':
                    tl.append(nt)
        return tl


class DbCreatorController(object):
    dbBooks=peewee.SqliteDatabase('PdfLib.sqlLite')
    class Books(peewee.Model):
        FileName = peewee.TextField()
        FilePath = peewee.TextField(unique=True)
        class Meta:
            database = DbCreatorController.dbBooks
    def __init__(self):
        pass
    @staticmethod
    def Create_Books_Table_For_Once():
        try:
            DbCreatorController.Books.create_table()
        except:
            print("ERROR::THIS TABLE IS EXIST")
    @staticmethod
    def Inser_Book_Into_Books_Table(book_name, book_path):
        try:
            Book__ = DbCreatorController.Books(FileName=book_name, FilePath=book_path)
            Book__.save()
        except:
            print("ERROR::INPUT::THIS VALUE IS EXIST")
