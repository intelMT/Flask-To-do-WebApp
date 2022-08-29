from flask import render_template, request, redirect, url_for
from app import app, db, ToDo

@app.route("/")
def index():
    todos = ToDo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/complete/<string:id>")
def updateToDo(id):
    entry = ToDo.query.filter_by(id=id).first()
    entry.completed = False if entry.completed else True
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteToDo(id):
    entry = ToDo.query.get(id)
    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/detail/<string:id>")
def addDetail(id):
    entry = ToDo.query.filter_by(id=id).first()
    if entry == None:
        return redirect(url_for("index"))
    return render_template("detail.html", todo = entry)


@app.route("/add", methods = ["POST"])
def addToDo():
    title = request.form.get("title")
    content = request.form.get("content")

    newToDo = ToDo(title=title, content=content, completed=False)
    db.session.add(newToDo)
    db.session.commit()

    return redirect(url_for("index"))
