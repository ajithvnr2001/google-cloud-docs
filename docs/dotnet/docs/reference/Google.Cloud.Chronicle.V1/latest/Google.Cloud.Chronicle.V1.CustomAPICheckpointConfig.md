---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig
title: Chronicle v1 API - Class CustomAPICheckpointConfig (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:51.081428+00:00
---

# Chronicle v1 API - Class CustomAPICheckpointConfig (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class CustomAPICheckpointConfig (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class CustomAPICheckpointConfig : IMessage<CustomAPICheckpointConfig>, IEquatable<CustomAPICheckpointConfig>, IDeepCloneable<CustomAPICheckpointConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class CustomAPICheckpointConfig.

Checkpoint configuration to enable sequential (cursor-based) polling.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CustomAPICheckpointConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### CustomAPICheckpointConfig()
    
    
    public CustomAPICheckpointConfig()

### CustomAPICheckpointConfig(CustomAPICheckpointConfig)
    
    
    public CustomAPICheckpointConfig(CustomAPICheckpointConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)`  
  
  
## Properties 

### IteratorStrategy
    
    
    public CustomAPICheckpointConfig.Types.IteratorStrategy IteratorStrategy { get; set; }

Use progress tokens provided by the API.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[IteratorStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.IteratorStrategy)` |   
  
### LatestRecordStrategy
    
    
    public CustomAPICheckpointConfig.Types.LatestRecordStrategy LatestRecordStrategy { get; set; }

Track the highest record ID to fetch only new records next.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[LatestRecordStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.LatestRecordStrategy)` |   
  
### LatestTimestampStrategy
    
    
    public CustomAPICheckpointConfig.Types.LatestTimestampStrategy LatestTimestampStrategy { get; set; }

Track the timestamp of the newest record to fetch newer ones next.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[LatestTimestampStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.LatestTimestampStrategy)` |   
  
### NoneStrategy
    
    
    public CustomAPICheckpointConfig.Types.NoneStrategy NoneStrategy { get; set; }

Fetch all available data in one go without tracking progress.

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types)[NoneStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.Types.NoneStrategy)` |   
  
### StrategyCase
    
    
    public CustomAPICheckpointConfig.StrategyOneofCase StrategyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CustomAPICheckpointConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig)[StrategyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPICheckpointConfig.StrategyOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
