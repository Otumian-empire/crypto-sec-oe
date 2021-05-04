# CRYPTO

Crypto is a sample practice project for the swift python programming material, [swift-python] that implements the Cesar-cipher. Isn't that great?

## Test

- Run test, `python -m pytest test.py` or just `python test.py`

## Dependency

- `pytest` - pip install pytest

## Usage

Create an encrypted text.

```python
from crypto import Crypto

plane_text = "Hello there"
shift = 2

crypto_obj = Crypto(shift, plane_text)

encrypted_text = crypto_obj.encrypt()

print(encrypted_text)

```

Deciper an encrypted text.

```python
from crypto import Crypto

ciphered_text = "jgnnq vjgtg"
shift = 2

crypto_obj = Crypto(shift, ciphered_text)

plane_text = crypto_obj.decrypt()

print(plane_text)

```

#

[swift-python]: https://github.com/Otumain-empire/swift-python
