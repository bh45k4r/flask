#!/usr/bin/python

import json

from flask import Flask, request, Response

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024


@app.route('/echo', methods = ['GET', 'POST'])
def echo():
  """
  echo data
  """
  if request.method == 'GET':
    json_response = json.dumps(request.args)
  else:
    json_response = json.dumps(request.form)

  return Response(json_response,
                  mimetype = 'application/json')


if __name__ == '__main__':
  app.run(host = '::',
          port = 80)
