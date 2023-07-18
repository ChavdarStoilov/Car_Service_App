#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


if grep -qzw 'handler404' ./car_service/urls.py
then 
	sed -i '13d;14d;15d;16d;20d' ./car_service/urls.py
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate


sed -i '13 i path("", include("apps.web_app.urls")),' ./car_service/urls.py
sed -i '14 i path("service/", include("apps.service_app.urls")),' ./car_service/urls.py
sed -i '15 i path("account/", include("apps.auth_app.urls")),' ./car_service/urls.py
sed -i '16 i path("api/", include("apps.api_app.urls")),' ./car_service/urls.py
sed -i '20 i handler404 = "apps.web_app.views.custom_404"' ./car_service/urls.py

exec "$@"