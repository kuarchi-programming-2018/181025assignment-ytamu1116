from turtle import *  # 描画環境 turtle をインポート
from rose import *  # plot1.pyと同一フォルダにあるrose.pyをインポート
hideturtle()
rose_window_recursion(
    [[-200, -200], [200, -200], [200, 200], [-200, 200]], 0.1, 40)
done()  # turtleの終了処理