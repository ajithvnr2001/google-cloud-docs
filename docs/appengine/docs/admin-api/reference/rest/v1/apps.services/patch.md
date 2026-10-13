---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/patch/
title: Method: apps.services.patch \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:55.432147+00:00
---

# Method: apps.services.patch  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Method: apps.services.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes
  * Try it!



Updates the configuration of the specified service.

### HTTP request

`PATCH https://appengine.googleapis.com/v1/{name=apps/*/services/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Name of the resource to update. Example: `apps/myapp/services/default`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.services.update`

  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` Required. Standard field mask for the set of fields to be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`migrateTraffic` |  `boolean` Set to `true` to gradually shift traffic to one or more versions that you specify. By default, traffic is shifted immediately. For gradual traffic migration, the target versions must be located within instances that are configured for both [warmup requests](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#InboundServiceType) and [automatic scaling](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AutomaticScaling). You must specify the [`shardBy`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#ShardBy) field in the Service resource. Gradual traffic migration is not supported in the App Engine flexible environment. For examples, see [Migrating and Splitting Traffic](https://cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic).  
  
### Request body

The request body contains an instance of `[Service](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#Service)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
