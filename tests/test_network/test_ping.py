from network_common import ping_check


def test_ping_check_success():
    assert ping_check("8.8.8.8") == True


def test_ping_check_fail():
    assert ping_check("240.0.0.0") == False
