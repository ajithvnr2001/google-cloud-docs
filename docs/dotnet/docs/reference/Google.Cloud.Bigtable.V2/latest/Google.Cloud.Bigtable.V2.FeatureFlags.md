---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.FeatureFlags
title: Google Bigtable v2 API - Class FeatureFlags (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:47.018487+00:00
---

# Google Bigtable v2 API - Class FeatureFlags (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.FeatureFlags

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class FeatureFlags (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class FeatureFlags : IMessage<FeatureFlags>, IEquatable<FeatureFlags>, IDeepCloneable<FeatureFlags>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class FeatureFlags.

Feature flags supported or enabled by a client. This is intended to be sent as part of request metadata to assure the server that certain behaviors are safe to enable. This proto is meant to be serialized and websafe-base64 encoded under the `bigtable-features` metadata key. The value will remain constant for the lifetime of a client and due to HTTP2's HPACK compression, the request overhead will be tiny. This is an internal implementation detail and should not be used by end users directly.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FeatureFlags

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[FeatureFlags](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.FeatureFlags), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FeatureFlags](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.FeatureFlags), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[FeatureFlags](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.FeatureFlags), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### FeatureFlags()
    
    
    public FeatureFlags()

### FeatureFlags(FeatureFlags)
    
    
    public FeatureFlags(FeatureFlags other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FeatureFlags](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.FeatureFlags)`  
  
  
## Properties 

### ClientSideMetricsEnabled
    
    
    public bool ClientSideMetricsEnabled { get; set; }

Notify the server that the client has client side metrics enabled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### DirectAccessRequested
    
    
    public bool DirectAccessRequested { get; set; }

Notify the server that the client explicitly opted in for Direct Access.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LastScannedRowResponses
    
    
    public bool LastScannedRowResponses { get; set; }

Notify the server that the client supports the last_scanned_row field in ReadRowsResponse for long-running scans.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MicrosecondTimestamp
    
    
    public bool MicrosecondTimestamp { get; set; }

Optional. Indicates whether the client supports microsecond precision timestamps.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MutateRowsRateLimit
    
    
    public bool MutateRowsRateLimit { get; set; }

Notify the server that the client enables batch write flow control by requesting RateLimitInfo from MutateRowsResponse. Due to technical reasons, this disables partial retries.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MutateRowsRateLimit2
    
    
    public bool MutateRowsRateLimit2 { get; set; }

Notify the server that the client enables batch write flow control by requesting RateLimitInfo from MutateRowsResponse. With partial retries enabled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PeerInfo
    
    
    public bool PeerInfo { get; set; }

If the client can support using BigtablePeerInfo.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RetryInfo
    
    
    public bool RetryInfo { get; set; }

Notify the server that the client supports using retry info back off durations to retry requests with.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ReverseScans
    
    
    public bool ReverseScans { get; set; }

Notify the server that the client supports reverse scans. The server will reject ReadRowsRequests with the reverse bit set when this is absent.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RoutingCookie
    
    
    public bool RoutingCookie { get; set; }

Notify the server that the client supports using encoded routing cookie strings to retry requests with.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SessionsCompatible
    
    
    public bool SessionsCompatible { get; set; }

Indicates whether the client supports the Bigtable Sessions API.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SessionsRequired
    
    
    public bool SessionsRequired { get; set; }

Internal flag to force sessions for internal projects.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### TrafficDirectorEnabled
    
    
    public bool TrafficDirectorEnabled { get; set; }

Notify the server that the client using Traffic Director endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
