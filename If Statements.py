#Basic if statements
is_male = True
is_tall = False


if is_male and is_tall:
  print("You are a tall male.")
elif is_male and not (is_tall):
  print("You are a short male")
elif not (is_male) and is_tall:
  print("You are a female who is tall.")
else:
  print("You are either not a male not tall.")