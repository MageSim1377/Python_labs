import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
from datetime import datetime
import json


fake = Faker("ru_RU")


def generateStudent():
    student = {
        "name": fake.name(),
        "year": fake.date_between_dates(datetime(2020, 1, 1), datetime(2025, 1, 1)).year,
        "study form": fake.random_element(elements=["Очная", "Заочная"]),
        "math mark": fake.random_int(60, 100),
        "physics mark": fake.random_int(60, 100),
        "language mark": fake.random_int(60, 100),
        "attestat mark": (fake.random_int(80, 100) / 10),
        "specialty": fake.random_element(elements=["Прикладная информатика", "Кибербезопасность", "Радиофизика"]),
        "address": fake.address(),
        "phone": fake.phone_number()
    } 

    student["full mark"] = student["math mark"] + student["physics mark"] + student["language mark"] + student["attestat mark"] * 10

    return student


students = [generateStudent() for i in range(1000)]

#sudents = []

#with open('students.json', 'r', encoding="utf-8") as f:
#    students = json.load(f)

df = pd.json_normalize(students)

print(df.head(5))

#pd.display(df)

#with open('students.json', 'w', encoding="utf-8") as f:
#    json.dump(students, f)



print(df)

plt.style.use("ggplot")

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(10, 10))

ax1.set_xlabel("Year")
ax1.set_ylabel("Math mark")
math = df[["year", "math mark"]].groupby("year")["math mark"].mean()
ax1.bar(df["year"].unique(), math)
ax1.set_ylim(70, 100)

ax2.set_xlabel("Year")
ax2.set_ylabel("Physics mark")
physics = df[["year", "physics mark"]].groupby("year")["physics mark"].mean()
ax2.bar(df["year"].unique(), physics)
ax2.set_ylim(70, 100)

ax3.set_xlabel("Year")
ax3.set_ylabel("Language mark")
language = df[["year", "language mark"]].groupby("year")["language mark"].mean()
ax3.bar(df["year"].unique(), language)
ax3.set_ylim(70, 100)

ax4.set_xlabel("Year")
ax4.set_ylabel("Attestat mark")
attestat = df[["year", "attestat mark"]].groupby("year")["attestat mark"].mean()
ax4.bar(df["year"].unique(), attestat)
ax4.set_ylim(7, 10)

data = df[['specialty', 'name']].groupby('specialty').count().reset_index()
print(data.head(5))
ax5.pie(data['name'], labels=data['specialty'], autopct='%1.1f%%')

plt.show()

#print(df[["year", "full mark"]].groupby("year").mean().head())