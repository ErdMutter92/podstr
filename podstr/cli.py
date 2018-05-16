#!/usr/bin/env python
import argparse
import podcastparser
import urllib.request
import requests
import pprint
import os
import shutil

def download(url):
    file = requests.get(url, stream=True)
    return file.raw

def save(path, filename, data):
    location = os.path.abspath(path)

    with open(filename, 'wb') as location:
        shutil.copyfileobj(data, location)

def parse(feedurl, count, output, override):
    feed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))
    for _, cast in zip(range(count), feed['episodes']):
        for item in cast['enclosures']:
            extension = os.path.splitext(item['url'])[1]
            filename = output + '/' + cast['title'] + extension
            path = os.path.abspath(filename)
            if (not os.path.isfile(path)) or (override):
                # pprint.pprint('download: {}'.format(item['url']))
                file = download(item['url'])
                # pprint.pprint('saving as: {}'.format(filename))
                save(path, filename, file)

def main():
    url = None
    count = 5
    output = "."
    override = False
    # verbose = False

    parser = argparse.ArgumentParser()

    parser.add_argument("url", help="the url for the podcast feed")
    parser.add_argument("-n", "--count", type=int, help="number of files from the top of list to download (int; default: 5)", default=5)
    parser.add_argument("-o", "--output", help="output directory for downloaded files (string; default: '.')", default=".")
    parser.add_argument("-f", "--override", type=bool, help="force files to be over written (boolean; default: false)", default=False)
    # parser.add_argument("-v", "--verbose", type=bool, help="output info to console (boolean; default: false)", default=False)

    args = parser.parse_args()

    parse(args.url, args.count, args.output, args.override)
