---
url: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureTemplates/list/
title: Method: organizations.locations.postureTemplates.list \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:07.979204+00:00
---

# Method: organizations.locations.postureTemplates.list  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureTemplates/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: organizations.locations.postureTemplates.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists every `[PostureTemplate](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureTemplates#PostureTemplate)` in a given organization and location.

### HTTP request

`GET https://securityposture.googleapis.com/v1/{parent=organizations/*/locations/*}/postureTemplates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name, in the format `organizations/{organization}/locations/global`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of posture templates to return. The default value is `500`.If you exceed the maximum value of `1000`, then the service uses the maximum value.  
`pageToken` |  `string` Optional. A pagination token returned from a previous request to list posture templates. Provide this token to retrieve the next page of results.  
`filter` |  `string` Optional. A filter to apply to the list of postures, in the format defined in [AIP-160: Filtering](https://google.aip.dev/160).  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "postureTemplates": [
        {
          object ([PostureTemplate](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureTemplates#PostureTemplate))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`postureTemplates[]` |  `object (`[PostureTemplate](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureTemplates#PostureTemplate)`)` The list of `[PostureTemplate](https://docs.cloud.google.com/security-command-center/docs/reference/securityposture/rest/v1/organizations.locations.postureTemplates#PostureTemplate)` resources.  
`nextPageToken` |  `string` A pagination token. To retrieve the next page of results, call the method again with this token.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `securityposture.postureTemplates.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-14 UTC."],[],[]] 
