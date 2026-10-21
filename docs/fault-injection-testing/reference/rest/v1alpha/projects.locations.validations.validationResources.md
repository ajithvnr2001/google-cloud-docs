---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations.validationResources
title: REST Resource: projects.locations.validations.validationResources \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:47.581121+00:00
---

# REST Resource: projects.locations.validations.validationResources  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations.validationResources

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  REST Resource: projects.locations.validations.validationResources Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ValidationResource
    * JSON representation
  * Methods



## Resource: ValidationResource

Represents a specific Google Cloud resource that a `Validation` dry run identified as _potentially_ being affected.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "affectedResourceUri": string,
      "cloudConsolePath": string,
      "state": enum ([State](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State)),
      "stateMessage": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Status))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique identifier for this specific record within the `Validation` results. Format: `projects/{project}/locations/{location}/validations/{validation}/validationResources/{validationResourceId}`.  
`displayName` |  `string` Optional. A human-readable name for the `ValidationResource` record.  
`affectedResourceUri` |  `string` Required. The full unique address (URI) of the Google Cloud resource that was identified.  
`cloudConsolePath` |  `string` Output only. A direct link to view this specific resource in the Google Cloud Console.  
`state` |  `enum (`[State](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State)`)` The current state of this resource within the dry run. Typically `COMPLETED`.  
`stateMessage` |  `string` A human-readable description of the validation status for this resource.  
`error` |  `object (`[Status](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Status)`)` Output only. Details of any error encountered while checking the resource during the dry run. Empty if the check was successful.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations.validationResources/get)`

|  Gets the details of a specific `ValidationResource`.  
  
### `[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations.validationResources/list)`

|  Lists all cloud resources identified as potentially affected within a specific `Validation` dry run.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-15 UTC."],[],[]] 
