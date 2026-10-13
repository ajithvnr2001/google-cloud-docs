---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.PscConnectionOrBuilder
title: Interface ServiceConnectionPolicy.PscConnectionOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:02.596062+00:00
---

# Interface ServiceConnectionPolicy.PscConnectionOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.PscConnectionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ServiceConnectionPolicy.PscConnectionOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.PscConnectionOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.PscConnectionOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.PscConnectionOrBuilder)


    
    
    public static interface ServiceConnectionPolicy.PscConnectionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConsumerAddress()
    
    
    public abstract String getConsumerAddress()

The resource reference of the consumer address.

`string consumer_address = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The consumerAddress.  
  
### getConsumerAddressBytes()
    
    
    public abstract ByteString getConsumerAddressBytes()

The resource reference of the consumer address.

`string consumer_address = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for consumerAddress.  
  
### getConsumerForwardingRule()
    
    
    public abstract String getConsumerForwardingRule()

The resource reference of the PSC Forwarding Rule within the consumer VPC.

`string consumer_forwarding_rule = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The consumerForwardingRule.  
  
### getConsumerForwardingRuleBytes()
    
    
    public abstract ByteString getConsumerForwardingRuleBytes()

The resource reference of the PSC Forwarding Rule within the consumer VPC.

`string consumer_forwarding_rule = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for consumerForwardingRule.  
  
### getConsumerTargetProject()
    
    
    public abstract String getConsumerTargetProject()

The project where the PSC connection is created.

`string consumer_target_project = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The consumerTargetProject.  
  
### getConsumerTargetProjectBytes()
    
    
    public abstract ByteString getConsumerTargetProjectBytes()

The project where the PSC connection is created.

`string consumer_target_project = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for consumerTargetProject.  
  
### getError()
    
    
    public abstract Status getError()

The most recent error during operating this connection.

`.google.rpc.Status error = 5;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

The most recent error during operating this connection.

`.google.rpc.Status error = 5;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getErrorType()
    
    
    public abstract ConnectionErrorType getErrorType()

The error type indicates whether the error is consumer facing, producer facing or system internal.

`.google.events.cloud.networkconnectivity.v1.ConnectionErrorType error_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ConnectionErrorType](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.networkconnectivity.v1.ConnectionErrorType)` | The errorType.  
  
### getErrorTypeValue()
    
    
    public abstract int getErrorTypeValue()

The error type indicates whether the error is consumer facing, producer facing or system internal.

`.google.events.cloud.networkconnectivity.v1.ConnectionErrorType error_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for errorType.  
  
### getGceOperation()
    
    
    public abstract String getGceOperation()

The last Compute Engine operation to setup PSC connection.

`string gce_operation = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gceOperation.  
  
### getGceOperationBytes()
    
    
    public abstract ByteString getGceOperationBytes()

The last Compute Engine operation to setup PSC connection.

`string gce_operation = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gceOperation.  
  
### getPscConnectionId()
    
    
    public abstract String getPscConnectionId()

The PSC connection id of the PSC forwarding rule.

`string psc_connection_id = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pscConnectionId.  
  
### getPscConnectionIdBytes()
    
    
    public abstract ByteString getPscConnectionIdBytes()

The PSC connection id of the PSC forwarding rule.

`string psc_connection_id = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pscConnectionId.  
  
### getState()
    
    
    public abstract ServiceConnectionPolicy.State getState()

State of the PSC Connection

`.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.State state = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionPolicy.State](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

State of the PSC Connection

`.google.events.cloud.networkconnectivity.v1.ServiceConnectionPolicy.State state = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasError()
    
    
    public abstract boolean hasError()

The most recent error during operating this connection.

`.google.rpc.Status error = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
