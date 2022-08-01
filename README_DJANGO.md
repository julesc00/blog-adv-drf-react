# Django, DRF and React Project
By Solo Python [https://youtu.be/EscHWLV43NQ](https://youtu.be/EscHWLV43NQ).

# Steps  
---  
1. Run `npx create-react-app blog-drf-react`  
2. Move into project directoy -> create Python environment and install dependencies to the latest version.
    Dependencies: django djangorestframework django-redis redis django-cors-headers channels celery python-decouple pytest-django django-ckeditor pytz Pillow mutagen pyscopg2-binary argon2-cffi boto3 django-storages gunicorn whitenoise requests
   1. Environment was created with: `python3 -m virtualenv --python=3.10 env`  
   2. Activated with: `source env/bin/activate`
   3. Dependencies are installed with: `pip install -r requirements.txt`  
      1. If there are problems with **psycopg2**, install required dependencies: Linux `sudo apt install python3-dev libpq-dev`
      2. If it's a Mac `pip install psycopg2-binary`
3. Create Django project in current directory: `django-admin startproject blog .`  
4. Start local servers: 
   1. NPM: `npm start` , defaults to port `3000`
   2. Django: `./manage.py runserver` or `python manage.py runserver` this will default to port `8000`
5. To set up templates in django, run first `npm run build`
6. Collect static files: `python manage.py collecstatic` or `./manage.py collectstatic` 
7. When pushing changes to repository, remember to include **build** directory which contains the static files.
8. Install React-Redux: `npm i axios react-redux react-router-dom redux redux-thunk redux-devtools-extension`
9. Install the **React Developer Tools** and **Redux Devtools** browser extensions on your browser.
10. Install TailwindCSS from Framework Guides `npm install -D tailwindcss postcss autoprefixer` then `npx tailwindcss init -p`
    1. Note: If TailwindCSS `npx tailwindcss init -p` cannot work, copy files from author's repo.

