def sort_strings(string):
  string_list = string.split()
  string_list.sort(key=lambda word: word.lower())
  return ' '.join(string_list) 

if __name__ == '__main__':
  print(sort_strings("banana ORANGE apple"))
  print(sort_strings("sort my Sentence"))