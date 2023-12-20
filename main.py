import mysql.connector

# Функция для выполнения SQL-запроса
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

# Функция для подключения к базе данных
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='dbt7',
            user='root',
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Основная функция
def main():
    # Подключаемся к базе данных
    connection = connect_to_database()

    if not connection:
        print("Не удалось подключиться к базе данных.")
        return

    try:
        # Запрос номера задания
        task_number = int(input("Введите номер задания (1-3): "))

        # Выполнение соответствующего SQL-запроса
        if task_number == 1:
            query = "SELECT COUNT(*) AS StudentCount FROM Students WHERE StudyForm = 'Day';"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        elif task_number == 2:
            query = "SELECT DisciplineName, Hours, ReportingForm FROM Curriculum WHERE DisciplineName = 'Программирование';"
            result = execute_query(connection, query)
            print("Результат запроса:")
            print(result)
        elif task_number == 3:
            # Добавление нового студента
            query = """
                INSERT INTO Students (LastName, FirstName, Patronymic, AdmissionYear, StudyForm, GroupName)
                VALUES ('Новиков', 'Николай', 'Игоревич', 2022, 'Evening', 'Группа6');
            """
            execute_query(connection, query)
            print("Студент добавлен успешно.")

            # Изменение информации о студенте (пример для студента с ID 1)
            query = "UPDATE Students SET StudyForm = 'Distance' WHERE StudentID = 1;"
            execute_query(connection, query)
            print("Информация о студенте изменена успешно.")

            # Добавление новой дисциплины в учебный план
            query = """
                INSERT INTO Curriculum (SpecialtyName, DisciplineName, Semester, Hours, ReportingForm)
                VALUES ('Информационные технологии', 'Новая дисциплина', 5, 45, 'Credit');
            """
            execute_query(connection, query)
            print("Дисциплина добавлена успешно.")

            # Изменение информации о дисциплине (пример для дисциплины с ID 1)
            query = "UPDATE Curriculum SET Hours = 80 WHERE CurriculumID = 1;"
            execute_query(connection, query)
            print("Информация о дисциплине изменена успешно.")

            # Добавление новой записи в журнал успеваемости
            query = "INSERT INTO Grades (Year, Semester, StudentID, CurriculumID, Grade) VALUES (2022, 1, 1, 1, 4.5);"
            execute_query(connection, query)
            print("Запись в журнал успеваемости добавлена успешно.")

            # Изменение оценки в журнале успеваемости (пример для записи с ID 1)
            query = "UPDATE Grades SET Grade = 5 WHERE GradeID = 1;"
            execute_query(connection, query)
            print("Оценка в журнале успеваемости изменена успешно.")
        else:
            print("Некорректный номер задания. Введите число от 1 до 3.")
    finally:
        # Закрываем соединение с базой данных
        connection.close()

if __name__ == "__main__":
    main()
