class Stop:
    def __init__(self, name: str):
        self.lines = list()
        self.name = name


class Line:
    def __init__(self, name: str):
        self.name = name
        self.stops = list()

    def add_stop(self, stop: Stop):
        self.stops.append(stop)
        stop.lines.append(self)


def main():
    a: Stop = Stop("Eichtalboden")
    b: Stop = Stop("Baden")
    line1 = Line("line1")
    line2 = Line("line2")
    line1.add_stop(a)
    line1.add_stop(b)
    line2.add_stop(a)
    line2.add_stop(b)

    print("lines in A")
    for i in a.lines:
        print(i.name)


if __name__ == "__main__":
    main()
