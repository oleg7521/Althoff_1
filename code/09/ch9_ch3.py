import csv

kino = [["Звездные войны","Терминатор","Искусственный интеллект"],
        ["Дурак","Матильда","Левиафан"],
        ["Люди в черном","Я - робот","Эволюция"]
       ]
with open("movie.csv", "w", encoding="utf8") as f:
    w = csv.writer(f, delimiter=",")
    for mv in kino:
        w.writerow(mv)
