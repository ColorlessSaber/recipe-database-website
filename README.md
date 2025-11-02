<!--Helps with compatibility of the back to top link-->
<a id="readme-top"></a>

<!--PROJECT SHIELDS-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- Project Title -->
<br>
<div>
    <h1 style="text-align:center">Recipe Database Website</h1>
</div>

<!-- Table of Contents -->
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#about-the-repo">About The Repo</a></li>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#Using">Using</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#acknowledgments">Acknowledgments</a></li>
    </ol>
</details>
<br>

# About the Repo
A personal project to create a local website to store recipes. The main goal was to allow someone to save a recipe they
like and be able to search for it again.<br>
Each recipe is given a tag that categorizes it--breakfast, lunch, dinner, snack, etc. And each recipe can have
multiple Ingredient Groups, a way to organize the ingredients to into separate groups (EX: the main dish versus the dressing)
and/or create an Ingredient Group that uses different ingredients than the recipe. 

<p style="text-align:right">(<a href="#readme-top">Back To Top</a>)</p>

# Built With
* [![Python][python-shield]][python-url]
* [![django][django-shield]][django-url]
* [![Bootstrap][bootstrap-shield]][bootstrap-url]
* [![HTML5][html-shield]][html-url]
* [![JavaScript][javascript-shield]][javascript-url]
<!--* [![JavaScript][javascript-shield]][javascript-url]-->

<p style="text-align:right">(<a href="#readme-top">Back To Top</a>)</p>

# Getting Started
//TODO update instructions for Docker use
Download a copy of the repo to your local computer. Next delete the db.sqlite3 and everything inside
recipes/migrations folder except the \_\_init__.py file. Run the following commands, in the order given, in the terminal 
to regenerate the sqlite database and the migrations.<br>
**NOTE** Make sure you are in the cookbook project directory given we will need to use the manage.py file.
<br><br>
 ``
python manage.py makemigrations
 ``
<br>
``
python manage.py migrate
``
<br><br>
With the sqlite database and the migrations created, we can now run the following command to start the server.
<br><br>
``
python manage.py runserver
``

<p style="text-align:right">(<a href="#readme-top">Back To Top</a>)</p>

# Using
## Creating a new Recipe
Select the "new recipe" on the navbar.
<img src="readme_images/new_recipe_01.png">
<br>
Next fill the form for the recipe, ingredient group, and the ingredients part of the group. Please note that you will
need at lest one ingredient in the ingredient group to be allowed to save the form. When you are finished, click the
"submit" button
<img src="readme_images/new_recipe_02.png">
<img src="readme_images/new_recipe_03.png">

## Seeing all Recipes
Select the "Cookbook" on the navbar.
<img src="readme_images/cookbook_01.png">
<br>
You can use the filer to view only recipes of a specific category--lunch, dinner, etc. Once you find the recipe you wish to view simple
click the open button.
<img src="readme_images/cookbook_02.png">

## Viewing / Editing Existing Recipe
With a selected recipe open, you can edit the recipe details (green box), any edit an ingredient group (blue box),
or create a new ingredient group via the "new group" button (pink arrow).<br>
You can also delete the recipe, which in turn deletes all ingredient group(s) associated with the recipe or delete one
ingredient group. Please note that each recipe must have at lest one ingredient group; the website will inform you of
this.
<img src="readme_images/recipe_details_01.png">

<p style="text-align:right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- Contact -->
# Contact
Please head to my portfolio website and use the contact form to reach out to me:
[My Portfolio Website][portfolio-url]

<p style="text-align:right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
# Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)

<p style="text-align:right">(<a href="#readme-top">Back To Top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ColorlessSaber/recipe-database-website.svg?style=for-the-badge
[contributors-url]: https://github.com/ColorlessSaber/recipe-database-website/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ColorlessSaber/recipe-database-website.svg?style=for-the-badge
[forks-url]: https://github.com/ColorlessSaber/recipe-database-website/network/members
[stars-shield]: https://img.shields.io/github/stars/ColorlessSaber/recipe-database-website.svg?style=for-the-badge
[stars-url]: https://github.com/ColorlessSaber/recipe-database-website/stargazers
[issues-shield]: https://img.shields.io/github/issues/ColorlessSaber/recipe-database-website.svg?style=for-the-badge
[issues-url]: https://github.com/ColorlessSaber/recipe-database-website/issues
[license-shield]: https://img.shields.io/github/license/ColorlessSaber/recipe-database-website.svg?style=for-the-badge
[license-url]: https://github.com/ColorlessSaber/recipe-database-website/blob/main/LICENSE

[javascript-shield]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[javascript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[html-shield]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[html-url]: https://html.spec.whatwg.org/multipage/
[css-shield]: https://img.shields.io/badge/CSS-663399?style=for-the-badge&logo=css&logoColor=white
[css-url]: https://www.w3.org/Style/CSS/Overview.en.html
[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org
[django-shield]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[django-url]: https://www.djangoproject.com/
[bootstrap-shield]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[bootstrap-url]: https://getbootstrap.com

[portfolio-url]: https://colorlesssaber.github.io/