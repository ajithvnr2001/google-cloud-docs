---
url: https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes/
title: About Custom runtimes \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:08.528452+00:00
---

# About Custom runtimes  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  About Custom runtimes Stay organized with collections  Save and categorize content based on your preferences. 

If you'd like to use an alternative implementation of Python, Java, Node.js, Go, Ruby, PHP, .NET or you write code in any other language, then custom runtimes are for you. Custom runtimes allow you to define new runtime environments, which might include additional components like language interpreters or application servers.

To create a custom runtime, you create a Dockerfile with a base image of your choice, and then add the `docker` commands that build your desired runtime environment. It's important to remember that you are responsible for ensuring that the components that you specified in your Dockerfile are compatible and configured to deliver the desired performance.

When you use a custom runtime, you must write your application code to handle certain flexible environment life-cycle and health checking requests. Start by reading about how to [build a custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build) before you begin developing your application.

Applications that use custom runtimes take advantage of all the various Google Cloud services by using the public REST APIs or client libraries, such as the [App Engine Admin API](https://docs.cloud.google.com/appengine/docs/admin-api) and the [Google Client Libraries](https://docs.cloud.google.com/python/docs/reference).

Use the following table to understand how a custom runtime compares to the existing set of App Engine runtimes:

Feature | Flexible runtime | Custom runtime  
---|---|---  
Dockerfile | Default file supplied automatically by the SDK | Hand-written by the developer  
Dockerfile modifications permitted | Yes | Yes  
Languages | Python, Java, Node.js, Go, Ruby, PHP, .NET | Any software that can service HTTP requests  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
