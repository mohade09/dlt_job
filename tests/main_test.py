from dlt_job.main import get_taxis, get_spark,hello


# def test_main():
#     taxis = get_taxis(get_spark())
#     assert taxis.count() > 5


def test_hello():
    assert hello() == "Hello, World!"