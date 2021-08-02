import re

def sentences(src:list):
  res = []
  for txt in src:
    res += re.findall(r'[^ \.\?\!][^\.\?\!]*[\.\?\!]', txt)
  return res

DECLAR = 1 # 平叙文 (declarative)
INTERRO = 2 # 疑問文 (interrogative)
EXCLAM = 4 # 感嘆文 (exclamatory)
def sentences_by_types(src:list, types:int):
  if types == 0:
    return []
  ptn = r'['
  if (types // DECLAR) % 2 == 1:
    ptn += r'\.'
  if (types // INTERRO) % 2 == 1:
    ptn += r'\?'
  if (types // EXCLAM) % 2 == 1:
    ptn += r'\!'
  ptn += r']$'
  res = []
  for txt in src:
    if re.search(ptn, txt):
      res += [txt]
  return res
