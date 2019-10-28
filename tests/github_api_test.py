import github_api
import pytest
import time

timestr = time.strftime("%Y-%m-%d-%H-%M")

def test_timestamp_name():
    assert github_api.timestamp_name() == timestr

def test_main

if __name__ == '__main__':
    pytest.main()