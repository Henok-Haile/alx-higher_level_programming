#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

"""
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    from urllib import request, parse
    import sys

    values = {'email': sys.argv[2]}
    data = parse.urlencode(values).encode('utf-8')

    url = sys.argv[1]

    resp = request.Request(url, data)
    with request.urlopen(resp) as response:
        print(response.read().decode('utf-8'))
