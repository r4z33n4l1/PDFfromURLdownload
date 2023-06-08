# PDF Downloader

This script is designed to download PDF files from a specified URL and save them in a local directory.

## Prerequisites

You need to have Python installed on your machine. In addition, this script uses the `requests` and `beautifulsoup4` libraries for fetching and parsing the webpage. You can install these libraries using pip:

```sh
pip install requests beautifulsoup4
```

## Usage

In the script, update the `url` variable with the webpage from which you want to download PDFs:

```python
url = "https://www.example.com"
```

When you run the script, it will create a directory named 'pdfs' (as specified in the `folder_location` variable) in the same directory as the script, if it doesn't already exist. It will then fetch the webpage, find all links to PDF files on the page, and download each one, saving it in the 'pdfs' directory. The filenames are based on the last part of each URL.

Wgeb you run the script, you should see output similar to the following:

```sh
Starting download of 20 PDFs
Downloading 1 of 20: pdfs/file1.pdf
Downloading 2 of 20: pdfs/file2.pdf
...
Downloading 20 of 20: pdfs/file20.pdf
Download completed.
```
This shows the progress of the downloads and lets you know when all files have been downloaded.