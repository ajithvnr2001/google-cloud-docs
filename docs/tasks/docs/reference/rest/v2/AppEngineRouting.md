---
url: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting/
title: AppEngineRouting \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:49.151988+00:00
---

# AppEngineRouting  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/tasks/docs/apis)



Send feedback 

#  AppEngineRouting Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



App Engine Routing.

Defines routing characteristics specific to App Engine - service, version, and instance.

For more information about services, versions, and instances see [An Overview of App Engine](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine), [Microservices Architecture on Google App Engine](https://cloud.google.com/appengine/docs/python/microservices-on-app-engine), [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed), and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed).

Using `[AppEngineRouting](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting)` requires [`appengine.applications.get`](https://cloud.google.com/appengine/docs/admin-api/access-control) Google IAM permission for the project and the following scope:

`https://www.googleapis.com/auth/cloud-platform`

JSON representation  
---  
      
    
    {
      "service": string,
      "version": string,
      "instance": string,
      "host": string
    }  
  
Fields  
---  
`service` |  `string` App service.By default, the task is sent to the service which is the default service when the task is attempted.For some queues or tasks which were created using the App Engine Task Queue API, `[host](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.host)` is not parsable into `[service](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.service)`, `[version](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.version)`, and `[instance](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.instance)`. For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If `[host](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.host)` is not parsable, then `[service](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.service)`, `[version](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.version)`, and `[instance](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.instance)` are the empty string.  
`version` |  `string` App version.By default, the task is sent to the version which is the default version when the task is attempted.For some queues or tasks which were created using the App Engine Task Queue API, `[host](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.host)` is not parsable into `[service](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.service)`, `[version](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.version)`, and `[instance](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.instance)`. For example, some tasks which were created using the App Engine SDK use a custom domain name; custom domains are not parsed by Cloud Tasks. If `[host](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.host)` is not parsable, then `[service](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.service)`, `[version](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.version)`, and `[instance](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.instance)` are the empty string.  
`instance` |  `string` App instance.By default, the task is sent to an instance which is available when the task is attempted.Requests can only be sent to a specific instance if [manual scaling is used in App Engine Standard](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?hl=en_US#scaling_types_and_instance_classes). App Engine Flex does not support instances. For more information, see [App Engine Standard request routing](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed) and [App Engine Flex request routing](https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed).  
`host` |  `string` Output only. The host that the task is sent to.The host is constructed from the domain name of the app associated with the queue's project ID (for example .appspot.com), and the `[service](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.service)`, `[version](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.version)`, and `[instance](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/AppEngineRouting#FIELDS.instance)`. Tasks which were created using the App Engine SDK might have a custom domain name.For more information, see [How Requests are Routed](https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
