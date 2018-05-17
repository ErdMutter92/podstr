# Podstr

A command line tool for managing your podcasts.

## Features

* Download latest podcast files from a podcast feed

## Usage

usage: podstr [-h] [-c] [-i URL] [-n COUNT] [-o OUTPUT] [-f OVERRIDE] URL

**optional arguments:**

  **-h**, **--help**: show this help message and exit

  **-c**, **--config**: Indicates we are using a configuration file

  **-n** *COUNT*, **--count** *COUNT*: number of files from the top of list to download (int; default: 5)

  **-o** *OUTPUT*, **--output** *OUTPUT*: output directory for downloaded files (string; default: '.')

  **-f** *OVERRIDE*, **--override** *OVERRIDE*: force files to be over written (boolean; default: false)

## Configuration File

The configuration file must be a yaml file following a similar structure to bellow:

    TheBestPodcastEver:
      output: './Podcasts'
      count: 5
      url: https://example.org/podcast/rss

## Planned Features

* Manages multiple podcast feeds by pointing to a file containing a list of URLs OR a single feed by pointing to a URL directly.
* control the number of podcasts download, and remove files when new ones are released.
* save podcasts for a specific amount of time before they are removed for additional podcasts
* limit the amount of space the manager is allowed to use, and it will free up space by deleting older podcasts.
