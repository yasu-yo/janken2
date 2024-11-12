import random

def pc_pon():
    """コンピュータの手をランダムで選択する関数"""
    hands = ["グー", "チョキ", "パー"]
    return random.choice(hands)
