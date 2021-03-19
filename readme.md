### Post Api

## Overview:
Modern RESTful APP allows to use data from database by usage of model serializers with HTML methods and JSON,  only for authenticated users.

## Technology used: 
Django, Django Rest Framework, OpenAPI (Swagger), Python UnitTest, AllAuth, Postman, Uritemplate, Pyyaml


### How to run app:
1. Create virtualenv:
```
pipenv shell
pipenv install
```
2. Run django app
```
python manage.py makemigrations posts
python manege.py migrate
python manage.py runserver
```

3. Check urls
* for some data creation of user is needed:
```
python manage.py createsuperuser
```

- Admin view: `/admin/`
- API: `api/v1/users`, `api/v2/posts`
- API auth `api/api-auth/`



For detailed data about endpoints methods please see url: `/swagger/`
