---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/migrate-to-python3/config-files/
title: Preparing configuration files for the Python 3 runtime \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:25.286406+00:00
---

# Preparing configuration files for the Python 3 runtime  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/migrate-to-python3/config-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Preparing configuration files for the Python 3 runtime Stay organized with collections  Save and categorize content based on your preferences. 

Before you can run your app in the Python 3 runtime of the App Engine standard environment, you may need to change some of the configuration files that App Engine uses:

  * `app.yaml`. This file contains information about your app's code, such as the runtime and the app handlers.

  * `appengine_config.py`. The Python 2 runtime uses this file to access third-party libraries and provide values for constants and "hook functions". The Python 3 runtime doesn't use this file.




## Updating `app.yaml`

The behavior of some fields in your [`app.yaml` configuration file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint) has been modified. Remove any fields that are no longer supported and update other fields as described in the following table.

Field | Change type | Description  
---|---|---  
app_engine_bundled_services | Applicable to Python 3 only | Configure this field to access specific [legacy bundled services for Python 3](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access). For more information about the `app_engine_bundled_services` configuration settings, see the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#app_engine_bundled_services) file reference.  
api_version  
application_readable  
builtins | No longer supported | Not applicable in the Python 3 runtime.  
threadsafe | No longer supported | All applications are presumed to be threadsafe. If your application isn't threadsafe specify an [`entrypoint`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint) configuring 1 thread per worker. For example, when using the F4 instance class: `entrypoint: gunicorn -b :$PORT -w 8 --threads 1 main:app` See [entrypoint best practices](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#entrypoint_best_practices) for recommended number of workers for each instance class.   
libraries | No longer supported |  Use the `requirements.txt` file to [declare dependencies and install client libraries](https://docs.cloud.google.com/appengine/docs/standard/python3/specifying-dependencies).   
handlers: login | Supported if you enable the Users API by configuring the `user` setting in the [`app_engine_bundled_services`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml?tab=python#app_engine_bundled_services) list. |  If you are not using the legacy bundled services for Python 3, use [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) for user management.   
handlers: script | Modified | In the Python 2 runtime, you use the [`script`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_static_dir) field to route incoming requests to your app's script. In the Python 3 runtime, you are required to use a web framework with in-app routing (such as Flask or Django) instead of using the `script` field. To migrate your `app.yaml` file to the Python 3 runtime, do one of the following, depending on whether the file contains [static handlers](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_static_dir) as well as script handlers:

  * If your `app.yaml` file contains static handlers, do one of the following to ensure that requests for dynamic content are routed to your app's script: 
    * Remove all `script` fields. Then add an [`entrypoint`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint) field to start a web server that runs your app. Requests that don't match any of your static handers will be directed to the web server you specified in the `entrypoint` field. The web server and your app's web framework are responsible for routing the request to the correct script. 
    * Replace the value of all `script` fields with `auto`. App Engine will automatically run your app in a web server (assuming your app meets [a few requirements](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#application_startup)), and all requests that match a script handler will be directed to the web server. The web server and your app's web framework are responsible for routing the request to the correct script.
    * If your `app.yaml` file does **not** contain static handlers, remove all `script` fields. All requests to your app will be directed to your app's web server, and your app's framework will route the request to the correct script. You can optionally add an [`entrypoint`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint) field to customize the [default startup behavior](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#application_startup). If your `app.yaml` has both types of handlers, you can still remove all the script handlers that would be marked `auto`, leaving behind the static handlers as well as `auto` handlers requiring other directives, such as the admin-only handler in the example below.

[Static file handling](https://docs.cloud.google.com/appengine/docs/standard/serving-static-files) remains unchanged.  
  
If you use any of the deprecated fields, App Engine returns an error when you deploy your app.

You can use the following examples to compare the differences between the `app.yaml` files:

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
    #list your services
    
    handlers:
    - url: /stylesheets
      static_dir: stylesheets
    
    - url: /(.*\.(gif|png|jpg))$
      static_files: static/\1
      upload: static/.*\.(gif|png|jpg)$
    
    - url: /admin/.*
      script: auto
      login: admin
    

**Note:** For Python 3 the preferred WSGI-compatible web server is `gunicorn`. When you use the optional `entrypoint` field in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#runtime_and_app_elements) configuration file, the timeout for `gunicorn` defaults to 30 seconds. To set a custom timeout, update the `entrypoint` field: for example, `entrypoint: gunicorn -b :$PORT --timeout=600`. In this case, [make sure you have included `gunicorn`](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#entrypoint_best_practices) in your `requirements.txt` file.

## Removing `appengine_config.py`

The Python 2 runtime in the App Engine standard environment uses the `appengine_config.py` file.

This file is ignored in the Python 3 runtime. Instead, the Python 3 runtime uses the standard `requirements.txt` file to [install dependencies](https://docs.cloud.google.com/appengine/docs/standard/python3/specifying-dependencies), including dependencies that use native code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
