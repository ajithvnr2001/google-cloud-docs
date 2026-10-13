---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration
title: Google Bigtable v2 API - Class SessionDiversionConfiguration (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:09.189142+00:00
---

# Google Bigtable v2 API - Class SessionDiversionConfiguration (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class SessionDiversionConfiguration (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class SessionDiversionConfiguration : IMessage<SessionDiversionConfiguration>, IEquatable<SessionDiversionConfiguration>, IDeepCloneable<SessionDiversionConfiguration>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class SessionDiversionConfiguration.

Configuration for how to divert load to sessions. Internal usage only.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SessionDiversionConfiguration

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SessionDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SessionDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SessionDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### SessionDiversionConfiguration()
    
    
    public SessionDiversionConfiguration()

### SessionDiversionConfiguration(SessionDiversionConfiguration)
    
    
    public SessionDiversionConfiguration(SessionDiversionConfiguration other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SessionDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration)`  
  
  
## Properties 

### DiversionStrategyCase
    
    
    public SessionDiversionConfiguration.DiversionStrategyOneofCase DiversionStrategyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration)[DiversionStrategyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration.DiversionStrategyOneofCase)` |   
  
### GlobalDiversion
    
    
    public SessionScopeDiversionConfiguration GlobalDiversion { get; set; }

If provided, all scopes should use this diversion config.

**Property Value**  
---  
**Type** | **Description**  
`[SessionScopeDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionScopeDiversionConfiguration)` |   
  
### PerScopeDiversion
    
    
    public SessionDiversionConfiguration.Types.PerScopeDiversion PerScopeDiversion { get; set; }

Diversion happens per-scope.

**Property Value**  
---  
**Type** | **Description**  
`[SessionDiversionConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration.Types)[PerScopeDiversion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionDiversionConfiguration.Types.PerScopeDiversion)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
