---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.PscAutoConnectionOrBuilder
title: Interface PscAutoConnectionOrBuilder (0.71.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:21.128894+00:00
---

# Interface PscAutoConnectionOrBuilder (0.71.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.PscAutoConnectionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PscAutoConnectionOrBuilder (0.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.71.0 (latest)  0.67.0  0.66.0  0.65.0  0.63.0  0.60.0  0.59.0  0.57.0  0.55.0  0.54.0  0.52.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.36.0  0.35.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface PscAutoConnectionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAddress()
    
    
    public abstract String getAddress()

Output only. The IP allocated on the consumer network for the PSC forwarding rule.

` string address = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The address.  
  
### getAddressBytes()
    
    
    public abstract ByteString getAddressBytes()

Output only. The IP allocated on the consumer network for the PSC forwarding rule.

` string address = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for address.  
  
### getConnectionType()
    
    
    public abstract ConnectionType getConnectionType()

Output only. Type of the PSC connection.

` .google.cloud.redis.cluster.v1beta1.ConnectionType connection_type = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ConnectionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.ConnectionType)` | The connectionType.  
  
### getConnectionTypeValue()
    
    
    public abstract int getConnectionTypeValue()

Output only. Type of the PSC connection.

` .google.cloud.redis.cluster.v1beta1.ConnectionType connection_type = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for connectionType.  
  
### getForwardingRule()
    
    
    public abstract String getForwardingRule()

Output only. The URI of the consumer side forwarding rule. Example: projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.

` string forwarding_rule = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The forwardingRule.  
  
### getForwardingRuleBytes()
    
    
    public abstract ByteString getForwardingRuleBytes()

Output only. The URI of the consumer side forwarding rule. Example: projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}.

` string forwarding_rule = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for forwardingRule.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_id}.

` string network = 5 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

Required. The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_id}.

` string network = 5 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getProjectId()
    
    
    public abstract String getProjectId()

Required. The consumer project_id where the forwarding rule is created from.

`string project_id = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The projectId.  
  
### getProjectIdBytes()
    
    
    public abstract ByteString getProjectIdBytes()

Required. The consumer project_id where the forwarding rule is created from.

`string project_id = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for projectId.  
  
### getPscConnectionId()
    
    
    public abstract String getPscConnectionId()

Output only. The PSC connection id of the forwarding rule connected to the service attachment.

`string psc_connection_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pscConnectionId.  
  
### getPscConnectionIdBytes()
    
    
    public abstract ByteString getPscConnectionIdBytes()

Output only. The PSC connection id of the forwarding rule connected to the service attachment.

`string psc_connection_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pscConnectionId.  
  
### getPscConnectionStatus()
    
    
    public abstract PscConnectionStatus getPscConnectionStatus()

Output only. The status of the PSC connection. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.

` .google.cloud.redis.cluster.v1beta1.PscConnectionStatus psc_connection_status = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PscConnectionStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-redis-cluster/latest/com.google.cloud.redis.cluster.v1beta1.PscConnectionStatus)` | The pscConnectionStatus.  
  
### getPscConnectionStatusValue()
    
    
    public abstract int getPscConnectionStatusValue()

Output only. The status of the PSC connection. Please note that this value is updated periodically. Please use Private Service Connect APIs for the latest status.

` .google.cloud.redis.cluster.v1beta1.PscConnectionStatus psc_connection_status = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for pscConnectionStatus.  
  
### getServiceAttachment()
    
    
    public abstract String getServiceAttachment()

Output only. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.

` string service_attachment = 6 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAttachment.  
  
### getServiceAttachmentBytes()
    
    
    public abstract ByteString getServiceAttachmentBytes()

Output only. The service attachment which is the target of the PSC connection, in the form of projects/{project-id}/regions/{region}/serviceAttachments/{service-attachment-id}.

` string service_attachment = 6 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAttachment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
