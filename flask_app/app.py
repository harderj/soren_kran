from flask import Flask
from flask import render_template

server = Flask(
    __name__,
    static_folder=r"static"
)

print(server.template_folder)

@server.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("soren.html")

