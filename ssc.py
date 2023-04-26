#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

e= challenge[2][1]
g= challenge[2][0]
n= challenge[3]

print(f"My {e}! The {g} do {n}")
print(f"My {e}! The {g} do {n}")
print(f"My {e}! The {g} do {n}")


trial= [
  "science",
  "turbo",
  {
    "eyes": "goggles",
    "goggles": "eyes"
  },
  "nothing"
]

a= trial[2]["goggles"]
b= trial[2]["eyes"]
c= trial[3]

print(f"My {a}! The {b} do {c}")
print(f"My {a}! The {b} do {c}")
print(f"My {a}! The {b} do {c}")
