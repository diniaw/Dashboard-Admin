from flask import Flask, render_template
from models.bukumodels import db, Item
from config import Config
from controllers.bukucontrollers import index, add_book, delete_book, edit_book
from flask import request, render_template, redirect, url_for, flash


app = Flask(__name__)
app.config.from_object(Config)  # Memuat konfigurasi dari config.py
db.init_app(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/buttons")
def buttons():
    return render_template('ui-features/buttons.html')

@app.route("/dropdowns")
def dropdowns():
    return render_template('ui-features/dropdowns.html')

@app.route("/typography")
def typography():
    return render_template('ui-features/typography.html')

@app.route("/font-awesome")
def font_awesome():
    return render_template('icons/font-awesome.html')

@app.route("/basic-table")
def basic_table():
    # Query semua data dari tabel reservasi_hotel
    hotel = Item.query.all()
    return render_template('tables/basic-table.html', hotel=hotel)

@app.route('/tambah-buku', methods=['GET', 'POST'])
def tambah_buku():
    if request.method == 'POST':
        return add_book()
    return render_template('tambahbuku.html')

@app.route('/delete-buku/<int:book_id>', methods=['POST', 'GET'])
def delete_buku(book_id):
    return delete_book(book_id)

@app.route('/edit-buku/<int:book_id>', methods=['GET', 'POST'])
def edit_buku(book_id):
    if request.method == 'POST':
        return edit_book(book_id)
    reservasi = edit_book(book_id)
    return render_template('editbuku.html', reservasi=reservasi)


@app.route("/basic-elements")
def basic_elements():
    return render_template('forms/basic-elements.html')

@app.route("/chartjs")
def chartjs():
    return render_template('charts/chartjs.html')

@app.route("/login")
def login():
    return render_template('samples/login.html')

@app.route("/register")
def register():
    return render_template('samples/register.html')

@app.route("/blankpage")
def blankpage():
    return render_template('samples/blank-page.html')

app.run(debug=True)