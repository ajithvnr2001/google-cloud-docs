---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder
title: Class PublisherSettings.Builder (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:19.108944+00:00
---

# Class PublisherSettings.Builder (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PublisherSettings.Builder (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public abstract static class PublisherSettings.Builder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PublisherSettings.Builder

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### Builder()
    
    
    public Builder()

## Methods 

### build()
    
    
    public abstract PublisherSettings build()

**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings)` |   
  
### setAdminClient(AdminClient adminClient)
    
    
    public abstract PublisherSettings.Builder setAdminClient(AdminClient adminClient)

The AdminClient to use, if provided.

**Parameter**  
---  
**Name** | **Description**  
`adminClient` | `[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setBatchingSettings(BatchingSettings batchingSettings)
    
    
    public abstract PublisherSettings.Builder setBatchingSettings(BatchingSettings batchingSettings)

Batching settings for this publisher to use. Apply per-partition.

**Parameter**  
---  
**Name** | **Description**  
`batchingSettings` | `[BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setCredentialsProvider(CredentialsProvider credentialsProvider)
    
    
    public abstract PublisherSettings.Builder setCredentialsProvider(CredentialsProvider credentialsProvider)

A provider for credentials.

**Parameter**  
---  
**Name** | **Description**  
`credentialsProvider` | `[CredentialsProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.CredentialsProvider.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setEnableCompression(boolean enableCompression)
    
    
    public abstract PublisherSettings.Builder setEnableCompression(boolean enableCompression)

Whether request compression is enabled. Default true.

**Parameter**  
---  
**Name** | **Description**  
`enableCompression` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setEnableIdempotence(boolean enableIdempotence)
    
    
    public abstract PublisherSettings.Builder setEnableIdempotence(boolean enableIdempotence)

Whether idempotence is enabled, where the server will ensure that unique messages within a single publisher session are stored only once. Default true.

**Parameter**  
---  
**Name** | **Description**  
`enableIdempotence` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setFramework(PubsubContext.Framework framework)
    
    
    public abstract PublisherSettings.Builder setFramework(PubsubContext.Framework framework)

A Framework tag for internal metrics. Please set this if integrating with a public framework!

**Parameter**  
---  
**Name** | **Description**  
`framework` | `[PubsubContext.Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.wire.PubsubContext.Framework)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setKeyExtractor(KeyExtractor keyExtractor)
    
    
    public abstract PublisherSettings.Builder setKeyExtractor(KeyExtractor keyExtractor)

A KeyExtractor for getting the routing key from a message.

**Parameter**  
---  
**Name** | **Description**  
`keyExtractor` | `[KeyExtractor](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.KeyExtractor)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setMessageTransformer(MessageTransformer<PubsubMessage,Message> messageTransformer)
    
    
    public abstract PublisherSettings.Builder setMessageTransformer(MessageTransformer<PubsubMessage,Message> messageTransformer)

A MessageTransformer for constructing wire messages from Cloud Pub/Sub PubsubMessages.

**Parameter**  
---  
**Name** | **Description**  
`messageTransformer` | `[MessageTransformer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageTransformer)<com.google.pubsub.v1.PubsubMessage,[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setServiceClient(PublisherServiceClient client)
    
    
    public abstract PublisherSettings.Builder setServiceClient(PublisherServiceClient client)

The PublisherServiceClient to use, if provided.

**Parameter**  
---  
**Name** | **Description**  
`client` | `[PublisherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.v1.PublisherServiceClient)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
### setTopicPath(TopicPath path)
    
    
    public abstract PublisherSettings.Builder setTopicPath(TopicPath path)

The topic path to publish to.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PublisherSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
