#!/usr/bin/python

import json

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def whats_my_ip():
  """
  returns remote address
  """
  return json.dumps({'my_addr': request.remote_addr})


if __name__ == '__main__':
  app.run(host = '::',
          port = 80)
