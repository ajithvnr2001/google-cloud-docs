---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments.affectedResources
title: REST Resource: projects.locations.experiments.affectedResources \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:44.774198+00:00
---

# REST Resource: projects.locations.experiments.affectedResources  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments.affectedResources

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  REST Resource: projects.locations.experiments.affectedResources Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AffectedResource
    * JSON representation
  * Methods



## Resource: AffectedResource

Represents a specific Google Cloud resource, like a virtual machine or database that is targeted by an experiment.

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
`name` |  `string` Identifier. Unique identifier for this record, linking it to a specific experiment and resource. Format: `projects/{projectId}/locations/{location}/experiments/{experimentId}/affectedResources/{affected_resource_id}`.  
`displayName` |  `string` Optional. A human-readable name for the affected resource record.  
`affectedResourceUri` |  `string` Required. The full unique address (URI) of the Google Cloud resource affected by this `Experiment`. Example: the full path to a specific Compute Engine instance.  
`cloudConsolePath` |  `string` Output only. A direct link to view this specific resource in the Google Cloud Console.  
`state` |  `enum (`[State](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/State)`)` The current state of this resource within the experiment. Example: `PREPARING`, `INJECTED`, `COMPLETED`.  
`stateMessage` |  `string` A plain-language explanation of what is currently happening with this resource in the experiment.  
`error` |  `object (`[Status](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/Status)`)` Output only. Details of any error that occurred while setting up, running, or stopping the experiment on this specific resource. Empty if no errors occurred.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments.affectedResources/get)`

|  Gets the details of a specific cloud resource that is being or was affected by a particular `Experiment`.  
  
### `[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments.affectedResources/list)`

|  Lists all cloud resources that are being or were affected by a specific `Experiment`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-15 UTC."],[],[]] 
