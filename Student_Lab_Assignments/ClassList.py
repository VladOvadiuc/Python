class List:
    def __init__(self, *par):
        self.ix = 0
        self.data = [*par]

    def __iter__(self):
        return self

    def __next__(self):
        self.ix += 1
        try:
            return self.data[self.ix - 1]
        except IndexError:
            self.ix = 0
            raise StopIteration

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        st = '['
        length = len(self.data) - 1
        for element in self.data:
            if type(element) == int:
                if self.data[length] != element:
                    st += str(element) + ', '
                else:
                    st += str(element)
            elif type(element) == str:
                if self.data[length] != element:
                    st += element + ', '
                else:
                    st += element
            elif type(element) == bool:
                if self.data[length] != element:
                    st += str(element) + ', '
                else:
                    st += str(element)
            elif type(element) == list:
                if self.data[length] != element:
                    st += str(element) + ', '
                else:
                    st += str(element)
            elif type(element) == List:
                if self.data[length] != element:
                    st += str(element) + ', '
                else:
                    st += str(element)
        st += ']'
        return st

    def extend(self, lenghtNew):
        self.data.extend(lenghtNew- len(self.data))

    def __setitem__(self, key, item):
        if key >= len(self):
            self.data.extend(key + 1)
        self.data[key] = item

    def index(self, element):
        return self.data.index(element)

    def append(self, item):
        return self.data.append(item)

    def remove(self, item):
        return self.data.remove(item)

    def insert(self, indx, item):
        return self.data.insert(indx,item)

    def clear(self):
        return self.data.clear()

def sort(data, cmpKey = lambda x: x, reverse = False):
    index = 0
    while index < len(data) - 1:
        if cmpKey(data[index + 1]) >= cmpKey(data[index]):
            index += 1
        else:
            data[index + 1], data[index] = data[index], data[index + 1]
            if index > 0:
                index -= 1
    if reverse == True:
        data = reversed(data)
    return data


def gnomeSort(items, cmpKey = lambda x: x, reverse = False):
    i = 0
    #print(items)
    while i < len(items):
        if i and cmpKey(items[i]) < cmpKey(items[i-1]):
            items[i], items[i-1] = items[i-1], items[i]
            i = i - 1
        else:
            i = i + 1
    if reverse == True:
        items = reversed(items)
    return items

def filter(data, cmpKey = lambda x: x, filelem = None):
    new = List()
    for element in data:
        if filelem[0] == '<':
            if cmpKey(element) < filelem[1]:
                new.append(element)
        elif filelem[0] == '=':
            if cmpKey(element) == filelem[1]:
                new.append(element)
        elif filelem[0] == '>':
            if cmpKey(element) > filelem[1]:
                new.append(element)
    return new