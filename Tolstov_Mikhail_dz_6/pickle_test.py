import pickle
import time
import json

nums = list(range(0, 5000000))

start = time.perf_counter()
with open('num_json1.json', 'w', encoding='utf-8') as f:
    json.dump(nums, f)
end = time.perf_counter()
print(f'Write time json: {end - start}')

start = time.perf_counter()
with open('num_json1.json', 'r', encoding='utf-8') as f:
    read_data = json.loads(f.read())
end = time.perf_counter()
print(f'read time json: {end - start}')


start = time.perf_counter()
with open('num_pickle.pickle', 'wb') as f:
    pickle.dump(nums, f)
end = time.perf_counter()

print(f'Write time pickle: {end - start}')

start = time.perf_counter()
with open('num_pickle.pickle', 'rb') as f:
    data = pickle.load(f)
end = time.perf_counter()
print(f'Read time pickle: {end - start}')

