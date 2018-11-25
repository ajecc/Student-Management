from service.check_input import InputError

class EditAction:
    def __init__(self):
        self._command_history = []
        self._command_history_inverse = []
        self._index = -1

    def _pop_commands_until_index(self):
        index_here = len(self._command_history) - 1
        while index_here > self._index:
            self._command_history.pop()
            self._command_history_inverse.pop()
            index_here -= 1

    def update_history(self, command, command_inverse):
        self._pop_commands_until_index()
        self._command_history.append(command)
        self._command_history_inverse.append(command_inverse)
        self._index += 1

    def undo(self):
        if self._index < 0:
            raise InputError
        self._command_history_inverse[self._index].call_function_cascade()
        self._index -= 1

    def redo(self):
        if self._index >= len(self._command_history) - 1:
            raise InputError
        self._index += 1
        self._command_history[self._index].call_function_cascade()







