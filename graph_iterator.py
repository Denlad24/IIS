from abc import ABCMeta, abstractmethod


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, message: str) -> None:
        pass


class Observable(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.observers = []  # инициализация списка наблюдателей

    def register(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)


class News(Observable):

    def add_news(self, news: str) -> None:
        self.notify_observers(news)


class Citizen(Observer):

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print('{} узнал следующее: {}'.format(self.name, message))


class GraphIterator:
    def __init__(self, graph, start='A'):
        self.graph = graph
        self.start = start
        self.next = self.start
        self.visited = []
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.next not in self.visited:
            self.visited.append(self.next)
            for n in graph[self.next]:
                dfs(graph, n, self.visited)
        if self.i > len(self.visited) - 1:
            raise StopIteration()
        self.next = self.visited[self.i]
        return self.next

    def current(self):
        return self.next

    def first(self):
        self.next = self.start
        self.i = 0


graph = {'A': (['B', 'C']),
         'B': (['A', 'D', 'E']),
         'C': (['A', 'F']),
         'D': (['B']),
         'E': (['B']),
         'F': (['C'])}

iter = GraphIterator(graph)
news = News()
news.register(Citizen('Иван'))
news.register(Citizen('Василий'))
for i in iter:
    print(i)
    if i == "B" or i == "F":
        str1 = "Прошли через точку " + i
        news.add_news(str1)
print(iter.current())
