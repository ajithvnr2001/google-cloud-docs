---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/get/
title: Method: contextProperties.get \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:33.368674+00:00
---

# Method: contextProperties.get  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Method: contextProperties.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



**Full name** : projects.locations.instances.cases.alerts.contextProperties.get

Get a context-property.

### HTTP request

Choose a location:

africa-south1 asia-northeast1 asia-south1 asia-southeast1 asia-southeast2 australia-southeast1 europe-central2 europe-west12 europe-west2 europe-west3 europe-west6 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast2 southamerica-east1 us eu

  
`GET https://chronicle.africa-south1.rep.googleapis.com/v1alpha/{name}`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the ContextProperty to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/contextProperties projects/{project}/locations/{location}/instances/{instance}/cases/{case}/contextProperties projects/{project}/locations/{location}/instances/{instance}/cases/{case}/alerts/{alert}/contextProperties projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}/connectors/{connector}/contextProperties projects/{project}/locations/{location}/instances/{instance}/integrations/{integration}/jobs/{job}/contextProperties  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ContextProperty](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.cases.alerts.contextProperties#ContextProperty)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.contextProperties.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-13 UTC."],[],[]] 
