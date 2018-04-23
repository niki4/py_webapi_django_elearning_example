This example project shows REST API for some MOOC platform with authentication and authorization.

## Installation and run...
... are pretty straightforward and you can just follow the same steps as for [py_webapi_django_example](https://github.com/niki4/py_webapi_django_example), however here's some differences.

* Once you've done `./manage.py migrate` command, create an admin user, which is allowed to make changes in data using REST API (in other words, Admin authorized user will be allowed to send POST/PUT/DELETE to endpoints):
```bash
python manage.py createsuperuser
```
Now you could run the server with `./manage.py runserver` command and open Django Admin Panel with the URL http://127.0.0.1:8000/admin/

Admins (as the one you've just created with the abovementioned command) can change data using both admin panel and REST API, whilst regular users and anonymous could only view data provided by the REST API endpoints. Those permissions are defined in `otus_site/permissions.py` and applied to endpoints in `catalog/views.py`

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

## Debug tools
The project comes with some 3rd-party debug tools connected, which helps on web-site debug and speed up development:
* [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/panels.html) - Nice and useful panel on the right hand side of your site. Displays the background site processes when you interact with (HTTP/SQL queries, templates, urls)
* [django-extensions](https://django-extensions.readthedocs.io/) - Provides additional set of commands/tools you can run with manage.py, like `shell_plus` or `generate_secret_key`. To list all the commands check the `[django_extensions]` section when you run `./manage.py` without any options.  
* [django-configurations](http://django-configurations.readthedocs.io/en/latest/) - This one makes `DJANGO_CONFIGURATION=Dev ./manage.py` command possible.

All the debug tools are turned on by default when `DJANGO_CONFIGURATION=Dev` (that means when `DEBUG = True`
 in `otus_site/settings.py`) and should be normally turned off in production environment, so bear this in mind.