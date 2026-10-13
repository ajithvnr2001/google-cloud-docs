---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat
title: DataStream v1alpha1 API - Class JsonFileFormat (2.0.0-alpha06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:48.811533+00:00
---

# DataStream v1alpha1 API - Class JsonFileFormat (2.0.0-alpha06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1alpha1 API - Class JsonFileFormat (2.0.0-alpha06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat)
  * [ 2.0.0-alpha05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/2.0.0-alpha05/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/1.0.0-beta02/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat)


    
    
    public sealed class JsonFileFormat : IMessage<JsonFileFormat>, IEquatable<JsonFileFormat>, IDeepCloneable<JsonFileFormat>, IBufferMessage, IMessage

Reference documentation and code samples for the DataStream v1alpha1 API class JsonFileFormat.

JSON file format configuration.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > JsonFileFormat

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[JsonFileFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[JsonFileFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[JsonFileFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1Alpha1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1)

## Assembly

Google.Cloud.Datastream.V1Alpha1.dll

## Constructors 

### JsonFileFormat()
    
    
    public JsonFileFormat()

### JsonFileFormat(JsonFileFormat)
    
    
    public JsonFileFormat(JsonFileFormat other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[JsonFileFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat)`  
  
  
## Properties 

### Compression
    
    
    public JsonFileFormat.Types.JsonCompression Compression { get; set; }

Compression of the loaded JSON file.

**Property Value**  
---  
**Type** | **Description**  
`[JsonFileFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat.Types)[JsonCompression](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.JsonFileFormat.Types.JsonCompression)` |   
  
### SchemaFileFormat
    
    
    public SchemaFileFormat SchemaFileFormat { get; set; }

The schema file format along JSON data files.

**Property Value**  
---  
**Type** | **Description**  
`[SchemaFileFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.SchemaFileFormat)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
