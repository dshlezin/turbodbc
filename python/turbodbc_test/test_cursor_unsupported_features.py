import pytest

from turbodbc import connect

from helpers import for_one_database

"""
Test optional features mentioned in PEP-249 "behave" as specified 
"""

@for_one_database
def test_callproc_unsupported(dsn, configuration):
    cursor = connect(dsn).cursor()

    with pytest.raises(AttributeError):
        cursor.callproc()


@for_one_database
def test_nextset_unsupported(dsn, configuration):
    cursor = connect(dsn).cursor()

    with pytest.raises(AttributeError):
        cursor.nextset()