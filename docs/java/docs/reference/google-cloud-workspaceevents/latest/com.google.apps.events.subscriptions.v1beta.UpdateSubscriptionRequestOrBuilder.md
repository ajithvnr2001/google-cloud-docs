---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.UpdateSubscriptionRequestOrBuilder
title: Interface UpdateSubscriptionRequestOrBuilder (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:23.863714+00:00
---

# Interface UpdateSubscriptionRequestOrBuilder (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.UpdateSubscriptionRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdateSubscriptionRequestOrBuilder (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface UpdateSubscriptionRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getSubscription()
    
    
    public abstract Subscription getSubscription()

Required. The subscription to update.

The subscription's `name` field is used to identify the subscription to update.

` .google.apps.events.subscriptions.v1beta.Subscription subscription = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.Subscription)` | The subscription.  
  
### getSubscriptionOrBuilder()
    
    
    public abstract SubscriptionOrBuilder getSubscriptionOrBuilder()

Required. The subscription to update.

The subscription's `name` field is used to identify the subscription to update.

` .google.apps.events.subscriptions.v1beta.Subscription subscription = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[SubscriptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.SubscriptionOrBuilder)` |   
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Optional. The field to update. If omitted, updates any fields included in the request.

You can update one of the following fields in a subscription:

  * `expire_time`: The timestamp when the subscription expires.
  * `ttl`: The time-to-live (TTL) or duration of the subscription.
  * `event_types`: The list of event types to receive about the target resource.

To fully replace the subscription (the equivalent of `PUT`), use `*`. Any omitted fields are updated with empty values.




`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Optional. The field to update. If omitted, updates any fields included in the request.

You can update one of the following fields in a subscription:

  * `expire_time`: The timestamp when the subscription expires.
  * `ttl`: The time-to-live (TTL) or duration of the subscription.
  * `event_types`: The list of event types to receive about the target resource.

To fully replace the subscription (the equivalent of `PUT`), use `*`. Any omitted fields are updated with empty values.




`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

Optional. If set to `true`, validates and previews the request, but doesn't update the subscription.

`bool validate_only = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasSubscription()
    
    
    public abstract boolean hasSubscription()

Required. The subscription to update.

The subscription's `name` field is used to identify the subscription to update.

` .google.apps.events.subscriptions.v1beta.Subscription subscription = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subscription field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Optional. The field to update. If omitted, updates any fields included in the request.

You can update one of the following fields in a subscription:

  * `expire_time`: The timestamp when the subscription expires.
  * `ttl`: The time-to-live (TTL) or duration of the subscription.
  * `event_types`: The list of event types to receive about the target resource.

To fully replace the subscription (the equivalent of `PUT`), use `*`. Any omitted fields are updated with empty values.




`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
