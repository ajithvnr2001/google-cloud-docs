---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats.WindowStatsOrBuilder
title: Interface ClientStats.WindowStatsOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:01.611032+00:00
---

# Interface ClientStats.WindowStatsOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats.WindowStatsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClientStats.WindowStatsOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static interface ClientStats.WindowStatsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAvgResponseLatencyMillis()
    
    
    public abstract long getAvgResponseLatencyMillis()

Optional. The average response latency observed in the window, expressed in milliseconds.

` optional int64 avg_response_latency_millis = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The avgResponseLatencyMillis.  
  
### getBytesSentCount()
    
    
    public abstract long getBytesSentCount()

Optional. How many bytes were sent in the window.

`optional int64 bytes_sent_count = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesSentCount.  
  
### getLongestWaitNoResponseMillis()
    
    
    public abstract long getLongestWaitNoResponseMillis()

Optional. The longest time spent waiting without receiving a response in the window. This could exceed max_response_latency_millis because the latter is evaluated only when a response is received. Expressed in milliseconds.

` optional int64 longest_wait_no_response_millis = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The longestWaitNoResponseMillis.  
  
### getMaxResponseLatencyMillis()
    
    
    public abstract long getMaxResponseLatencyMillis()

Optional. The maximum response latency observed in the window, expressed in milliseconds.

` optional int64 max_response_latency_millis = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxResponseLatencyMillis.  
  
### getRequestsSentCount()
    
    
    public abstract long getRequestsSentCount()

Optional. How many requests were sent in the window.

`optional int64 requests_sent_count = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The requestsSentCount.  
  
### getResponsesReceivedCount()
    
    
    public abstract long getResponsesReceivedCount()

Optional. How many responses were received in the window.

`optional int64 responses_received_count = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The responsesReceivedCount.  
  
### getWindowMillis()
    
    
    public abstract long getWindowMillis()

Optional. Duration of the window interval for which these stats are aggregated, expressed in milliseconds.

`optional int64 window_millis = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The windowMillis.  
  
### getWindowStartTimeEpochMillis()
    
    
    public abstract long getWindowStartTimeEpochMillis()

Optional. Start time of the window interval for which these stats are aggregated, expressed in epoch milliseconds.

` optional int64 window_start_time_epoch_millis = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The windowStartTimeEpochMillis.  
  
### hasAvgResponseLatencyMillis()
    
    
    public abstract boolean hasAvgResponseLatencyMillis()

Optional. The average response latency observed in the window, expressed in milliseconds.

` optional int64 avg_response_latency_millis = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avgResponseLatencyMillis field is set.  
  
### hasBytesSentCount()
    
    
    public abstract boolean hasBytesSentCount()

Optional. How many bytes were sent in the window.

`optional int64 bytes_sent_count = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bytesSentCount field is set.  
  
### hasLongestWaitNoResponseMillis()
    
    
    public abstract boolean hasLongestWaitNoResponseMillis()

Optional. The longest time spent waiting without receiving a response in the window. This could exceed max_response_latency_millis because the latter is evaluated only when a response is received. Expressed in milliseconds.

` optional int64 longest_wait_no_response_millis = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the longestWaitNoResponseMillis field is set.  
  
### hasMaxResponseLatencyMillis()
    
    
    public abstract boolean hasMaxResponseLatencyMillis()

Optional. The maximum response latency observed in the window, expressed in milliseconds.

` optional int64 max_response_latency_millis = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxResponseLatencyMillis field is set.  
  
### hasRequestsSentCount()
    
    
    public abstract boolean hasRequestsSentCount()

Optional. How many requests were sent in the window.

`optional int64 requests_sent_count = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the requestsSentCount field is set.  
  
### hasResponsesReceivedCount()
    
    
    public abstract boolean hasResponsesReceivedCount()

Optional. How many responses were received in the window.

`optional int64 responses_received_count = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the responsesReceivedCount field is set.  
  
### hasWindowMillis()
    
    
    public abstract boolean hasWindowMillis()

Optional. Duration of the window interval for which these stats are aggregated, expressed in milliseconds.

`optional int64 window_millis = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowMillis field is set.  
  
### hasWindowStartTimeEpochMillis()
    
    
    public abstract boolean hasWindowStartTimeEpochMillis()

Optional. Start time of the window interval for which these stats are aggregated, expressed in epoch milliseconds.

` optional int64 window_start_time_epoch_millis = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowStartTimeEpochMillis field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
