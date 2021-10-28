#!/usr/bin/env python

import os
import sys
import argparse
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from func import run

warnings.filterwarnings('ignore')


def sys_path():
    path = os.path.join(os.getcwd(), 'chromedriver', 'bin', 'chromedriver')
    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('campus', type=str, default="燕园")
    parser.add_argument('reason', type=str, default="恰饭")
    parser.add_argument('in_habitation', type=str, default="北京")
    parser.add_argument('in_district', type=str, default="海淀区")
    parser.add_argument('in_street', type=str, default="燕园街道")
    parser.add_argument('out_destination', type=str, default="北京")
    parser.add_argument('out_track', type=str, default="燕园-畅春园")
    parser.add_argument('wechat', type=str, default="False")
    parser.add_argument('sckey', type=str, default="xxxxxxxx")
    args = parser.parse_args()

    print('Driver Launching...')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    assert os.path.isfile(sys_path())
    driver_pjs = webdriver.Chrome(
        options=chrome_options,
        executable_path=sys_path(),
        service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'],
    )
    print('Driver Launched\n')

    run(driver_pjs, args.username, args.password, args.campus, args.reason,
        args.out_destination, args.out_track,
        args.in_habitation, args.in_district, args.in_street, False, '',
        eval(args.wechat), args.sckey)

    driver_pjs.quit()