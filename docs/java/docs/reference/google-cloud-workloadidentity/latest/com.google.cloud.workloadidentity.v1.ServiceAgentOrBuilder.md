---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadidentity/latest/com.google.cloud.workloadidentity.v1.ServiceAgentOrBuilder
title: Interface ServiceAgentOrBuilder (0.4.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:59.492992+00:00
---

# Interface ServiceAgentOrBuilder (0.4.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadidentity/latest/com.google.cloud.workloadidentity.v1.ServiceAgentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServiceAgentOrBuilder (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface ServiceAgentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContainer()
    
    
    public abstract String getContainer()

Optional. Name of the container that the service agent is associated with. For example:

  * projects/1234
  * folders/1234
  * organizations/2344



` string container = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The container.  
  
### getContainerBytes()
    
    
    public abstract ByteString getContainerBytes()

Optional. Name of the container that the service agent is associated with. For example:

  * projects/1234
  * folders/1234
  * organizations/2344



` string container = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for container.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The name of the service agent resource

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The name of the service agent resource

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPrincipal()
    
    
    public abstract String getPrincipal()

Optional. The principal identifier for the service agent. This identifier is used in allow policies to grant access to the service agent.

`string principal = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The principal.  
  
### getPrincipalBytes()
    
    
    public abstract ByteString getPrincipalBytes()

Optional. The principal identifier for the service agent. This identifier is used in allow policies to grant access to the service agent.

`string principal = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for principal.  
  
### getRole()
    
    
    public abstract String getRole()

Optional. The role that should be granted to service agent on consumer project, if any. For example, "roles/aiplatform.serviceAgent".

`string role = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The role.  
  
### getRoleBytes()
    
    
    public abstract ByteString getRoleBytes()

Optional. The role that should be granted to service agent on consumer project, if any. For example, "roles/aiplatform.serviceAgent".

`string role = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for role.  
  
### getServiceProducer()
    
    
    public abstract String getServiceProducer()

Optional. The service the agent belongs to. For example, bigquery.googleapis.com

`string service_producer = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceProducer.  
  
### getServiceProducerBytes()
    
    
    public abstract ByteString getServiceProducerBytes()

Optional. The service the agent belongs to. For example, bigquery.googleapis.com

`string service_producer = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceProducer.  
  
### getState()
    
    
    public abstract ServiceAgent.State getState()

Output only. Service agent state.

` .google.cloud.workloadidentity.v1.ServiceAgent.State state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceAgent.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadidentity/latest/com.google.cloud.workloadidentity.v1.ServiceAgent.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. Service agent state.

` .google.cloud.workloadidentity.v1.ServiceAgent.State state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
