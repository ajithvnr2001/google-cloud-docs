---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration
title: Google Bigtable v2 API - Class SessionClientConfiguration.Types.ChannelPoolConfiguration (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:08.777320+00:00
---

# Google Bigtable v2 API - Class SessionClientConfiguration.Types.ChannelPoolConfiguration (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class SessionClientConfiguration.Types.ChannelPoolConfiguration (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class SessionClientConfiguration.Types.ChannelPoolConfiguration : IMessage<SessionClientConfiguration.Types.ChannelPoolConfiguration>, IEquatable<SessionClientConfiguration.Types.ChannelPoolConfiguration>, IDeepCloneable<SessionClientConfiguration.Types.ChannelPoolConfiguration>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class SessionClientConfiguration.Types.ChannelPoolConfiguration.

Configuration for the channel pool.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SessionClientConfiguration.Types.ChannelPoolConfiguration

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### ChannelPoolConfiguration()
    
    
    public ChannelPoolConfiguration()

### ChannelPoolConfiguration(ChannelPoolConfiguration)
    
    
    public ChannelPoolConfiguration(SessionClientConfiguration.Types.ChannelPoolConfiguration other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration)`  
  
  
## Properties 

### CloudPathOnly
    
    
    public SessionClientConfiguration.Types.ChannelPoolConfiguration.Types.CloudPathOnly CloudPathOnly { get; set; }

CloudPath only.

**Property Value**  
---  
**Type** | **Description**  
`[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration.Types)[CloudPathOnly](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration.Types.CloudPathOnly)` |   
  
### DirectAccessOnly
    
    
    public SessionClientConfiguration.Types.ChannelPoolConfiguration.Types.DirectAccessOnly DirectAccessOnly { get; set; }

DirectAccess only.

**Property Value**  
---  
**Type** | **Description**  
`[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration.Types)[DirectAccessOnly](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration.Types.DirectAccessOnly)` |   
  
### DirectAccessWithFallback
    
    
    public SessionClientConfiguration.Types.ChannelPoolConfiguration.Types.DirectAccessWithFallback DirectAccessWithFallback { get; set; }

DirectAccess with a fallback to CloudPath.

**Property Value**  
---  
**Type** | **Description**  
`[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration.Types)[DirectAccessWithFallback](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration.Types.DirectAccessWithFallback)` |   
  
### MaxServerCount
    
    
    public int MaxServerCount { get; set; }

The maximum number of distinct servers to connect to in the channel pool. The client will ensure that the channel pool will have at most this many distinct servers.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MinServerCount
    
    
    public int MinServerCount { get; set; }

The minimum number of distcint servers to connect to in the channel pool. The client will ensure that the channel pool will have at least this many distinct servers, but may have multiple channels connected to the same server (e.g. the client may have M channels on N machines, where M > N).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ModeCase
    
    
    public SessionClientConfiguration.Types.ChannelPoolConfiguration.ModeOneofCase ModeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration)[ModeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration.ModeOneofCase)` |   
  
### PerServerSessionCount
    
    
    public int PerServerSessionCount { get; set; }

Soft maximum for how many sessions are allowed per server. Normally, the client will ensure that it does not host more than this count of sessions per server, unless there are other limits encountered (e.g. the connected servers is already at max_servers).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
