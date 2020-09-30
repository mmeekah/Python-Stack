numbers = [1, 3, 5]
doubled = [ num * 2 for num in numbers]


friends = ["Rolf", "Sam", "Samantha", "Jen", "Saken"]
starts_s = [ friend  for friend in friends if friend.startswith("S")]


# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)