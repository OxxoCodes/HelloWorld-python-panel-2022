arr = ["John","went","to","the","store","to","buy","some","milk"]

shorterThanFour = []
for x in arr:
    if len(x) < 4 and x not in shorterThanFour:
        shorterThanFour.append(x)

print(shorterThanFour)