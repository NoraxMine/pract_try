class Person:
    def __init__(self, name, surname, age, email):
        try:
            self.test(name)    
            self.name = name
        except:
             print('Неверно указанно имя')
        try:
            self.test(surname)    
            self.surname = surname
        except:
             print('Неверно указанно фамилия')
        try:
            if int(age) > 0 and int(age) < 125:
                    self.age = int(age)
            else:
                 raise ValueError
        except:
             print('Введи нормальный возвраст')
        try:
            if '@' in email and '.' in email:
                a = email
                b = ("@")
                c = (".")
                s = a.find ("@") + 1
                e = a.rfind(".")
                z = a[s:e]
                if z == None:
                     raise ValueError("0")
                elif a.count('@') == 1 and a.count('.') == 1:
                    if email.find(b) and email.find(b):
                            self.email = email
                    else:
                        raise ValueError("1")
                else:
                 raise ValueError("2")    
            else:
                 raise ValueError("3")
        except Exception as e:
             print(e)
    def test(self, name):
         asc = [ord(char) for char in name]
         for i in asc:
              if i not in range(97, 123) and i != 45:
                   raise ValueError
    
    def __del__(self):
         print('')

cv = Person('asdfa-asd', 'qwe', '12', 'weq1we@21312.fg')