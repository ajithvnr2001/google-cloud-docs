---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration
title: Google Bigtable v2 API - Class SessionClientConfiguration (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:07.913596+00:00
---

# Google Bigtable v2 API - Class SessionClientConfiguration (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class SessionClientConfiguration (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class SessionClientConfiguration : IMessage<SessionClientConfiguration>, IEquatable<SessionClientConfiguration>, IDeepCloneable<SessionClientConfiguration>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class SessionClientConfiguration.

Configuration for the Session API. Internal usage only.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SessionClientConfiguration

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### SessionClientConfiguration()
    
    
    public SessionClientConfiguration()

### SessionClientConfiguration(SessionClientConfiguration)
    
    
    public SessionClientConfiguration(SessionClientConfiguration other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)`  
  
  
## Properties 

### ChannelConfiguration
    
    
    public SessionClientConfiguration.Types.ChannelPoolConfiguration ChannelConfiguration { get; set; }

Configuration for the channel pool.

**Property Value**  
---  
**Type** | **Description**  
`[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[ChannelPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.ChannelPoolConfiguration)` |   
  
### LoadBalancingOptions
    
    
    [Obsolete]
    public LoadBalancingOptions LoadBalancingOptions { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[LoadBalancingOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.LoadBalancingOptions)` |   
  
### SessionDiversionConfiguration
    
    
    public SessionDiversionConfiguration SessionDiversionConfiguration { get; set; }

How load should be divered to sessions.

**Property Value**  
---  
**Type** | **Description**  
`[SessionDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration)` |   
  
### SessionLoad
    
    
    [Obsolete]
    public float SessionLoad { get; set; }

Deprecated: Prefer session_diversion_configuration. If both are provided, the client should apply this session_load to Bigtable.ReadRow & Bigtable.MutateRow, then process the session_diversion_configuration, overwriting any behavior established by this value.

What share of the following methods should operate on a session, [0, 1]:

  * Bigtable.ReadRow
  * Bigtable.MutateRow



The rest should operate on the classic API, e.g. have session_load = 0.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### SessionPoolConfiguration
    
    
    public SessionClientConfiguration.Types.SessionPoolConfiguration SessionPoolConfiguration { get; set; }

Configuration for the session pools.

**Property Value**  
---  
**Type** | **Description**  
`[SessionClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types)[SessionPoolConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionClientConfiguration.Types.SessionPoolConfiguration)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
