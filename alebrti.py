import sys

ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
sude = "QWERTYUIOPASDFGHJKLZXCVBNM "
liche = "MNBVCXZLKJHGFDSAPOIUYTREWQ "


def main():
  i = input("Enter your mess: ")
  o = i.upper()
  ok = input("Do you want to encrypt or decrypt: ")
  if ok.lower() == "encrypt":
    print(encmess(o))
  
  elif ok.lower() == "decrypt":
    print(decmess(o))

  else:
    sys.exit("Wrong input")




def encmess(word):
  finall = ""
  for x in word:
    k = word.find(x)
    if k % 2 == 0 or k == 0:
      u = ab.find(x)
      g = sude[u]
      finall += g

    elif k % 2 != 0:
      u = ab.find(x)
      g = liche[u]
      finall += g

    else:
      finall += x
  
  return finall.lower()
    
def decmess(word):
  finall = ""
  for x in word:
    k = word.find(x)
    if k % 2 == 0 or k == 0:
      u = sude.find(x)
      g = ab[u]
      finall += g

    elif k % 2 != 0:
      u = liche.find(x)
      g = ab[u]
      finall += g

    else:
      finall += x

  return finall.lower()

if __name__ == "__main__":
  main()
    
