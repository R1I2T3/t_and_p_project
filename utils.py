from werkzeug.utils import secure_filename
import csv
from openpyxl import load_workbook
import pandas as pd

ALLOWED_EXTENSIONS = {"csv", "xlsx", "xls"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_file(file):
    filename = secure_filename(file.filename)
    file_extension = filename.rsplit(".", 1)[1].lower()
    if file_extension == "csv":
        try:
            csv.reader(file.stream)
            file.stream.seek(0)  # Reset file pointer
            return True
        except csv.Error:
            return False
    elif file_extension in ["xlsx", "xls"]:
        try:
            load_workbook(file.stream, read_only=True)
            file.stream.seek(0)  # Reset file pointer
            print("I am here")
            return True
        except:
            return False
    return False


def makeCategoryAndSaveExcel(file):
    df = pd.read_excel(file)
    df["CATEGORY"] = df.apply(
        lambda row: "Category_1"
        if row["CGPA"] >= 7.84
        and row["AY"] >= 75
        and row["TY"] >= 75
        and row["TEST SCORE"] >= 75
        else "Category_2"
        if row["CGPA"] >= 6.77
        and row["AY"] >= 75
        and row["TY"] >= 65
        and row["TEST SCORE"] >= 65
        else "Category_3"
        if row["CGPA"] < 6.77
        and row["AY"] >= 75
        and row["TY"] < 65
        and row["TEST SCORE"] < 65
        else "Category_4",
        axis=1,
    )
    df.to_excel("updated_file.xlsx", index=False)


def GetFirst10Row(file_name):
    placement_df = pd.read_excel(file_name)
    rows = placement_df.head(10)
    return rows
