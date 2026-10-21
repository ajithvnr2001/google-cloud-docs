---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/deferred/
title: Module: google.appengine.ext.deferred.deferred \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:16:02.910464+00:00
---

# Module: google.appengine.ext.deferred.deferred  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/deferred/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.ext.deferred.deferred Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/ext/deferred/deferred.py) A module that handles deferred execution of callables via the task queue. Tasks consist of a callable and arguments to pass to it. The callable and its arguments are serialized and put on the task queue, which deserializes and executes them. The following callables can be used as tasks: 1) Functions defined in the top level of a module 2) Classes defined in the top level of a module 3) Instances of classes in (2) that implement **call** 4) Instance methods of objects of classes in (2) 5) Class methods of classes in (2) 6) Built-in functions 7) Built-in methods The following callables can NOT be used as tasks: 1) Nested functions or closures 2) Nested classes or objects of them 3) Lambda functions 4) Static methods The arguments to the callable, and the object (in the case of method or object calls) must all be pickleable. If you want your tasks to execute reliably, don't use mutable global variables; they are not serialized with the task and may not be the same when your task executes as they were when it was enqueued (in fact, they will almost certainly be different). If your app relies on manipulating the import path, make sure that the function you are deferring is defined in a module that can be found without import path manipulation. Alternately, you can include deferred.TaskHandler in your own webapp application instead of using the easy-install method detailed below. When you create a deferred task using deferred.defer, the task is serialized, and an attempt is made to add it directly to the task queue. If the task is too big (larger than about 10 kilobytes when serialized), a datastore entry will be created for the task, and a new task will be enqueued, which will fetch the original task from the datastore and execute it. This is much less efficient than the direct execution model, so it's a good idea to minimize the size of your tasks when possible. By default, the deferred module uses the URL '/_ah/queue/deferred', and the default queue. To enable the Deferred API, set 'use_deferred=True' in the call to 'wrap_wsgi_app()'. Example for a Flask app: app = Flask(**name**) app.wsgi_app = wrap_wsgi_app(app.wsgi_app, use_deferred=True) Deferring a task in Flask:
    
    
    from flask import Flask, request
    from google.appengine.api import wrap_wsgi_app
    from google.appengine.ext import ndb
    from google.appengine.ext import deferred
    
    class MyModel(ndb.Model):
      total = ndb.IntegerProperty(indexed=True)
    
    my_key = "defaultKey"
    
    def do_something_later(key, amount):
       entity = MyModel.get_or_insert(key, total=0)
       entity.total += amount
       entity.put()
    
    @app.route("/home")
    def hello_world():
      # Use default URL and queue name, no task name, execute ASAP.
      deferred.defer(do_something_later, my_key, 20)
    
      # Execute after 60s
      deferred.defer(do_something_later, my_key, 20, _countdown=60)
    
      # Using a non-default queue (a TaskQueue 'foo' should already exist)
      deferred.defer(do_something_later, my_key, 20, _queue="foo", _countdown=60)
    
    app = Flask(__name__)
    app.wsgi_app = wrap_wsgi_app(app.wsgi_app, use_deferred=True)
    

## Classes

[`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/Error): Base class for exceptions in this module. [`class Handler`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/Handler): A handler class for processesing deferred invocations. [`class PermanentTaskFailure`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/PermanentTaskFailure): Indicates that a task failed, and will never succeed. [`class SingularTaskFailure`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/SingularTaskFailure): Indicates that a task failed once.

## Functions

[`application(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/application): A handler class for processesing deferred invocations. [`defer(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/defer): Defers a callable for execution later. [`invoke_member(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/invoke_member): Retrieves a member of an object, then calls it with the provided arguments. [`run(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/run): Unpickles and executes a task. [`run_from_datastore(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/run_from_datastore): Retrieves a task from the datastore and executes it. [`serialize(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/serialize): Serializes a callable into a format recognized by the deferred executor. [`set_log_level(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred/set_log_level): Sets the log level deferred will log to in normal circumstances. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
