Using Django version 2.0.7
(Optionally use virtualenv to prevent django version clashes)

How to run (Windows):
1) Open two powershell windows in administrator mode
2) Navigate to the src folder in both of these windows
3) To start the server type: "python manage.py runserver" which will give you an local ip to connect to the server
4) Copy the ip into a browser and you should be connected to the server
5) When you make changes to any of the models in the src code you might need to run migrations so the server can be updated
6) First type: "python manage.py makemigrations" followed with "python manage.py migrate"
