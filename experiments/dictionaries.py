capitals = {
  'india': 'dehli',
  'usa': 'washington dc',
  'canada': 'ottawa',
  'france': 'paris'
}

# sorted order
# Loop on the keys / values / iteams
for country, capital in sorted(capitals.items()): # keys() to get keys, # values() to iterate over values
  print(country.title() + " : " + capital.upper())

