# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:06:17 2023

@author: ken3

Introduction:
    argparse is a module in Python's standard library that makes it easy to 
    write command-line interfaces. It simplifies the process of defining and 
    parsing command-line arguments and options. With argparse, you can create 
    a command-line interface for your Python script without having to manually parse sys.argv.
"""

import argparse

def main(name, job):
    print(f"{name} works as a {job}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get name and job")
    parser.add_argument('-n', '--name', type=str, help='Your name', required=True)
    parser.add_argument('-j', '--job', type=str, help='Your job', required=True)

    args = parser.parse_args()

    main(args.name, args.job)