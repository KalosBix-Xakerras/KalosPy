import re

def extract_tweets(src_path, encoding='UTF-8'):
  '''
  一部の記号等に対応していない可能性があります。
  なるべく既に作ってあるテキストファイルを使用し、この関数を積極的には使用しないでください。
  '''
  res = []
  with open(src_path, encoding=encoding) as src:
    for line in src:
      if not re.match(r'#', line):
        tweet_content = re.sub('^@[^ ]+ ', '', line).replace('\n', '')
        if not tweet_content:
          continue
        res += [tweet_content]
  return res
