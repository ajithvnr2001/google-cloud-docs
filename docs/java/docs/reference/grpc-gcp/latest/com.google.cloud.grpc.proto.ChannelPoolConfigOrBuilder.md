---
url: https://docs.cloud.google.com/java/docs/reference/grpc-gcp/latest/com.google.cloud.grpc.proto.ChannelPoolConfigOrBuilder
title: Interface ChannelPoolConfigOrBuilder (1.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:12.907574+00:00
---

# Interface ChannelPoolConfigOrBuilder (1.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/grpc-gcp/latest/com.google.cloud.grpc.proto.ChannelPoolConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ChannelPoolConfigOrBuilder (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.13.0  1.12.0  1.11.0 
    
    
    public interface ChannelPoolConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIdleTimeout() (deprecated)
    
    
    public abstract long getIdleTimeout()

The idle timeout (seconds) of channels without bound affinity sessions.

`uint64 idle_timeout = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The idleTimeout.  
  
### getMaxConcurrentStreamsLowWatermark() (deprecated)
    
    
    public abstract int getMaxConcurrentStreamsLowWatermark()

The low watermark of max number of concurrent streams in a channel. New channel will be created once it get hit, until we reach the max size of the channel pool. Values outside of [0..100] will be ignored. 0 = always create a new channel until max size is reached.

`uint32 max_concurrent_streams_low_watermark = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxConcurrentStreamsLowWatermark.  
  
### getMaxSize() (deprecated)
    
    
    public abstract int getMaxSize()

The max number of channels in the pool.

`uint32 max_size = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxSize.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
