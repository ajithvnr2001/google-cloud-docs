---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.sfdcInstances/patch/
title: Method: projects.locations.products.sfdcInstances.patch \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:59.650646+00:00
---

# Method: projects.locations.products.sfdcInstances.patch  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.sfdcInstances/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Method: projects.locations.products.sfdcInstances.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * IAM Permissions



Updates an sfdc instance. Updates the sfdc instance in spanner. Returns the sfdc instance.

### HTTP request

`PATCH https://integrations.googleapis.com/v1/{sfdcInstance.name=projects/*/locations/*/products/*/sfdcInstances/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`sfdcInstance.name` |  `string` Resource name of the SFDC instance projects/{project}/locations/{location}/sfdcInstances/{sfdcInstance}.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` Field mask specifying the fields in the above SfdcInstance that have been modified and need to be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[SfdcInstance](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.sfdcInstances#SfdcInstance)`.

### Response body

If successful, the response body contains an instance of `[SfdcInstance](https://docs.cloud.google.com/apigee/docs/reference/apis/integrations/rest/v1/projects.locations.products.sfdcInstances#SfdcInstance)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `integrations.apigeeSfdcInstances.update`
  * `integrations.sfdcInstances.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
