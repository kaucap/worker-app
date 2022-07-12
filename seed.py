import random

from django_seed import Seed
from app_worker.models import Worker

women_names = [
    'Анна', 'Ирина', 'Екатерина', 'Асель', 'Айгерим', 'Нурсулу', 'Марина', 'Лиза', 'Мадина',
    'Кунсулу', 'Алтынай', 'Инна', 'Надежда', 'Галина', 'Роза', 'София', 'Амели'
]

men_names = [
    'Кайрат', 'Игорь', 'Пётр', 'Даурен', 'Бакижан', 'Даулет', 'Иван', 'Алексей', 'Фаррух',
    'Константин', 'Виталий', 'Айсултан', 'Нурсултан', 'Никита', 'Арслан', 'Ерслан'
]

surname = [
    'Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Соколов', 'Михайлов', 'Новиков', 'Лебедев',
    'Султанов', 'Рахимов', 'Назаров', 'Мухтаров', 'Тахиров', 'Смагулов', 'Ашимов'
]

seeder = Seed.seeder()

# Добавление директоров
seeder.add_entity(Worker, 500, {
    'name': lambda x: random.choice(women_names) + ' ' + random.choice(surname) + 'а',
    'position': lambda x: 'Директор',
    'salary': lambda x: random.randint(500000, 600000),
    'chief': lambda x: 0
})
seeder.add_entity(Worker, 500, {
    'name': lambda x: random.choice(men_names) + ' ' + random.choice(surname),
    'position': lambda x: 'Директор',
    'salary': lambda x: random.randint(500000, 600000),
    'chief': lambda x: 0
})
seeder.execute()

# Добавление зам-директоров
directors = Worker.objects.filter(position='Директор')
seeder.add_entity(Worker, 1500, {
    'name': lambda x: random.choice(women_names) + ' ' + random.choice(surname) + 'а',
    'position': lambda x: 'Зам. директора',
    'salary': lambda x: random.randint(400000, 500000),
    'chief': lambda x: random.choice(directors).pk,
})
seeder.add_entity(Worker, 1500, {
    'name': lambda x: random.choice(men_names) + ' ' + random.choice(surname),
    'position': lambda x: 'Зам. директора',
    'salary': lambda x: random.randint(400000, 500000),
    'chief': lambda x: random.choice(directors).pk,
})

seeder.execute()

# Добавление начальников отделов
deputy_director = Worker.objects.filter(position='Зам. директора')
seeder.add_entity(Worker, 3000, {
    'name': lambda x: random.choice(women_names) + ' ' + random.choice(surname) + 'а',
    'position': lambda x: 'Начальник отдела',
    'salary': lambda x: random.randint(300000, 400000),
    'chief': lambda x: random.choice(deputy_director).pk,
})

seeder.add_entity(Worker, 3000, {
    'name': lambda x: random.choice(men_names) + ' ' + random.choice(surname),
    'position': lambda x: 'Начальник отдела',
    'salary': lambda x: random.randint(300000, 400000),
    'chief': lambda x: random.choice(deputy_director).pk,
})

seeder.execute()

#Добавление Старших менеджеров
head_of_department = Worker.objects.filter(position='Начальник отдела')
seeder.add_entity(Worker, 7500, {
    'name': lambda x: random.choice(women_names) + ' ' + random.choice(surname) + 'а',
    'position': lambda x: 'Старший менеджер',
    'salary': lambda x: random.randint(200000, 300000),
    'chief': lambda x: random.choice(head_of_department).pk,
})

seeder.add_entity(Worker, 7500, {
    'name': lambda x: random.choice(men_names) + ' ' + random.choice(surname),
    'position': lambda x: 'Старший менеджер',
    'salary': lambda x: random.randint(200000, 300000),
    'chief': lambda x: random.choice(head_of_department).pk,
})

seeder.execute()

#Добавление менеджеров
senior_manager = Worker.objects.filter(position='Старший менеджер')
seeder.add_entity(Worker, 12500, {
    'name': lambda x: random.choice(men_names) + ' ' + random.choice(surname),
    'position': lambda x: 'Менеджер',
    'salary': lambda x: random.randint(100000, 200000),
    'chief': lambda x: random.choice(senior_manager).pk,
})

seeder.add_entity(Worker, 12500, {
    'name': lambda x: random.choice(women_names) + ' ' + random.choice(surname) + 'а',
    'position': lambda x: 'Менеджер',
    'salary': lambda x: random.randint(100000, 200000),
    'chief': lambda x: random.choice(senior_manager).pk,
})

seeder.execute()
