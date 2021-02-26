alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789. "

def lobby():
  k = input("Enter your message: ")
  j = input("Do you want to encrypt or decrypt: ")
  l = int(input("Enter the key: "))
  if j.lower() == "encrypt":
    print(encryptmess(k, l))

  elif j.lower() == "decrypt":
    print(decryptmess(k, l))

  else:
    print("U must enter encrypt or decrypt")


def encryptmess(mess, key):
  encrypted = ""
  for x in mess.upper():
    if x in alphabet:
      m = alphabet.find(x)
      fin = m + key
      while fin > len(alphabet):
        fin = fin - len(alphabet)

      encrypted += alphabet[fin]
    
    else:
      encrypted += x
  
  return encrypted.lower()


def decryptmess(mess, key):
  decrypted = ""
  for x in mess.upper():
    if x in alphabet:
      m = alphabet.find(x)
      fin = m - key
      while 0 > fin:
        fin = fin + len(alphabet)

      decrypted += alphabet[fin]

    else:
      decrypted += x
  
  return decrypted.lower()


lobby()

      
    

