abeceda = "abcdefghijklmnopqrstuvwxyz123456789!?. "


messa = "Hello my friend. How are you?"

def enc_formula(x):
  return round(x**5/4)

def dec_formula(x):
  p = x*4
  b = 0.2
  return round(p**b)


def encrypt(mess):
  mess = mess.lower()
  positions = []
  for x in mess:
    m = abeceda.find(x)
    positions.append(m)

  new_positions = []

  for i in positions:
    j = enc_formula(i)
    new_positions.append(j)

  return new_positions

l = encrypt(messa)

    
def decrypt(n):
  text = ""
  for b in n:
    v = dec_formula(b)
    print(v)
    text += abeceda[v]

  return text

print(decrypt(l))


  
  
  