---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore
title: Gemini Enterprise for Customer Experience v1beta API - Class DataStore (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:04.288769+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class DataStore (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class DataStore (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class DataStore : IMessage<DataStore>, IEquatable<DataStore>, IDeepCloneable<DataStore>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class DataStore.

A DataStore resource in Vertex AI Search.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataStore

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### DataStore()
    
    
    public DataStore()

### DataStore(DataStore)
    
    
    public DataStore(DataStore other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore)`  
  
  
## Properties 

### ConnectorConfig
    
    
    public DataStore.Types.ConnectorConfig ConnectorConfig { get; set; }

Output only. The connector config for the data store connection.

**Property Value**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types)[ConnectorConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types.ConnectorConfig)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Timestamp when the data store was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Output only. The display name of the data store.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DocumentProcessingMode
    
    
    public DataStore.Types.DocumentProcessingMode DocumentProcessingMode { get; set; }

Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.

**Property Value**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types)[DocumentProcessingMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types.DocumentProcessingMode)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Full resource name of the DataStore. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public DataStore.Types.DataStoreType Type { get; set; }

Output only. The type of the data store. This field is readonly and populated by the server.

**Property Value**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types)[DataStoreType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStore.Types.DataStoreType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
