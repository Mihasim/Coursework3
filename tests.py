import utils


def test_load_operation():
    assert type(utils.load_operaion()) == list

def test_sort_operations():
    assert type(utils.sort_operations()) == list
    for operation in utils.sort_operations():
        assert operation != {}

def test_get_five():
    assert type(utils.get_five()) == list
    assert len(utils.get_five()) == 5
    five = utils.get_five()
    for data in five:
        assert data["state"] == "EXECUTED"

def test_mask():
    assert utils.mask("Visa Platinum 1813166339376336") == "Visa Platinum 1813 16** **** 6336"
    assert utils.mask("Maestro 1913883747791351") == "Maestro 1913 88** **** 1351"

def test_mask_to():
    assert utils.mask_to("Visa Platinum 1813166339376336") == "Visa Platinum **6336"
    assert utils.mask_to("Maestro 1913883747791351") == "Maestro **1351"


