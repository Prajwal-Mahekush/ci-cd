from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory task list (resets when the server restarts — fine for learning purposes)
tasks = ["Buy groceries", "Finish CI/CD practice", "Call mom"]


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    new_task = request.form.get("task")
    tasks.append(new_task)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)