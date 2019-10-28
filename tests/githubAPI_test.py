from githubAPI import *
import pytest
import time

timestr = time.strftime("%Y-%m-%d-%H-%M")

def test_timestamp_name():
    assert githubAPI.timestamp_name() == timestr

if __name__ == '__main__':
    pytest.main()