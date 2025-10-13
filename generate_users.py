import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "usermanagement.settings")
django.setup()

from django.contrib.auth.models import User

CSV_FILE_PATH = './users.csv'
BATCH_SIZE = 1000  

existing_usernames = set(User.objects.values_list('username', flat=True))

batch = []

with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        username = row['username']
        if username in existing_usernames:
            continue

        user = User(
            username=username,
            first_name=row['first_name'],
            last_name=row['last_name'],
            email=row['email'],
            password=row['password'] or "Password123", 
            is_active=True
        )
        batch.append(user)
        existing_usernames.add(username)

        if len(batch) >= BATCH_SIZE:
            User.objects.bulk_create(batch)
            batch = []

if batch:
    User.objects.bulk_create(batch)

print("All users inserted with plaintext passwords.")
