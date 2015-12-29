#!/usr/bin/python

import json

from flask import Flask, request
app = Flask(__name__)


@app.route('/echo', methods = ['GET', 'POST'])
def echo():
  """
  echo data
  """
  if request.method == 'GET':
    return json.dumps(request.args)
  else:
    return json.dumps(request.form)


if __name__ == '__main__':
  app.run(host = '::',
          port = 80)
