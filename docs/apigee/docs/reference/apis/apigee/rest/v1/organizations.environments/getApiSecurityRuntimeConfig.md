---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getApiSecurityRuntimeConfig/
title: Method: organizations.environments.getApiSecurityRuntimeConfig \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:44.198666+00:00
---

# Method: organizations.environments.getApiSecurityRuntimeConfig  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/getApiSecurityRuntimeConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.getApiSecurityRuntimeConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Gets the API Security runtime configuration for an environment. This named ApiSecurityRuntimeConfig to prevent conflicts with ApiSecurityConfig from addon config.

### HTTP request

`GET https://apigee.googleapis.com/v1/{name=organizations/*/environments/*/apiSecurityRuntimeConfig}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the environment API Security Runtime configuration resource. Use the following structure in your request: `organizations/{org}/environments/{env}/apiSecurityRuntimeConfig` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.environments.get`

  
  
### Request body

The request body must be empty.

### Response body

Response for environments.getApiSecurityRuntimeConfig[EnvironmentService.GetApiSecurityRuntimeConfig].

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "revisionId": string,
      "updateTime": string,
      "location": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Name of the environment API Security Runtime configuration resource. Format: `organizations/{org}/environments/{env}/apiSecurityRuntimeConfig`  
`uid` |  `string` Unique ID for the API Security Runtime configuration. The ID will only change if the environment is deleted and recreated.  
`revisionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Revision ID of the API Security Runtime configuration. The higher the value, the more recently the configuration was deployed.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time that the API Security Runtime configuration was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`location[]` |  `string` A list of up to 5 Cloud Storage Blobs that contain SecurityActions.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
