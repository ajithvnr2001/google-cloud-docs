---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/queryOrgVpcFlowLogsConfigs/
title: Method: projects.locations.vpcFlowLogsConfigs.queryOrgVpcFlowLogsConfigs \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:33.798797+00:00
---

# Method: projects.locations.vpcFlowLogsConfigs.queryOrgVpcFlowLogsConfigs  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs/queryOrgVpcFlowLogsConfigs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.vpcFlowLogsConfigs.queryOrgVpcFlowLogsConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



vpcFlowLogsConfigs.queryOrgVpcFlowLogsConfigs returns a list of all organization-level VPC Flow Logs configurations applicable to the specified project.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:queryOrgVpcFlowLogsConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the VpcFlowLogsConfig, specified in the following format: `projects/{projectId}/locations/global` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkmanagement.vpcflowlogsconfigs.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Number of `VpcFlowLogsConfigs` to return.  
`pageToken` |  `string` Optional. Page token from an earlier query, as returned in `nextPageToken`.  
`filter` |  `string` Optional. Lists the `VpcFlowLogsConfigs` that match the filter expression. A filter expression must use the supported [CEL logic operators](https://cloud.google.com/vpc/docs/about-flow-logs-records#supported_cel_logic_operators).  
  
### Request body

The request body must be empty.

### Response body

Response for the `QueryVpcFlowLogsConfigs` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "vpcFlowLogsConfigs": [
        {
          object ([VpcFlowLogsConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`vpcFlowLogsConfigs[]` |  `object (`[VpcFlowLogsConfig](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/organizations.locations.vpcFlowLogsConfigs#VpcFlowLogsConfig)`)` List of VPC Flow Log configurations.  
`nextPageToken` |  `string` Page token to fetch the next set of configurations.  
`unreachable[]` |  `string` Locations that could not be reached (when querying all locations with `-`).  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-01 UTC."],[],[]] 
