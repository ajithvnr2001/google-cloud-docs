---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/services/deferred/
title: Deferred API for Python 3 \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:01.107710+00:00
---

# Deferred API for Python 3  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/services/deferred/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Deferred API for Python 3 Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the Deferred API, one of the legacy bundled services, with the [Python 3 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3) for the standard environment. Your app can access the bundled services through the [**App Engine services SDK for Python 3**](https://github.com/GoogleCloudPlatform/appengine-python-standard).

## Overview

Previously, the Deferred package [`google.appengine.ext.deferred`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred) depended on the webapp framework in Python 2. Since the webapp framework has been removed in the App Engine services SDK for Python 3, you need to make some changes when upgrading your Python 2 app to Python 3.

## Enabling the Deferred API

To enable the Deferred API for Python 3, you no longer need to set `builtins.deferred` [`app.yaml` file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml). Instead, to enable the API, you must pass `use_deferred=True` in the call to `wrap_wsgi_app()`.

**Important:** When using the [local development server](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access#testing_and_deployment) to test Python 3 apps that use the [Deferred API](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred), you must set the following environment variable in your `app.yaml`:  
`DEFERRED_USE_CROSS_COMPATIBLE_PICKLE_PROTOCOL: 'True'`

## Similarites and differences

By default, the Deferred API for Python 3 uses the same URL `/_ah/queue/deferred` and the same [default queue](https://docs.cloud.google.com/appengine/docs/standard/python/taskqueue/push/migrating-push-queues#creating_queues) as it did in Python 2. Note that for apps migrating to [Cloud Tasks](https://docs.cloud.google.com/tasks), the default queue is [not created automatically](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues#creating_queues) and the [deferred tasks library is not available](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrating-push-queues#features-not-available).

If your app uses the default `/_ah/queue/deferred` endpoint, using [`deferred.defer()` in Python 3](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/deferred) remains the same as [Python 2](https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/creating-push-tasks). If your app uses a custom URL for execution of deferred tasks, you need to make some changes since the `TaskHandler` class in the `deferred` module for Python 2 has been removed in the Python 3 version of this API.

To set a custom URL for execution of deferred tasks, the app can override either the `post` or the `run_from_request` method in the [`deferred.Handler` class](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/Handler) (formerly `deferred.TaskHandler` in Python 2), and pass the `environ` parameter which represents a dictionary containing WSGI request parameters. The `post` method can then be called from the custom endpoint (as shown in the Python 3 samples).

The end-to-end usage of the Python 3 Deferred API, such as routing of requests and accessing the [`environ` dictionary](https://www.python.org/dev/peps/pep-0333/#id19), depends on the web framework the app is migrating to. Compare code changes made from the Python 2 example to the Python 3 examples in the following sections.

## Python 3 examples

The following example shows how to execute a deferred task using a default endpoint and a custom endpoint in a Flask app and Django app. 

### Flask
    
    
    import os
    
    from flask import Flask, request
    from google.appengine.api import wrap_wsgi_app
    from google.appengine.ext import deferred
    from google.appengine.ext import ndb
    
    my_key = os.environ.get("GAE_VERSION", "Missing")
    
    app = Flask(__name__)
    app.wsgi_app = wrap_wsgi_app(app.wsgi_app, use_deferred=True)
    
    
    class Counter(ndb.Model):
        count = ndb.IntegerProperty(indexed=False)
    
    
    def do_something_later(key, amount):
        entity = Counter.get_or_insert(key, count=0)
        entity.count += amount
        entity.put()
    
    
    @app.route("/counter/increment")
    def increment_counter():
        # Use default URL and queue name, no task name, execute ASAP.
        deferred.defer(do_something_later, my_key, 10)
    
        # Use default URL and queue name, no task name, execute after 1 minute.
        deferred.defer(do_something_later, my_key, 10, _countdown=60)
    
        # Providing non-default task queue arguments
        deferred.defer(do_something_later, my_key, 10, _url="/custom/path", _countdown=120)
    
        return "Deferred counter increment."
    
    
    @app.route("/counter/get")
    def view_counter():
        counter = Counter.get_or_insert(my_key, count=0)
        return str(counter.count)
    
    
    @app.route("/custom/path", methods=["POST"])
    def custom_deferred():
        print("Executing deferred task.")
        # request.environ contains the WSGI `environ` dictionary (See PEP 0333)
        return deferred.Handler().post(request.environ)
    
    

### Django
    
    
    import os
    
    from django.conf import settings
    from django.core.wsgi import get_wsgi_application
    from django.http import HttpResponse
    from django.urls import path
    from google.appengine.api import wrap_wsgi_app
    from google.appengine.ext import deferred
    from google.appengine.ext import ndb
    
    my_key = os.environ.get("GAE_VERSION", "Missing")
    
    
    class Counter(ndb.Model):
        count = ndb.IntegerProperty(indexed=False)
    
    
    def do_something_later(key, amount):
        entity = Counter.get_or_insert(key, count=0)
        entity.count += amount
        entity.put()
    
    
    def increment_counter(request):
        # Use default URL and queue name, no task name, execute ASAP.
        deferred.defer(do_something_later, my_key, 10)
    
        # Use default URL and queue name, no task name, execute after 1 minute.
        deferred.defer(do_something_later, my_key, 10, _countdown=60)
    
        # Providing non-default task queue arguments
        deferred.defer(do_something_later, my_key, 10, _url="/custom/path", _countdown=120)
    
        return HttpResponse("Deferred counter increment.")
    
    
    def view_counter(request):
        counter = Counter.get_or_insert(my_key, count=0)
        return HttpResponse(str(counter.count))
    
    
    def custom_deferred(request):
        print("Executing deferred task.")
        # request.environ contains the WSGI `environ` dictionary (See PEP 0333)
        response, status, headers = deferred.Handler().post(request.environ)
        return HttpResponse(response, status=status.value)
    
    
    urlpatterns = (
        path("counter/get", view_counter, name="view_counter"),
        path("counter/increment", increment_counter, name="increment_counter"),
        path("custom/path", custom_deferred, name="custom_deferred"),
    )
    
    settings.configure(
        DEBUG=True,
        SECRET_KEY="thisisthesecretkey",
        ROOT_URLCONF=__name__,
        MIDDLEWARE_CLASSES=(
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ),
        ALLOWED_HOSTS=["*"],
    )
    
    app = wrap_wsgi_app(get_wsgi_application(), use_deferred=True)

### Without any framework
    
    
    import os
    import re
    
    from google.appengine.api import wrap_wsgi_app
    from google.appengine.ext import deferred
    from google.appengine.ext import ndb
    
    my_key = os.environ.get("GAE_VERSION", "Missing")
    
    
    class Counter(ndb.Model):
        count = ndb.IntegerProperty(indexed=False)
    
    
    def do_something_later(key, amount):
        entity = Counter.get_or_insert(key, count=0)
        entity.count += amount
        entity.put()
    
    
    def IncrementCounter(environ, start_response):
        # Use default URL and queue name, no task name, execute ASAP.
        deferred.defer(do_something_later, my_key, 10)
    
        # Use default URL and queue name, no task name, execute after 1 minute.
        deferred.defer(do_something_later, my_key, 10, _countdown=60)
    
        # Providing non-default task queue arguments
        deferred.defer(do_something_later, my_key, 10, _url="/custom/path", _countdown=120)
    
        start_response("200 OK", [("Content-Type", "text/html")])
        return [b"Deferred counter increment."]
    
    
    def ViewCounter(environ, start_response):
        counter = Counter.get_or_insert(my_key, count=0)
        start_response("200 OK", [("Content-Type", "text/html")])
        return [str(counter.count).encode("utf-8")]
    
    
    class CustomDeferredHandler(deferred.Handler):
        """Deferred task handler that adds additional logic."""
    
        def post(self, environ):
            print("Executing deferred task.")
            return super().post(environ)
    
    
    routes = {
        "counter/increment": IncrementCounter,
        "counter/get": ViewCounter,
        "custom/path": CustomDeferredHandler(),
    }
    
    
    class WSGIApplication:
        def __call__(self, environ, start_response):
            path = environ.get("PATH_INFO", "").lstrip("/")
            for regex, handler in routes.items():
                match = re.search(regex, path)
                if match is not None:
                    return handler(environ, start_response)
    
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"Not found"]
    
    
    app = wrap_wsgi_app(WSGIApplication(), use_deferred=True)

## Code samples

To view the complete code samples from this guide, see [GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/appengine/standard_python3/bundled-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
