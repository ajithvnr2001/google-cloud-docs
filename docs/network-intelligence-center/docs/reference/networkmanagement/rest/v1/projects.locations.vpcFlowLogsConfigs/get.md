---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/get/
title: Method: projects.locations.vpcFlowLogsConfigs.get \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:33.046105+00:00
---

# Method: projects.locations.vpcFlowLogsConfigs.get  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.vpcFlowLogsConfigs.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets the details of a specific `VpcFlowLogsConfig`.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the VpcFlowLogsConfig, in one of the following formats:

  * For project-level resources: `projects/{projectId}/locations/global/vpcFlowLogsConfigs/{vpcFlowLogsConfigId}`
  * For organization-level resources: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpcFlowLogsConfigId}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `networkmanagement.vpcflowlogsconfigs.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[VpcFlowLogsConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
