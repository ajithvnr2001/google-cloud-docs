---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.SessionPoolConfiguration
title: Google Bigtable v2 API - Class SessionClientConfiguration.Types.SessionPoolConfiguration (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:09.887095+00:00
---

# Google Bigtable v2 API - Class SessionClientConfiguration.Types.SessionPoolConfiguration (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.SessionPoolConfiguration

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class SessionClientConfiguration.Types.SessionPoolConfiguration (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class SessionClientConfiguration.Types.SessionPoolConfiguration : IMessage<SessionClientConfiguration.Types.SessionPoolConfiguration>, IEquatable<SessionClientConfiguration.Types.SessionPoolConfiguration>, IDeepCloneable<SessionClientConfiguration.Types.SessionPoolConfiguration>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class SessionClientConfiguration.Types.SessionPoolConfiguration.

Configuration for the session pools. Session pools are tied to a scope like a table, an app profile, and a permission.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SessionClientConfiguration.Types.SessionPoolConfiguration

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[SessionPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.SessionPoolConfiguration), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[SessionPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.SessionPoolConfiguration), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[SessionPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.SessionPoolConfiguration), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### SessionPoolConfiguration()
    
    
    public SessionPoolConfiguration()

### SessionPoolConfiguration(SessionPoolConfiguration)
    
    
    public SessionPoolConfiguration(SessionClientConfiguration.Types.SessionPoolConfiguration other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[SessionPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.SessionPoolConfiguration)`  
  
  
## Properties 

### ConsecutiveSessionFailureThreshold
    
    
    public int ConsecutiveSessionFailureThreshold { get; set; }

A threshold for cancelling all pending vRPCs based on how many consecutive session establishment errors have been observed. The client will eagerly cancel queued vRPCs after this threshold is met to avoid them waiting their entire deadlines before terminating (while waiting for any session to establish to actually send the vRPC).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Headroom
    
    
    public float Headroom { get; set; }

Fraction of idle sessions to keep in order to manage an increase in requests-in-flight. For example, a headroom of 0.5 will keep enough sessions to deal with a 50% increase in QPS.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### LoadBalancingOptions
    
    
    public LoadBalancingOptions LoadBalancingOptions { get; set; }

How to balance vRPC load over connections to AFEs.

Set only if session_load or session_diversion_configuration indicates that there will be some session traffic.

**Property Value**  
---  
**Type** | **Description**  
`[LoadBalancingOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.LoadBalancingOptions)` |   
  
### MaxSessionCount
    
    
    public int MaxSessionCount { get; set; }

The maximum number of sessions for a given scope.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MinSessionCount
    
    
    public int MinSessionCount { get; set; }

The minimum number of sessions for a given scope.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### NewSessionCreationBudget
    
    
    public int NewSessionCreationBudget { get; set; }

How many concurrent session establishments are allowed. The client will hold onto a count against this budget whenever it is establishing a new session, and release that count once the session is successfully established or failed to establish.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### NewSessionCreationPenalty
    
    
    public Duration NewSessionCreationPenalty { get; set; }

How long to penalize the creation budget for a failed session creation attempt.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### NewSessionQueueLength
    
    
    public int NewSessionQueueLength { get; set; }

Number of vRPCs that can be queued per starting session.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SoftSessionCloseBudget
    
    
    public int SoftSessionCloseBudget { get; set; }

How many concurrent session closures are allowed. The client will hold onto a count against this budget whenever it is closing a session, and release that count once the session is successfully established or failed to establish.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
