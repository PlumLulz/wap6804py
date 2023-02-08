# Keygen for Zyxel WAP6804, and perhaps the WAP7205 and EMG3415_CBT
# Extracted from the firmware of the WAP7205 from ftp.zyxel.lv
# /bin/GenPresharedkey mode 13, run via qemu-arm

import hashlib
import argparse

def wap6804(serial):
	serial = serial.upper()
	charset = '3456789ABCDEFGHJKLMNPQRTUXYSVW'

	# First round
	dgst = hashlib.sha256()
	dgst.update(serial.encode())
	hexdgst = dgst.hexdigest()

	# Second round
	inp = hexdgst[0:32]+"PSK_ra0"
	dgst2 = hashlib.sha256()
	dgst2.update(inp.encode())
	dgst2 = dgst2.digest()

	key = ""
	for i in range(0, 10):
		letter_position = dgst2[i] % len(charset)
		letter = charset[letter_position]
		key += letter
	print(key)


parser = argparse.ArgumentParser(description='WAP6804 Keygen')
parser.add_argument('serial', help='Serial number')
args = parser.parse_args()

wap6804(args.serial)
