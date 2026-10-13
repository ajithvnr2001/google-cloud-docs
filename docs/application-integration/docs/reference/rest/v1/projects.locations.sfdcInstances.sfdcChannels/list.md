---
url: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances.sfdcChannels/list/
title: Method: projects.locations.sfdcInstances.sfdcChannels.list \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:01.330188+00:00
---

# Method: projects.locations.sfdcInstances.sfdcChannels.list  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances.sfdcChannels/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback 

#  Method: projects.locations.sfdcInstances.sfdcChannels.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists all sfdc channels that match the filter. Restrict to sfdc channels belonging to the current client only.

### HTTP request

`GET https://integrations.googleapis.com/v1/{parent=projects/*/locations/*/sfdcInstances/*}/sfdcChannels`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The client, which owns this collection of SfdcChannels.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The size of entries in the response. If unspecified, defaults to 100.  
`pageToken` |  `string` The token returned in the previous response.  
`filter` |  `string` Filtering as supported in <https://developers.google.com/authorized-buyers/apis/guides/list-filters>.  
`readMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The mask which specifies fields that need to be returned in the SfdcChannel's response.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListSfdcChannelsResponse](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ListSfdcChannelsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `integrations.sfdcChannels.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
