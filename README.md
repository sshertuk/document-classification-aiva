# FileClassifier API - Classification Test

Helping train AIVA.

## Getting Started

The web application (hosted on AWS EC2 Ubuntu dev server) can be accessed at: http://13.58.127.83:8000

The application uses the REST API deploy on AWS infrastrcture: https://rb2pqd7dte.execute-api.us-east-2.amazonaws.com/dev

Addtionally, following instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The following plugins/dependecies have been used for development. Please ensure you have atleast these versions installed.

```
Python 3, Django 1.11, Bootsrap 4, Font-Awesome 5.0.8
```

### Installing
1. Clone repository and run the following command to create required migration files
```
python manage.py makemigrations
```
2. Apply created migration files to the database by running
```
python manage.py migrate
```
3. Run application on localhost
```
python manage.py runserver
```

### Description
```
a. This is a web application built on the Django MVC framework v1.11
b. The application interacts with the file classifier REST API built and deploy on AWS using its storage(S3), compute(lambda), and API (API Gateway) infrastructure
```

### Directions to Use
```
a.After accessing the website (http://13.58.127.83:8000), input the words (in the same format as the provided data) from the file to classified
b.Click on Predict to trigger the process. The predicted value would be shown once the classification is run on the model.
```

