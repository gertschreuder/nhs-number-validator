class Validator(object):

    def __init__(self):
        self.isValid = False
    
    def validate(self, number):
        try:
            if number is None:
                return self.isValid
            if isinstance(number, str) and number.find(' ') >= 0:
                number = number.replace(' ', '')
            self.isValid =  number.isdigit() and len(number) == 10
            if self.isValid:
                multiplier = 10
                n = 0
                numArray = list(number)
                for value in numArray:
                    if multiplier == 1:
                        break
                    n = n + (int(value) * multiplier)
                    multiplier = multiplier - 1
                n = 11 - (n % 11)
                if n == 11:
                    n = 0
                if n == 10:
                    self.isValid = False
                    return self.isValid
                
                self.isValid = int(numArray[9]) == n
            return self.isValid
        except Exception:
            self.isValid = False
            return self.isValid
