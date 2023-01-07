# Create a new file in this folder called loop_lists.py.

# Inside it, define a list of strings of your 5 favourite movies.
movies = ["Die Hard", "Avengers", "Black Panther", "Dr Strange", "Snow white and the huntman"]

# Now, loop over the list. For each item in the list, print out "Movie: " plus the movie's name.
for i in range(len(movies)):
    print(f"Movie {i+1}: {movies[i]}")