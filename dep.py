__author__ = 'tongqingqiu'

#http://codekata.com/kata/kata18-transitive-dependencies/

class Dep:
    def __init__(self):
        self.graph = dict()

    def dependencies_for(self, source):
        """print all source dependencies"""
        dep_set = set()
        if source in self.graph:
            child_set = self.graph[source].copy()
            while len(child_set) > 0:
                s = child_set.pop()
                if s in self.graph:
                    child_set = child_set.union(self.graph[s])
                dep_set.add(s)
        result = list(dep_set)
        result.sort()
        print result

    def add_direct(self, source, target):
        if source in self.graph:
            temp = self.graph[source]
            temp.add(target)
            self.graph[source] = temp
        else:
            self.graph[source] = {target}


if __name__ == '__main__':
    dep = Dep()
    dep.add_direct('A', 'B')
    dep.add_direct('A', 'C')

    dep.add_direct('B', 'C')
    dep.add_direct('B', 'E')

    dep.add_direct('C', 'G')
    dep.add_direct('D', 'A')
    dep.add_direct('D', 'F')

    dep.add_direct('E', 'F')
    dep.add_direct('F', 'H')

    dep.dependencies_for('A')
    dep.dependencies_for('B')
    dep.dependencies_for('C')
    dep.dependencies_for('D')
    dep.dependencies_for('E')
    dep.dependencies_for('F')