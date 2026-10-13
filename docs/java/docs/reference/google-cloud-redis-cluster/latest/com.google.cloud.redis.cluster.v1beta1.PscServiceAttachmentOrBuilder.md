---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.PscServiceAttachmentOrBuilder
title: Interface PscServiceAttachmentOrBuilder (0.71.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:14.270196+00:00
---

# Interface PscServiceAttachmentOrBuilder (0.71.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.PscServiceAttachmentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PscServiceAttachmentOrBuilder (0.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.71.0 (latest)  0.67.0  0.66.0  0.65.0  0.63.0  0.60.0  0.59.0  0.57.0  0.55.0  0.54.0  0.52.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.36.0  0.35.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface PscServiceAttachmentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConnectionType()
    
    
    public abstract ConnectionType getConnectionType()

Output only. Type of a PSC connection targeting this service attachment.

` .google.cloud.redis.cluster.v1beta1.ConnectionType connection_type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ConnectionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ConnectionType)` | The connectionType.  
  
### getConnectionTypeValue()
    
    
    public abstract int getConnectionTypeValue()

Output only. Type of a PSC connection targeting this service attachment.

` .google.cloud.redis.cluster.v1beta1.ConnectionType connection_type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for connectionType.  
  
### getServiceAttachment()
    
    
    public abstract String getServiceAttachment()

Output only. Service attachment URI which your self-created PscConnection should use as target

`string service_attachment = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAttachment.  
  
### getServiceAttachmentBytes()
    
    
    public abstract ByteString getServiceAttachmentBytes()

Output only. Service attachment URI which your self-created PscConnection should use as target

`string service_attachment = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAttachment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
