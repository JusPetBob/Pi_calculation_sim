from flask import Flask,render_template,request
from numba import njit,prange
from numpy import random
from json import dumps
import functools

@functools.lru_cache
@njit(parallel=True)
def cal_pi(n):
    a = 0
    for _ in prange(n):
        a += (1 >= random.uniform()**2+random.uniform()**2)
    return (a/n)*4

## web application
app = Flask(__file__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/pi",methods=["GET"])
def get_pi():
    n = request.args.get("loops")
    if n and n.isdecimal():
        pi = cal_pi(int(n))
        return dumps({"pi":pi}), 200
    else:
        return "", 400

if __name__ == "__main__":
    app.run(debug=True)