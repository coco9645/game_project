import random


class Game:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]

    def get_valid_choice(self):
        while True:
            user = input("\n가위/바위/보 중 하나를 입력하세요 : ")
            if user in self.choices:
                return user
            print("\n가위, 바위, 보 중에 입력해주세요.")

    def play_rock_paper_scissors(self):
        while True:
            user = self.get_valid_choice()
            computer = random.choice(self.choices)
            print(f"컴퓨터: {computer}")
            if user == computer:
                print("\n다시!")
            else:
                if (user == "가위" and computer == "보") or (user == "바위" and computer == "가위") or (user == "보" and computer == "바위"):
                    print("사용자가 공격권을 가져갑니다.")
                    return "사용자"
                else:
                    print("컴퓨터가 선공권을 가져갑니다.\n")
                    return "컴퓨터"


    def play_muk_jji_ppa(self,initial_attacker):
        print("[묵찌빠 시작]")
        attacker = initial_attacker
        while True :
            print(f"현재 공격자 : {attacker}")
            user = self.get_valid_choice()
            computer = random.choice(self.choices)
            print(f"컴퓨터: {computer}")
            if user == computer:
                print(f"{attacker} 승리!")
                return attacker
            if (user == "가위" and computer == "보") or (user == "바위" and computer == "가위") or (user == "보" and computer == "바위"):
                attacker = "사용자"
            else:
                attacker = "컴퓨터"
            print(f"공격권이 {attacker}에게 넘어갑니다.")
            
            

            


    def play(self):
        print("묵찌빠 게임입니다.")
        win = 0
        lose = 0
        while True:
            initial_attacker = self.play_rock_paper_scissors()
            attacker = self.play_muk_jji_ppa(initial_attacker)
            if attacker == "사용자":
                win += 1
            elif attacker == "컴퓨터":
                lose += 1
            while True:
                again = int(input("게임을 다시 시작하시겠습니까?\n1. 예\n2. 아니오\n : "))
                if again == 1:
                    break
                elif again == 2:
                    total_game = win + lose
                    print(f"게임종료!\n총 게임 수: {total_game}\n승리: {win}\n패배: {lose}")
                    nickname = input("닉네임을 입력하세요: ")
                    return nickname, win, lose, total_game
                else:
                    print("1,2 중에 입력해주세요.")
            
