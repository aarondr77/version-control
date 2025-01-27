import copy
from version_control.State import State
from version_control.Operation import Operation

class FileOpRemove(Operation):

    def __init__(self, file_name):
        self.file_name = file_name

    def apply_operation(self, state):
        if not self.valid_operation(state):
            return None

        files = copy.deepcopy(state.files)
        del(files[self.file_name])

        return State(files)

    def valid_operation(self, state):
        return self.file_name in state.files

    def to_string(self):
        return "FileOpRemove\t{}".format(self.file_name)

    @staticmethod
    def from_string(operation_string):
        operation = operation_string.split("\t")
        return FileOpRemove(operation[1])