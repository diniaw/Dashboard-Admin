from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'reservasi_hotel'
    
    ID_reservasi = db.Column(db.Integer, primary_key=True)
    nama_tamu = db.Column(db.String(50), nullable=False)
    tanggal_checkin = db.Column(db.Date, nullable=False)
    tanggal_checkout = db.Column(db.Date, nullable=False)
    jenis_kamar = db.Column(db.String(20), nullable=False)
    harga_per_malam = db.Column(db.Integer, nullable=False)
    status_pembayaran = db.Column(db.Enum('lunas', 'pending', 'cancel'), nullable=False)
    kontak_tamu = db.Column(db.String(15), nullable=False)
    email_tamu = db.Column(db.String(100), nullable=False)
