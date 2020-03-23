from src.database import EmployeeDB
import pytest


@pytest.fixture(scope='module')
def db():
    print('-----------------setup----------------')
    db = EmployeeDB()
    db.connect('src/data.json')
    yield db
    print('-----------------teardown----------------')
    db.close()


@pytest.mark.parametrize('emp_id, name, is_employee',
                         [
                             (1, 'vicky', True),
                             (2, 'unknown', False)
                         ])
def test_employee_data(db, emp_id, name, is_employee):
    employee_data = db.get_data(name)
    assert employee_data['emp_id'] == emp_id
    assert employee_data['name'] == name
    assert employee_data['is_employee'] == is_employee


# TearDown Module Method to initialise the db before running test case by setup module

# db = None
#
#
# def setup_module(module):
#     print('-----------------setup----------------')
#     global db
#     db = EmployeeDB()
#     db.connect('data.json')


# def teardown_module(module):
#     print('-----------------teardown----------------')
#     db.close()

# def test_vicky_data(db):
#     vicky_data = db.get_data('vicky')
#     assert vicky_data['emp_id'] == 1
#     assert vicky_data['name'] == 'vicky'
#     assert vicky_data['is_employee'] == True