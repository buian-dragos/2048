from src.service.service import Service
from src.repo.repo import Repo
from src.gui.gui import Gui

if __name__ == '__main__':
    repo = Repo()
    serv = Service(repo)
    gui = Gui(serv)

    gui.run()

    # serv.test_move()
    # serv.flipFromDown()u