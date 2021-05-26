# Copyright (c) 2021 Sebastian Pipping <sebastian@pipping.org>
# Licensed under the MIT license

import base64
import hashlib
import os
import tempfile
from argparse import ArgumentParser

import requests


def download_url_to_file(url):
    response = requests.get(url, allow_redirects=True)
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(response.content)
    return f.name


def obtain_hash_for_local_file(filename: str) -> str:
    h = hashlib.sha256()
    with open(filename, 'br') as f:
        h.update(f.read())
    bytes_digest = b'sha256-' + base64.b64encode(h.digest())
    return bytes_digest.decode('ascii')


def run(config):
    delete_file = False
    if config.filename_or_url.startswith('https://'):
        filename = download_url_to_file(config.filename_or_url)
        delete_file = True
    else:
        filename = config.filename_or_url

    try:
        print(obtain_hash_for_local_file(filename))
    finally:
        if delete_file:
            os.remove(filename)


def main():
    parser = ArgumentParser()
    parser.add_argument('filename_or_url',
                        metavar='FILE|URL',
                        help='File or https:// URL to compute checksum for')
    config = parser.parse_args()
    run(config)


if __name__ == '__main__':
    main()
