def caught_speeding(speed, is_birthday):
  if speed <= 60 and not is_birthday:
    return 0
  elif (speed > 60 and not is_birthday) and (speed <= 80 and not is_birthday):
    return 1
  elif (speed > 80 and not is_birthday):
    return 2
  elif (speed <= 65 and is_birthday):
    return 0
  elif (speed > 65 and is_birthday) and (speed <= 85 and is_birthday):
    return 1
  elif (speed > 85 and is_birthday):
    return 2