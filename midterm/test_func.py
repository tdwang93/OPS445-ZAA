#!/usr/bin/env python3

from func import has_bad_chars

# Test cases
print(has_bad_chars("hello-world"))  # Expected output: True
print(has_bad_chars("hello.world"))  # Expected output: True
print(has_bad_chars("helloworld"))   # Expected output: False
print(has_bad_chars("test-string.")) # Expected output: True
print(has_bad_chars("simpletest"))   # Expected output: False
