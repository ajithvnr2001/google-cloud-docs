---
url: https://docs.cloud.google.com/java/docs/reference/grpc-gcp/latest/com.google.cloud.grpc.GcpManagedChannel.ChannelRef
title: Class GcpManagedChannel.ChannelRef (1.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:03.938378+00:00
---

# Class GcpManagedChannel.ChannelRef (1.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/grpc-gcp/latest/com.google.cloud.grpc.GcpManagedChannel.ChannelRef

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GcpManagedChannel.ChannelRef (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.13.0  1.12.0  1.11.0 
    
    
    protected class GcpManagedChannel.ChannelRef

A wrapper of real grpc channel, it provides helper functions to calculate affinity counts and active streams count.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GcpManagedChannel.ChannelRef

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

### ChannelRef(ManagedChannel channel)
    
    
    protected ChannelRef(ManagedChannel channel)

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.ManagedChannel`  
  
  
### ChannelRef(ManagedChannel channel, int affinityCount, int activeStreamsCount)
    
    
    protected ChannelRef(ManagedChannel channel, int affinityCount, int activeStreamsCount)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.ManagedChannel`  
  
`affinityCount` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`activeStreamsCount` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
## Methods 

### activeStreamsCountDecr(long startNanos, Status status, boolean fromClientSide)
    
    
    protected void activeStreamsCountDecr(long startNanos, Status status, boolean fromClientSide)

**Parameters**  
---  
**Name** | **Description**  
`startNanos` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`status` | `io.grpc.Status`  
  
`fromClientSide` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### activeStreamsCountIncr()
    
    
    protected void activeStreamsCountIncr()

### affinityCountDecr()
    
    
    protected void affinityCountDecr()

### affinityCountIncr()
    
    
    protected void affinityCountIncr()

### getActiveStreamsCount()
    
    
    protected int getActiveStreamsCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAffinityCount()
    
    
    protected int getAffinityCount()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAndResetErrCalls()
    
    
    protected long getAndResetErrCalls()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAndResetOkCalls()
    
    
    protected long getAndResetOkCalls()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getChannel()
    
    
    protected ManagedChannel getChannel()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ManagedChannel` |   
  
### getCreatedNanos()
    
    
    protected long getCreatedNanos()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getId()
    
    
    protected int getId()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLastActivityNanos()
    
    
    protected long getLastActivityNanos()

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPickerLoad()
    
    
    protected int getPickerLoad()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getState()
    
    
    protected ConnectivityState getState()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ConnectivityState` |   
  
### isActive()
    
    
    protected boolean isActive()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### messageReceived()
    
    
    protected void messageReceived()

### resetAffinityCount()
    
    
    protected void resetAffinityCount()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
