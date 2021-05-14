from helper_functions import Helper
import pytest
import pandas as pd


@pytest.fixture
def test_helper():
    df = pd.DataFrame([[1, 2, 3], [2, 2, 3], [3, 3, 3]])
    help = Helper()
    assert type(help) == pd.Dataframe
