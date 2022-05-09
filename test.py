import tracemalloc as tm
from collections import Counter

s = "a" * 10**6


def with_list():
    " ".join(list(s))


def without_list():
    " ".join(s)


without_bytes = Counter()
with_bytes = Counter()


for func in [with_list, without_list] * 3:
    tm.start()
    func()
    peak = tm.get_traced_memory()[1]
    tm.stop()
    if func.__name__ == "without_list":
        without_bytes[peak] = without_bytes.get(peak, 0) + 1
    else:
        with_bytes[peak] = with_bytes.get(peak, 0) + 1

print("Without list:")
for b, c in without_bytes.items():
    print(f"{b:,} : {c}")

print("With list:")
for b, c in with_bytes.items():
    print(f"{b:,} : {c}")
