FROM python:3.11.8

RUN mkdir /website

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
RUN mkdir -p /app/static_collected
RUN DJANGO_SECRET_KEY=dummy python manage.py collectstatic --no-input
EXPOSE 8000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "hackspace_cms.wsgi:application"]
