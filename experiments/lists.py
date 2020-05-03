airlines = ["delta", "american", "united", "southwest", "lufthansa"]

#print element from end. -1 is the last element in the list.
#print(airlines[-2])

#using list comprehension
airlines_appended = [ airline+" airlines" for airline in airlines]
print(airlines_appended)