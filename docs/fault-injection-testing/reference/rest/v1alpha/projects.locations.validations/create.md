---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/create/
title: Method: projects.locations.validations.create \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:45.732979+00:00
---

# Method: projects.locations.validations.create  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/create/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Method: projects.locations.validations.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Creates a new `Validation` dry run. This process involves analyzing the provided `Action` to identify all the Google Cloud resources that match the targeting criteria. You can view the results by listing the `ValidationResource` children of the `Validation` dry run. The `Validation` dry run starts in the `PREPARING` state and transitions to `COMPLETED` once the analysis is finished.

### HTTP request

`POST https://faulttesting.googleapis.com/v1alpha/{parent=projects/*/locations/*}/validations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location where this dry run will be created. Format: `projects/{projectId}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`validationId` |  `string` Optional. The ID to use for the dry run, which will become the final component of the resource name. If not provided, a UUID will be generated. This value should be 4-63 characters, start with a letter or number, end with a letter or number, and contain only lowercase letters, numbers, and hyphens.  
  
### Request body

The request body contains an instance of `[Validation](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations#Validation)`.

### Response body

If successful, the response body contains a newly created instance of `[Validation](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations#Validation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `faulttesting.validations.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
