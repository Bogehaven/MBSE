from bs4 import BeautifulSoup
import random
import sys
import json

filename = sys.argv[1]
dist=json.loads(sys.argv[2])

with open(filename, 'r') as f:
    data = f.read()
bs_data = BeautifulSoup(data, 'xml')

new_types = random.choices(
    population=list(dist.keys()),
    weights=list(dist.values()),
    k=len(bs_data.find_all('trip'))
)


bs_data.find_all('type')
for idx, tag in enumerate(bs_data.find_all('trip')):
    tag['type'] = new_types[idx]

f = open(filename, "w")
f.write(bs_data.prettify())
f.close()