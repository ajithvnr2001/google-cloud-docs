---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/services/access/
title: Access legacy bundled services for Python 3 \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:45.604474+00:00
---

# Access legacy bundled services for Python 3  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/services/access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Access legacy bundled services for Python 3 Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to install and use legacy bundled services with the [Python 3 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime) for the standard environment. Your app must access the bundled services through the [**App Engine services SDK for Python 3**](https://github.com/GoogleCloudPlatform/appengine-python-standard).

**Note:** To continue using legacy bundled services with the [latest supported version of Python](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python), ensure you upgrade to the latest version of the App Engine services SDK by adding `appengine-python-standard>=1.0.0` in your `requirements.txt` file.

## Before you begin

  * Refer to the [list of legacy bundled services APIs](https://docs.cloud.google.com/appengine/docs/standard/services/overview) you can call in the Python runtime.
  * Before starting a migration project to Python 3, see the [runtime migration overview](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services) and migration considerations when using legacy bundled services.



## Installing the App Engine services SDK

To install the App Engine services SDK, follow these steps:

  1. Include the SDK with your app by adding the following line to your `requirements.txt` file:
         
         appengine-python-standard>=1.0.0
         

You can find the SDK on GitHub under the [`appengine-python-standard`](https://github.com/GoogleCloudPlatform/appengine-python-standard) repository, and on [PyPI](https://pypi.org/project/appengine-python-standard/).

  2. Add the following code in your main Python script. This code creates WSGI middleware that sets the variables required to enable your API calls.

### Flask
         
         from flask import Flask
         from google.appengine.api import wrap_wsgi_app
         
         app = Flask(__name__)
         app.wsgi_app = wrap_wsgi_app(app.wsgi_app)
         

### Django
         
         from DJANGO_PROJECT_NAME.wsgi import application
         from google.appengine.api import wrap_wsgi_app
         
         app = wrap_wsgi_app(application)
         

### Pyramid
         
         from pyramid.config import Configurator
         from google.appengine.api import wrap_wsgi_app
         
         config = Configurator()
         # make configuration settings
         app = config.make_wsgi_app()
         app = wrap_wsgi_app(app)
         

### WSGI
         
         import google.appengine.api
         
         def app(environ, start_response):
             start_response('200 OK', [('Content-Type', 'text/plain')])
             yield b'Hello world!\n'
         
         app = google.appengine.api.wrap_wsgi_app(app)
         

  3. Update your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#app_engine_bundled_services) file to specify one or more legacy bundled services. For example:
         
         app_engine_bundled_services:
         - datastore_v3
         - memcache
         - user
         

If you use features such as `login: admin` in the `handlers` section of `app.yaml` file, enable the Users API by configuring the `user` setting in the `app_engine_bundled_services` list.

  4. To deploy your app, use the [`gcloud app deploy`](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service) command.




## Migration considerations

You should be aware of the following considerations if you are migrating to the Python 3 runtime and your app uses legacy bundled services.

### Testing

**Important:**

  * Before running the local development server, follow the [setup instructions](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server#set-up). 
  * The `dev_appserver` tool does not support development of Python 3 apps on Windows.



To locally test the legacy bundled services functionality in your Python 3 app, use the [local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server). When running the `dev_appserver.py` command, you must set the `--runtime_python_path` argument to include a path to the Python 3 interpreter. For example:
    
    
       python3 CLOUD_SDK_ROOT/bin/dev_appserver.py --runtime_python_path=/usr/bin/python3
    

You can also set the argument to a comma-separated list of `[RUNTIME_ID]=[PYTHON_INTERPRETER_PATH]` pairs. For example:
    
    
       python3 CLOUD_SDK_ROOT/bin/dev_appserver.py --runtime_python_path="python27=/user/bin/python2.7,python3=/usr/bin/python3"
    

**Important:** When using the local development server to test Python 3 apps that use the [Deferred API](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/deferred), you must set the following environment variable in your `app.yaml`: `DEFERRED_USE_CROSS_COMPATIBLE_PICKLE_PROTOCOL: 'True'`

### Pickle Compatibility

Shared services including Memcache, Cloud NDB and [deferred](https://cloud.google.com/appengine/docs/standard/python3/services/deferred) use the [pickle](https://docs.python.org/3/library/pickle.html) module to serialize and share Python objects. If your App Engine environment uses both Python 2 and Python 3, which is common during a migration, you must ensure that shared serialized objects written by one version of Python can be reconstitued by the other. You can find guidance on implementing cross version pickle compatibility in the [guide](https://github.com/imankulov/pickle-compat#readme).

By default, Python 3 uses pickling protocols that are not supported in Python 2. This can cause failures when your app tries to reconstitute a Python object in a Python 2 environment that was written in a Python 3 environment. To avoid this issue, set the following [environment variables](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#environment_variables) in the `app.yaml` file for your Python 3 app as needed:

  * For apps that use Memcache including apps that use NDB, set: `MEMCACHE_USE_CROSS_COMPATIBLE_PROTOCOL: 'True'`
  * For apps that use NDB to connect to Datastore, set: `NDB_USE_CROSS_COMPATIBLE_PICKLE_PROTOCOL: 'True'`
  * For apps that use deferred, set: `DEFERRED_USE_CROSS_COMPATIBLE_PICKLE_PROTOCOL: 'True'`



In Python 2, `string` objects hold a sequence of 8 bit byte values. In Python 3, `string` objects hold a sequence of unicode characters. By default Python 3 pickle translates a Python 2 `string` to unicode by interpreting the Python 3 `string` as ASCII. This can lead to errors for values outside the ASCII character range of 0 to 127. Memcache supports overriding this default mapping.
    
    
    from google.appengine.api import memcache
    import six.moves.cPickle as pickle
    
    def _unpickle_factory(file):
        return pickle.Unpickler(file, encoding='latin1')
    
    memcache.setup_client(memcache.Client(unpickler=_unpickle_factory))
    

The `latin1` encoding, defines a mapping for each of the 256 possible values of each byte in a Python 2 `string`. This prevents decoding errors. However, if your Python 2 `string` contains actual unicode data outside of the `latin1` range, such as data read from a file, cPickle won't map the data correctly. Therefore, it is important that you update your Python 2 code to hold unicode data with `unicode` objects and not `string` objects, for objects you Pickle. The compatibility [guide](https://github.com/imankulov/pickle-compat#readme) includes details on the needed updates.

The previous described method for updating your Python 2 code to produce Python 3 compatible serializations addresses short-lived serializations, such as those stored in Memcache. You might need to update or rewrite long-lived Python 2 serializations, such as those stored in Datastore as part of your migration. For example, serialization written using [`google.appengine.ext.ndb.model.PickleProperty`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/ext/ndb/PickleProperty) might require an upgrade.

See the compatibility [guide](https://github.com/imankulov/pickle-compat#readme) to learn more about limitations and less common issues.

### Web frameworks

`webapp2` is not bundled or supported in Python 3, so any application needs to be rewritten to make use of any WSGI-compatible framework (such as [Flask](https://flask.palletsprojects.com)).

A recommended migration strategy is to first replace the use of `webapp2` in your Python 2.7 app with Flask (or an alternative web framework such as [Django](https://www.djangoproject.com/), [Pyramid](http://www.pylonsproject.org/), [Bottle](http://bottlepy.org/), or [web.py](http://webpy.org/)), while remaining on Python 2.7. Then, when your updated app is stable, migrate the code to Python 3 and deploy and test using App Engine for Python 3.

For examples of how to convert Python 2.7 apps which use `webapp2` to use the Flask framework, you can refer to [these additional resources](https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/python-differences#resources).

### Using handlers

A Python 3 app can only have one script associated with it, so if your `app.yaml` has multiple `script` handlers mapping URLs to different scripts, you will need to combine those scripts into one which handles the URL routing.

The following example shows the handler differences in the `app.yaml` file for the respective runtimes.

### Python 2
    
    
    runtime: python27
    api_version: 1
    threadsafe: true
    
    handlers:
    - url: /
      script: home.app
    
    - url: /index\.html
      script: home.app
    
    - url: /stylesheets
      static_dir: stylesheets
    
    - url: /(.*\.(gif|png|jpg))$
      static_files: static/\1
      upload: static/.*\.(gif|png|jpg)$
    
    - url: /admin/.*
      script: admin.app
      login: admin
    
    - url: /.*
      script: not_found.app
    

### Python 3
    
    
    runtime: python314
    
    app_engine_bundled_services:
    - datastore_v3
    - memcache
    - user
    ...
    
    #list your bundled services
    
    handlers:
    - url: /stylesheets
      static_dir: stylesheets
    
    - url: /(.*\.(gif|png|jpg))$
      static_files: static/\1
      upload: static/.*\.(gif|png|jpg)$
    
    - url: /admin/.*
      script: auto
      login: admin
    

Your Python 3 app must handle URL routing (for example, with Flask decorators).

If you want to use multiple `script` handlers with different URL patterns, or if you want to use other attributes in your handlers, each handler must specify `script: auto`.

You can also override the default startup behavior by [specifying an `entrypoint` field](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#application_startup) in your `app.yaml` file.

See the [Blobstore](https://docs.cloud.google.com/appengine/docs/standard/python3/services/blobstore), [Deferred](https://docs.cloud.google.com/appengine/docs/standard/python3/services/deferred), and [Mail](https://docs.cloud.google.com/appengine/docs/standard/python3/services/mail) overviews for more information on how to use specific handlers.

### Thread safety

Apps are assumed to be thread safe. API calls must be made on the request thread. If you use a legacy bundled services API when the app is starting, this can lead to security errors.

To learn more, see [Security errors when using legacy bundled services for Python](https://docs.cloud.google.com/appengine/docs/standard/troubleshooting#security-errors-on-legacy-bundled).

### Using URL Fetch

To use URL Fetch for Python, you need to explicitly call the URL Fetch library.

If your Python 3 app uses the URL Fetch API, the `X-Appengine-Inbound-Appid` request header is added when your app sends a request to another App Engine app. This allows the receiving app to verify the calling app's identity. To learn more, see [Migrating outbound requests](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-outbound-requests).

## Example (App Engine `ndb`)

Below is a basic Python 2 app registering page visits using App Engine `ndb` to access Datastore. Its companion is a Python 3 equivalent app where `webapp2` usage has been replaced by Flask, and the required changes described above to access bundled services in Python 3 have been implemented.

### Python 2 (`webapp2`)
    
    
    import os
    import webapp2
    from google.appengine.ext import ndb
    from google.appengine.ext.webapp import template
    
    class Visit(ndb.Model):
        'Visit entity registers visitor IP address & timestamp'
        visitor   = ndb.StringProperty()
        timestamp = ndb.DateTimeProperty(auto_now_add=True)
    
    def store_visit(remote_addr, user_agent):
        'create new Visit entity in Datastore'
        Visit(visitor='{}: {}'.format(remote_addr, user_agent)).put()
    
    def fetch_visits(limit):
        'get most recent visits'
        return Visit.query().order(-Visit.timestamp).fetch(limit)
    
    class MainHandler(webapp2.RequestHandler):
        'main application (GET) handler'
        def get(self):
            store_visit(self.request.remote_addr, self.request.user_agent)
            visits = fetch_visits(10)
            tmpl = os.path.join(os.path.dirname(__file__), 'index.html')
            self.response.out.write(template.render(tmpl, {'visits': visits}))
    
    app = webapp2.WSGIApplication([
        ('/', MainHandler),
    ], debug=True)

### Python 3 (Flask)
    
    
    from flask import Flask, render_template, request
    from google.appengine.api import wrap_wsgi_app
    from google.appengine.ext import ndb
    
    app = Flask(__name__)
    app.wsgi_app = wrap_wsgi_app(app.wsgi_app)
    
    
    class Visit(ndb.Model):
        'Visit entity registers visitor IP address & timestamp'
        visitor   = ndb.StringProperty()
        timestamp = ndb.DateTimeProperty(auto_now_add=True)
    
    def store_visit(remote_addr, user_agent):
        'create new Visit entity in Datastore'
        Visit(visitor='{}: {}'.format(remote_addr, user_agent)).put()
    
    def fetch_visits(limit):
        'get most recent visits'
        return Visit.query().order(-Visit.timestamp).fetch(limit)
    
    
    @app.route('/')
    def root():
        'main application (GET) handler'
        store_visit(request.remote_addr, request.user_agent)
        visits = fetch_visits(10)
        return render_template('index.html', visits=visits)

Both of these apps can be found in the [open source repo](https://github.com/googlecodelabs/migrate-python2-appengine) for the Python App Engine migration content (code samples, [videos](https://developers.googleblog.com/2021/06/introducing-serverless-migration.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_smsintro_201023), [codelabs](https://developers.googleblog.com/2021/03/modernizing-your-google-app-engine-applications.html?utm_source=blog&utm_medium=partner&utm_campaign=CDR_wes_aap-serverless_modernizegae_codelabsannounce_201031)), specifically in the [`mod0`](https://github.com/googlecodelabs/migrate-python2-appengine/tree/master/mod0-baseline) and [`mod1b`](https://github.com/googlecodelabs/migrate-python2-appengine/tree/master/mod1b-flask) folders, respectively.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
