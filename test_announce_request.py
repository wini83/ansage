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
