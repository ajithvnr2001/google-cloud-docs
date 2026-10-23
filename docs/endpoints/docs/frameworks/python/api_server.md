---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server/
title: Creating a web server \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:11.959575+00:00
---

# Creating a web server  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/api_server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Creating a web server Stay organized with collections  Save and categorize content based on your preferences. 

You must define a web server that uses the [API or APIs you have created](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api). Cloud Endpoints Frameworks for Python implements the standard [Web Server Gateway Interface](https://wsgi.readthedocs.io/) (WSGI) to route requests to your API to the methods in your code.

As with every application that runs on App Engine, you must create a file called [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/python/config/appref) in which you configure your App Engine app's settings. To define the web server, you make changes to your `app.yaml` file.

To define a web server:

  1. Create a Python module, for example `main.py`, and create an `endpoints.api_server` object at the top-level:
         
         api = endpoints.api_server([EchoApi])

The code `api = endpoints.api_server([EchoApi])` creates a WSGI application that routes API requests to the methods in the `EchoAPI` class.

You can provide a list of `remote.Service` objects (which you defined when you [created your API](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create_api)) to `endpoints.api_server`. If you have an API that is implemented in several classes, then your `remote.Service` object is a collection of classes as described in [Creating an API implemented with multiple classes](https://docs.cloud.google.com/endpoints/docs/frameworks/python/create-multi-class-api).

Whether you create a separate module for the `endpoints.api_server` object depends on whether you created a single API or multiple APIs.

     * If you created multiple APIs (using multiple `remote.Service` subclasses) that are defined in multiple files, then we recommend that you create a separate module for the `endpoints.api_server` object so that you can import all the class files.

     * If you created a single API, you can add the required `endpoints.api_server` code to the module where you define your API because you don't need to import any other classes.

**Warning:** if your code doesn't call `endpoints.api_server`, you will get a deployment failure when you try to deploy.
  2. In your `app.yaml` file, map the web server you just created to the Cloud Endpoints location as follows:
         
         handlers:
         # The endpoints handler must be mapped to /_ah/api.
         - url: /_ah/api/.*
           script: main.api
         
         

where `main` is the Python module you in which you defined the `endpoints.api_server` object.




## Serving your API from a different path

Optional: To serve your API from a different path, for example `/api/`:

  1. Modify the decorator:
         
         @endpoints.api(name='echo', version='v1', base_path='/api/')
         

  2. Change the `handlers` section in the `app.yaml` file:
         
         handlers:
         - url: /api/.*
           script: main.api
         




## Logging in Endpoints Frameworks for Python

Endpoints Frameworks for Python uses the [standard Python logging module](https://docs.python.org/2/library/logging.html) to log information about the application's status and request lifecycle. To learn more about App Engine logs and how to view them, review [Reading and writing application logs](https://docs.cloud.google.com/appengine/docs/standard/python/logs#writing_application_logs) in the App Engine documentation.

The Python logging module provides predefined log levels. In increasing order of severity, the log levels are:

Log level | Description  
---|---  
`DEBUG` | Provides detailed logs. Typically you set this level only when troubleshooting a problem.  
`INFO` | The default log level for Endpoints Frameworks. Lets you trace the progress of the application at a high level.  
`WARNING` | Alerts you that something unexpected happened, but the application can recover and still run normally.  
`ERROR` | Alerts you that an error happened that might cause some loss of functionality, but the application is still running.  
`CRITICAL` | Alerts you that a serious error or event happened that might cause the application to shutdown.  
  
Loggers exist in a dot-separated hierarchy. For example, the logger `endpoints.api_config` is a child of the logger `endpoints`. This hierarchy gives you precise control over which logs are emitted or suppressed. Typically, you only change the two root loggers for Endpoints Frameworks: `endpoints` and `endpoints_management`.

### Enable `DEBUG` logging for Endpoints Frameworks

To avoid overloading the log reader, Endpoints Frameworks sets its loggers to only record log entries with the `INFO` log level or higher. At any time after Endpoints Frameworks has been imported into your module, you can change the log level as follows:
    
    
    import logging
    logging.getLogger('endpoints').setLevel(logging.DEBUG)
    logging.getLogger('endpoints_management').setLevel(logging.DEBUG)
    

The `setLevel` method sets the minimum log level for the logger.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
