# Данные о выступлениях гостей с временем
conference_data = [
    {"name": "Alice", "talk": "Introduction to AI", "time": 30},
    {"name": "Bob", "talk": "Machine Learning Algorithms", "time": 60},
    {"name": "Charlie", "talk": "Deep Learning Fundamentals", "time": 90},
    # Добавьте дополнительных гостей, если необходимо, следуя примерам
]

# Функция для создания программы конференции
def generate_conference_program(data):
    program = ""
    total_time = 0

    for index, participant in enumerate(data, start=1):
        name = participant["name"]
        talk = participant["talk"]
        time = participant["time"]

        program += f"{index}. {name} - {talk} ({time} minutes)\n"
        total_time += time

    program += f"\nTotal duration: {total_time} minutes"
    return program

# Сформируйте программу конференции
conference_program = generate_conference_program(conference_data)
print(conference_program)