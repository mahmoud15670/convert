import csv
from cs50 import SQL
def main():

    # Ensure correct usage

    db = SQL("sqlite:///patients.db")
    # db.execute("CREATE TABLE tests (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT NOT NULL,  grob TEXT NOT NULL, price INTEGER NOT NULL")
    with open("tests.csv") as file:
        reader = csv.DictReader(file, fieldnames=['id', 'name', 'group', 'price'])
        for patient in reader:
            # if patient["phone"] == "NULL" and patient["tel"] != "NULL":
                # db.execute("INSERT INTO info (id, name, phone) VALUES (?,?,?)",patient["id"], patient["name"], patient["tel"])
            # elif patient["phone"] != "NULL" and patient["tel"] == "NULL":
                # db.execute("INSERT INTO info (id, name, phone) VALUES (?,?,?)",patient["id"], patient["name"], patient["phone"])
            # else:
            db.execute("INSERT INTO tests (id, name, grop, price) VALUES (?,?,?,?)",patient["id"], patient["name"], patient["group"], patient["price"])



if __name__ == "__main__":
    main()
# with open() as file :
#     patients = csv.reader(file)
#     for patient in patients:
#         print(patient)
