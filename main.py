from flask import Flask, render_template, request, flash, redirect, url_for
from utils import allowed_file, validate_file

app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        if "select_file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        select_file = request.files["select_file"]
        if select_file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if select_file and allowed_file(select_file.filename):
            if validate_file(select_file):
                flash("File is valid and successfully uploaded")
                return redirect("/")
            else:
                flash("Invalid file format")
                return redirect(request.url)
        else:
            flash("File type not allowed")
            return redirect(request.url)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
