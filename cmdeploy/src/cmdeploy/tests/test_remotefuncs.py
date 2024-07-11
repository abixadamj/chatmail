import pytest

from cmdeploy import remote_funcs


@pytest.fixture
def mockdns(monkeypatch):
    qdict = {
        "A": {"some.domain": "1.1.1.1"},
        "AAAA": {"some.domain": "fde5:cd7a:9e1c:3240:5a99:936f:cdac:53ae"},
        "CNAME": {"mta-sts.some.domain": "some.domain"},
    }.copy()

    def query_dns(typ, domain):
        try:
            return qdict[typ][domain]
        except KeyError:
            return ""

    monkeypatch.setattr(remote_funcs, query_dns.__name__, query_dns)
    return qdict


def test_perform_initial_checks_ok1(mockdns):
    remote_data = remote_funcs.perform_initial_checks("some.domain")
    assert len(remote_data) == 6


@pytest.mark.parametrize("drop", ["A", "AAAA"])
def test_perform_initial_checks_with_one_of_A_AAAA(mockdns, drop):
    del mockdns[drop]
    remote_data = remote_funcs.perform_initial_checks("some.domain")
    assert len(remote_data) == 6
    assert not remote_data[drop]


def test_perform_initial_checks_no_mta_sts(mockdns):
    del mockdns["CNAME"]
    remote_data = remote_funcs.perform_initial_checks("some.domain")
    assert len(remote_data) == 3
    assert not remote_data["MTA_STS"]
