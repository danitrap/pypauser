from flask import Flask, redirect
from pynput.keyboard import Key, Controller

keyboard = Controller()

app = Flask(__name__)

@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>PyPauser</title>
  </head>
  <body>
    <form method="post" action="/pause"><button style="width: 100%; height: 200px; margin-top: 200px; font-size: 50px">Pause / Play</button></form>
  </body>
</html>
"""

@app.route('/pause', methods=['POST'])
def pause():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')