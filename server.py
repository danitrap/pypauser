from flask import Flask, redirect
import os

app = Flask(__name__)

def type(string):
    os.system(f'YDOTOOL_SOCKET="$HOME/.ydotool_socket" ydotool type "{string}"')

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
    type(' ')
    return redirect('/')

@app.route('/next', methods=['POST'])
def next():
    # press Shift + n
    os.system('YDOTOOL_SOCKET="$HOME/.ydotool_socket" ydotool key 42:1 49:1 49:0 42:0')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
