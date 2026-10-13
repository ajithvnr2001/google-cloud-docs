---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig
title: Chronicle v1 API - Class AdvancedFilterConfig (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:35.914864+00:00
---

# Chronicle v1 API - Class AdvancedFilterConfig (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class AdvancedFilterConfig (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class AdvancedFilterConfig : IMessage<AdvancedFilterConfig>, IEquatable<AdvancedFilterConfig>, IDeepCloneable<AdvancedFilterConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class AdvancedFilterConfig.

Advanced filter configuration for the filter widget.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AdvancedFilterConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### AdvancedFilterConfig()
    
    
    public AdvancedFilterConfig()

### AdvancedFilterConfig(AdvancedFilterConfig)
    
    
    public AdvancedFilterConfig(AdvancedFilterConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)`  
  
  
## Properties 

### DefaultValues
    
    
    public RepeatedField<string> DefaultValues { get; }

Optional. Default values to use if no value is selected/provided.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MultipleAllowed
    
    
    public bool MultipleAllowed { get; set; }

Optional. Whether to allow selection of multiple values.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Prefix
    
    
    public string Prefix { get; set; }

Optional. String to prepend to the final replaced value (e.g., "/", "^(", """).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Separator
    
    
    public string Separator { get; set; }

Optional. Delimiter to join multiple selected values (e.g., "|", " OR field = ").

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SkipDefaultAffixes
    
    
    public bool SkipDefaultAffixes { get; set; }

Optional. Whether to skip the configured prefix and suffix when using default values. If true, default values are inserted raw (joined by the separator).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Suffix
    
    
    public string Suffix { get; set; }

Optional. String to append to the final replaced value (e.g., "/", ")$", """).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Token
    
    
    public string Token { get; set; }

Required. The token name to look for in the query (e.g., "hostname"). The system will automatically wrap this in '$' (e.g., "$hostname$").

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValueSource
    
    
    public AdvancedFilterConfig.Types.ValueSource ValueSource { get; set; }

Required. Source of the values for the filter.

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedFilterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types)[ValueSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.AdvancedFilterConfig.Types.ValueSource)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
