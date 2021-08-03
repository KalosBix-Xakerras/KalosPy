import re

def sentences(src:list) -> list:
  res = []
  for txt in src:
    sen = re.findall(r'[^ \.\?\!][^\.\?\!]*[\.\?\!] ', txt + ' ')
    for s in sen:
      res += [re.match(r'(.*) ', s).group(1)]
  return res

DECLAR = 1 # 平叙文 (declarative)
INTERRO = 2 # 疑問文 (interrogative)
EXCLAM = 4 # 感嘆文 (exclamatory)
def sentences_by_types(src:list, types:int) -> list:
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

# カンマを...
COMMA_REMOVE = 0 # 除去する
COMMA_INCLUDE = 1 # 語中に含む
COMMA_SPLIT = 2 # 独立の語とみなす
# ピリオド（疑問符・感嘆符含む）を...
PERIOD_REMOVE = 0 # 除去する
PERIOD_INCLUDE = 3 # 語中に含む
PERIOD_SPLIT = 6 # 独立の語とみなす
def words_from_sentence(sentence:str, option:int=COMMA_REMOVE+PERIOD_REMOVE) -> list:
  if not option in range(9):
    raise ValueError("argument 'comma' must be in 0 to 8")
  splited = sentence.split()
  res = []
  PTN = [
    r'[^\,\.\?\!]+',              # 0 + 0
    r'[^\.\?\!]+',                # 1 + 0
    r'(\,|[^\,\.\?\!]+)',         # 2 + 0
    r'[^\,]+',                    # 0 + 3
    r'.+',                        # 1 + 3
    r'(\,|[^\,]+)',               # 2 + 3
    r'(\.|\?|\!|[^\,\.\?\!]+)',   # 0 + 6
    r'(\.|\?|\!|[^\.\?\!]+)',     # 1 + 6
    r'(\,|\.|\?|\!|[^\,\.\?\!]+)' # 2 + 6
  ][option]
  for word in splited:
    res += re.findall(PTN, word)
  return res

def count_sylls(word:str) -> int:
  VOWELS = r'[aeiouAEIOU]'
  res = len(re.findall(VOWELS, word))
  return res

def backpos(whatth, num_of_words) -> int:
  res = whatth - num_of_words - 1
  return res

def relpos(whatth, num_of_words) -> float:
  res = (whatth - 0.5) / num_of_words
  return res

FRONT = 0
BACK = 1
REL = 2
SYLL = True
LENGTH = False
def pos_syll_len(sentence:str, x_type:int, y_type:bool) -> (list, list):
  '''
  x_type: FRONT or BACK or REL
  y_type: SYLL or LENGTH
  '''
  if not x_type in range(3):
    raise ValueError("argument 'x_type' must be in 0 to 2")
  x_list, y_list = [], []
  words = words_from_sentence(sentence)
  for words_index in range(len(words)):
    word = words[words_index]
    whatth = words_index + 1
    if x_type == FRONT:
      x = whatth
    elif x_type == BACK:
      x = backpos(whatth, len(words))
    else:
      x = relpos(whatth, len(words))
    y = count_sylls(word) if y_type == SYLL else len(word)
    x_list += [x]
    y_list += [y]
  return x_list, y_list
