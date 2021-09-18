# Keep running the program though we closed the repl
# using flask - Server program

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello. I am alive"

def run():
  app.run(host='0.0.0.0', port=8000)

def keep_alive():
  t = Thread(target=run)
  t.start()