# -*- coding: utf-8 -*-

from flask import Flask, render_template
import yd_spider

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', items = yd_spider.list_home())


if __name__ == '__main__':
    app.run(debug=True)
