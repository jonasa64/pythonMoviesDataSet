import os
import urllib.request as req
import pandas as pd

# Function to download a given url
def download(url, to=None):
    '''
    Downloads a file from a given url(arg1) and return the relative file name
    :param url: Address of the file to download
    :param to: URL of the file to download to - if none is specified, download to current folder and keep it's file name
    :return: Returns the relative path for futher usage(e.g to open the file)
    '''
    print("Downloading file ...")
    opener = req.build_opener()
    # add headers imitating a browser to enforce download permission from all websites
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    req.install_opener(opener)
    req.urlretrieve(url, to)
    print("Done")

    return to