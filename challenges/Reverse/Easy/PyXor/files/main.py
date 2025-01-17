#!/usr/bin/env python3

import sys

def chall():
	secret = [0xcabb, 0xcabd, 0xcaaa, 0xcab8, 0xca85, 0xcaa6, 0xca91, 0xca8c, 0xcab7, 0xca8d, 0xcabf, 0xca90, 0xcab1, 0xca8e, 0xca9b, 0xca8c, 0xca9f, 0xca8a, 0xca97, 0xca91, 0xca90, 0xcaa9, 0xca97, 0xca8a, 0xca96, 0xcab8, 0xca8b, 0xca90, 0xca90, 0xca87, 0xcaae, 0xca8c, 0xca91, 0xca8e, 0xca9b, 0xca8c, 0xca8a, 0xca97, 0xca9b, 0xca8d, 0xca83]
	usr_input = sys.argv[1]
	usr_secret = []
	for letter in usr_input:
		usr_secret.append(ord(letter) ^ 0xcafe)
	for i in range(len(secret)):
		if secret[i] != usr_secret[i]:
			print("Fail :'(")
			exit(1)
	print("Well played, you can use %s as flag for the challenge" % (sys.argv[1]))

if len(sys.argv) == 2:
	chall()
	exit(0)
else:
	print("Invalid number of arguments", file=sys.stderr)
	exit(1)
