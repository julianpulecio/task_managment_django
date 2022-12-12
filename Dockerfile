FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /employee_manager
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:80