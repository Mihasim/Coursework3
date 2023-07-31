import pytest

import utils


def test_load_operation():
    assert type(utils.load_operaion()) == list


def test_sort_operations():
    assert type(utils.sort_operations()) == list
    for operation in utils.sort_operations():
        assert operation != {}
    assert type(operation["date"]) == str
    assert utils.load_operaion() != utils.sort_operations()
    assert utils.sort_operations()[0]["date"] > utils.sort_operations()[1]["date"]
    assert utils.sort_operations()[2]["date"] > utils.sort_operations()[3]["date"]



def test_get_five():
    assert type(utils.get_five()) == list
    assert len(utils.get_five()) == 5
    five = utils.get_five()
    for data in five:
        assert data["state"] == "EXECUTED"
        assert data != {}
    assert type(data["date"]) == str
    assert utils.get_five()[0]["date"] > utils.get_five()[1]["date"]
    assert utils.get_five()[2]["date"] > utils.get_five()[3]["date"]

def test_mask():
    assert utils.mask("Visa Platinum 1813166339376336") == "Visa Platinum 1813 16** **** 6336"
    assert utils.mask("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351"
    with pytest.raises(TypeError):
        utils.mask()

def test_mask_to():
    assert utils.mask_to("Visa Platinum 1813166339376336") == "Visa Platinum **6336"
    assert utils.mask_to("Maestro 1913883747791351") == "Maestro **1351"
    with pytest.raises(TypeError):
        utils.mask_to()


