class Task(dict):
    def __getattr__(self, name):
        return self[name]

    def __dir__(self):
        return super().__dir__() + [str(x) for x in self.keys()]

    def  __setattr__(self, name, value):
        super().__setattr__(name, value)
        raise AttributeError 


t = Task()
t['rr'] = '122'
print(t.rr)
t.rr = 34
print(t.rr)
print(t['rr'])