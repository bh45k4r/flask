#!/usr/bin/python

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def whats_my_ip():
  """
  returns remote address
  """
  return jsonify({'my_addr': request.remote_addr})


if __name__ == '__main__':
  app.run(host = '::',
          port = 80)