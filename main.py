from flask import Flask, render_template, request, flash, redirect
from utils import allowed_file, validate_file, makeCategoryAndSaveExcel
from utils import GetFirst10Row

app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route("/", methods=["GET", "POST"])
def create_category():
    if request.method == "POST":
        if "select_file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        select_file = request.files["select_file"]
        if select_file.filename == "":
            flash("No selected file")
            return redirect("/category")
        if select_file and allowed_file(select_file.filename):
            if validate_file(select_file):
                makeCategoryAndSaveExcel(select_file)
                flash("File is valid and successfully uploaded")
                return redirect("/category")
            else:
                flash("Invalid file format")
                return redirect(request.url)
        else:
            flash("File type not allowed")
            return redirect(request.url)
    return render_template("index.html")


@app.route("/category")
def get_category():
    data = GetFirst10Row("updated_file.xlsx")
    ld = len(data)
    require_data = []
    for i in range(ld):
        require_data.append(data.iloc[i].to_dict())
    print(require_data)
    return render_template("category_table.html", data=require_data)


if __name__ == "__main__":
    app.run(debug=True)
