# -*- coding: utf-8 -*-
"""
夢がかなう手帳 ランチャー
ローカルサーバー経由で手帳を開きます。ブラウザの保存制限を確実に回避するためのものです。

※ ポートは 8777 に固定しています。
   保存データはアドレス(http://127.0.0.1:8777)に紐づくため、
   ポートを変えると過去のデータが見えなくなります。絶対に変更しないでください。
"""
import http.server
import os
import socketserver
import sys
import threading
import urllib.parse
import webbrowser

PORT = 8777
FILE = "index.html"

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

URL = "http://127.0.0.1:{}/{}".format(PORT, urllib.parse.quote(FILE))


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    if not os.path.exists(FILE):
        print("エラー: {} (手帳の本体) が見つかりません。".format(FILE))
        input("Enterキーで閉じます...")
        return 1

    try:
        httpd = socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler)
    except OSError:
        # すでに起動済み。ブラウザを開くだけ。
        print("すでに起動しています。ブラウザを開きます。")
        webbrowser.open(URL)
        return 0

    print("=" * 56)
    print("  夢がかなう手帳をひらいています")
    print("=" * 56)
    print()
    print("  {}".format(URL))
    print()
    print("  ※ この黒い画面は開いたままにしてください。")
    print("     閉じると手帳が使えなくなります（データは消えません）。")
    print("  ※ 終わるときは、この画面で Ctrl+C を押すか、画面を閉じてください。")
    print()

    threading.Timer(0.7, lambda: webbrowser.open(URL)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n終了しました。")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
