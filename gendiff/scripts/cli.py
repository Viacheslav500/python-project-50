#!/usr/bin/env python3
# gendiff/scripts/gendiff.py

import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.',
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('first_file', help='first_file')
    parser.add_argument('second_file', help='second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()


if __name__ == "__main__":
    main()
