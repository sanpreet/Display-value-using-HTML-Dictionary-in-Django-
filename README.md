# Display-value-using-HTML-Dictionary-in-Django-
# How to run the code
Please go the folder Project_folder and run the following code.
```
python manage.py runserver
```
## Aim of this Project
HTML file is used and **Key:Value** or concept of dictionary is used where the key is there in the body part of HTML. 
```
<html>
<head>
 <!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
{{testvar}}   #This is the key and this is passed in the views.py which you will see down
</body>
</html>
```
See the code in the views.py file to write the string which acts as the **value**. You may change it accordingly
```
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#here is the response to the request and this function is passed in the urls.py file so that this response is
#shown in the web at http://127.0.0.1:8000/
def index(request):
 return render(request,'main.html',{"testvar":"My name is Sanpreet Singh and I am dispalying the result with the help of key-pair."
                                              " Key is taken from the html file and value is passed here."
                                    "HTML is made using Bootstrapping cdn with javaquery, javascript is added"
                                              })
```
render is used to return the response. Please see the Value written for key.
## Result

![result_html](https://user-images.githubusercontent.com/3431730/42725885-1e4626dc-87a9-11e8-8559-54745aea06b3.png)

