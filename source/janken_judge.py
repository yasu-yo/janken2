def judge(player_hand, computer_hand):
    """じゃんけんの勝敗を判定する関数"""
    if player_hand == computer_hand:
        return 0  # 引き分け
    elif (player_hand == "グー" and computer_hand == "チョキ") or \
         (player_hand == "チョキ" and computer_hand == "パー") or \
         (player_hand == "パー" and computer_hand == "グー"):
        return 1  # プレイヤーの勝ち
    else:
        return -1  # コンピュータの勝ち
