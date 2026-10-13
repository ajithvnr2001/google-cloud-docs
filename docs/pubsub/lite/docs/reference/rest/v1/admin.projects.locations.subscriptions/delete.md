---
url: https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/delete/
title: Method: admin.projects.locations.subscriptions.delete \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:47.094382+00:00
---

# Method: admin.projects.locations.subscriptions.delete  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/reference/rest/v1/admin.projects.locations.subscriptions/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)



Send feedback 

#  Method: admin.projects.locations.subscriptions.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes



Deletes the specified subscription.

### HTTP request

`DELETE https://{endpoint}/v1/admin/{name=projects/*/locations/*/subscriptions/*}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/pubsub/lite/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the subscription to delete. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `pubsublite.subscriptions.delete`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
