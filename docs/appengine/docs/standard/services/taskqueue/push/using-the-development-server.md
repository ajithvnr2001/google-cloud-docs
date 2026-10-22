---
url: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/using-the-development-server/
title: Testing Push Queues in the Development Server \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:00.909092+00:00
---

# Testing Push Queues in the Development Server  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/taskqueue/push/using-the-development-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Testing Push Queues in the Development Server Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page describes some limitations with using the [local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server) (`dev_appserver`) to test push queues in your application. In most respects, you set up your queues and tasks just as you would to run them in the App Engine production environment, but there are some differences:

  * The development server doesn't respect the `rate` and `bucket-size` attributes of your queues. As a result, tasks are executed as close to their ETA as possible. Setting a rate of `0` doesn't prevent tasks from being executed automatically.
  * The development server doesn't preserve queue state across restarts.

**Important:** Before running the local development server, follow the [setup instructions](https://docs.cloud.google.com/appengine/docs/standard/tools/using-local-server#set-up).

To prevent push tasks from running in the development server at all, use the following command:
    
    
    python3 CLOUD_SDK_ROOT/bin/dev_appserver.py --enable_task_running no
    

For more detailed information on the options available using the local development server, see [Using the local development server](https://docs.cloud.google.com/appengine/docs/standard/tools/local-devserver-command).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
