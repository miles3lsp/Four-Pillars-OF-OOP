from abc import ABC, abstractmethod

class Movie(ABC):
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    @abstractmethod
    def play_trailer(self):
        pass

class NetflixMovie(Movie):
    def play_trailer(self):
        print(f"Playing trailer for '{self.title}' ({self.genre})...")

streaming_movie = NetflixMovie("Interstellar", "Sci-Fi")
streaming_movie.play_trailer()
