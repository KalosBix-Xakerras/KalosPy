import re

def extract_tweets(src_path, encoding='UTF-8'):
  res = []
  with open(src_path, encoding=encoding) as src:
    for line in src:
      if not re.match(r'#', line):
        tweet_content = re.sub('^@[^ ]+ ', '', line).replace('\n', '')
        if not tweet_content:
          continue
        res += [tweet_content]
  return res
