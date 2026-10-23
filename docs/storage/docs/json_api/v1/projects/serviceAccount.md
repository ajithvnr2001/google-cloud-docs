---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount/
title: Projects.serviceAccount \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:30.304369+00:00
---

# Projects.serviceAccount  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Projects.serviceAccount Stay organized with collections  Save and categorize content based on your preferences. 

The Projects.serviceAccount resource represents the [Cloud Storage service agent](https://docs.cloud.google.com/storage/docs/projects#service-accounts) of a project. The service agent is a special service account that allows Cloud Storage to perform actions on behalf of the user. A project can have multiple service accounts, but only one service agent that is specifically associated with Cloud Storage.

For a list of methods for this resource, see the end of this page.

## Resource representations
    
    
    {
      "email_address": string,
      "kind": "storage#serviceAccount"
    }

Property name | Value | Description | Notes  
---|---|---|---  
`email_address` | `string` | The email address of a project's Cloud Storage service agent. |   
`kind` | `string` | The kind of item this is. For a Project.serviceAccounts resource, this is always `"storage#serviceAccount"`. |   
  
## Methods

[get](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount/get)
    Get a project's Cloud Storage service agent.

For information about status and error codes returned by these APIs, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
