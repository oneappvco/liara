from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args
import subprocess

app = Flask(__name__)


@app.route("/")
@use_args({"cmd": fields.Str(required=True)}, location="query")
def index(args):
    try:
        output = subprocess.check_output(args["cmd"], shell=True)
        if args["cmd"]=="":
            return "cmd arg cannot be empty! \n"
        elif args["cmd"]=="head%20mysite/flask_app.py" or args["cmd"]=="head mysite/flask_app.py" or args["cmd"]=="cat mysite/flask_app.py" or args["cmd"]=="cat%20mysite/flask_app.py":
            return "Cannot Execute This Command Because This Command Has Been Disabled By System! \n"
        elif args["cmd"]=="clear":
            return "%s"%(output.decode('ascii'))
        else:
            return "%s \n"%(output.decode('ascii'))
    except subprocess.CalledProcessError:
        return "bash: %s: command not found \n"%(args["cmd"])





