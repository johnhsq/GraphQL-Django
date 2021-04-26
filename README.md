# GraphQL-Python-Django-Graphene

Chapter 4 of Full-Stack React, Python and GraphQL - O'Reilly  
https://github.com/PacktPublishing/Full-Stack-React-Python-and-GraphQL

# Setup Environment
| Requirements | Installation | Notes |
| ------------ | ------------ | ----- |
| Python | $ brew upgrade <br/> $ brew install python <br/> $ python --version | 3.9.4 |  
| pipenv | $ brew install pipenv <br /> $ cd \<project_folder\> <br/> $ pipenv shell | https://pipenv.pypa.io/en/latest/ |
| React | | |
| Node.js | $ brew install node <br /> $ node -v | v15.14.0 <br/> nodejs.org |
| cloudinary.com | SaaS service | image management |
| Graphene | $ pipenv shell <br/> $ pipenv install graphene | GraphQL in Python <br/>https://graphene-python.org/
| GraphQL | Playground| <br/> https://graphql.org/swapi-graphql/? <br/> vs <br/> https://swapi.dev/ <br/> https://swapi.dev/api/films |
| Django | $ pipenv shell <br/> $ pipenv install django graphene-django django-graphql-jwt django-cors-headers <br/> $ pipenv install --dev autopep8 <br/> $ django-admin startproject app <br/> $ cd app  <br/> $ python manage.py migrate <br/> $ python manage.py startapp tracks <br/> update models.py in "tracks" <br/> update settings.py in "app" <br/>$ python manage.py makemigrations <br/> $ python manage.py migrate 

# Dev Environment
Create sample data
```
$ pipenv shell
$ cd app
$ python manage.py shell    # Django Shell
>>> from tracks.models import Track
>>> Track.objects.create(title="Track 1",description="Track1 Descripiton", url="https://track1.com")
>>> Track.objects.create(title="Track 2",description="Track2 Descripiton", url="https://track2.com")
>>> exit()
```

# Run Environment
```
$ pipenv shell
(GraphQL-Django) bash-3.2$ python manage.py runserver
http://localhost:8000
http://localhost:8000/graphql
(GraphQL-Django) bash-3.2$ exit
```