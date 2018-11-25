class Repository:
    def __init__(self, repo=None):
        if repo is None:
            self._repo = []
        else:
            self._repo = repo

    def get_repo(self):
        return self._repo

    def set_repo(self, lst):
        self._repo = lst

    def get_size_of_list(self):
        # made this function in case we modify our repo type
        return len(self._repo)

    def add(self, obj):
        """
        Adds object to list
        :param obj: Student, Assignment or Grade
        """
        if obj not in self._repo:
            self._repo.append(obj)

    def remove(self, obj):
        """
        removes object from list
        :param obj: Student, Assignment or Grade
        """
        if obj in self._repo[:]:
            self._repo.remove(obj)

    def in_list(self, id_):
        """
        Checks if object with id_ is in list
        :param id_: a string (that can be casted to int)
        """
        for obj in self._repo:
            if obj.get_id() == id_:
                return True
        return False

    def get_by_id(self, id_):
        """
        Get an object with id_ as its id
        :param id_: a string (that can be casted to uint)
        :return: Student, Assignment or Grade
        """
        for obj in self._repo:
            if obj.get_id() == id_:
                return obj

    def remove_by_id(self, id_):
        """
        Removes object from list with id_ as its id
        :param id_: a string (that can be casted to uint)
        """
        self.remove(self.get_by_id(id_))

    def sorted_list(self):
        return sorted(self._repo[:])

    def __eq__(self, other):
        return self._repo == other.get_repo()

    def __str__(self):
        list_to_string = ""
        for i in self._repo:
            list_to_string += str(i) + '\n'
        return list_to_string

    def __contains__(self, item):
        for obj in self._repo:
            if item == obj:
                return True
        return False

