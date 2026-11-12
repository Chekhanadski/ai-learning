text = "Hello Python 2026!"

only_letters = "".join(letter for letter in text if letter.isalpha())
# print(only_letters)

only_number = "".join(number for number in text if number.isdigit())
# print(only_number)

without_space = "".join(ch for ch in text if not ch.isspace())
# print(without_space)


text2 = "Programming"

index_letter_m = ", ".join(str(i) for i, ch in enumerate(text2) if ch == "m")
# print(index_letter_m)

text3 = "Developer"

reversed_developer = "".join(reversed(text3))
# print(reversed_developer)

text4 = "banana"

sorted_text = "".join(sorted(text4))
reversed_sorted_text = ''.join(reversed(sorted_text))

# print(sorted_text)
# print(reversed_sorted_text)

text5 = "Python"
min_text = min(text5)
max_text = max(text5)

# print(min_text)
# print(max_text)


text6 = "PyThOn 2026 Programming!"

count_letter_g = sum(1 for ch in text6 if ch == "g")
# print(count_letter_g)

only_upper_letters = "".join(ch for ch in text6 if ch.isupper())

# print(only_upper_letters)

with_numbers_and_letters = "".join(ch for ch in text6 if not ch.isalnum())
# print(with_numbers_and_letters)

indexes_space = ", ".join(str(i) for i, ch in enumerate(text6) if ch.isspace())
# print(indexes_space)

sort_text = "".join(sorted(
    (ch for ch in text6 if ch.isalpha()), 
    key=str.lower
))
# print(sort_text)

name = "Andrei"
upper_letter = name.isupper()
# print(upper_letter)

text7 = "Hello Python 2026!"

have_number = any(ch.isdigit() for ch in text7)
# print(have_number)

only_letters = all(ch.isalpha() for ch in text7)
# print(only_letters)

numbers = [4, 8, -3, 12, 7]

have_negative_number = any(n < 0 for n in numbers)
# print(have_negative_number)

numbers2 = [12, 15, 21, 30, 7]

all_numbers_more_ten = all(n > 10 for n in numbers2)
# print(all_numbers_more_ten)

text8 = "Hello Python!"

all_letters_ascii = all(ch.isascii() for ch in text8)
have_one_upper_letter = any(ch.isupper() for ch in text8)

# print(all_letters_ascii)
# print(have_one_upper_letter)

text9 = "PyThOn 2026 Programming!"

have_number_or_upper_letter = any(ch.isdigit() or ch.isupper() for ch in text9)
# print(have_number_or_upper_letter)

only_lower_letters = all(ch.islower() for ch in text9 if ch.isalpha())
# print(only_lower_letters)

only_even_numbers = all(int(ch) % 2 == 0 for ch in text9 if ch.isdigit())
# print(only_even_numbers)

names = ['Andrei', 'Anton', 'Maryna']

def write_names(names):
  for name in names:
    yield name

names_generator = write_names(names)

for name_generator in names_generator:
    # print(name_generator)


text_try_except = "Python"

try
