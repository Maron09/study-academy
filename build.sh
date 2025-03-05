#!/bin/bash
pip install -r requirements.txt
python manage.py migrate

if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser \
        --no-input \
        --email "$DJANGO_SUPERUSER_EMAIL" \
        --first_name "$DJANGO_SUPERUSER_FIRSTNAME" \
        --last_name "$DJANGO_SUPERUSER_LASTNAME"
fi

python manage.py collectstatic --noinput
