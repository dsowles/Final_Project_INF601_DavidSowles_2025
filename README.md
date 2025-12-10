# Final_Project_INF601_DavidSowles_2025
Final Project for Advanced Python Class

#


## Description  

- The Fictional Archive is a Django-based web application designed for book enthusiasts.Users can create articles to write book reviews, opinions, or general articles, with optional comments.  


## Installing

1. Clone the repository:

```bash
git clone <repository_url>
cd <project_folder>

# (Optional) Check to see if terminal's current working
# directory was actually moved to cloned repository.
pwd
```

2. Setup the virtual environment:

```bash
source venv/Scripts/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations to set up the database:

```bash
python manage.py migrate
```

5. Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your browser and go to: http://127.0.0.1:8000/ to view the site.

### Dependencies  

* Python 3.x  
* Django 5.2.8  
* SQLite3 (default Django database)  
* Bootstrap 5 (via crispy-bootstrap5)  
* Pillow (for image handling)  