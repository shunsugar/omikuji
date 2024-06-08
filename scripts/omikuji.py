from tkinter import *
import random

def KillWindow():
    root.destroy()

def ResetWindow():
    canvas.delete("all")

def DivineFortune():
    num = random.randint(0, 11)

    furigana_list = ["Daikichi", "Daikichi",
                     "Kichi", "Kichi",
                     "Chukichi", "Chukichi",
                     "Shokichi", "Shokichi",
                     "Suekichi", "Suekichi",
                     "Kyo", "Kyo"]
    
    fortune_list = ["大吉", "大吉",
                    "吉", "吉",
                    "中吉", "中吉",
                    "小吉", "小吉",
                    "末吉", "末吉",
                    "凶", "凶"]
    
    advice_list = ["","","","","","","","","","","",""]

    canvas.create_text(220, 180, text=furigana_list[num], font=("Meiryo", 16))
    canvas.create_text(220, 240, text=fortune_list[num], font=("Meiryo", 50))

# Create root window
root = Tk()
root.title("おみくじ (Omikuji)")
root.geometry("450x450")
root.resizable(False, False)

# Create canvas
canvas = Canvas(root, width=450, height=450)
canvas.place(x=0, y=0)

# Define objects
title_label = Label(root, text="おみくじ (Omikuji)", font=("Meiryo", 20))

introduction_ja_label = Label(root, text="あなたの運勢は・・・", font=("Meiryo", 12))
introduction_en_label = Label(root, text="Your fortune is ...", font=("Meiryo", 12))
#center_label = Label(root, text="大吉", font=("Meiryo", 50))
#brief_comment_label = Label(root, text="何事もうまくいくよ！", font=("Meiryo", 12))
attention_label = Label(root, text="*This omikuji is not true.", font=("Meiryo", 8))

start_button = Button(root, text="占う (Start)", font=("Meiryo", 14), command=DivineFortune)
reset_button = Button(root, text="もう一度 (Retry)", font=("Meiryo", 8), command=ResetWindow)
kill_button = Button(root, text="閉じる (Exit)", font=("Meiryo", 8), command=KillWindow)

# Layout objects
title_label.place(x=100, y=10)
#detail_label.place(x=10, y=60)

introduction_ja_label.place(x=40, y=80)
introduction_en_label.place(x=40, y=110)
#center_label.place(x=150, y=170)
#brief_comment_label.place(x=250, y=290)

start_button.place(x=160, y=330)
reset_button.place(x=100, y=390)
kill_button.place(x=250, y=390)

attention_label.place(x=300, y=430)

# Display window
root.mainloop()
