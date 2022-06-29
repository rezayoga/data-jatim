from app.models import Ptsl

def test_new_ptsl():
    """
    
    GIVEN a PTSL Model
    THEN a new PTPSL object is created
    THEN check the object it self right or wrong
    """
    
    ptsl = Ptsl('Kabupaten Malang', 1, 2, 3)
    assert ptsl.kabupaten_kota == 'Kabupaten Malang'
    assert ptsl.target_pbt == 1
    assert ptsl.target_shat != 2
    assert ptsl.target_k4 == 3
    