---
url: https://docs.cloud.google.com/appengine/docs/flexible/python/customizing-the-python-runtime/
title: Customizing the Python runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:09.666451+00:00
---

# Customizing the Python runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/python/customizing-the-python-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Customizing the Python runtime Stay organized with collections  Save and categorize content based on your preferences. 

You can use [custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) to add additional functionality to a Python app running in the flexible environment. To configure a custom runtime, you replace this line in your `app.yaml` file:
    
    
    runtime: python
    

with this line:
    
    
    runtime: custom
    

You must also [specify a base image](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base) by adding a Dockerfile in the same directory that contains the `app.yaml` file.

Visit the [Custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) documentation to learn how to define a Dockerfile in a custom runtime.

## Health Checking

By default, all programs running in the flexible environment receive [health check requests](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes#health_check_requests). If a base image supports health checking, you don't need to write any additional code. If it does not, you will need to disable health checks, or write your own code to handle health check requests.

## Selecting the Python version

The `python` runtime has [Python 2.7.12](https://www.python.org/downloads/release/python-2712/) and [Python 3.6.10](https://www.python.org/downloads/release/python-3610/) pre-installed. You can customize the `Dockerfile` to install other versions or alternative interpreters if needed.

You can specify a whether to use Python 2 or Python 3 in your application's `Dockerfile` when creating the virtual environment:
    
    
    # Python 3
    RUN venv /env -p python3.7
    
    # Python 2 (implicit)
    RUN virtualenv /env
    
    # Python 2 (explicit)
    RUN virtualenv /env -p python2.7
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
