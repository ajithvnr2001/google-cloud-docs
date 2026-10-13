---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types.DataStoreSource
title: Gemini Enterprise for Customer Experience v1 API - Class DataStoreTool.Types.DataStoreSource (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:34.773068+00:00
---

# Gemini Enterprise for Customer Experience v1 API - Class DataStoreTool.Types.DataStoreSource (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types.DataStoreSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1 API - Class DataStoreTool.Types.DataStoreSource (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta04 
    
    
    public sealed class DataStoreTool.Types.DataStoreSource : IMessage<DataStoreTool.Types.DataStoreSource>, IEquatable<DataStoreTool.Types.DataStoreSource>, IDeepCloneable<DataStoreTool.Types.DataStoreSource>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1 API class DataStoreTool.Types.DataStoreSource.

Configuration for searching within a specific DataStore.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataStoreTool.Types.DataStoreSource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DataStoreTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types)[DataStoreSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types.DataStoreSource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DataStoreTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types)[DataStoreSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types.DataStoreSource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DataStoreTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types)[DataStoreSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types.DataStoreSource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1)

## Assembly

Google.Cloud.Ces.V1.dll

## Constructors 

### DataStoreSource()
    
    
    public DataStoreSource()

### DataStoreSource(DataStoreSource)
    
    
    public DataStoreSource(DataStoreTool.Types.DataStoreSource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DataStoreTool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types)[DataStoreSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStoreTool.Types.DataStoreSource)`  
  
  
## Properties 

### DataStore
    
    
    public DataStore DataStore { get; set; }

Optional. The data store.

**Property Value**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DataStore)` |   
  
### Filter
    
    
    public string Filter { get; set; }

Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
