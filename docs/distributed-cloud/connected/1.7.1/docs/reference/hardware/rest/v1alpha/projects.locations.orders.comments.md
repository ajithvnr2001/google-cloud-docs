---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments
title: REST Resource: projects.locations.orders.comments \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:15.012169+00:00
---

# REST Resource: projects.locations.orders.comments  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments




#  REST Resource: projects.locations.orders.comments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Comment
    * JSON representation
  * Methods



## Resource: Comment

A comment on an order.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "labels": {
        string: string,
        ...
      },
      "author": string,
      "text": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of this comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Time when this comment was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels associated with this comment as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`author` |  `string` Output only. Username of the author of this comment. This is auto-populated from the credentials used during creation of the comment.  
`text` |  `string` Required. Text of this comment. The length of text must be <= 1000 characters.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments/create)`

|  Creates a new comment on an order.  
  
### `[get](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments/get)`

|  Gets the content of a comment.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.orders.comments/list)`

|  Lists the comments on an order.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
