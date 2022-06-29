from app.models import Ptsl


def test_new_ptsl(new_ptsl):
    """
    
    GIVEN a PTSL Model
    THEN a new PTPSL object is created
    THEN check the object it self right or wrong
    """
    
    assert new_ptsl.kabupaten_kota == 'Kabupaten Malang'
    assert new_ptsl.target_pbt == 1
    assert new_ptsl.target_shat == 2
    assert new_ptsl.target_k4 == 3
    