---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.SequencedPublisher
title: Interface SequencedPublisher<ResponseT> (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:22.711064+00:00
---

# Interface SequencedPublisher<ResponseT> (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.SequencedPublisher

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SequencedPublisher<ResponseT> (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public interface SequencedPublisher<ResponseT> extends ApiService, Flushable

A PubSub Lite publisher that requires a sequence number assigned to every message, for publish idempotency. Errors are handled out of band. Thread safe.

## Implements

[ApiService](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiService.html), [Flushable](https://docs.oracle.com/javase/8/docs/api/java/io/Flushable.html)

## Type Parameter  
  
---  
**Name** | **Description**  
`ResponseT` |   
  
## Methods 

### cancelOutstandingPublishes()
    
    
    public abstract void cancelOutstandingPublishes()

Attempts to cancel all outstanding publishes.

### publish(PubSubMessage message, PublishSequenceNumber sequenceNumber)
    
    
    public abstract ApiFuture<ResponseT> publish(PubSubMessage message, PublishSequenceNumber sequenceNumber)

Publish a new message with an assigned sequence number.

Behavior is undefined if a call to flush() is outstanding or close() has already been called. This method never blocks.

Guarantees that if a single publish future has an exception set, all publish calls made after that will also have an exception set.

**Parameters**  
---  
**Name** | **Description**  
`message` | `[PubSubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.PubSubMessage)`  
  
`sequenceNumber` | `[PublishSequenceNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.PublishSequenceNumber)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<ResponseT>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
