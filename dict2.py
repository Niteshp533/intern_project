class KeyNotFoundError(Exception):
    #Custom exception
      pass

class Dict2:
    def __init__(self):
        self.keys = []
        self.values = []

    def __setitem__(self, key, value):
        if key in self.keys:
            idx = self.keys.index(key)
            self.values[idx] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def __getitem__(self, key):
        if key in self.keys:
            idx = self.keys.index(key)
            return self.values[idx]
        else:
            raise KeyNotFoundError(f"Key '{key}' not found")

    def __iter__(self):
        return iter(self.keys)

