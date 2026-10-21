---
url: https://docs.cloud.google.com/app-optimize/reference/rest/
title: App Optimize API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:13.368901+00:00
---

# App Optimize API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  App Optimize API Stay organized with collections  Save and categorize content based on your preferences. 

The App Optimize API provides developers and platform teams with tools to monitor, analyze, and improve the performance and cost-efficiency of their cloud applications.

  * REST Resource: v1beta.projects.locations
  * REST Resource: v1beta.projects.locations.operations
  * REST Resource: v1beta.projects.locations.reports



## Service: appoptimize.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://appoptimize.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://appoptimize.googleapis.com`



## REST Resource: [v1beta.projects.locations](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations/get)` |  `GET /v1beta/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations/list)` |  `GET /v1beta/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta.projects.locations.operations](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.operations/cancel)` |  `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.operations/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.operations/list)` |  `GET /v1beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta.projects.locations.reports](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports)

Methods  
---  
`[create](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/reports`   
Creates a new report.  
`[delete](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/reports/*}`   
Deletes the specified report.  
`[get](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/get)` |  `GET /v1beta/{name=projects/*/locations/*/reports/*}`   
Retrieves the details of a report configuration.  
`[list](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/reports`   
Lists reports within a given project.  
`[read](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/read)` |  `POST /v1beta/{name=projects/*/locations/*/reports/*}:read`   
Reads data within a specified report.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
