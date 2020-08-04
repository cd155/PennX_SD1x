class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def decrement(self):
        self.count -= 1
        return self.count
    
    def get_count(self):
        return self.count