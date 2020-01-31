import json
from datetime import date

f = open("test.json", 'r+')
data = json.load(f)
data['date'] = str(date.today())
print(data)
f.seek(0)
json.dump(data, f, indent=4)
f.truncate()
f.close()