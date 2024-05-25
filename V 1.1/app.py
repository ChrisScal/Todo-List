from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder="templates")

todo_list = [] #Example Todos , delete later
#Single Todo  = dictionary 
#Todo States: 1)Done
#             2) Ongoing
def locate_index(todo_list = [], todo_str = str):
    if len(todo_list)>0:
        for index in range(len(todo_list)):
            if todo_list[index]["todo"] == todo_str:
                return index

@app.route("/")
def index():
    #Synarthsh Apothhkeyshs Leksikou
    return render_template("index.html", todos = todo_list)

@app.route("/complete/<index>", methods = ["POST","GET"])
def complete(index):
    if request.method == 'POST':
        todo_list[int(index)]["state"] = 'done'
        return redirect(url_for("index"))
    else: 
        return redirect(url_for("index"))

@app.route("/reset/<index>", methods = ["POST","GET"])
def reset(index):
    if request.method == "POST":
        todo_list[int(index)]["state"] = 'ongoing'
        return redirect(url_for("index"))
    else: 
        return redirect(url_for("index"))
    

@app.route("/add", methods = ["POST"]) #POST gia dhmiourgia neou todo
def add():
    if request.form["new_todo"]!='':
        new_todo = request.form["new_todo"]
        todo_list.append({"todo":new_todo,"state":"ongoing"})
        return redirect(url_for("index"))
    else :
        #Empty input
        return redirect(url_for("index"))

@app.route("/delete/<index>" , methods = ["GET"])
def delete(index):
    del todo_list[int(index)]
    return redirect(url_for("index"))

 
@app.route("/edit/<index>", methods = ["POST","GET"])
def edit_page(index):
    if request.form :
        if request.form["edit_todo"] == '':
            return render_template("edit.html",todo_list = todo_list,index = index)
        todo_list[int(index)]["todo"] = request.form["edit_todo"]
        return redirect(url_for("index"))
    else:               
        return render_template("edit.html", todo_list = todo_list ,index = int(index))


if __name__ == "__main__":
    app.run(debug=True)