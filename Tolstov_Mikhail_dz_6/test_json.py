import json

nums = list(map(chr, list(range(0, 100))))
nums_json = json.dumps(nums)
print(nums_json, type(nums_json))


with open('num_json.json', 'w', encoding='utf-8') as f:
    f.write(nums_json)

with open('num_json.json', 'r', encoding='utf-8') as f:
    read_data = json.loads(f.read())
# print(read_data, type(read_data))
with open('num_json.json', 'w', encoding='utf-8') as f:
    #f.write(nums_json)
    json.dump(nums, f)
with open('num_json.txt', 'w', encoding='utf-8') as f:
    f.write(str(nums))