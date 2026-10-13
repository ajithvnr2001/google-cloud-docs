---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetailsOrBuilder
title: Interface ProbingDetailsOrBuilder (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:32.936216+00:00
---

# Interface ProbingDetailsOrBuilder (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProbingDetailsOrBuilder (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.1.10 
    
    
    public interface ProbingDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAbortCause()
    
    
    public abstract ProbingDetails.ProbingAbortCause getAbortCause()

The reason probing was aborted.

`.google.cloud.networkmanagement.v1.ProbingDetails.ProbingAbortCause abort_cause = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ProbingDetails.ProbingAbortCause](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetails.ProbingAbortCause)` | The abortCause.  
  
### getAbortCauseValue()
    
    
    public abstract int getAbortCauseValue()

The reason probing was aborted.

`.google.cloud.networkmanagement.v1.ProbingDetails.ProbingAbortCause abort_cause = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for abortCause.  
  
### getDestinationEgressLocation()
    
    
    public abstract ProbingDetails.EdgeLocation getDestinationEgressLocation()

The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field _must not_ be used as an indication that the destination is part of the Google network.

` .google.cloud.networkmanagement.v1.ProbingDetails.EdgeLocation destination_egress_location = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ProbingDetails.EdgeLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetails.EdgeLocation)` | The destinationEgressLocation.  
  
### getDestinationEgressLocationOrBuilder()
    
    
    public abstract ProbingDetails.EdgeLocationOrBuilder getDestinationEgressLocationOrBuilder()

The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field _must not_ be used as an indication that the destination is part of the Google network.

` .google.cloud.networkmanagement.v1.ProbingDetails.EdgeLocation destination_egress_location = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ProbingDetails.EdgeLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetails.EdgeLocationOrBuilder)` |   
  
### getEdgeResponses(int index)
    
    
    public abstract ProbingDetails.SingleEdgeResponse getEdgeResponses(int index)

Probing results for all edge devices.

` repeated .google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponse edge_responses = 10; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProbingDetails.SingleEdgeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponse)` |   
  
### getEdgeResponsesCount()
    
    
    public abstract int getEdgeResponsesCount()

Probing results for all edge devices.

` repeated .google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponse edge_responses = 10; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getEdgeResponsesList()
    
    
    public abstract List<ProbingDetails.SingleEdgeResponse> getEdgeResponsesList()

Probing results for all edge devices.

` repeated .google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponse edge_responses = 10; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SingleEdgeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponse)>` |   
  
### getEdgeResponsesOrBuilder(int index)
    
    
    public abstract ProbingDetails.SingleEdgeResponseOrBuilder getEdgeResponsesOrBuilder(int index)

Probing results for all edge devices.

` repeated .google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponse edge_responses = 10; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProbingDetails.SingleEdgeResponseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponseOrBuilder)` |   
  
### getEdgeResponsesOrBuilderList()
    
    
    public abstract List<? extends ProbingDetails.SingleEdgeResponseOrBuilder> getEdgeResponsesOrBuilderList()

Probing results for all edge devices.

` repeated .google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponse edge_responses = 10; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.networkmanagement.v1.ProbingDetails.SingleEdgeResponseOrBuilder>` |   
  
### getEndpointInfo()
    
    
    public abstract EndpointInfo getEndpointInfo()

The source and destination endpoints derived from the test input and used for active probing.

`.google.cloud.networkmanagement.v1.EndpointInfo endpoint_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[EndpointInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.EndpointInfo)` | The endpointInfo.  
  
### getEndpointInfoOrBuilder()
    
    
    public abstract EndpointInfoOrBuilder getEndpointInfoOrBuilder()

The source and destination endpoints derived from the test input and used for active probing.

`.google.cloud.networkmanagement.v1.EndpointInfo endpoint_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[EndpointInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.EndpointInfoOrBuilder)` |   
  
### getError()
    
    
    public abstract Status getError()

Details about an internal failure or the cancellation of active probing.

`.google.rpc.Status error = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Details about an internal failure or the cancellation of active probing.

`.google.rpc.Status error = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getProbedAllDevices()
    
    
    public abstract boolean getProbedAllDevices()

Whether all relevant edge devices were probed.

`bool probed_all_devices = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The probedAllDevices.  
  
### getProbingLatency()
    
    
    public abstract LatencyDistribution getProbingLatency()

Latency as measured by active probing in one direction: from the source to the destination endpoint.

`.google.cloud.networkmanagement.v1.LatencyDistribution probing_latency = 8;`

**Returns**  
---  
**Type** | **Description**  
`[LatencyDistribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.LatencyDistribution)` | The probingLatency.  
  
### getProbingLatencyOrBuilder()
    
    
    public abstract LatencyDistributionOrBuilder getProbingLatencyOrBuilder()

Latency as measured by active probing in one direction: from the source to the destination endpoint.

`.google.cloud.networkmanagement.v1.LatencyDistribution probing_latency = 8;`

**Returns**  
---  
**Type** | **Description**  
`[LatencyDistributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.LatencyDistributionOrBuilder)` |   
  
### getResult()
    
    
    public abstract ProbingDetails.ProbingResult getResult()

The overall result of active probing.

`.google.cloud.networkmanagement.v1.ProbingDetails.ProbingResult result = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ProbingDetails.ProbingResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1.ProbingDetails.ProbingResult)` | The result.  
  
### getResultValue()
    
    
    public abstract int getResultValue()

The overall result of active probing.

`.google.cloud.networkmanagement.v1.ProbingDetails.ProbingResult result = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for result.  
  
### getSentProbeCount()
    
    
    public abstract int getSentProbeCount()

Number of probes sent.

`int32 sent_probe_count = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sentProbeCount.  
  
### getSuccessfulProbeCount()
    
    
    public abstract int getSuccessfulProbeCount()

Number of probes that reached the destination.

`int32 successful_probe_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The successfulProbeCount.  
  
### getVerifyTime()
    
    
    public abstract Timestamp getVerifyTime()

The time that reachability was assessed through active probing.

`.google.protobuf.Timestamp verify_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The verifyTime.  
  
### getVerifyTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getVerifyTimeOrBuilder()

The time that reachability was assessed through active probing.

`.google.protobuf.Timestamp verify_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasDestinationEgressLocation()
    
    
    public abstract boolean hasDestinationEgressLocation()

The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field _must not_ be used as an indication that the destination is part of the Google network.

` .google.cloud.networkmanagement.v1.ProbingDetails.EdgeLocation destination_egress_location = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the destinationEgressLocation field is set.  
  
### hasEndpointInfo()
    
    
    public abstract boolean hasEndpointInfo()

The source and destination endpoints derived from the test input and used for active probing.

`.google.cloud.networkmanagement.v1.EndpointInfo endpoint_info = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endpointInfo field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

Details about an internal failure or the cancellation of active probing.

`.google.rpc.Status error = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasProbingLatency()
    
    
    public abstract boolean hasProbingLatency()

Latency as measured by active probing in one direction: from the source to the destination endpoint.

`.google.cloud.networkmanagement.v1.LatencyDistribution probing_latency = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the probingLatency field is set.  
  
### hasVerifyTime()
    
    
    public abstract boolean hasVerifyTime()

The time that reachability was assessed through active probing.

`.google.protobuf.Timestamp verify_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the verifyTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
