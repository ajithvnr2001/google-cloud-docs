---
url: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/create/
title: Method: projects.locations.services.create \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:57.209709+00:00
---

# Method: projects.locations.services.create  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Reference ](https://docs.cloud.google.com/run/docs/apis)



Send feedback 

#  Method: projects.locations.services.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a new Service in a given project and location.

### HTTP request

`POST https://run.googleapis.com/v2/{parent}/services`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The location and project in which this service should be created. Format: projects/{project}/locations/{location}, where {project} can be project id or number. Only lowercase characters, digits, and hyphens. It takes the form `projects/{project}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `run.services.create`

  
  
### Query parameters

Parameters  
---  
`serviceId` |  `string` Optional. The unique identifier for the Service. It must begin with letter, and cannot end with hyphen; must contain fewer than 50 characters. The name of the service becomes {parent}/services/{serviceId}. If not provided, the server will generate a unique `serviceId`.  
`validateOnly` |  `boolean` Indicates that the request should be validated and default values populated, without persisting the request or creating any resources.  
  
### Request body

The request body contains an instance of `[Service](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.services#Service)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-10 UTC."],[],[]] 
