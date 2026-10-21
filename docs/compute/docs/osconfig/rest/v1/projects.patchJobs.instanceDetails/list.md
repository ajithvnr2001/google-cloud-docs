---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs.instanceDetails/list/
title: Method: projects.patchJobs.instanceDetails.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:53.123908+00:00
---

# Method: projects.patchJobs.instanceDetails.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs.instanceDetails/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.patchJobs.instanceDetails.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Get a list of instance details for a given patch job.

### HTTP request

`GET https://osconfig.googleapis.com/v1/{parent=projects/*/patchJobs/*}/instanceDetails`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent for the instances are in the form of `projects/*/patchJobs/*`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of instance details records to return. Default is 100.  
`pageToken` |  `string` A pagination token returned from a previous call that indicates where this listing should continue from.  
`filter` |  `string` A filter expression that filters results listed in the response. This field supports filtering results by instance zone, name, state, or `failureReason`.  
  
### Request body

The request body must be empty.

### Response body

A response message for listing the instances details for a patch job.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "patchJobInstanceDetails": [
        {
          object ([PatchJobInstanceDetails](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs.instanceDetails#PatchJobInstanceDetails))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`patchJobInstanceDetails[]` |  `object (`[PatchJobInstanceDetails](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs.instanceDetails#PatchJobInstanceDetails)`)` A list of instance status.  
`nextPageToken` |  `string` A pagination token that can be used to get the next page of results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `osconfig.patchJobs.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
