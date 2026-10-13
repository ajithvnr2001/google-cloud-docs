---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource
title: Chronicle v1 API - Class AdvancedFilterConfig.Types.ValueSource (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:36.532589+00:00
---

# Chronicle v1 API - Class AdvancedFilterConfig.Types.ValueSource (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class AdvancedFilterConfig.Types.ValueSource (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class AdvancedFilterConfig.Types.ValueSource : IMessage<AdvancedFilterConfig.Types.ValueSource>, IEquatable<AdvancedFilterConfig.Types.ValueSource>, IDeepCloneable<AdvancedFilterConfig.Types.ValueSource>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class AdvancedFilterConfig.Types.ValueSource.

Source of the values for the filter.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AdvancedFilterConfig.Types.ValueSource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[ValueSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[ValueSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[ValueSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### ValueSource()
    
    
    public ValueSource()

### ValueSource(ValueSource)
    
    
    public ValueSource(AdvancedFilterConfig.Types.ValueSource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[ValueSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource)`  
  
  
## Properties 

### ManualOptions
    
    
    public AdvancedFilterConfig.Types.ManualOptions ManualOptions { get; set; }

Optional. Manual options provided by the user.

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[ManualOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ManualOptions)` |   
  
### QueryOptions
    
    
    public AdvancedFilterConfig.Types.QueryOptions QueryOptions { get; set; }

Optional. Query options to fetch the values from the query engine. This is used for the filter's population query.

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[QueryOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.QueryOptions)` |   
  
### SourceCase
    
    
    public AdvancedFilterConfig.Types.ValueSource.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[ValueSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource.SourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
