from dataclasses import dataclass
from app import db


@dataclass
class Ptsl(db.Model):
    __tablename__ = 'tb_progres_ptsl'

    id: int
    kabupaten_kota: str
    target_pbt: str
    target_shat: str
    target_k4: str
    survei: str
    pemetaan: str
    puldadis: str
    pemberkasan: str
    potensi_k1: str
    k1: str
    k2: str
    k31: str
    k32: str
    k33: str
    k4: str
    kw456: str
    siap_diserahkan: str
    diserahkan: str
    k1_pbt_sebelumnya: str
    persen_capaian_pbt: str
    persen_capaian_shat: str
    persen_capaian_k4: str
    y: str
    m: str
    d: str
    created_at: str

    id = db.Column(db.Integer, primary_key=True)
    kabupaten_kota = db.Column(db.String(128), nullable=False)
    target_pbt = db.Column(db.String(12), nullable=False)
    target_shat = db.Column(db.String(12), nullable=False)
    target_k4 = db.Column(db.String(12), nullable=False)
    survei = db.Column(db.String(12), nullable=False)
    pemetaan = db.Column(db.String(12), nullable=False)
    puldadis = db.Column(db.String(12), nullable=False)
    pemberkasan = db.Column(db.String(12), nullable=False)
    potensi_k1 = db.Column(db.String(12), nullable=False)
    k1 = db.Column(db.String(12), nullable=False)
    k2 = db.Column(db.String(12), nullable=False)
    k31 = db.Column(db.String(12), nullable=False)
    k32 = db.Column(db.String(12), nullable=False)
    k33 = db.Column(db.String(12), nullable=False)
    k4 = db.Column(db.String(12), nullable=False)
    kw456 = db.Column(db.String(12), nullable=False)
    siap_diserahkan = db.Column(db.String(12), nullable=True)
    diserahkan = db.Column(db.String(12), nullable=True)
    k1_pbt_sebelumnya = db.Column(db.String(12), nullable=True)
    persen_capaian_pbt = db.Column(db.String(12), nullable=True)
    persen_capaian_shat = db.Column(db.String(12), nullable=True)
    persen_capaian_k4 = db.Column(db.String(12), nullable=True)
    y = db.Column(db.String(4), nullable=True)
    m = db.Column(db.String(2), nullable=True)
    d = db.Column(db.String(2), nullable=True)
    created_at = db.Column(db.String(24))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    def __init__(self, kabupaten_kota: str, target_pbt: str, target_shat: str, target_k4:str) -> None:
        """ Create new PTSL dummy object
        
        Keyword arguments:
        argument -- kabupaten_kota, target_pbt, target_shat, target_k4
        Return: PTSL object
        """
        
        # super().__init__()

        self.kabupaten_kota = kabupaten_kota
        self.target_pbt = target_pbt
        self.target_shat = target_shat
        self.target_k4 = target_k4
        
        

    def __repr__(self):
        return f'<PTSL id: {self.id} - {self.kabupaten_kota} - {self.target_pbt} - {self.target_shat} - {self.target_k4} - {self.persen_capaian_pbt} - {self.persen_capaian_shat} - {self.persen_capaian_k4} - {self.created_at}>'


@dataclass
class KualitasDataLengkap(db.Model):
    __tablename__ = 'tb_transformasi_digital_kualitas_data_lengkap'
    __table_args__ = {'extend_existing': True}
    id: int
    kantor: str
    luas_wilayah: str
    jumlah_persil: str
    luas_persil: str
    luas_persil_valid: str
    jumlah_kw456: str
    luas_kw456: str
    jumlah_bt: str
    bt_valid: str
    warkah_bt: str
    persen_bt_valid: str
    persen_luas_persil_valid: str
    persen_warkah_bt: str
    persen_nilai_desa_lengkap: str
    potensi_desa_lengkap: str
    deklarasi_desa_lengkap: str
    jumlah_desa: str
    jumlah_persil_deliniasi: str
    luas_persil_deliniasi: str
    y: str
    m: str
    d: str
    created_at: str

    id = db.Column(db.Integer, primary_key=True)
    kantor = db.Column(db.String(128), nullable=False)
    luas_wilayah = db.Column(db.String(64), nullable=False)
    jumlah_persil = db.Column(db.String(64), nullable=False)
    luas_persil = db.Column(db.String(64), nullable=False)
    luas_persil_valid = db.Column(db.String(64), nullable=False)
    jumlah_kw456 = db.Column(db.String(64), nullable=False)
    luas_kw456 = db.Column(db.String(64), nullable=False)
    jumlah_bt = db.Column(db.String(64), nullable=False)
    bt_valid = db.Column(db.String(64), nullable=False)
    warkah_bt = db.Column(db.String(64), nullable=False)
    persen_bt_valid = db.Column(db.String(64), nullable=False)
    persen_luas_persil_valid = db.Column(db.String(64), nullable=False)
    persen_warkah_bt = db.Column(db.String(64), nullable=False)
    persen_nilai_desa_lengkap = db.Column(db.String(64), nullable=False)
    potensi_desa_lengkap = db.Column(db.String(64), nullable=False)
    deklarasi_desa_lengkap = db.Column(db.String(64), nullable=False)
    jumlah_desa = db.Column(db.String(64), nullable=False)
    jumlah_persil_deliniasi = db.Column(db.String(64), nullable=False)
    luas_persil_deliniasi = db.Column(db.String(64), nullable=False)
    y = db.Column(db.String(4), nullable=True)
    m = db.Column(db.String(2), nullable=True)
    d = db.Column(db.String(2), nullable=True)
    created_at = db.Column(db.String(24))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Kualitas Data Lengkap id: {self.id} - {self.kantor} - {self.luas_wilayah} - {self.jumlah_bt} - {self.bt_valid} - {self.persen_bt_valid} - {self.persen_nilai_desa_lengkap} - {self.deklarasi_desa_lengkap} - {self.created_at}>'


