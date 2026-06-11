from abc import ABC, abstractmethod

# Abstract class acting as a blueprint
class Movie(ABC):
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    @abstractmethod
    def play_trailer(self):
        pass # Implementation detail hidden here

# Concrete class implementing the abstract method
class NetflixMovie(Movie):
    def play_trailer(self):
        print(f"Playing trailer for '{self.title}' ({self.genre})...")

streaming_movie = NetflixMovie("Interstellar", "Sci-Fi")
streaming_movie.play_trailer()