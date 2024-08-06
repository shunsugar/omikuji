from tkinter import *
import random

def KillWindow():
    root.destroy()

def ResetWindow():
    canvas.delete("all")
    if start_button["state"] == DISABLED:
        start_button["state"] = NORMAL

def DivineFortune():
    i = random.randrange(1, 100, 1)
    if (0 < i <= 10):
        canvas.create_text(220, 220, text="凶", font=("Meiryo", 50))
        canvas.create_text(320, 290, text="いっぱい食べていっぱい寝てね！", font=("Meiryo", 12))
    if (10 < i <= 25):
        canvas.create_text(220, 220, text="末吉", font=("Meiryo", 50))
        canvas.create_text(340, 290, text="ちょっとひと休みしよう！", font=("Meiryo", 12))
    if (25 < i <= 50):
        canvas.create_text(220, 220, text="小吉", font=("Meiryo", 50))
        canvas.create_text(350, 290, text="散歩に出かけよう！", font=("Meiryo", 12))
    if (50 < i <= 75):
        canvas.create_text(220, 220, text="中吉", font=("Meiryo", 50))
        canvas.create_text(350, 290, text="慌てずに進めよう！", font=("Meiryo", 12))
    if (75 < i <= 90):
        canvas.create_text(220, 220, text="吉", font=("Meiryo", 50))
        canvas.create_text(350, 290, text="何事もうまくいくよ！", font=("Meiryo", 12))
    if (90 < i <= 100):
        canvas.create_text(220, 220, text="大吉", font=("Meiryo", 50))
        canvas.create_text(350, 290, text="今日は絶好調だね！", font=("Meiryo", 12))
    if start_button["state"] == NORMAL:
        start_button["state"] = DISABLED

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
start_button = Button(root, text="占う (Start)", font=("Meiryo", 14), command=DivineFortune)
reset_button = Button(root, text="もう一度 (Reset)", font=("Meiryo", 8), command=ResetWindow)
kill_button = Button(root, text="閉じる (Exit)", font=("Meiryo", 8), command=KillWindow)
attention_label = Label(root, text="*This omikuji is not true.", font=("Meiryo", 8))

# Layout objects
title_label.place(x=100, y=10)
introduction_ja_label.place(x=40, y=100)
introduction_en_label.place(x=40, y=130)
start_button.place(x=160, y=330)
reset_button.place(x=100, y=390)
kill_button.place(x=250, y=390)
attention_label.place(x=300, y=430)

# Display window
root.mainloop()
