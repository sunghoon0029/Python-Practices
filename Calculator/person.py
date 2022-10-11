class Person():
    count = 0
    def __init__(self) -> None:
        self.count += 1

    @classmethod
    def printCunt(cls):
        print(cls.count)
        
    def printCunt2(self):
        print(self.count)