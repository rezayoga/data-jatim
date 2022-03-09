from dataclasses import dataclass
from app import db


@dataclass
class Ptsl(db.Model):
    __tablename__ = 'tb_progres_ptsl_kanwil'

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
    unggah_bt: str
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
    unggah_bt = db.Column(db.String(12), nullable=True)
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

    def __repr__(self):
        return f'<PTSL id: {self.id} - {self.kabupaten_kota} - {self.target_pbt} - {self.target_shat} - {self.target_k4} - {self.persen_capaian_pbt} - {self.persen_capaian_shat} - {self.persen_capaian_k4} - {self.created_at}>'
