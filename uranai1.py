import tkinter as tk
import os.path
import random

def uranau():
    # 占いを実行
    show_kuji["image"] = random.choice(kujis)
    
def clear():
    # 占いをクリア
		show_kuji["image"] = default_img

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("おみくじ")

# くじの中身
kujis = ["大吉", "中吉", "小吉", "凶"]

# ボタンを配置するフレームワーク
btn_frame = tk.Frame(root, padx=10, pady=20)
btn_frame.pack()

# 「占う」ボタン
uranau__btn = tk.Button(btn_frame, text="占う", command=uranau, bg="lightblue")
uranau__btn.pack(side='left')
# 「クリア」ボタン
clear_btn = tk.Button(btn_frame, text="クリア", command=clear, bg="yellow")
clear_btn.pack(side='left')

# デフォルトのイメージの読み込み（パスの相違を吸収）
default_img = tk.PhotoImage(
        file=os.path.join(os.path.dirname(__file__), "kujis/empty.png")
)

# くじの４つのイメージファイル
kujis = [tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "kujis/kyo.png")),
        tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "kujis/syoukiti.png")),
        tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "kujis/chukiti.png")),
        tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "kujis/daikiti.png")),]

# 占い結果を表示するラベル
show_kuji = tk.Label(root, image=default_img)
show_kuji.pack()

# メインループ
root.mainloop()
