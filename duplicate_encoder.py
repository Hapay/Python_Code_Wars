def duplicate_encode(word):
  chars = []
  word = word.lower()
  for char in word:
    if word.count(char) == 1:
      chars.append("(")
    else:
      chars.append(")")
  return "".join(chars)


word = "Ada ma lalke i kota!@#$"
print(duplicate_encode(word))
