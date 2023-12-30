from models.model import Model





class students(Model):
    __GroupName = 'GroupName'
    __nameTable = 'students'
    __LastName = 'LastName'
    __FirstName = 'FirstName'
    __AdmissionYear = 'AdmissionYear'
    __StudyForm = 'StudyForm'
    


    def get(self):
        return super().get(self.__nameTable)

    def delete(self, id):
        super().delete(self.__nameTable, id)

    def add(self):
        LastName = input("Введите Фамилию: ")
        FirstName = input("Введите имя: ")
        AdmissionYear = input("Введите год поступления: ")
        StudyForm = input("Введите форму обучения: ")
        GroupName - input("Введите названеи группы: ")

        str = f"{self.__LastName}, {self.__FirstName},  {self.__AdmissionYear}, {self.__StudyForm}, {self.__GroupName}"
        super().add(self.__nameTable, str, LastName, FirstName, AdmissionYear, StudyForm, GroupName)

    def update(self):
        id = input("Введите id записи которую надо обновить ")
        field = input("Введите переменную записи которую надо обновить ")
        values = input("Введите значение записи которую надо обновить ")
        super().update(self.__nameTable, id, field, values)

    def getOneField(self, field):
        return super().getOneField(self.__nameTable, field)
    
    def studentCount(self):
        return super().studentCount(self.__nameTable)

