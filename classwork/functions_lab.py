
chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

def count_eggs(list):
    total_eggs = 0
    for birb in list:
        total_eggs += birb["eggs"]
        birb["eggs"] = 0 # eggs have been collected
    print(f"{total_eggs} eggs collected")

count_eggs(chickens)