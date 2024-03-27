import api.models.models as models
import pytest

@pytest.fixture
def create_crypto():
    cryptocurrency = models.Cryptocurrency(symbol='bitcoin')

    yield cryptocurrency


@pytest.fixture
def create_crypto_price(create_crypto):
    crypto_price = models.CryptoPrices(symbol=create_crypto, price_usd=52000, timestamp=46392902374839328)

    yield crypto_price


def test_crypto_has_name(create_crypto):
    assert create_crypto.symbol == 'bitcoin'


def test_crypto_prices(create_crypto_price):
    assert create_crypto_price.price_usd == 52000
    assert create_crypto_price.symbol.symbol == 'bitcoin'

