---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/insert/
title: Notifications: insert \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:43.301114+00:00
---

# Notifications: insert  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Notifications: insert Stay organized with collections  Save and categorize content based on your preferences. 

Creates a [Pub/Sub notification configuration](https://docs.cloud.google.com/storage/docs/pubsub-notifications) for a given bucket.

## Required permissions

The authenticated user must have the `storage.buckets.update` IAM permission to use this method.

## Request

### HTTP request
    
    
    POST https://storage.googleapis.com/storage/v1/b/bucket/notificationConfigs

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

To see an example of how to include query parameters in a request, see the [JSON API Overview](https://docs.cloud.google.com/storage/docs/json_api#query_parameters) page.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  The parent bucket of the notification.   
  
### Request body

In the request body, supply a [notification resource](https://docs.cloud.google.com/storage/docs/json_api/v1/notifications#resource) with the following properties:

Property name | Value | Description | Notes  
---|---|---|---  
**Required Properties**  
`topic` | `string` | The Pub/Sub topic to which this subscription publishes. Formatted as: `"//pubsub.googleapis.com/projects/PROJECT-IDENTIFIER/topics/TOPIC-NAME"` |  writable   
`payload_format` | `string` | The desired content of the Payload.   
  
Acceptable values are: 

  * `"JSON_API_V1"`
  * `"NONE"`

|  writable   
**Optional Properties**  
`custom_attributes` | `object` | An optional list of additional attributes to attach to each Pub/Sub message published for this notification subscription. |  writable   
`event_types[]` | `list` | If present, only send notifications about listed [event types](https://docs.cloud.google.com/storage/docs/pubsub-notifications#events). If empty, send notifications for all event types. |  writable   
`object_name_prefix` | `string` | If present, only apply this notification configuration to object names that begin with this prefix. |  writable   
  
## Response

If successful, this method returns a [notification resource](https://docs.cloud.google.com/storage/docs/json_api/v1/notifications#resource) in the response body.

## Try it!

Use the APIs Explorer below to call this method on live data and see the response. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
