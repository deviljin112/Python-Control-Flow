import random

ratings = [18, 15, 12, 8, 0]
movie_rating = random.choice(ratings)

user_age = int(input("How old are you?\n=> "))

if user_age >= movie_rating or movie_rating == 0:
    print("You are old enough to watch the movie.\nEnjoy the show!")
elif movie_rating == 8:
    parents = input("Did you come with a parent?\n=> ")

    if parents.lower() == "yes":
        print("You can watch the movie!\nEnjoy the show!")
    else:
        print(
            "Sorry you are not old enough to watch this movie!\nYou will need to come back with a parent!"
        )
else:
    print("Sorry you are not old enough to watch this movie!")

print(f"Movie Rating was: {movie_rating}")