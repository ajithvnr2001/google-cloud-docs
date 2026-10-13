---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs/list/
title: Method: organizations.locations.vpcFlowLogsConfigs.list \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:36.282614+00:00
---

# Method: organizations.locations.vpcFlowLogsConfigs.list  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/organizations.locations.vpcFlowLogsConfigs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: organizations.locations.vpcFlowLogsConfigs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists all `VpcFlowLogsConfigs` in a given organization.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1beta1/{parent=organizations/*/locations/*}/vpcFlowLogsConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the VpcFlowLogsConfig, in one of the following formats:

  * For project-level resources: `projects/{projectId}/locations/global`
  * For organization-level resources: `organizations/{organization_id}/locations/global`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkmanagement.vpcflowlogsconfigs.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Number of `VpcFlowLogsConfigs` to return.  
`pageToken` |  `string` Optional. Page token from an earlier query, as returned in `nextPageToken`.  
`filter` |  `string` Optional. Lists the `VpcFlowLogsConfigs` that match the filter expression. A filter expression must use the supported [CEL logic operators](https://cloud.google.com/vpc/docs/about-flow-logs-records#supported_cel_logic_operators).  
`orderBy` |  `string` Optional. Field to use to sort the list.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1beta1/ListVpcFlowLogsConfigsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-26 UTC."],[],[]] 
