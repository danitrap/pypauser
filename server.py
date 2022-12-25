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
    <form method="post" action="/next"><button style="width: 100%; height: 200px; margin-top: 50px; font-size: 50px">Next</button></form>
  </body>
</html>
"""

@app.route('/pause', methods=['POST'])
def pause():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    return redirect('/')

@app.route('/next', methods=['POST'])
def next():
    with keyboard.pressed(Key.shift):
      keyboard.press('n')
      keyboard.release('n')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')