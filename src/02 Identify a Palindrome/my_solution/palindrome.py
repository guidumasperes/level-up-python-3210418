from string import punctuation

def palindrome(text):
  parsed_text = "".join(text.translate(str.maketrans("", "", punctuation + "1234567890")).lower().split(" "))
  reversed_parsed_text = parsed_text[::-1]
  if parsed_text == reversed_parsed_text:
    return True
  else:
    return False

if __name__ == '__main__':
  print(palindrome("hello world"))  # false
  print(palindrome("Go hang a salami, I'm a lasagna hog."))  # true