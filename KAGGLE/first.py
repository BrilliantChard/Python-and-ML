spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 2

if spam_amount > 5:
    print("But I don't want ANY spam!")

elif spam_amount > 3:
    print("I said no spam!")

else:
    print("I love spam!")

viking_song = "Spam \n" * spam_amount
print(viking_song)


print(f'\nThe data type of spam amount is {type(spam_amount)}\n')
print(f'\nThe data type of viking song is {type(viking_song)}\n')

print(8-3+2)

# Using tje modulo division operator

alice_candies = 121
bob_candies = 77
carol_candies = 109

total_candies = alice_candies + bob_candies + carol_candies
print(f'Total candies: {total_candies}')
candies_to_smash = (alice_candies + bob_candies + carol_candies) % 3