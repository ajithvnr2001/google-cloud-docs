---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext/
title: ServiceContext \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:37:07.717026+00:00
---

# ServiceContext  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  ServiceContext Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Describes a running service that sends errors. Its version changes over time and multiple versions can run in parallel.

JSON representation  
---  
      
    
    {
      "service": string,
      "version": string,
      "resourceType": string
    }  
  
Fields  
---  
`service` |  `string` An identifier of the service, such as the name of the executable, job, or Google App Engine service name. This field is expected to have a low number of values that are relatively stable over time, as opposed to `version`, which can be changed whenever new code is deployed.Contains the service name for error reports extracted from Google App Engine logs or `default` if the App Engine default service is used.  
`version` |  `string` Represents the source code version that the developer provided, which could represent a version label or a Git SHA-1 hash, for example. For App Engine standard environment, the version is set to the version of the app.  
`resourceType` |  `string` Type of the MonitoredResource. List of possible values: <https://cloud.google.com/monitoring/api/resources>Value is set automatically for incoming errors and must not be set when reporting errors.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-14 UTC."],[],[]] 
