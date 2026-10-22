---
url: https://docs.cloud.google.com/appengine/docs/flexible/python/specifying-dependencies/
title: Specifying dependencies \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:03.045050+00:00
---

# Specifying dependencies  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/python/specifying-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Specifying dependencies Stay organized with collections  Save and categorize content based on your preferences. 

Dependencies for python applications are declared in a standard [`requirements.txt`](https://pip.pypa.io/en/latest/user_guide/#requirements-files) file. For example:
    
    
    Flask==MAJOR.MINOR.PATCH
    google-cloud-storage
    

Replace MAJOR, MINOR, and PATCH with the desired [Flask version numbers](https://pypi.org/project/Flask/#history).

You can use any Linux-compatible Python package in the App Engine flexible environment, including packages that require native (C) extensions.

The Python runtime will [automatically install](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#dependencies) all dependencies declared in your `requirements.txt` during deployment.

## Installing dependencies locally

When developing and testing your application locally, we recommended you use [`venv`](https://docs.python.org/3/library/venv.html) to isolate your application's dependencies from your system packages. This also ensures that your dependencies will be the same version on your local machine and the deployed application.

To use `venv` to install dependencies, complete the following steps: 

### Mac OS / Linux

Note: These instructions describe how to set up a virtual environment in Python 3. For Python 2 apps, use [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv) to set up a virtual environment.

  1. Create an [isolated Python environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv): 
         
         python3 -m venv env
         source env/bin/activate

  2. If you're not in the directory that contains the sample code, navigate to the directory that contains the `hello_world` sample code. Then install dependencies: 
         
         cd YOUR_SAMPLE_CODE_DIR
         pip install -r requirements.txt




### Windows

Note: These instructions describe how to set up a virtual environment in Python 3. For Python 2 apps, use [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv) to set up a virtual environment.

Use PowerShell to run your Python packages.

  1. Locate your installation of [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows). 
  2. Right-click on the shortcut to PowerShell and start it as an administrator.
  3. Create an [isolated Python environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv). 
         
         python -m venv env
         .\env\Scripts\activate

  4. Navigate to your project directory and install dependencies. If you're not in the directory that contains the sample code, navigate to the directory that contains the `hello_world` sample code. Then, install dependencies: 
         
         cd YOUR_SAMPLE_CODE_DIR
         pip install -r requirements.txt




This ensures that when you run your app locally, only the dependencies that are declared in the `requirements.txt` file are available. The dependencies installed by App Engine during deployment are based on the contents of the `requirements.txt` file, not the contents of the `env/` directory.

**Tip:** Often you will not know your exact dependencies. After you install dependencies, you can use [`pip freeze`](https://pip.pypa.io/en/latest/reference/pip_freeze.html#pip-freeze) to write the name and version of all installed packages to your `requirements.txt`.

## Installing a web framework

You'll need to use a web framework to enable your app to serve web requests. You can use any Python web framework including the following:

  * [Flask](http://flask.pocoo.org/)
  * [Django](https://www.djangoproject.com/)
  * [Pyramid](http://www.pylonsproject.org/)
  * [Bottle](http://bottlepy.org/)
  * [web.py](http://webpy.org/)
  * [Tornado](http://www.tornadoweb.org/)



To use a particular web framework, just add it to your `requirements.txt`:
    
    
    Flask==MAJOR.MINOR.PATCH
    

## Installing a WSGI server

Some web frameworks have built-in WSGI servers; however, few of them are suitable for serving production traffic. Most web applications use a standalone [WSGI server](http://www.fullstackpython.com/wsgi-servers.html) such as [Gunicorn](http://gunicorn.org/), [uWSGI](http://uwsgi-docs.readthedocs.org/en/latest/) or [Waitress](https://pylons.readthedocs.org/projects/waitress/en/latest/). For more information on installing, configuring, and using a WSGI server see [application startup](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#application_startup).

## Installing the Cloud Client Libraries

The [Cloud Client Libraries for Python](https://docs.cloud.google.com/python/docs/reference) is a client library for accessing Google Cloud services that significantly reduces the boilerplate code you have to write. The library provides high-level API abstractions so they're easier to understand. It embraces idioms of Python, works well with the standard Python library, and integrates better with your codebase.

For example, you can install the corresponding Python client library for [Datastore](https://docs.cloud.google.com/datastore) or [Cloud Storage](https://docs.cloud.google.com/storage) to integrate those services with your app.

To install the Python client library for Cloud Datastore:

  1. Install the client library locally by using `pip`:
         
         pip install google-cloud-datastore

  2. Set up authentication. You can configure the Cloud Client Libraries for Python to [handle authentication automatically](https://docs.cloud.google.com/docs/authentication/client-libraries). The client library can automatically handle authentication for you locally as well by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).
         
         gcloud auth login
         

  3. Use the [Datastore Client Libraries reference](https://docs.cloud.google.com/datastore/docs/reference/libraries) to implement support for the Cloud Datastore service in your app.




For a complete list of all of the Cloud Client Libraries for Python for the supported Google Cloud services, see [APIs & Python Libraries](https://docs.cloud.google.com/python/docs/reference).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
