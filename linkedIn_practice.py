# import random
# print(random.randint(1,10))
# print(random.random())

# answer = random.randint(1,3)
# if answer == 1:
#     print("yes")
# if answer == 2:
#     print("No")
# if answer==3:
#     print("May be")
# fortune_number = random.randint(1,3)
# lucky_number = random.randint(1,100)

# fortune_text = ''
# if fortune_number == 1:
#     fortune_text='you will have a great day!'
# if fortune_number ==2:
#     fortune_text='today will be tough... but worth it'
# if fortune_number==3:
#     fortune_text='you will get married'
# print(f'{fortune_text} your lucky number is :{lucky_number} ')
text = """
a a A b n n
"""
print(text.split())

word_count= {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] =1
print(word_count)

