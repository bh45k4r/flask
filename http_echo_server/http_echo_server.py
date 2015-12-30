#!/usr/bin/python

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024


@app.route('/echo', methods = ['GET', 'POST'])
def echo():
  """
  echo data
  """
  if request.method == 'GET':
    return jsonify(request.args)
  else:
    return jsonify(request.form)


if __name__ == '__main__':
  app.run(host = '::',
          port = 80)