# Определяем место и время конференции
conference_details = {
    'name': 'Python in Science Conference',
    'date': 'June 1-3, 2023',
    'location': 'San Francisco, CA'
}

# Определите список приглашенных гостей с указанием их имен и адресов электронной почты
guests = [
    {'name': 'Alice Smith', 'email': 'alice@example.com'},
    {'name': 'Bob Johnson', 'email': 'bob@example.com'},
    {'name': 'Charlie Brown', 'email': 'charlie@example.com'},
    # Добавьте дополнительных гостей, если необходимо, следуя примерам
]

# Определите функцию для создания персонализированного приглашения
def generate_invitation(guest, conference):
    invitation = (
        f"Dear {guest['name']},\n\n"
        f"We are pleased to invite you to the {conference['name']},"
        f" which will take place on {conference['date']} in {conference['location']}."
        f"\n\nWe hope that you can join us and share your insights and"
        f" experiences with the Python in Science community.\n\n"
        f"Best regards,\nThe Python in Science Conference Team"
    )
    return invitation

# Создавайте персонализированные приглашения в виде текстовых файлов
for guest in guests:
    invitation = generate_invitation(guest, conference_details)
    with open(f"{guest['name']}_invitation.txt", "w") as f:
        f.write(invitation)