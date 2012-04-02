import os
from flask import Flask
from simpleBlog import *
app = Flask(__name__)

@app.route("/")
def index():
  entries = Entries()
  return create_page(entries)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host = '0.0.0.0', port=port)