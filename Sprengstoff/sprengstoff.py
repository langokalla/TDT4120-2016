from sys import stdin


class Record:
    value = None
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None


def search(record):
    heaviestw = record.value
    while record.next is not None:
        if heaviestw < record.next.value:
            heaviestw = record.next.value
        record = record.next
    return heaviestw


def main():
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    print(search(first))


if __name__ == "__main__":
    main()
