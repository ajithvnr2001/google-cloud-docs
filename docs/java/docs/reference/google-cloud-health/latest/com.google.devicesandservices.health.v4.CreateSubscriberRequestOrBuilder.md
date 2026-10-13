---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequestOrBuilder
title: Interface CreateSubscriberRequestOrBuilder (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:40.647361+00:00
---

# Interface CreateSubscriberRequestOrBuilder (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateSubscriberRequestOrBuilder (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public interface CreateSubscriberRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParent()
    
    
    public abstract String getParent()

Required. The parent resource where this subscriber will be created. Format: projects/{project_number} Example: projects/1234567890

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource where this subscriber will be created. Format: projects/{project_number} Example: projects/1234567890

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getSubscriber()
    
    
    public abstract CreateSubscriberPayload getSubscriber()

Required. The subscriber to create.

` .google.devicesandservices.health.v4.CreateSubscriberPayload subscriber = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[CreateSubscriberPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberPayload)` | The subscriber.  
  
### getSubscriberId()
    
    
    public abstract String getSubscriberId()

Optional. The ID to use for the subscriber, which will become the final component of the subscriber's resource name.

This value should be 4-36 characters, and valid characters are /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/.

`string subscriber_id = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subscriberId.  
  
### getSubscriberIdBytes()
    
    
    public abstract ByteString getSubscriberIdBytes()

Optional. The ID to use for the subscriber, which will become the final component of the subscriber's resource name.

This value should be 4-36 characters, and valid characters are /[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/\[a-z0-9-\]{2,34}\[a-z0-9\])/.

`string subscriber_id = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subscriberId.  
  
### getSubscriberOrBuilder()
    
    
    public abstract CreateSubscriberPayloadOrBuilder getSubscriberOrBuilder()

Required. The subscriber to create.

` .google.devicesandservices.health.v4.CreateSubscriberPayload subscriber = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[CreateSubscriberPayloadOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberPayloadOrBuilder)` |   
  
### hasSubscriber()
    
    
    public abstract boolean hasSubscriber()

Required. The subscriber to create.

` .google.devicesandservices.health.v4.CreateSubscriberPayload subscriber = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the subscriber field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
