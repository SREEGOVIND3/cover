# Ex.06 Book Front Cover Page Design
## Date:05-05-2025

## AIM:
To design a book front cover page using HTML and CSS.

## DESIGN STEPS:

### Step 1:
Create a Django Admin project.

### Step 2:
Create an app in the Django interface.

### Step 3:
Create a folder named 'static' in the app folder.

### Step 4:
Create a new HTML file in the static folder.

### Step 5:
Write the HTML code with relevant CSS properties.

### Step 6:
Choose the appropriate style and color scheme.

### Step 7:
Insert the images in their appropriate places.

### Step 8:
Publish the website in the LocalHost.

## PROGRAM:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Cover</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color:rgb(10, 10, 222);
        }

        .bookpage {
            width: 400px;
            height: 600px;
            margin: 50px auto;
            padding: 20px;
            background-image: url("{% static 'bookapp/backg.jpg' %}");
            background-size: cover;
            background-position: center;
            color: white;
            position: relative;
            box-shadow: 0 0 10px rgba(8, 222, 61, 0.5);
        }

        .section-title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-top: 40px;
        }

        hr {
            border: 1px solid white;
            width: 120px;
            margin: 10px auto;
        }

        .main-title {
            text-align: center;
            font-size: 22px;
            margin-top: 40px;
        }

        .subtitle {
            text-align: center;
            font-size: 14px;
            margin-top: 10px;
            font-family: 'Lucida Handwriting', cursive;

        }

        .author {
            position: absolute;
            bottom: 60px;
            left: 20px;
            font-size: 18px;
            font-family: monospace;
        }

        .edition {
            position: absolute;
            bottom: 20px;
            left: 20px;
            font-size: 16px;
        }

        .book-image {
            position: absolute;
            bottom: 20px;
            right: 20px;
            width: 100px;
            height: 110px;
            object-fit: cover;
            border: 2px solid white;
        }

    </style>
</head>
<body>
    <div class="bookpage">
        <div class="section-title">DEVELOPER'S GUIDE</div>
        <hr>

        <div class="main-title">
            Building Modern Websites<br> with HTML & CSS
        </div>
        <br><br>

        <div class="subtitle">


            A hands-on guide to mastering responsive<br>
            layouts, flexible design patterns, and <br>
            real-world web development tools.


        </div>

        <img src="{% static 'bookapp/my recnt.jpeg' %}" alt="Book Image" class="book-image">

        <div class="author">Sree Govind</div>
        <div class="edition">Second Edition</div>
    </div>
</body>
</html>
```


## OUTPUT:
![alt text](<Screenshot 2025-05-13 020407.png>)

## RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
