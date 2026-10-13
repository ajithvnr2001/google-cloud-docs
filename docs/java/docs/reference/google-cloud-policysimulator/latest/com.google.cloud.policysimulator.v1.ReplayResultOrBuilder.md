---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ReplayResultOrBuilder
title: Interface ReplayResultOrBuilder (0.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:32.849762+00:00
---

# Interface ReplayResultOrBuilder (0.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ReplayResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReplayResultOrBuilder (0.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.78.0 (latest)  0.74.0  0.73.0  0.72.0  0.70.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.59.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ReplayResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccessTuple()
    
    
    public abstract AccessTuple getAccessTuple()

The access tuple that was replayed. This field includes information about the principal, resource, and permission that were involved in the access attempt.

`.google.cloud.policysimulator.v1.AccessTuple access_tuple = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AccessTuple](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.AccessTuple)` | The accessTuple.  
  
### getAccessTupleOrBuilder()
    
    
    public abstract AccessTupleOrBuilder getAccessTupleOrBuilder()

The access tuple that was replayed. This field includes information about the principal, resource, and permission that were involved in the access attempt.

`.google.cloud.policysimulator.v1.AccessTuple access_tuple = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AccessTupleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.AccessTupleOrBuilder)` |   
  
### getDiff()
    
    
    public abstract ReplayDiff getDiff()

The difference between the principal's access under the current (baseline) policies and the principal's access under the proposed (simulated) policies.

This field is only included for access tuples that were successfully replayed and had different results under the current policies and the proposed policies.

`.google.cloud.policysimulator.v1.ReplayDiff diff = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ReplayDiff](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ReplayDiff)` | The diff.  
  
### getDiffOrBuilder()
    
    
    public abstract ReplayDiffOrBuilder getDiffOrBuilder()

The difference between the principal's access under the current (baseline) policies and the principal's access under the proposed (simulated) policies.

This field is only included for access tuples that were successfully replayed and had different results under the current policies and the proposed policies.

`.google.cloud.policysimulator.v1.ReplayDiff diff = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ReplayDiffOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ReplayDiffOrBuilder)` |   
  
### getError()
    
    
    public abstract Status getError()

The error that caused the access tuple replay to fail.

This field is only included for access tuples that were not replayed successfully.

`.google.rpc.Status error = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

The error that caused the access tuple replay to fail.

This field is only included for access tuples that were not replayed successfully.

`.google.rpc.Status error = 6;`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getLastSeenDate()
    
    
    public abstract Date getLastSeenDate()

The latest date this access tuple was seen in the logs.

`.google.type.Date last_seen_date = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Date` | The lastSeenDate.  
  
### getLastSeenDateOrBuilder()
    
    
    public abstract DateOrBuilder getLastSeenDateOrBuilder()

The latest date this access tuple was seen in the logs.

`.google.type.Date last_seen_date = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.DateOrBuilder` |   
  
### getName()
    
    
    public abstract String getName()

The resource name of the `ReplayResult`, in the following format:

`{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}/results/{replay-result-id}`, where `{resource-id}` is the ID of the project, folder, or organization that owns the Replay.

Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36/results/1234`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The resource name of the `ReplayResult`, in the following format:

`{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}/results/{replay-result-id}`, where `{resource-id}` is the ID of the project, folder, or organization that owns the Replay.

Example: `projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36/results/1234`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getParent()
    
    
    public abstract String getParent()

The Replay that the access tuple was included in.

`string parent = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

The Replay that the access tuple was included in.

`string parent = 2 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getResultCase()
    
    
    public abstract ReplayResult.ResultCase getResultCase()

**Returns**  
---  
**Type** | **Description**  
`[ReplayResult.ResultCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ReplayResult.ResultCase)` |   
  
### hasAccessTuple()
    
    
    public abstract boolean hasAccessTuple()

The access tuple that was replayed. This field includes information about the principal, resource, and permission that were involved in the access attempt.

`.google.cloud.policysimulator.v1.AccessTuple access_tuple = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the accessTuple field is set.  
  
### hasDiff()
    
    
    public abstract boolean hasDiff()

The difference between the principal's access under the current (baseline) policies and the principal's access under the proposed (simulated) policies.

This field is only included for access tuples that were successfully replayed and had different results under the current policies and the proposed policies.

`.google.cloud.policysimulator.v1.ReplayDiff diff = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diff field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

The error that caused the access tuple replay to fail.

This field is only included for access tuples that were not replayed successfully.

`.google.rpc.Status error = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasLastSeenDate()
    
    
    public abstract boolean hasLastSeenDate()

The latest date this access tuple was seen in the logs.

`.google.type.Date last_seen_date = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastSeenDate field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