@dataclass
class DataSiapElektronik(db.Model):
    __tablename__ = 'tb_transformasi_digital_data_siap_elektronik'

    id: int
    kantor: str
    jumlah_bt: str
    persen_bt_valid: str
    jumlah_persil: str
    persen_persil_valid: str
    jumlah_siap_elektronik: str
    persen_siap_elektronik: str
    jumlah_su: str
    persen_su_valid: str
    jumlah_data_valid: str
    persen_data_valid: str
    bt_layanan_elektronik: str
    persen_bt_layanan_elektronik: str
    y: str
    m: str
    d: str
    created_at: str

    id = db.Column(db.Integer, primary_key=True)
    kantor = db.Column(db.String(128), nullable=False)
    jumlah_bt = db.Column(db.String(64), nullable=False)
    persen_bt_valid = db.Column(db.String(64), nullable=False)
    jumlah_persil = db.Column(db.String(64), nullable=False)
    persen_persil_valid = db.Column(db.String(64), nullable=False)
    jumlah_siap_elektronik = db.Column(db.String(64), nullable=False)
    persen_siap_elektronik = db.Column(db.String(64), nullable=False)
    jumlah_su = db.Column(db.String(64), nullable=False)
    persen_su_valid = db.Column(db.String(64), nullable=False)
    jumlah_data_valid = db.Column(db.String(64), nullable=False)
    persen_data_valid = db.Column(db.String(64), nullable=False)
    bt_layanan_elektronik = db.Column(db.String(64), nullable=False)
    persen_bt_layanan_elektronik = db.Column(db.String(64), nullable=False)
    y = db.Column(db.String(4), nullable=True)
    m = db.Column(db.String(2), nullable=True)
    d = db.Column(db.String(2), nullable=True)
    created_at = db.Column(db.String(24))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Data Siap Elektronik id: {self.id} - {self.kantor} - {self.jumlah_bt} - {self.persen_bt_valid} - {self.jumlah_su} - {self.persen_su_valid} - {self.created_at}>'


@dataclass
class RekapWarkahDigital(db.Model):
    __tablename__ = 'tb_transformasi_digital_rekap_warkah_digital'

    id: int
    kantor: str
    warkah_di208: str
    scan_wakrah_di208: str
    persen_scan_warkah_digital: str
    jumlah_buku_tanah: str
    scan_buku_tanah: str
    persen_scan_buku_tanah: str
    jumlah_surat_ukur: str
    scan_surat_ukur: str
    persen_scan_surat_ukur: str
    y: str
    m: str
    d: str
    created_at: str

    id = db.Column(db.Integer, primary_key=True)
    kantor = db.Column(db.String(128), nullable=False)
    warkah_di208 = db.Column(db.String(64), nullable=False)
    scan_wakrah_di208 = db.Column(db.String(64), nullable=False)
    persen_scan_warkah_digital = db.Column(db.String(64), nullable=False)
    jumlah_buku_tanah = db.Column(db.String(64), nullable=False)
    scan_buku_tanah = db.Column(db.String(64), nullable=False)
    persen_scan_buku_tanah = db.Column(db.String(64), nullable=False)
    jumlah_surat_ukur = db.Column(db.String(64), nullable=False)
    scan_surat_ukur = db.Column(db.String(64), nullable=False)
    persen_scan_surat_ukur = db.Column(db.String(64), nullable=False)
    y = db.Column(db.String(4), nullable=True)
    m = db.Column(db.String(2), nullable=True)
    d = db.Column(db.String(2), nullable=True)
    created_at = db.Column(db.String(24))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Rekap Warkah Digital id: {self.id} - {self.kantor} - {self.jumlah_buku_tanah} - {self.warkah_di208} - {self.scan_wakrah_di208} - {self.persen_scan_warkah_digital} - {self.jumlah_surat_ukur} - {self.scan_surat_ukur} - {self.persen_scan_surat_ukur} - {self.created_at}>'
