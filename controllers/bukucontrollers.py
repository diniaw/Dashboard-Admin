from models.bukumodels import Item, db
from flask import request, redirect, url_for, flash

# Ambil semua data reservasi
def index():
    return Item.query.all()

# Tambah data reservasi
def add_book():
    if request.method == 'POST':
        ID_reservasi = request.form.get('ID_reservasi')
        nama_tamu = request.form.get('nama_tamu')
        tanggal_checkin = request.form.get('tanggal_checkin')
        tanggal_checkout = request.form.get('tanggal_checkout')
        jenis_kamar = request.form.get('jenis_kamar')
        harga_per_malam = request.form.get('harga_per_malam')
        status_pembayaran = request.form.get('status_pembayaran')
        kontak_tamu = request.form.get('kontak_tamu')
        email_tamu = request.form.get('email_tamu')

        # Validasi input
        if not nama_tamu or not tanggal_checkin or not tanggal_checkout or not jenis_kamar or not harga_per_malam or not status_pembayaran or not kontak_tamu or not email_tamu:
            flash("Semua kolom harus diisi!", "error")
            return redirect(url_for('tambah_buku'))

        # Tambah data ke database
        new_reservasi = Item(
            ID_reservasi=ID_reservasi,
            nama_tamu=nama_tamu,
            tanggal_checkin=tanggal_checkin,
            tanggal_checkout=tanggal_checkout,
            jenis_kamar=jenis_kamar,
            harga_per_malam=harga_per_malam,
            status_pembayaran=status_pembayaran,
            kontak_tamu=kontak_tamu,
            email_tamu=email_tamu
            )

        db.session.add(new_reservasi)
        db.session.commit()
        flash("Reservasi berhasil ditambahkan!", "success")
        return redirect(url_for('basic_table'))

# Hapus data reservasi
def delete_book(book_id):
    item_to_delete = Item.query.get(book_id)

    if not item_to_delete:
        flash("Reservasi tidak ditemukan!", "error")
        return redirect(url_for('basic_table'))

    db.session.delete(item_to_delete)
    db.session.commit()
    flash("Reservasi berhasil dihapus!", "success")
    return redirect(url_for('basic_table'))

# Edit data reservasi
def edit_book(book_id):
    reservasi = Item.query.get(book_id)

    if not reservasi:
        flash("Reservasi tidak ditemukan!", "error")
        return redirect(url_for('basic_table'))

    if request.method == 'POST':
        reservasi.ID_reservasi = request.form.get('ID_reservasi')
        reservasi.nama_tamu = request.form.get('nama_tamu')
        reservasi.tanggal_checkin = request.form.get('tanggal_checkin')
        reservasi.tanggal_checkout = request.form.get('tanggal_checkout')
        reservasi.jenis_kamar = request.form.get('jenis_kamar')
        reservasi.harga_per_malam = request.form.get('harga_per_malam')
        reservasi.status_pembayaran = request.form.get('status_pembayaran')
        reservasi.kontak_tamu = request.form.get('kontak_tamu')
        reservasi.email_tamu = request.form.get('email_tamu')

        db.session.commit()
        flash("Reservasi berhasil diperbarui!", "success")
        return redirect(url_for('basic_table'))

    return reservasi
