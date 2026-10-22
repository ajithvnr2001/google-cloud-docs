---
url: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/custom-runtimes/
title: Troubleshooting custom runtimes \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:22.354882+00:00
---

# Troubleshooting custom runtimes  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/custom-runtimes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Troubleshooting custom runtimes Stay organized with collections  Save and categorize content based on your preferences. 

Issue | Solutions  
---|---  
When starting my application I see a 503 error. | Is your container listening for HTTP requests on port 8080? It should be---HTTP requests are routed to this port on your container.  
  
Is your application responding to health check handlers? A well formed application should always respond to health checks. Make sure your application can respond to these requests or disable health checking in your `app.yaml` file.  
Building my application takes a long time. | This can be caused by sub-optimal layering in your Dockerfile. When your Dockerfile is built, a layered caching system is applied that rebuilds those layers that have changed, and any subsequent layers.  
  
We recommended that your Dockerfile be structured so that frequently changing layers are built last, so that the previously built layers can remain cached during changes. You can read more about Dockerfile syntax and best practices on the [Docker user guide](https://docs.docker.com/reference/builder/).  
Some files are not included in my application. | `docker build` does not respect symlinks, so make sure you are not relying on symlinks in your application directory.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
