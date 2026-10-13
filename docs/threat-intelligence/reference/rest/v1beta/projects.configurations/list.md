---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/list/
title: Method: projects.configurations.list \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:40.359426+00:00
---

# Method: projects.configurations.list  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  Method: projects.configurations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Get a list of configurations that meet the filter criteria.

### HTTP request

`GET https://threatintelligence.googleapis.com/v1beta/{parent=projects/*}/configurations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent of the configuration. Format: vaults/{vault}  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. Filter criteria.  
`orderBy` |  `string` Optional. Order by criteria in the csv format: "field1,field2 desc" or "field1,field2" or "field1 asc, field2".  
`pageToken` |  `string` Optional. Page token.  
`pageSize` |  `integer` Optional. Page size.  
  
### Request body

The request body must be empty.

### Response body

Response message for configurations.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "configurations": [
        {
          object ([Configuration](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#Configuration))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`configurations[]` |  `object (`[Configuration](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#Configuration)`)` List of configurations.  
`nextPageToken` |  `string` Page token.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `threatintelligence.configurations.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
