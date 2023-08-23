import random


def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


# account_a = random.choice(data)
# account_b = random.choice(data)
# if account_a == account_b:
#   account_b = random.choice(data)

# game_is_on = True
# score = 0
# while game_is_on:
#   print(f"Compare A: {format_data(account_a)}")
#   print(f"Against B: {format_data(account_b)}")
#   print(account_a["follower_count"])
#   print(account_b["follower_count"])
#   # print(account_a["follower_count"])
#   print(f"Your current score: {score}")
#   compare = input("Who has more followers? Type 'A' or 'B'").upper()
#   if compare == 'A':
#     if account_a["follower_count"] > account_b["follower_count"]:
#       print("You win")
#       account_b = random.choice(data)
#       if account_a == account_b:
#         account_b = random.choice(data)
#       score += 1
#     else:
#       print("You loose")
#       game_is_on = False
#   elif compare == 'B':
#     if account_b["follower_count"] > account_a["follower_count"]:
#       print("You win")
#       account_a = account_b
#       account_b = random.choice(data)
#       if account_a == account_b:
#         account_b = random.choice(data)
#       score += 1
#     else:
#       print("You loose")
#       game_is_on = False

game_is_on = True
score = 0

account_a = random.choice(data)
while game_is_on:
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # print(account_a['follower_count']) Debug code
    # print(account_b['follower_count']) Debug code - shows the follower count
    print(f"Your current score: {score}")
    compare = input("Who has more followers? Type 'A' or 'B'").upper()

    if (
            (compare == 'A' and account_a['follower_count'] > account_b['follower_count']) or
            (compare == 'B' and account_b['follower_count'] > account_a['follower_count'])
    ):
        print("You win")
        score += 1
        if compare == 'B':
            account_a = account_b
    else:
        print("You lose")
        game_is_on = False

