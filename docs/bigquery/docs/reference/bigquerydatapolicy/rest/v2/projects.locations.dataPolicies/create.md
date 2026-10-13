---
url: https://docs.cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest/v2/projects.locations.dataPolicies/create/
title: Method: projects.locations.dataPolicies.create \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:00.085133+00:00
---

# Method: projects.locations.dataPolicies.create  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest/v2/projects.locations.dataPolicies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback 

#  Method: projects.locations.dataPolicies.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates a new data policy under a project with the given `dataPolicyId` (used as the display name), and data policy type.

### HTTP request

`POST https://bigquerydatapolicy.googleapis.com/v2/{parent=projects/*/locations/*}/dataPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Resource name of the project that the data policy will belong to. The format is `projects/{projectNumber}/locations/{locationId}`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataPolicyId": string,
      "dataPolicy": {
        object ([DataPolicy](https://docs.cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest/v2/projects.locations.dataPolicies#DataPolicy))
      }
    }  
  
Fields  
---  
`dataPolicyId` |  `string` Required. User-assigned (human readable) ID of the data policy that needs to be unique within a project. Used as {dataPolicyId} in part of the resource name.  
`dataPolicy` |  `object (`[DataPolicy](https://docs.cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest/v2/projects.locations.dataPolicies#DataPolicy)`)` Required. The data policy to create. The `name` field does not need to be provided for the data policy creation.  
  
### Response body

If successful, the response body contains a newly created instance of `[DataPolicy](https://docs.cloud.google.com/bigquery/docs/reference/bigquerydatapolicy/rest/v2/projects.locations.dataPolicies#DataPolicy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigquery`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `routine` resource:

  * `bigquery.routines.get`



Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `bigquery.dataPolicies.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
