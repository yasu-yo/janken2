def human_pon():
    """プレイヤーの手を選択する関数"""
    while True:
        try:
            user_input = int(input('1.グー 2.チョキ 3.パー\nあなたの手を選択してください：')) - 1
            if user_input in [0, 1, 2]:
                return user_input
            else:
                print("1から3の数字を入力してください。")
        except ValueError:
            print("数字を入力してください。")
