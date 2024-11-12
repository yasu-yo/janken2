import player
import computer
import janken_judge

def janken_main():
    cnt_player = 0  
    cnt_computer = 0  
    ken = 0
    for ken in range(1, 4):  
        print(f"\n--- ラウンド{ken}---")
        
        # 勝敗が決まるまでループ
        while True:
            # プレイヤーの手を選択
            player_hand_index = player.human_pon()
            player_hands = ["グー", "チョキ", "パー"]
            player_hand = player_hands[player_hand_index]

            # コンピュータの手を選択
            computer_hand = computer.pc_pon()

            # プレイヤーとコンピュータの手を表示
            print(f"あなたの手: {player_hand}")
            print(f"コンピュータの手: {computer_hand}")

            # 勝敗判定
            result = janken_judge.judge(player_hand, computer_hand)

            if result == 0:
                print("引き分けです。\n")
                continue  
            elif result == 1:
                print("あなたの勝ちです！\n")
                cnt_player += 1  
            else:
                print("コンピュータの勝ちです！\n")
                cnt_computer += 1  
            break  

    # 最終結果を表示
    print(f"最終結果：")
    print(f"あなたの勝ち数: {cnt_player} 勝")
    print(f"コンピュータの勝ち数: {cnt_computer} 勝")

if __name__ == '__main__':
    janken_main()
