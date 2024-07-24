babbling = ["aya", "yee", "u", "maa", "wyeoo"]


words = ["aya", "ye", "ma", "woo"]
for i in range(len(babbling)):
    for word in words:
        babbling[i] = babbling[i].replace(word, ' ')
    babbling[i] = babbling[i].replace(' ', '')
print(babbling.count(''))


# def babble(babbling):
#     words = ["aya", "ye", "ma", "woo"]
#     for i in range(len(babbling)):
#         for word in words:
#             babbling[i] = babbling[i].replace(word, ' ')
#         babbling[i] = babbling[i].replace(' ', '')
#     return babbling.count('')


