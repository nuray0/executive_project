# Installing, Setting Up, and Using the Web Application

## Step 1: Download the code from the repository
```
git clone https://github.com/nuray0/executive_test_project.git
```

## Step 2: Go to the project folder
```
cd executive_test_project
```
or if you downloaded the project as a zip archive:
```
cd executive_test_project-master
```

## Step 3: Install Docker
If you haven't installed Docker yet, download and install it from the [official Docker website.](https://www.docker.com/get-started) 

## Step 4: Start Docker Desktop
To ensure Docker is working, open a terminal (or command prompt on Windows) and run the command ```docker --version```. If Docker is installed correctly, you will see the version of Docker installed on your computer.


## Step 5: Create migrations
```
docker-compose run web python manage.py makemigrations
```

## Apply migrations
```
docker-compose run web python manage.py migrate
```

## Step 7: Start Docker containers
This step may take a few minutes.
```
docker-compose up
```

## Step 8: Open the application in your browser at:
```
http://0.0.0.0:8000/
```

If the address above doesn’t open, try visiting:
```
http://localhost:8000/
```
or

```
http://127.0.0.1:8000/
```

## Step 9: Register and log in to your account
![Sign up page](https://github.com/nuray0/executive_test_project/raw/master/assets/images/signup_page.jpeg)
![Login page](https://github.com/nuray0/executive_test_project/raw/master/assets/images/login_page.jpeg)

## Step 10: Create an executive
![Главная страница](https://github.com/nuray0/executive_test_project/raw/master/assets/images/dashboard_empty.jpeg)
![Form to create an executive](https://github.com/nuray0/executive_test_project/raw/master/assets/images/add_executive.jpeg)

## Step 11: Add more information to the executive (optional)
Можно добавить информацию, такую как опыт работы, сертификаты, согласия на занятие должности и образование.
![Main page](https://github.com/nuray0/executive_test_project/raw/master/assets/images/executive_details.jpeg)

## Step 12: View the list of executives
На главной странице отображается список всех управляющих с краткой информацией о каждом из них.
![Main page](https://github.com/nuray0/executive_test_project/raw/master/assets/images/dashboard.jpeg)

## Step 13: Edit and delete executive profiles (optional)
You can edit and delete executives and their profile data at your discretion.

## Voila! Congratulations, you've now fully explored this app!
