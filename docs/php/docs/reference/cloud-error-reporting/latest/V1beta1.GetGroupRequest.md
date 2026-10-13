---
url: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.GetGroupRequest
title: Stackdriver Error Reporting V1beta1 Client - Class GetGroupRequest (0.27.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:49.386109+00:00
---

# Stackdriver Error Reporting V1beta1 Client - Class GetGroupRequest (0.27.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.GetGroupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Stackdriver Error Reporting V1beta1 Client - Class GetGroupRequest (0.27.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.3 (latest)  0.26.1  0.25.3  0.24.0  0.23.1  0.22.10  0.21.1  0.20.2  0.19.12 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Stackdriver Error Reporting V1beta1 Client class GetGroupRequest.

A request to return an individual group.

Generated from protobuf message `google.devtools.clouderrorreporting.v1beta1.GetGroupRequest`

## Namespace

Google \ Cloud \ ErrorReporting \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ group_name` |  `string`   
Required. The group resource name. Written as either `projects/{projectID}/groups/{group_id}` or `projects/{projectID}/locations/{location}/groups/{group_id}`. Call [groupStats.list] [google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListGroupStats] to return a list of groups belonging to this project. Examples: `projects/my-project-123/groups/my-group`, `projects/my-project-123/locations/global/groups/my-group` In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.  
  
### getGroupName

Required. The group resource name. Written as either `projects/{projectID}/groups/{group_id}` or `projects/{projectID}/locations/{location}/groups/{group_id}`. Call [groupStats.list](https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.Client.ErrorStatsServiceClient#_Google_Cloud_ErrorReporting_V1beta1_Client_ErrorStatsServiceClient__listGroupStats__) to return a list of groups belonging to this project.

Examples: `projects/my-project-123/groups/my-group`, `projects/my-project-123/locations/global/groups/my-group` In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setGroupName

Required. The group resource name. Written as either `projects/{projectID}/groups/{group_id}` or `projects/{projectID}/locations/{location}/groups/{group_id}`. Call [groupStats.list](https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.Client.ErrorStatsServiceClient#_Google_Cloud_ErrorReporting_V1beta1_Client_ErrorStatsServiceClient__listGroupStats__) to return a list of groups belonging to this project.

Examples: `projects/my-project-123/groups/my-group`, `projects/my-project-123/locations/global/groups/my-group` In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`groupName` |  `string`   
Required. The group resource name. Written as either `projects/{projectID}/groups/{group_id}` or `projects/{projectID}/locations/{location}/groups/{group_id}`. Call [groupStats.list](https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.Client.ErrorStatsServiceClient#_Google_Cloud_ErrorReporting_V1beta1_Client_ErrorStatsServiceClient__listGroupStats__) to return a list of groups belonging to this project. Examples: `projects/my-project-123/groups/my-group`, `projects/my-project-123/locations/global/groups/my-group` In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice). For a list of supported locations, see [Supported Regions](https://cloud.google.com/logging/docs/region-support). `global` is the default when unspecified. Please see ErrorGroupServiceClient::errorGroupName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[GetGroupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-error-reporting/latest/V1beta1.GetGroupRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
