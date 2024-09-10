specifications = [
    "name",
    "age",
    "gender",
    "occupation",
    "marital status",
    "number of children",
    "education level",
    "location",
    "nationality",
    "languages spoken",
    "current emotions",
    "anxiety symptoms",
    "depression symptoms",
    "stress symptoms",
    "sleep issues",
    "eating issues",
    "concentration issues",
    ]

with open("specifications.txt", "w") as file:
    for index, item in enumerate(specifications, start=1):
        file.write(f"{index}_{item}: \n")

print("Specifications saved to Specifications.txt")
