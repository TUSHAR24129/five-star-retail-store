web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn retail_shop.wsgi --bind 0.0.0.0:$PORT --timeout 120
