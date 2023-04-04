class Someting:
    def __init__(self) -> None:
        pass
    def start(self):
        print("hello")
    def stop(self):
        print("by by")

    def howAreYou(self,time):
        print(f"How are you {time}")
    def book(self,name):
        print(f"i like your {name}")
    def hate(self):
        print("i hate you")

    def say(self,functions):
        self.start()
        for function in functions:
            function()
        self.stop()

    def do(self):
        time = "today"
        self.say(
            (
            lambda:self.howAreYou(f"{time}"),
            lambda:self.book("book"))
            )
    def dont(self):
        self.say(self.hate)

Someting().do()