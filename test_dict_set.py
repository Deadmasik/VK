import pytest
from pytest_mock import MockerFixture
import allure

@pytest.fixture
def dict_t(scope='session') -> dict:
    dict_t = {1:1, 2:3, 4:4}
    return dict_t

@pytest.fixture
def set_t(scope='session') -> set:
    set_t = {'1','4','6'}
    return set_t

@allure.title("Dict get")
@allure.tag("Dict", "get")
@pytest.mark.dict
@pytest.mark.parametrize('x,expected', [(1,1),(6,None)])
def test_get(dict_t: dict, x:int, expected:int, mocker:MockerFixture)->None:
    assert dict_t.get(x) == expected

@allure.title("Dict pop")
@allure.tag("Dict", "pop")
@pytest.mark.dict
def test_pop()->None:
    dict_t = {1:2, 2:3}
    k = dict_t.pop(1)
    assert dict_t == {2:3}
    assert k == 2
    
@allure.title("Dict pop neg")
@allure.tag("Dict", "pop","neg")
@pytest.mark.dict
def test_pop2()->None:
    dict_t = {1:2, 2:3}
    try:
        k = dict_t.pop(5)
    except KeyError:
        pass
    assert dict_t == {1:2, 2:3}
    
@allure.title("Set in")
@allure.tag("Set", "in")
@pytest.mark.set
@pytest.mark.parametrize('x,expected', [('1',True),('2',False),(4,False),(3.2,False),(False,False)])
def test_in(set_t: set, x, expected)->None:
    assert (x in set_t) == expected

@allure.title("Set add")
@allure.tag("Set", "add")
@pytest.mark.set
def test_add()->None:
    set_t = {1,4,6}
    set_t.add(7)
    assert set_t == {1,4,6,7}

@allure.title("Set remove")
@allure.tag("Set", "remove")
@pytest.mark.set
def test_remove()->None:
    set_t = {1,4,6}
    set_t.remove(6)
    assert set_t == {1,4}

@allure.title("Set remove")
@allure.tag("Set", "remove","neg")
@pytest.mark.set
def test_remove2()->None:
    set_t = {1,4,6}
    try:
        set_t.remove(7)
    except KeyError:
        pass
    assert set_t == {1,4,6}
