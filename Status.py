
class Status:

        num_iter = 0
        max_iter = 0
        func_calls = 0

        def __init__(self):
                pass

        def __init__(self, max_iter):
                self.max_iter = max_iter
                self.num_iter = 0
                self.func_calls = 0

        def add_iter(self):
                self.num_iter = self.num_iter + 1;

        def add_func_call(self):
                self.func_calls = self.func_calls
