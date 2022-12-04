sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

sentence_replace = sentence.replace("!", " ").strip(".")
sentence_upper = sentence_replace.upper()
sentence_reverse = sentence_replace[::-1]

print(sentence_replace)
print()
print(sentence_upper)
print()
print(sentence_reverse)