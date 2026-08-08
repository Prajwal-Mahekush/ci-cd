from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = ["Buy groceries", "Finish CI/CD practice", "Call mom"]


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    new_task = request.form.get("task")
    if new_task and new_task.strip():
        tasks.append(new_task.strip())
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
