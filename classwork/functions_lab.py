
# chickens = [
#   { "name": "Margaret", "age": 2, "eggs": 0 },
#   { "name": "Hetty", "age": 1, "eggs": 2 },
#   { "name": "Henrietta", "age": 3, "eggs": 1 },
#   { "name": "Audrey", "age": 2, "eggs": 0 },
#   { "name": "Mabel", "age": 5, "eggs": 1 },
# ]

# # def count_eggs(list):
# #     total_eggs = 0
# #     for birb in list:
# #         total_eggs += birb["eggs"]
# #         birb["eggs"] = 0 # eggs have been collected
# #     print(f"{total_eggs} eggs collected")

# # count_eggs(chickens)

# def find_by_name(list, name):
#     found_name = None
#     for x in list:
#         if x["name"] == name:
#             found_name = x
#             return found_name
#     return None

# chicken = find_by_name(chickens, "Mabel")
# print(chicken)


users = [
  { "user_id": 1, "first_name": "Guido", "last_name": "van Rossum" },
  { "user_id": 2, "first_name": "Katherine", "last_name": "Johnson" },
  { "user_id": 3, "first_name": "Dorothy", "last_name": "Vaughan" },
  { "user_id": 4, "first_name": "Hen", "last_name": "Solo" },
  { "user_id": 5, "first_name": "Mary", "last_name": "Jackson" },
]

def find_by_id(list, id):
    found_id = None     
    for i in list:
        if i["user_id"] == id:
            found_id = i
            return found_id
    return None

user = find_by_id(users, 5)
print(user)