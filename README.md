# py_webapi_django_elearning_example
REST API for some MOOC platform with authentication and authorization

Installation and run is pretty straightforward and you can follow the same steps as for [py_webapi_django_example](https://github.com/niki4/py_webapi_django_example), however here's some differences.

* Once you've done `./manage.py migrate` command, create an admin user, which is allowed to make changes in data using REST API (in other words, Admin authorized user will be able to send POST/PUT/DELETE to endpoints):
```bash
python manage.py createsuperuser
```
Now you could run the server with `./manage.py runserver` command and open Django Admin Panel with the URL http://127.0.0.1:8000/admin/

Admins (as the user you've just created with the abovementioned command) to make changes in data using both admin panel and REST API, whilst regular users and anonymous could only view data provided by the REST API endoints.

By the way, navigating to root level in your browser (or another http client like _curl_) will return list of available endpoints:
```
GET /
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "tags": "http://127.0.0.1:8000/tags/",
    "courses": "http://127.0.0.1:8000/courses/",
    "webinars": "http://127.0.0.1:8000/webinars/"
}
```
