class Movie:
    def __init__(self,titel,hero,herion):
        self.title = titel
        self.hero = hero
        self.herion = herion

    def info(self):
        print("Movie Name:", self.title)
        print("Hero Name:", self.hero)
        print("herion Name:", self.herion)

list_of_movie = []
while True:
    titel = input("Enter Movie Name:")
    hero = input("Enter Hero Name:")
    herion = input("Enter Herion Name:")
    m = Movie(titel,hero,herion)
    list_of_movie.append(m)
    option = input("Do You Want to Add More Movies Name [Yes|No]:")
    if option.lower() == 'no':
        break

print("All Movies Info")
print("#"*40)
for movies in list_of_movie:
    movies.info()
