---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/create/
title: Method: feeds.create \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:04.617897+00:00
---

# Method: feeds.create  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: feeds.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates a feed in a parent project/folder/organization to listen to its asset updates.

### HTTP request

`POST https://cloudasset.googleapis.com/v1/{parent=*/*}/feeds`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the project/folder/organization where this feed should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "feedId": string,
      "feed": {
        object ([Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#Feed))
      }
    }  
  
Fields  
---  
`feedId` |  `string` Required. This is the client-assigned asset feed identifier and it needs to be unique under a specific parent project/folder/organization.  
`feed` |  `object (`[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#Feed)`)` Required. The feed details. The field `name` must be empty and it will be generated in the format of: projects/projectNumber/feeds/feedId folders/folder_number/feeds/feedId organizations/organization_number/feeds/feedId  
  
### Response body

If successful, the response body contains a newly created instance of `[Feed](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#Feed)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
