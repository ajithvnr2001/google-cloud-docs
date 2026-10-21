---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketDataCenterWebhook/
title: Method: projects.locations.connections.gitRepositoryLinks.processBitbucketDataCenterWebhook \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:08.799002+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.processBitbucketDataCenterWebhook  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketDataCenterWebhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.processBitbucketDataCenterWebhook Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Try it!



gitRepositoryLinks.processBitbucketDataCenterWebhook is called by the external Bitbucket Data Center instances for notifying events.

### HTTP request

`POST https://developerconnect.googleapis.com/v1/{name=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:processBitbucketDataCenterWebhook`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The GitRepositoryLink where the webhook will be received. Format: `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "body": {
        object ([HttpBody](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/HttpBody))
      }
    }  
  
Fields  
---  
`body` |  `object (`[HttpBody](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/HttpBody)`)` Required. HTTP request body.  
  
### Response body

If successful, the response body is an empty JSON object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
