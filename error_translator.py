class ErrorTranslator:
    def __init__(self, err: Exception):
        self.__error = err
    def read_error(self):
        if('Invalid' in str(self.__error)):
            return  'Maluquice eu não entendo, painhô!'
        if('NoneType' in str(self.__error)):
            return 'Deu ruim, não entendi nada!!!'
        return 'Deu ruim, não entendi nada!!!'