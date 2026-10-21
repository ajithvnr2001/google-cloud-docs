---
url: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations.revisions/list/
title: Method: projects.configurations.revisions.list \u00a0|\u00a0 Google Threat Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:40.671512+00:00
---

# Method: projects.configurations.revisions.list  |  Google Threat Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations.revisions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Threat Intelligence ](https://docs.cloud.google.com/threat-intelligence)
  * [ REST Reference ](https://docs.cloud.google.com/threat-intelligence/reference/rest)



Send feedback 

#  Method: projects.configurations.revisions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * ConfigurationRevision
    * JSON representation



List configuration revisions that meet the filter criteria.

### HTTP request

`GET https://threatintelligence.googleapis.com/v1beta/{parent=projects/*/configurations/*}/revisions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the Configuration to retrieve Revisions for  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. An AIP-160 filter string  
`orderBy` |  `string` Optional. Specify ordering of response  
`pageSize` |  `integer` Optional. Page Size  
`pageToken` |  `string` Optional. A page token provided by the API  
  
### Request body

The request body must be empty.

### Response body

Response message for revisions.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "revisions": [
        {
          object ([ConfigurationRevision](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations.revisions/list#ConfigurationRevision))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`revisions[]` |  `object (`[ConfigurationRevision](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations.revisions/list#ConfigurationRevision)`)` The Configuration Revisions associated with the specified Configuration  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `threatintelligence.configurations.listRevisions`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## ConfigurationRevision

A ConfigurationRevision is a snapshot of a Configuration at a point in time. It is immutable.

JSON representation  
---  
      
    
    {
      "name": string,
      "snapshot": {
        object ([Configuration](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#Configuration))
      },
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the ConfigurationRevision Format: projects//configurations//revisions/  
`snapshot` |  `object (`[Configuration](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/projects.configurations#Configuration)`)` The snapshot of the configuration  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the Revision was createdUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-19 UTC."],[],[]] 
