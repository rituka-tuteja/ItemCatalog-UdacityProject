# Item Catalog Project
A web application that creates a restaurant menu web app where users can add, edit, and delete restaurants and menu items in the restaurants.

## Features:
- Authorization is implemented at all levels, i.e restaurants and menu items.
- App is easy to eyes and easy to read, keeping in mind users start to read from left to right and top to bottom

## Setup and steps to run the project
### Requirements
* Python 2.7
* Vagrant
* VirtualBox

### How to Run
1. Download and Install VirtualBox and Vagrant

2. Clone or download this repository

3. Navigate into the directory

4. Launch Vagrant
```
$ Vagrant up 
```
5. Login to Vagrant
```
$ Vagrant ssh
```
6. Change directory to `/vagrant` to access the shared repository
```
$ Cd /vagrant
```
7. Initialize the database
```
$ Python database_setup.py
```
8. Populate the database with some data to work with
```
$ Python lotsofmenus.py
```
9. Launch application
```
$ Python project.py
```
10. Open the browser and go to http://localhost:5000

### JSON endpoints
#### Returns JSON of all restaurants

```
/restaurants/JSON
```
#### Returns JSON of specific menu item

```
/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON
```
#### Returns JSON of menu

```
/restaurants/<int:restaurant_id>/menu/JSON
```
### To debug:
- If the Login and Gdisconnect doesn't reflect correct login status of the user, empty your web browser's cache and run the application again.

### Credits:
Credits for all my learning and basic code flow goes to Udacity, credits to growth each day goes to mistakes and errors made and corrected during the Iterative Development process, mixed credits to google search, udacity knowledge and stack overflow. Thank you!

Credits for Google Login Button:

https://knowledge.udacity.com/questions/33509
https://gist.github.com/shyamgupta/d8ba035403e8165510585b805cf64ee6
