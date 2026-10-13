---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.changeLogEntries/get/
title: Method: projects.locations.orders.changeLogEntries.get \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:47.320619+00:00
---

# Method: projects.locations.orders.changeLogEntries.get  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.changeLogEntries/get/




#  Method: projects.locations.orders.changeLogEntries.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Gets details of a change to an order.

### HTTP request

`GET https://gdchardwaremanagement.googleapis.com/v1alpha/{name=projects/*/locations/*/orders/*/changeLogEntries/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the change log entry. Format: `projects/{project}/locations/{location}/orders/{order}/changeLogEntries/{change_log_entry}`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ChangeLogEntry](https://docs.cloud.google.com/distributed-cloud/edge/1.7.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.changeLogEntries#ChangeLogEntry)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `gdchardwaremanagement.changeLogEntries.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
