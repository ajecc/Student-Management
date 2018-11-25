class FunctionCascade:
    def __init__(self):
        self._functions = []
        self._args_list = []
        self._nr_functions = 0

    def add_function(self, function, args):
        self._functions.append(function)
        self._args_list.append(args)
        self._nr_functions += 1

    def call_function_cascade(self):
        for i in range(self._nr_functions):
            function_here = self._functions[i]
            args_here = self._args_list[i]
            function_here(*args_here)
