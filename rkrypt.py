from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from binascii import hexlify
from binascii import unhexlify
import sys

mode = sys.argv[1]

def gen_rsa_keypair():
	random_gen = Random.new().read
	key = RSA.generate(2048, random_gen)
	private_key = key.exportKey()
	public_key = key.publickey().exportKey()
	priv_keyfile = "k_private"
	pub_keyfile = "k_public"
	priv_key_fd = open(priv_keyfile, "w")
	pub_key_fd = open(pub_keyfile, "w")
	priv_key_fd.write(private_key)
	pub_key_fd.write(public_key)
	priv_key_fd.close()
	pub_key_fd.close()

def import_priv_key():
	priv_keyfile = "k_private"
	priv_key_fd = open(priv_keyfile, "r")
	private_key = RSA.importKey(priv_key_fd.read())
	priv_key_fd.close()
	return private_key

def import_pub_key():
	pub_keyfile = "k_public"
	pub_key_fd = open(pub_keyfile, "r")
	public_key = RSA.importKey(pub_key_fd.read())
	pub_key_fd.close()
	return public_key

def rsa_encrypt(data, public_key):
	cipher = PKCS1_OAEP.new(public_key)
	cipher_text = cipher.encrypt(data)
	return cipher_text

def rsa_decrypt(data, private_key):
	cipher = PKCS1_OAEP.new(private_key)
	plain_text = cipher.decrypt(data)
	
	return plain_text

if mode == "gen":
	gen_rsa_keypair()
	print "Private and Public RSA keys output to Z_private and Z_public"
elif mode == "encrypt":
	infile = sys.argv[2]
	outfile = sys.argv[3]
	in_fd = open(infile, "r")
	out_fd = open(outfile, "w")
	plain_text = in_fd.read()
	public_key = import_pub_key()
	cipher_text = ""
	cipher_text_buf = rsa_encrypt(plain_text, public_key)
	cipher_text_buf_len = len(cipher_text_buf)
	for x in range(0,cipher_text_buf_len):
		cipher_text += cipher_text_buf[x]
	out_fd.write(cipher_text)
	in_fd.close()
	out_fd.close()
elif mode == "decrypt":
	infile = sys.argv[2]
	outfile = sys.argv[3]
	in_fd = open(infile, "r")
	out_fd = open(outfile, "w")
	cipher_text = in_fd.read()
	private_key = import_priv_key()
	plain_text = rsa_decrypt(cipher_text, private_key)
	out_fd.write(plain_text)
	in_fd.close()
	out_fd.close()

