class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def getInstance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Erro na declaração do interpretador')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)