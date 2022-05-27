import string
from types import new_class
from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, tracks, score, name, age):
        self.name : str = name
        self.age : int = age
        self.tracks : list = tracks
        self.score :float = score

    def change_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self.name = new_name
        print(self.name)
    
    def change_age(self, new_age):
        if not isinstance(new_age, int):
            raise TypeError("age must be an integer")
        self.age = new_age
        print(self.age)
    
    def add_track(self, added_track):
        if not isinstance (added_track, str):
            raise TypeError("track must be type string")
        self.tracks.append(added_track)
        print(self.tracks)
    
    def get_score(self):

        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(45)
print(Bob.get_score())
Bob.add_track("UI/UX")
