from werkzeug.utils import secure_filename
import csv
from openpyxl import load_workbook

ALLOWED_EXTENSIONS = {"csv", "xlsx", "xls"}


def allowed_file(filename):
    print("." in filename and filename.rsplit(".", 1)[1].lower())
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
