from repository import Repository
import pickle
class RepositoryWithPickle(Repository):
    def __init__(self, fileName):
        Repository.__init__(self)
        self.fileName = fileName
        self.loadFromFile()

    def add(self, object):

        Repository.add(self, object)
        self.storeToFile()




    def remove(self, objectId):
        Repository.remove(self, objectId)
        self.storeToFile()


    def update(self, old, new):

        s=Repository.update(self, old, new)

        self.storeToFile()

        return s

    def loadFromFile(self):
        f = open(self.fileName, "rb")

        """
        You cannot unpickle an empty file
            - EOFError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        try:
            self._data = pickle.load(f)
        except EOFError:
            self._data = []
        except Exception as e:
            raise e
        finally:
            f.close()

    def storeToFile(self):
        f = open(self.fileName, "wb")
        pickle.dump(self._data, f)
        f.close()