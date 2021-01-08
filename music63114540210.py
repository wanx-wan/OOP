class Music:

    def __init__(self, music_genre, music_name, artist, web):
        self.web = web
        self.artist = artist
        self.music_name = music_name

        if music_genre == "Pop":
            self.music_name = "Bad Romance"
            self.artist = "Lady Gaga"
            self.web = "https://youtu.be/qrO4YZeyl0I"

        elif music_genre == "Rock":
            self.music_name = "Rollin"
            self.artist = "Limp Bizkit"
            self.web = "https://youtu.be/RYnFIRc0k6E"

        elif music_genre == "R&B":
            self.music_name = "I Cry"
            self.artist = "Usher"
            self.web = "https://youtu.be/ulqyG0DbAGA"

        else:
            self.music_name = "The song you're looking for is none."
            self.artist = "Please search again."
            self.web = "Please search again."

    def displayData(self):
        print("The song you are looking for is:", "name:", self.music_name,
              "artist:", self.artist, "Music link:", self.web)
        print(Music)


obj1 = Music("R&B", "artist", "music", "web")
obj1.displayData()