#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

if __name__ == '__main__':
    from urllib.error import HTTPError
    from urllib import request
    import sys

    try:
        with request.urlopen(sys.argv[1]) as res:
            res = res.read().decode('UTF-8')
            print(res)
    except HTTPError as exception:
        print('Error code:', exception.code)
