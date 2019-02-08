from domain import Student ,Assignment
from RepositoryWithPickle import *
from GradeController import GradeController
from StudControllerWithUndo import StudControllerWithUndo
from AssigControllerWithUndo import AssigControllerWithUndo
from controller import Controller

from undoController import undoController
from menu import *


from StudCSVRepository import StudCSVRepository


SETTINGS_FILE = "settings_binary.properties"


def readSettings():
    '''
    Reads the program's settings file
    output:
        A dictionary containing the program settings
    '''
    f = open(SETTINGS_FILE, "r")
    lines = f.read().split("\n")
    settings = {}

    for line in lines:
        setting = line.split("=")
        if len(setting) > 1:
            settings[setting[0]] = setting[1]
    f.close()
    return settings


settings = readSettings()

studRepo = None
assigRepo = None
gradeRepo = None

if 'binary' == settings['repository']:
    studRepo = RepositoryWithPickle(settings['students'])
    assigRepo = RepositoryWithPickle(settings['assignments'])
    gradeRepo = RepositoryWithPickle(settings['grades'])

if 'CSV'==settings['repository']:
    studRepo=StudCSVRepository(settings['students'])


controller = Controller(studRepo, assigRepo, gradeRepo)

GradeController = GradeController(gradeRepo)

undoController = undoController()
StudControllerWithUndo = StudControllerWithUndo(undoController, GradeController, studRepo)
AssigControllerWithUndo = AssigControllerWithUndo(undoController, GradeController, assigRepo)


ui = UI(controller,StudControllerWithUndo,AssigControllerWithUndo,GradeController,undoController)
ui.start()