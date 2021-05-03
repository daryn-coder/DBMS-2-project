from django.shortcuts import render, redirect

# Create your views here.
import cx_Oracle
import pandas as pd
import matplotlib.pyplot as plt

connection = cx_Oracle.connect("HR", "hr", "localhost:1521/xe",
                               encoding="UTF-8")
cursor = connection.cursor()
cursor.execute("Select * from Clothes")
rows = cursor.fetchall()
# for row in rows:
    # print(row)


def index_view(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def about(request):
    return render(request, "about.html", {})

def brilliant(request):
    return render(request, "brilliant.html", {})

def collection(request):
    return render(request, "collection.html", {})

def delivery(request):
    return render(request, "delivery.html", {})

def jewellery(request):
    return render(request, "jewellery.html", {})

def order(request):
    return render(request, "order.html", {})

def premium(request):
    return render(request, "premium.html", {})

def present(request):
    return render(request, "present.html", {})

def wedding(request):
    return render(request, "wedding.html", {})

def statistics(request):
    return render(request, "statistics.html", {})


def add(request):
    cursor.execute("insert")

# def stat(request):
    # clothes = pd.read_sql("SELECT * FROM Clothes", con=connection)
    # clothes = clothes.convert_dtypes()
    # print("helo")
    # clothes.columns = clothes.columns.str.lower()
    # pivot2 = clothes.pivot_table(index='season', values='year', aggfunc='count')
    # pivot2.sort_values(by='season', ascending=False).head(9).plot(figsize=(15, 6), style='o-', grid=True)
    # plt.title("The count of clothes grouped by season")
    # plt.ylabel("Count of clothes")
    # plt.savefig('my_plot.png')
    #
    # return redirect('/index')