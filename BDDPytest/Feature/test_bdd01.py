import pytest
from pytest_bdd import scenario, given, when, then
from pathlib import Path

featureFileDir = ''
featureFile = 'Feature101.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)


def pytest_configure():  # Global Variable
    pytest.AMT = 0


@scenario(str(FEATURE_FILE), 'Withdrawal money')
def test_withdrawl():
    print("End of Withdrawal money test")


@given('the account balance is 100')
def current_balnce():
    pytest.AMT = 100


@when('the account holder withdrawn 100')
def withdrawn_Amount():
    pytest.AMT = pytest.AMT - 30


@then('the account balance should be 70')
def final_balance():
    assert pytest.AMT == 70
