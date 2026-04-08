#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import make_prepare_dict
import make_relic_list
import make_prime_dict

PRIME_JSON_FILE_NAME = "prime.json"
RELICS_JSON_FILE_NAME = "relics.json"
TARGET_URL = "https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html"
# TARGET_URL = "https://www.warframe.com/ja/droptables"

def create_dir(dir_name):
    dir = os.path.join(os.getcwd(), dir_name)

    if not os.path.isdir(dir):
        os.makedirs(dir)

    return dir


def make_json_file(json_dict, dir, filename, sort_keys=False):
    file_path = os.path.join(dir, filename)
    print(dir)
    print(file_path)

    with open(file_path, "w") as f:
        json.dump(json_dict, f, indent=2, sort_keys=sort_keys)


def main(dir_name="output"):
    html = requests.get(TARGET_URL)
    bs_obj = BeautifulSoup(html.text, "html.parser")

    # 準備
    prepare_dict = make_prepare_dict.main(bs_obj)
    relic_list = make_relic_list.main(bs_obj)

    now = datetime.now().strftime("Last Updated: %d %b %Y %H:%M:%S")
    prepare_dict["relics"] = relic_list
    prepare_dict["updateDate"] = now

    dir = create_dir(dir_name)

    # prime.json作成
    prime_dict = make_prime_dict.main(prepare_dict)
    make_json_file(prime_dict, dir, PRIME_JSON_FILE_NAME)

    # relics.json作成
    relics_dict = {}
    relics_dict["relics"] = relic_list
    relics_dict["updateDate"] = now
    make_json_file(relics_dict, dir, RELICS_JSON_FILE_NAME)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        main(args[1])
    else:
        main()
