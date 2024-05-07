# Usage
```
python3 urlcoder.py -h
```
```
usage: python3 urlcoder.py [-h] [-u URL] [-e] [-d] [-n {1,2,3}] [-f]

URL encoder and decoder

options:
  -h, --help         show this help message and exit
  -u URL, --url URL  URL to encode or decode. Should be enclosed in quotes.
  -e, --encode       Encode the URL
  -d, --decode       Decode the URL
  -n {1,2,3}         Number of times to encode or decode the URL (1, 2, or 3)
  -f, --full         Encode the full URL including the prefix
```
```
ex: python3 urlcoder.py -e -u "http://test_encode_url/someone id=1"
Encoded URL (1 times): http://test_encode_url/someone%20id%3D1

ex2: python3 urlcoder.py -d -u "http://test_encode_url/someone%20id%3D1"
Decoded URL (1 times): http://test_encode_url/someone id=1

ex3: python3 urlcoder.py -e -n3 -u "http://test_encode_url/someone%20id%3D1"
Encoded URL (3 times): http://test_encode_url/someone%25252520id%2525253D1

ex4: python3 urlcoder.py -e -f -u "http://test_encode_url/someone%20id%3D1"
Encoded Full URL (1 times): http%3A//test_encode_url/someone%2520id%253D1

```
