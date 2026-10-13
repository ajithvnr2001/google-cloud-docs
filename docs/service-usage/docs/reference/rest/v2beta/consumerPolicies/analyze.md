---
url: https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/consumerPolicies/analyze/
title: Method: consumerPolicies.analyze \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:34.509633+00:00
---

# Method: consumerPolicies.analyze  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/consumerPolicies/analyze/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage)
  * [ Reference ](https://docs.cloud.google.com/service-usage/docs/apis)



Send feedback 

#  Method: consumerPolicies.analyze Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * AnalysisType



Analyze a consumer policy change without kicking off the actual update. The consumer policy is subject to change before the actual update takes place.

### HTTP request

`POST https://serviceusage.googleapis.com/v2beta/{proposedPolicy.name=*/*/consumerPolicies/*}:analyze`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`proposedPolicy.name` |  `string` Output only. The resource name of the policy. Only the `default` policy is supported: `projects/12345/consumerPolicies/default`, `folders/12345/consumerPolicies/default`, `organizations/12345/consumerPolicies/default`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "proposedPolicy": {
        "name": string,
        "etag": string,
        "createTime": string,
        "updateTime": string,
        "enableRules": [
          {
            "services": [
              string
            ]
          }
        ]
      },
      "analysisTypes": [
        enum ([AnalysisType](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/consumerPolicies/analyze#AnalysisType))
      ]
    }  
  
Fields  
---  
`proposedPolicy.etag` |  `string` An opaque tag indicating the current version of the policy, used for concurrency control.  
`proposedPolicy.createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the policy was created. For singleton policies, this is the first touch of the policy.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`proposedPolicy.updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the policy was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`proposedPolicy.enableRules[]` |  `object (`[EnableRule](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/EnableRule)`)` Enable rules define usable services, groups, and categories. There can currently be at most one `EnableRule`. This restriction will be lifted in later releases.  
`analysisTypes[]` |  `enum (`[AnalysisType](https://docs.cloud.google.com/service-usage/docs/reference/rest/v2beta/consumerPolicies/analyze#AnalysisType)`)` The type of analysis to conduct. It returns INVALID_ARGUMENT if the empty list is provided.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## AnalysisType

The enum of analysis types.

Enums  
---  
`ANALYSIS_TYPE_UNSPECIFIED` | Unspecified analysis type. Do not use.  
`ANALYSIS_TYPE_DEPENDENCY` | The analysis of service dependencies.  
`ANALYSIS_TYPE_RESOURCE_USAGE` | The analysis of service resource usage.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-11 UTC."],[],[]] 
