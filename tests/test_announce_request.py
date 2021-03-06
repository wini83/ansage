from announce_request import *


def test_validate_text():
    res, err = validate_text(None)
    assert not res
    res, err = validate_text("")
    assert not res
    res, err = validate_text(False)
    assert not res
    res, err = validate_text("sample")
    assert res


def test_validate_lang_none():
    res, err = validate_lang(None)
    assert res


def test_validate_lang_not_string():
    res, err = validate_lang(1.0)
    assert not res


def test_validate_lang_blank():
    res, err = validate_lang("")
    assert not res


def test_validate_lang_not_sup():
    res, err = validate_lang("dp")
    assert not res


def test_validate_lang_pl():
    res, err = validate_lang("pl")
    assert res


def test_validate_volume_none():
    res, err = validate_volume(None)
    assert res


def test_validate_volume_not_float():
    res, err = validate_volume("1g")
    assert not res


def test_validate_volume_out_range():
    res, err = validate_volume(2.0)
    assert not res
    res, err = validate_volume(-0.9)
    assert not res


def test_validate_volume_in_range():
    res, err = validate_volume(1.0)
    assert res
    res, err = validate_volume("0.8")
    assert res


def test_validate_chime_none():
    res, err = validate_chime(None)
    assert res


def test_validate_chime_blank():
    res, err = validate_chime("")
    assert not res


class TestAnnounceRequest:

    payload_minimal = '{"payload":"dupa"}'
    payload_chime1 = '{"payload":"dupa","chime":"none"}'
    payload_chime2 = '{"payload":"dupa","chime":"noge"}'

    def test_load_from_json_minimal(self):
        sa = AnnounceRequest()
        res, err = sa.load_from_json(self.payload_minimal)
        assert res

    def test_load_from_json_chime(self):
        sa = AnnounceRequest()
        res, err = sa.load_from_json(self.payload_chime1)
        assert res
        res, err = sa.load_from_json(self.payload_chime2)
        assert not res
