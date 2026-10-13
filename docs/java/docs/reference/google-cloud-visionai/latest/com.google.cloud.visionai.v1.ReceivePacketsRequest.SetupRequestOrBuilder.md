---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceivePacketsRequest.SetupRequestOrBuilder
title: Interface ReceivePacketsRequest.SetupRequestOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:08.102421+00:00
---

# Interface ReceivePacketsRequest.SetupRequestOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceivePacketsRequest.SetupRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReceivePacketsRequest.SetupRequestOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ReceivePacketsRequest.SetupRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConsumerModeCase()
    
    
    public abstract ReceivePacketsRequest.SetupRequest.ConsumerModeCase getConsumerModeCase()

**Returns**  
---  
**Type** | **Description**  
`[ReceivePacketsRequest.SetupRequest.ConsumerModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ReceivePacketsRequest.SetupRequest.ConsumerModeCase)` |   
  
### getControlledReceiveMode()
    
    
    public abstract ControlledMode getControlledReceiveMode()

Options for configuring controlled mode.

`.google.cloud.visionai.v1.ControlledMode controlled_receive_mode = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ControlledMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ControlledMode)` | The controlledReceiveMode.  
  
### getControlledReceiveModeOrBuilder()
    
    
    public abstract ControlledModeOrBuilder getControlledReceiveModeOrBuilder()

Options for configuring controlled mode.

`.google.cloud.visionai.v1.ControlledMode controlled_receive_mode = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ControlledModeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.ControlledModeOrBuilder)` |   
  
### getEagerReceiveMode()
    
    
    public abstract EagerMode getEagerReceiveMode()

Options for configuring eager mode.

`.google.cloud.visionai.v1.EagerMode eager_receive_mode = 3;`

**Returns**  
---  
**Type** | **Description**  
`[EagerMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.EagerMode)` | The eagerReceiveMode.  
  
### getEagerReceiveModeOrBuilder()
    
    
    public abstract EagerModeOrBuilder getEagerReceiveModeOrBuilder()

Options for configuring eager mode.

`.google.cloud.visionai.v1.EagerMode eager_receive_mode = 3;`

**Returns**  
---  
**Type** | **Description**  
`[EagerModeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.EagerModeOrBuilder)` |   
  
### getHeartbeatInterval()
    
    
    public abstract Duration getHeartbeatInterval()

The maximum duration of server silence before the client determines the server unreachable.

The client must either receive a `Packet` or a heart beat message before this duration expires; otherwise, the client will automatically cancel the current connection and retry.

`.google.protobuf.Duration heartbeat_interval = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The heartbeatInterval.  
  
### getHeartbeatIntervalOrBuilder()
    
    
    public abstract DurationOrBuilder getHeartbeatIntervalOrBuilder()

The maximum duration of server silence before the client determines the server unreachable.

The client must either receive a `Packet` or a heart beat message before this duration expires; otherwise, the client will automatically cancel the current connection and retry.

`.google.protobuf.Duration heartbeat_interval = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getMetadata()
    
    
    public abstract RequestMetadata getMetadata()

The configurations that specify where packets are retrieved.

`.google.cloud.visionai.v1.RequestMetadata metadata = 1;`

**Returns**  
---  
**Type** | **Description**  
`[RequestMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.RequestMetadata)` | The metadata.  
  
### getMetadataOrBuilder()
    
    
    public abstract RequestMetadataOrBuilder getMetadataOrBuilder()

The configurations that specify where packets are retrieved.

`.google.cloud.visionai.v1.RequestMetadata metadata = 1;`

**Returns**  
---  
**Type** | **Description**  
`[RequestMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.RequestMetadataOrBuilder)` |   
  
### getReceiver()
    
    
    public abstract String getReceiver()

A name for the receiver to self-identify.

This is used to keep track of a receiver's read progress.

`string receiver = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The receiver.  
  
### getReceiverBytes()
    
    
    public abstract ByteString getReceiverBytes()

A name for the receiver to self-identify.

This is used to keep track of a receiver's read progress.

`string receiver = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for receiver.  
  
### getWritesDoneGracePeriod()
    
    
    public abstract Duration getWritesDoneGracePeriod()

The grace period after which a `writes_done_request` is issued, that a `WritesDone` is expected from the client.

The server is free to cancel the RPC should this expire.

A system default will be chosen if unset.

`.google.protobuf.Duration writes_done_grace_period = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The writesDoneGracePeriod.  
  
### getWritesDoneGracePeriodOrBuilder()
    
    
    public abstract DurationOrBuilder getWritesDoneGracePeriodOrBuilder()

The grace period after which a `writes_done_request` is issued, that a `WritesDone` is expected from the client.

The server is free to cancel the RPC should this expire.

A system default will be chosen if unset.

`.google.protobuf.Duration writes_done_grace_period = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### hasControlledReceiveMode()
    
    
    public abstract boolean hasControlledReceiveMode()

Options for configuring controlled mode.

`.google.cloud.visionai.v1.ControlledMode controlled_receive_mode = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the controlledReceiveMode field is set.  
  
### hasEagerReceiveMode()
    
    
    public abstract boolean hasEagerReceiveMode()

Options for configuring eager mode.

`.google.cloud.visionai.v1.EagerMode eager_receive_mode = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the eagerReceiveMode field is set.  
  
### hasHeartbeatInterval()
    
    
    public abstract boolean hasHeartbeatInterval()

The maximum duration of server silence before the client determines the server unreachable.

The client must either receive a `Packet` or a heart beat message before this duration expires; otherwise, the client will automatically cancel the current connection and retry.

`.google.protobuf.Duration heartbeat_interval = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the heartbeatInterval field is set.  
  
### hasMetadata()
    
    
    public abstract boolean hasMetadata()

The configurations that specify where packets are retrieved.

`.google.cloud.visionai.v1.RequestMetadata metadata = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metadata field is set.  
  
### hasWritesDoneGracePeriod()
    
    
    public abstract boolean hasWritesDoneGracePeriod()

The grace period after which a `writes_done_request` is issued, that a `WritesDone` is expected from the client.

The server is free to cancel the RPC should this expire.

A system default will be chosen if unset.

`.google.protobuf.Duration writes_done_grace_period = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the writesDoneGracePeriod field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
