---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/runtime/
title: Python 3 Runtime Environment \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:23.345803+00:00
---

# Python 3 Runtime Environment  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Python 3 Runtime Environment Stay organized with collections  Save and categorize content based on your preferences. 

The Python runtime is the software stack responsible for installing your web service's code and its dependencies and running your App Engine service.

The Python runtime for App Engine in the standard environment is declared in the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/python3/configuring-your-app-with-app-yaml) file:
    
    
    runtime: pythonVERSION

Where VERSION is the Python `MAJOR` and `MINOR` version numbers. For example, to use the latest Python version, Python 3.14, specify `314`.

For other supported Python versions, and the corresponding Ubuntu version for your Python version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python).

## Python 3 versions

The latest supported Python version is 3.14. The Python runtime uses the latest stable release of the version that is specified in your `app.yaml` file. App Engine automatically updates to new patch versions, but it does not automatically update the minor version.

For example, your application might be deployed at Python 3.7.0 and later automatically updated to Python 3.7.1, but it will not be automatically updated to the next minor version Python 3.8.0.

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how App Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try App Engine free ](https://console.cloud.google.com/freetrial)

App Engine runs Python apps in a container secured by gVisor on an up-to-date Ubuntu Linux distribution.

## Dependencies

During deployment, App Engine uses the Python package manager [`pip`](http://pip.readthedocs.org/) to install dependencies defined in the [`requirements.txt`](http://pip.readthedocs.org/en/stable/user_guide/#requirements-files) metadata file located in your project's root directory. You do not need to upload dependencies as App Engine performs a fresh install.

Dependency specification using the `Pipfile`/`Pipfile.lock` standard is currently not supported and your project must not have these files present.

## Application startup

The runtime starts your app by running the command you specify in the [`entrypoint`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint) field in your `app.yaml` file. If you have configured a Gunicorn web server entrypoint in the `app.yaml` file, you must also add `gunicorn` to your `requirements.txt` file.

The entrypoint should start a web server that listens on the port specified by the `PORT` environment variable. For example:
    
    
    entrypoint: gunicorn -b :$PORT main:app
    

The web framework that your app uses is responsible for routing requests to the appropriate handlers in your app.

If your app meets the following requirements, App Engine will start your app with the [`gunicorn`](https://gunicorn.org/) web server if you don't specify the `entrypoint` field:

  * The root of your app directory contains a `main.py` file with a WSGI-compatible object called `app`.

  * Your app does not contain `Pipfile` or `Pipfile.lock` files.




If you don't specify an entrypoint for the Python 3 runtime, App Engine configures and starts the default Gunicorn web server using the `gthread` worker class with `4` threads per worker. For `F1` and `B1` instances, the `gthread` worker class uses `4` workers, and for `F2`, `B2`, and larger instances, it uses `8` workers. If you specify a custom `entrypoint` without setting `--workers` (`-w`), Gunicorn defaults to one `sync` worker.

**Note:** The [`default timeout of gunicorn`](https://docs.gunicorn.org/en/stable/settings.html#timeout) is 30 seconds when the `entrypoint` field is specified. Workers silent for more than this many seconds are killed and restarted. If your handler takes more than 30 seconds, you may face `[CRITICAL] WORKER TIMEOUT` error. To ensure that the request successfully completes, based on your use-case, you can use the [`-- timeout flag`](https://docs.gunicorn.org/en/stable/settings.html#timeout) in the entrypoint field to increase the timeout.

### Entrypoint best practices

  * Ensure the Python module required to run the specified entrypoint in `app.yaml` is present in the `requirements.txt` file. Add `gunicorn` to the `requirements.txt` file only if a `gunicorn` endpoint is explicitly specified in the `app.yaml` file.

  * For the best performance, the entrypoint should be lightweight because it runs whenever a new instance of your application is created.

  * You can use the entrypoint field to tune the performance of your app. For example, if you use `gunicorn` as your web server, you can use the [`--workers` flag](http://docs.gunicorn.org/en/stable/settings.html#workers) in the entrypoint field to configure the number of workers serving your app.

The number of workers you specify should match the [instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) of your App Engine app:

Instance class | Workers  
---|---  
F1 | 4  
F2 | 8  
F4 | 8  
F4_1G | 8  
B1 | 4  
B2 | 8  
B4 | 8  
B4_1G | 8  
B8 | 8  
  
This guidance serves as a starting point for selecting the number of workers. You may need to use a different number of workers depending on your app's performance characteristics. The example below shows an App Engine deployment that uses two `gunicorn` workers for serving apps:
        
        entrypoint: gunicorn -b :$PORT -w 2 main:app
        

  * We recommend that you configure your web server to listen and respond to HTTP requests on the port specified by your `$PORT` environment variable. Using the default port `8080` prevents App Engine from using its NGINX layer to compress HTTP responses. Note that if you use port `8080`, warnings about port `8080` and NGINX will show in your app's log files.




### Other web frameworks

In addition to Django and Flask, you can use other web frameworks with App Engine, such as [`uwsgi`](https://uwsgi-docs.readthedocs.io/en/latest/) and [`Tornado`](https://www.tornadoweb.org/en/stable/). The following example shows how to use `uwsgi` with App Engine:
    
    
    runtime: python313
    entrypoint: uwsgi --http-socket :$PORT --wsgi-file main.py --callable app --master --processes 1 --threads 2
    
    
    uwsgi==2.0.22
    Flask==3.1.3; python_version >= '3.9'
    

## Environment variables

The following environment variables are set by the runtime:

Environment variable | Description  
---|---  
`GAE_APPLICATION` | The ID of your App Engine application. This ID is prefixed with 'region code~' such as 'e~' for applications deployed in Europe.  
`GAE_DEPLOYMENT_ID` | The ID of the current deployment.  
`GAE_ENV` | The App Engine environment. Set to `standard`.  
`GAE_INSTANCE` | The ID of the instance on which your service is currently running.  
`GAE_MEMORY_MB` | The amount of memory available to the application process, in MB.  
`GAE_RUNTIME` | The runtime specified in your `app.yaml` file.  
`GAE_SERVICE` | The service name specified in your `app.yaml` file. If no service name is specified, it is set to `default`.  
`GAE_VERSION` | The current version label of your service.  
`GOOGLE_CLOUD_PROJECT` | The Google Cloud project ID associated with your application.  
`PORT` | The port that receives HTTP requests.  
`NODE_ENV` (Only available in the Node.js runtime) | Set to `production` when your service is deployed.  
  
You can [define additional environment variables in your `app.yaml` file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#environment_variables), but the above values cannot be overridden, except for `NODE_ENV`. 

## HTTPS and forwarding proxies

App Engine terminates HTTPS connections at the load balancer and forwards requests to your application. Some applications need to determine the original request IP and protocol. The user's IP address is available in the standard `X-Forwarded-For` header. Applications that require this information should configure their web framework to trust the proxy.

## Filesystem

The runtime includes a full filesystem. The filesystem is read-only except for the location `/tmp`, which is a virtual disk storing data in your App Engine instance's RAM. 

## Metadata server

Each instance of your application can use the App Engine metadata server to query information about the instance and your project.

**Note:** Custom metadata is not supported in the standard environment.

You can access the metadata server through the following endpoints:

  * `http://metadata`
  * `http://metadata.google.internal`



Requests sent to the metadata server must include the request header `Metadata-Flavor: Google`. This header indicates that the request was sent with the intention of retrieving metadata values.

The following table lists the endpoints where you can make HTTP requests for specific metadata:

Metadata endpoint | Description  
---|---  
`/computeMetadata/v1/project/numeric-project-id` | The project number assigned to your project.  
`/computeMetadata/v1/project/project-id` | The project ID assigned to your project.  
`/computeMetadata/v1/instance/region` | The region the instance is running in.  
`/computeMetadata/v1/instance/service-accounts/default/aliases` |   
`/computeMetadata/v1/instance/service-accounts/default/email` | The default service account email assigned to your project.  
`/computeMetadata/v1/instance/service-accounts/default/` | Lists all the default service accounts for your project.  
`/computeMetadata/v1/instance/service-accounts/default/scopes` | Lists all the supported scopes for the default service accounts.  
`/computeMetadata/v1/instance/service-accounts/default/token` | Returns the auth token that can be used to authenticate your application to other Google Cloud APIs.  
  
For example, to retrieve your project ID, send a request to `http://metadata.google.internal/computeMetadata/v1/project/project-id`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
