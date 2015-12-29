#!/usr/bin/python

import json

from flask import Flask, request, Response
app = Flask(__name__)


@app.route('/')
def whats_my_ip():
  """
  returns remote address
  """
  return Response(json.dumps({'my_addr': request.remote_addr}), mimetype = 'application/json')


if __name__ == '__main__':
  app.run(host = '::',
          port = 80)
