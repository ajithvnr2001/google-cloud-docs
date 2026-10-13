---
url: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances.sfdcChannels/create/
title: Method: projects.locations.sfdcInstances.sfdcChannels.create \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:46.010285+00:00
---

# Method: projects.locations.sfdcInstances.sfdcChannels.create  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances.sfdcChannels/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback 

#  Method: projects.locations.sfdcInstances.sfdcChannels.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates an sfdc channel record. Store the sfdc channel in Spanner. Returns the sfdc channel.

### HTTP request

`POST https://integrations.googleapis.com/v1/{parent=projects/*/locations/*/sfdcInstances/*}/sfdcChannels`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. "projects/{project}/locations/{location}" format.  
  
### Request body

The request body contains an instance of `[SfdcChannel](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.products.sfdcInstances.sfdcChannels#SfdcChannel)`.

### Response body

If successful, the response body contains a newly created instance of `[SfdcChannel](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.products.sfdcInstances.sfdcChannels#SfdcChannel)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `integrations.sfdcChannels.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
