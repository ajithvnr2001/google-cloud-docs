---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/handling-api-versioning/
title: Handling API versioning \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:18.452622+00:00
---

# Handling API versioning  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/handling-api-versioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Handling API versioning Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to do versioning for your API and how to deploy to multiple versions.

## Recommendations for managing API versions

In managing your API versions, consider these recommendations:

  * When you want to introduce an incremental, but non-breaking change, keep the API version constant and deploy over the existing API.
  * When you introduce a breaking change to your API, increment the API version.
  * For additional protection, increment the App Engine application version as well, and then deploy the new API version to that new App Engine application version. This lets you use the built-in flexibility of App Engine to quickly switch between App Engine versions and serve from the old working versions if you run into unexpected problems.



The following table is an illustration of cascading backend API versions to different App Engine application versions.

Application version | Backend API version  
---|---  
1 | 

  * v1 --> v1 (2) --> v1 (n)

  
2 | 

  * v1 (n)
  * v2 --> v2 (2) --> v2 (n)

  
3 | 

  * v1 (n)
  * v2 (n)
  * v3 --> v3 (2) --> v3 (n)

  
  
As shown in the table, incremental, non-breaking updates to v1 of the API are rolled out, each overwriting the previous version. When breaking changes are introduced, the API version is incremented to v2 and it is deployed to a new App Engine application version. That allows you to switch back to the previous applications version if needed.

In the table, notice that application version 2 supports both the latest v1 version and the new v2 version of your API. If you don't delete the existing v1 code from your project, when you deploy the project both `v2` and `vl` (n) of your API are deployed to version 2 of your application.

## Deploying to multiple application versions

When you deploy your backend API, you deploy it to the project ID of the Google Cloud project you created for your API, and you must also specify the App Engine version you deploy to. You specify the App Engine app version in the `<version>` element of the [`/WEB-INF/appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java/config/appref) file. The App Engine app version isn't the same thing as the backend API version number, which you specify in the `version` attribute of the `@Api` annotation.

![apiversions](https://docs.cloud.google.com/static/endpoints/docs/frameworks/java/images/apiversions.png)

As shown in the preceding figure, you can deploy multiple API versions to the same App Engine version. And, you can have many App Engine versions for an application.

### Accessing API versions deployed to a serving version

The first [App Engine version](https://docs.cloud.google.com/appengine/docs/python/an-overview-of-app-engine#versions_and_instances) that you deploy your API to is the serving version. This version runs at the URL `http://YOUR_PROJECT_ID.appspot.com` where `YOUR_PROJECT_ID` represents your Google Cloud project ID. You can access all of the API versions deployed to that App Engine application version by using that URL.

The serving version remains the same until you explicitly change it, in the [Google Cloud console](https://console.cloud.google.com/appengine/versions).

### Accessing API versions deployed to a non-serving application version

If you need to access API versions that are _not_ deployed to the currently serving App Engine version, you use a _version-specific_ URL, similar to the following:
    
    
    https://VERSION-dot-YOUR_PROJECT_ID.appspot.com
    

Replace `VERSION` with your App Engine version, and `YOUR_PROJECT_ID` with your Google Cloud project ID. For example, suppose your App Engine serving version is 1, but you want to access an API version deployed to version 2. You would use this URL: `https://2-dot-YOUR_PROJECT_ID.appspot.com`.

**Important:** For backend APIs, only host names formed using `-dot-` in place of literal periods work for versioned apps.

For more details, see the [App Engine documentation](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed).

### Accessing API versions deployed to non-serving services (previously modules)

If you need to access API versions that are _not_ deployed to the default App Engine service, you can use a _service-specific_ URL using the dot syntax as follows:
    
    
    https://SERVICE-NAME-dot-YOUR_PROJECT_ID.appspot.com/_ah/api/...
    

For more details, see the [App Engine documentation](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
