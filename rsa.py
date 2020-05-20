from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time
import matplotlib.pyplot as plt

#Three empty lists to store the values for time taken for execution
key = list()
enc = list()
dec = list()

#Generates and returns the key object containing the private and public keys
def newkeys(keysize):
   key = RSA.generate(keysize)
   private, public = key, key.publickey()
   return public, private

#Encrypts the message with the public key using OAEP padding
def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

#Decrypts the encrypted message with the generated private key
def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

def main():
   #The chosedn key lengths(in bits)
   key_lengths = [1024, 2048, 3072, 4096, 5120]
	
   for i in key_lengths:
      start = time.time()
      public, private = newkeys(i)
      end = time.time()
      key.append(1000*(end-start))	

      start = time.time()
      ciphertext = encrypt(b"A message for encryption", public)
      end = time.time()
      enc.append(1000*(end-start))

      start = time.time()
      message = decrypt(ciphertext, private) 
      end = time.time()
      dec.append(1000*(end-start))

   #print(key, enc, dec)

   '''
   Plotting the graph with the key lengths on the x-axis and logscale
   of time taken(in milliseconds) on the y-axis
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
