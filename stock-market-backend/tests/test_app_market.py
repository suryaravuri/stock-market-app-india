import pytest

from app.market import app_market as am


@pytest.mark.parametrize(
    "market, exchange, allowed",
    [
        ("US", "NASDAQ", True),
        ("US", "NYSE", True),
        ("US", "NSE", False),
        ("US", "BSE", False),
        ("IN", "NSE", True),
        ("IN", "NASDAQ", False),
        ("ALL", "NSE", True),
        ("ALL", "NASDAQ", True),
    ],
)
def test_exchange_allowed(monkeypatch, market, exchange, allowed):
    monkeypatch.setattr(am.settings, "app_market", market, raising=False)
    assert am.exchange_allowed(exchange) is allowed


def test_enabled_markets(monkeypatch):
    monkeypatch.setattr(am.settings, "app_market", "us", raising=False)
    assert am.enabled_markets() == {"US"}
    monkeypatch.setattr(am.settings, "app_market", "ALL", raising=False)
    assert am.enabled_markets() == {"US", "IN"}
    monkeypatch.setattr(am.settings, "app_market", "nonsense", raising=False)
    assert am.enabled_markets() == {"US"}


def test_indian_symbols_get_sectors():
    from app.market.sectors import sector_for

    assert sector_for("HDFCBANK.NS") == "IN_BANKS_FINANCE"
    assert sector_for("TCS.BO") == "IN_IT_SERVICES"
    assert sector_for("RELIANCE") == "IN_ENERGY_OIL_GAS"
