#!/usr/bin/env python
import argparse
import podcastparser
import urllib.request
import requests
import pprint
import os
import shutil
import yaml
from tqdm import tqdm
import math

def download(url, path, filename):
    request = requests.get(url, stream=True)
    total_size = int(request.headers.get('content-length', 0))
    block_size = 1024
    wrote = 0

    location = os.path.abspath(path)
    with open(location, 'wb') as file:
        for data in tqdm(request.iter_content(block_size), desc=filename, total=math.ceil(total_size//block_size) , unit='KB', unit_scale=True):
            file.write(data)

def parse(feedurl, count, root, override, managed):
    feed = podcastparser.parse(feedurl, urllib.request.urlopen(feedurl))
    for _, cast in zip(range(count), feed['episodes']):
        for item in cast['enclosures']:
            extension = os.path.splitext(item['url'])[1]

            if managed:
                directory = root + '/' + feed['title']

                if not os.path.isdir(directory):
                    os.mkdir(directory)
            else:
                directory = root

            filename = directory + '/' + cast['title'] + extension
            path = os.path.abspath(filename)
            if (not os.path.isfile(path)) or (override):
                download(item['url'], path, cast['title'])
            else:
                print('{}: File already exists'.format(cast['title']))

def parseFromConfig(filename):
    path = os.path.abspath(filename)
    if (os.path.isfile(path)):
        with open(path) as stream:
            try:
                config = yaml.load(stream)
                for channel in config:
                    args = config[channel]
                    parse(args['url'], args['count'], args['output'], False, True)
            except yaml.YAMLError as exc:
                print(exc)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("url", help="the url for the podcast feed")
    parser.add_argument("-c", "--config", help="Indicates we are using a configuration file", action="store_true")
    parser.add_argument("-n", "--count", type=int, help="number of files from the top of list to download (int; default: 5)", default=5)
    parser.add_argument("-o", "--output", help="output directory for downloaded files (string; default: '.')", default=".")
    parser.add_argument("-f", "--override", help="force files to be over written (boolean; default: false)", action="store_true")
    parser.add_argument("-m", "--managed", action="store_true")

    args = parser.parse_args()

    if args.config:
        parseFromConfig(args.url)
    else:
        parse(args.url, args.count, args.output, args.override, args.managed)
