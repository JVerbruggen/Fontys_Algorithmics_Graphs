from vcover_validation import *

def test_validate_vcover():
    assert DefaultVCoverValidator([1,2,3], [(1,2)], [False, True, True], 2).validate() == True
    assert DefaultVCoverValidator([1,2,3], [(1,2)], [False, False, True], 2).validate() == False

    assert DefaultVCoverValidator([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], [False, False, True, False], 2).validate() == False
    assert DefaultVCoverValidator([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], [False, False, True, True], 2).validate() == True
    assert DefaultVCoverValidator([0,1,2,3], [(0,2),(0,3),(2,3),(1,2),(1,3)], [False, True, True, False], 2).validate() == False