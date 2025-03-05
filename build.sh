#!/bin/bash
pip install -r requirements.txt
python manage.py migrate

if [[ $CREATE_SUPERUSER ]]; then
    python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email="$DJANGO_SUPERUSER_EMAIL").exists():
    User.objects.create_superuser(
        email="$DJANGO_SUPERUSER_EMAIL",
        password="$DJANGO_SUPERUSER_PASSWORD",
        first_name="$DJANGO_SUPERUSER_FIRSTNAME",
        last_name="$DJANGO_SUPERUSER_LASTNAME"
    )
EOF
fi

python manage.py collectstatic --noinput
