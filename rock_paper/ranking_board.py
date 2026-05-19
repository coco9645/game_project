class RankingBoard:
    def __init__(self):
        self.records = []

    def add_record(self, nickname, win, lose, total_game):
        record = {
            "name": nickname,
            "win": win,
            "lose": lose,
            "total_game": total_game
        }

        self.records.append(record)

    def show_ranking(self):
        if len(self.records) == 0:
            print("등록된 기록이 없습니다.")
            return

        self.records.sort(key=lambda x: (-x["win"], x["lose"], x["name"]))

        print("----전적----")

        for i in range(min(3, len(self.records))):
            print(f"{i + 1}위 - 닉네임: {self.records[i]['name']}, 총 게임 수: {self.records[i]['total_game']}, 승리: {self.records[i]['win']}, 패배: {self.records[i]['lose']}")