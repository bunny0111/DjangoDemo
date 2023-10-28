# DjangoDemo

Step 1: Prepare a Local Environment

1. Create a new directory for your project and navigate to it in your terminal.
2. Create a Python virtual environment (Python 3.8 is used here):

code:- python3 -m venv env
3. Activate the virtual environment:
On Linux/macOS:
code:- source env/bin/activate
On Windows:
.\env\Scripts\activate

Step 2: Install Django and Django REST framework

1. Install Django and Django REST framework within your virtual environment:
code:- pip install django djangorestframework

Step 3: Create 'requirements.txt'
Generate a 'requirements.txt' file containing the installed packages:
code:- pip freeze > requirements.txt

Step 4: Prepare Dockerfile
Create a 'Dockerfile' in your project directory with the following content:

  # Use an official Python runtime as a parent image
  FROM python:3.8

  # Set environment variables for Python
  ENV PYTHONDONTWRITEBYTECODE 1
  ENV PYTHONUNBUFFERED 1

  # Set the working directory in the container
  WORKDIR /app

  # Copy the requirements file into the container at /app
  COPY requirements.txt /app/

  # Install any needed packages specified in requirements.txt
  RUN pip install --no-cache-dir -r requirements.txt

  # Copy the current directory contents into the container at /app
  COPY . /app/

  # Expose port 8080 to allow communication
  EXPOSE 8080

  # Run the Django development server
  CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

Step 5: Prepare docker-compose.yml file
1. Create a docker-compose.yml file in your project directory:
  version: '3'

  services:
    mysql:
      image: 'mysql:8.1'
      ports:
        - '3306:3306'
      environment:
        MYSQL_ROOT_PASSWORD: 'password'
        MYSQL_DATABASE: 'ecommerce'
        MYSQL_USER: 'db_user'
        MYSQL_PASSWORD: 'password'
        MYSQL_ALLOW_EMPTY_PASSWORD: 1
      volumes:
        - 'mysql_data:/var/lib/mysql'

   

    django_demo:
      build:
        context: .
      container_name: django_demo
      ports:
        - "8000:8000"
    depends_on:
        - mysql

volumes:
  mysql_data:
    driver: local

Important Points:-
  Install Django and Django REST framework:
  code:- pip install django djangorestframework

  command for makemigrations and migrate:-
  python manage.py makemigrations
  python manage.py migrate

  command for runserver:
  python manage.py runserver 0.0.0.0:8080
  
  Generate a requirements.txt file:
  code:- pip freeze > requirements.txt

  Build and run the Docker containers:
  code:-   docker-compose up --build

Important endpoints to test code:- 
  'GET' Method:- http://127.0.0.1:8080/products/products/
  
  'POST' Method:- http://127.0.0.1:8080/products/products/
  Raw data in JSON format to add data:- 
    {
      "name": "AC",
      "description": "Test",
      "price": "9000.00" 
    }

  'PUT' Method:- http://127.0.0.1:8080/products/products/
    Raw data in JSON format to edit data:- 
    {
    "id": 1,
    "name": "Fridge",
    "description": "Test",
    "price": "9000.00" 
    }

  'PATCH' Method:- http://127.0.0.1:8080/products/products/
    Raw data in JSON format to edit data partially:- 
    {
    "id": 1,
    "name": "TELEVISION"
    }

  'DELETE' Method:- http://127.0.0.1:8080/products/products/
    Raw data in JSON format to delete data completely:- 
    {
    "id": 1
    }



