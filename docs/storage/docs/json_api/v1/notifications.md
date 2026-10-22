---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/
title: Notifications \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:50.615409+00:00
---

# Notifications  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Notifications Stay organized with collections  Save and categorize content based on your preferences. 

To try out the methods for this resource, see Methods.

## Resource representations

A subscription to receive [Pub/Sub notifications](https://docs.cloud.google.com/storage/docs/pubsub-notifications).
    
    
    {
      "id": string,
      "topic": string,
      "event_types": [
        string
      ],
      "custom_attributes": {
        (key): string
      },
      "payload_format": string,
      "object_name_prefix": string,
      "etag": string,
      "selfLink": string,
      "kind": "storage#notification"
    }

Property name | Value | Description | Notes  
---|---|---|---  
`custom_attributes` | `object` | An optional list of additional attributes to attach to each Pub/Sub message published for this notification subscription. |  writable   
`custom_attributes.(key)` | `string` |  |   
`etag` | `string` | HTTP 1.1 [Entity tag](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3) for this subscription notification. |   
`event_types[]` | `list` | If present, only send notifications about listed [event types](https://docs.cloud.google.com/storage/docs/pubsub-notifications#events). If empty, send notifications for all event types. |  writable   
`id` | `string` | The ID of the notification. |   
`kind` | `string` | The kind of item this is. For notifications, this is always `"storage#notification"`. |   
`object_name_prefix` | `string` | If present, only apply this notification configuration to object names that begin with this prefix. |  writable   
`payload_format` | `string` | The desired content of the Payload.   
  
Acceptable values are: 

  * `"JSON_API_V1"`
  * `"NONE"`

|  writable   
`selfLink` | `string` | The canonical URL of this notification. |   
`topic` | `string` | The Pub/Sub topic to which this subscription publishes. Formatted as: `"//pubsub.googleapis.com/projects/PROJECT-IDENTIFIER/topics/TOPIC-NAME"` |  writable   
  
## Methods

[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/delete)
    Permanently deletes a notification subscription.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/get)
    View a notification configuration.
[insert](https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/insert)
    Creates a notification subscription for a given bucket.
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/notifications/list)
    Retrieves a list of notification subscriptions for a given bucket.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
