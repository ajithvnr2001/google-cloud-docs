---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.AzureEventHubsFailureReasonOrBuilder
title: Interface IngestionFailureEvent.AzureEventHubsFailureReasonOrBuilder (1.157.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:55.172821+00:00
---

# Interface IngestionFailureEvent.AzureEventHubsFailureReasonOrBuilder (1.157.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.AzureEventHubsFailureReasonOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface IngestionFailureEvent.AzureEventHubsFailureReasonOrBuilder (1.157.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.157.0 (latest)  1.153.0  1.152.0  1.151.0  1.150.1  1.149.0  1.148.0  1.147.0  1.145.0  1.143.1  1.142.0  1.141.5  1.140.2  1.139.4  1.138.0  1.137.1  1.136.1  1.135.0  1.134.2  1.133.1  1.132.2  1.131.0  1.130.0  1.129.6  1.127.3  1.126.6  1.125.13  1.123.18  1.122.2  1.121.1  1.120.24  1.119.1  1.118.0  1.117.0  1.116.4  1.115.5 
    
    
    public static interface IngestionFailureEvent.AzureEventHubsFailureReasonOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getApiViolationReason()
    
    
    public abstract IngestionFailureEvent.ApiViolationReason getApiViolationReason()

Optional. The Pub/Sub API limits prevented the desired message from being published.

` .google.pubsub.v1.IngestionFailureEvent.ApiViolationReason api_violation_reason = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestionFailureEvent.ApiViolationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.ApiViolationReason)` | The apiViolationReason.  
  
### getApiViolationReasonOrBuilder()
    
    
    public abstract IngestionFailureEvent.ApiViolationReasonOrBuilder getApiViolationReasonOrBuilder()

Optional. The Pub/Sub API limits prevented the desired message from being published.

` .google.pubsub.v1.IngestionFailureEvent.ApiViolationReason api_violation_reason = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestionFailureEvent.ApiViolationReasonOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.ApiViolationReasonOrBuilder)` |   
  
### getEventHub()
    
    
    public abstract String getEventHub()

Optional. The name of the event hub being ingested from.

`string event_hub = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The eventHub.  
  
### getEventHubBytes()
    
    
    public abstract ByteString getEventHubBytes()

Optional. The name of the event hub being ingested from.

`string event_hub = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for eventHub.  
  
### getMessageTransformationFailureReason()
    
    
    public abstract IngestionFailureEvent.MessageTransformationFailureReason getMessageTransformationFailureReason()

Optional. Failure encountered when applying a message transformation to the Pub/Sub message.

` .google.pubsub.v1.IngestionFailureEvent.MessageTransformationFailureReason message_transformation_failure_reason = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestionFailureEvent.MessageTransformationFailureReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.MessageTransformationFailureReason)` | The messageTransformationFailureReason.  
  
### getMessageTransformationFailureReasonOrBuilder()
    
    
    public abstract IngestionFailureEvent.MessageTransformationFailureReasonOrBuilder getMessageTransformationFailureReasonOrBuilder()

Optional. Failure encountered when applying a message transformation to the Pub/Sub message.

` .google.pubsub.v1.IngestionFailureEvent.MessageTransformationFailureReason message_transformation_failure_reason = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestionFailureEvent.MessageTransformationFailureReasonOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.MessageTransformationFailureReasonOrBuilder)` |   
  
### getNamespace()
    
    
    public abstract String getNamespace()

Optional. The namespace containing the event hub being ingested from.

`string namespace = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The namespace.  
  
### getNamespaceBytes()
    
    
    public abstract ByteString getNamespaceBytes()

Optional. The namespace containing the event hub being ingested from.

`string namespace = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for namespace.  
  
### getOffset()
    
    
    public abstract long getOffset()

Optional. The offset within the partition of the message that failed to be ingested.

`int64 offset = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The offset.  
  
### getPartitionId()
    
    
    public abstract long getPartitionId()

Optional. The partition ID of the message that failed to be ingested.

`int64 partition_id = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The partitionId.  
  
### getReasonCase()
    
    
    public abstract IngestionFailureEvent.AzureEventHubsFailureReason.ReasonCase getReasonCase()

**Returns**  
---  
**Type** | **Description**  
`[IngestionFailureEvent.AzureEventHubsFailureReason.ReasonCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.AzureEventHubsFailureReason.ReasonCase)` |   
  
### getSchemaViolationReason()
    
    
    public abstract IngestionFailureEvent.SchemaViolationReason getSchemaViolationReason()

Optional. The Pub/Sub message failed schema validation.

` .google.pubsub.v1.IngestionFailureEvent.SchemaViolationReason schema_violation_reason = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestionFailureEvent.SchemaViolationReason](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.SchemaViolationReason)` | The schemaViolationReason.  
  
### getSchemaViolationReasonOrBuilder()
    
    
    public abstract IngestionFailureEvent.SchemaViolationReasonOrBuilder getSchemaViolationReasonOrBuilder()

Optional. The Pub/Sub message failed schema validation.

` .google.pubsub.v1.IngestionFailureEvent.SchemaViolationReason schema_violation_reason = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[IngestionFailureEvent.SchemaViolationReasonOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionFailureEvent.SchemaViolationReasonOrBuilder)` |   
  
### hasApiViolationReason()
    
    
    public abstract boolean hasApiViolationReason()

Optional. The Pub/Sub API limits prevented the desired message from being published.

` .google.pubsub.v1.IngestionFailureEvent.ApiViolationReason api_violation_reason = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the apiViolationReason field is set.  
  
### hasMessageTransformationFailureReason()
    
    
    public abstract boolean hasMessageTransformationFailureReason()

Optional. Failure encountered when applying a message transformation to the Pub/Sub message.

` .google.pubsub.v1.IngestionFailureEvent.MessageTransformationFailureReason message_transformation_failure_reason = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the messageTransformationFailureReason field is set.  
  
### hasSchemaViolationReason()
    
    
    public abstract boolean hasSchemaViolationReason()

Optional. The Pub/Sub message failed schema validation.

` .google.pubsub.v1.IngestionFailureEvent.SchemaViolationReason schema_violation_reason = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the schemaViolationReason field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
