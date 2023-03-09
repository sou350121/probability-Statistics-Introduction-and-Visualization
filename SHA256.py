# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:39:14 2023

@author: ken3

Introduction:
    cryptographic hash function that generates a fixed-length output of 
    256 bits (32 bytes).
    it operates on a message of arbitrary length and produces 
    a fixed-length hash value. It involves several rounds of bit manipulation and 
    logical operations such as AND, OR, and XOR. The input message is 
    divided into 512-bit blocks, and each block undergoes a series of transformations 
    using a set of fixed constants and functions. The resulting hash value is 
    unique to the input message, and even small changes to the message will result 
    in a completely different hash value.
"""

import hashlib

message = b"Hello, world!"
hash_object = hashlib.sha256(message)
hash_hex = hash_object.hexdigest()

print(hash_hex)