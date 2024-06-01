from tkinter import *

def KillWindow():
    root.destroy()

def ResetWindow():
    canvas.delete("all")

def DivineFortune():
    canvas.create_text(220, 220, text="大吉", font=("Meiryo", 50))
    canvas.create_text(350, 290, text="何事もうまくいくよ！", font=("Meiryo", 12))

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
#detail_label = Label(root, text="今日の運勢を占ってみよう！ (Let's read today's fortune!)", font=("Meiryo", 12))

introduction_ja_label = Label(root, text="あなたの運勢は・・・", font=("Meiryo", 12))
introduction_en_label = Label(root, text="Your fortune is ...", font=("Meiryo", 12))
#center_label = Label(root, text="大吉", font=("Meiryo", 50))
#brief_comment_label = Label(root, text="何事もうまくいくよ！", font=("Meiryo", 12))
attention_label = Label(root, text="*This omikuji is not true.", font=("Meiryo", 8))

start_button = Button(root, text="占う (Start)", font=("Meiryo", 14), command=DivineFortune)
stop_button = Button(root, text="")
reset_button = Button(root, text="もう一度 (Retry)", font=("Meiryo", 8), command=ResetWindow)
kill_button = Button(root, text="閉じる (Exit)", font=("Meiryo", 8), command=KillWindow)

# Layout objects
title_label.place(x=100, y=10)
#detail_label.place(x=10, y=60)

introduction_ja_label.place(x=40, y=100)
introduction_en_label.place(x=40, y=130)
#center_label.place(x=150, y=170)
#brief_comment_label.place(x=250, y=290)

start_button.place(x=160, y=330)
reset_button.place(x=100, y=390)
kill_button.place(x=250, y=390)

attention_label.place(x=300, y=430)

# Display window
root.mainloop()
