from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import matplotlib.pyplot as plt

key = list()
enc = list()
dec = list()

def newkeys(keysize):
   key = RSA.generate(keysize)
   private, public = key, key.publickey()
   return public, private

def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

def main():
   key_lengths = [1024, 2048, 3072, 4096, 5120]
   for i in key_lengths:
      start = time.time()
      public, private = newkeys(i)
      end = time.time()
      key.append(1000*(end-start))	

      start = time.time()
      ciphertext = encrypt(b"A message for encryption", public)
      end = time.time()
      print(public.e, private.d)
      enc.append(1000*(end-start))

      start = time.time()
      message = decrypt(ciphertext, private) 
      end = time.time()
      dec.append(1000*(end-start))

   print(key, enc, dec)

   '''
   plt.figure()

   plt.subplot(221)
   plt.plot(key_lengths, key, ".-r", label="kg")
   plt.plot(key_lengths, enc, "*-b", label="enc")
   plt.plot(key_lengths, dec, "o-g", label="dec")
   plt.title("The usual")
   plt.xlabel("Key sizes")
   plt.ylabel("Time(in milliseconds)")
   plt.legend()

   plt.subplot(222)
   plt.plot(key_lengths, key, ".-r", label="kg")
   plt.plot(key_lengths, enc, "*-b", label="enc")
   plt.plot(key_lengths, dec, "o-g", label="dec")
   plt.yscale("log")
   plt.xlabel("Key sizes")
   plt.ylabel("Time(ms)")
   plt.title("Log scale of time")
   plt.legend()

   plt.subplot(223)
   plt.plot(key_lengths, enc, "*-b", label="enc")
   plt.plot(key_lengths, dec, "o-g", label="dec")
   plt.title("Encryption vs Decryption")
   plt.xlabel("Key sizes")
   plt.ylabel("Time(in milliseconds)")
   plt.legend()
   '''

   plt.figure()

   plt.plot(key_lengths, key, ".-b", label="Key_generation")
   plt.plot(key_lengths, enc, ".-g", label="Encryption")
   plt.plot(key_lengths, dec, ".-y", label="Decrption")
   plt.yscale("log")
   plt.xlabel("Key sizes")
   plt.ylabel("Time(ms)")
   plt.title("Log scale of time")
   plt.legend()

   plt.show()

if __name__ == "__main__":
	main()
