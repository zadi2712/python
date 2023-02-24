filenames = ["1.data", "2.reports", "3.Presentations"]

for filename in filenames:
    print(filename)
    filename = filename.replace(".", "-")
    print(filename)