from .config import ADMIN_ID, ADMIN_PASSWORD, MAX_LOGIN_ATTEMPTS
from .login_manager import LoginManager
from .ranking_board import RankingBoard
from .game import Game
# .은 같은 폴더인 경우에는 사용 안해도 됨.

class Rock_App:
    def __init__(self):
        self.login_manager = LoginManager(ADMIN_ID, ADMIN_PASSWORD,MAX_LOGIN_ATTEMPTS)
        self.ranking_board = RankingBoard()

    def print_menu(self):
        print()
        print("1. 게임 시작")
        print("2. 랭킹 보기")
        print("3. 게임 종료")

    def input_menu(self):
        while True:
            try:
                menu = int(input("메뉴를 선택하세요: "))
                return menu
            except ValueError:
                print("숫자만 입력해주세요.")

    def run(self):
        if not self.login_manager.login():
            return

        while True:
            self.print_menu()
            menu = self.input_menu()

            if menu == 1:
                game = Game()
                nickname, win, lose, total_game = game.play()
                self.ranking_board.add_record(nickname, win, lose, total_game)

            elif menu == 2:
                self.ranking_board.show_ranking()

            elif menu == 3:
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 메뉴입니다.")