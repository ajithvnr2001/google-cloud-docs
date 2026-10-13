---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues
title: API hub v1 API - Class AttributeValues (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:44.468849+00:00
---

# API hub v1 API - Class AttributeValues (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class AttributeValues (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.AttributeValues)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.AttributeValues)


    
    
    public sealed class AttributeValues : IMessage<AttributeValues>, IEquatable<AttributeValues>, IDeepCloneable<AttributeValues>, IBufferMessage, IMessage

Reference documentation and code samples for the API hub v1 API class AttributeValues.

The attribute values associated with resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AttributeValues

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### AttributeValues()
    
    
    public AttributeValues()

### AttributeValues(AttributeValues)
    
    
    public AttributeValues(AttributeValues other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues)`  
  
  
## Properties 

### Attribute
    
    
    public string Attribute { get; set; }

Output only. The name of the attribute. Format: projects/{project}/locations/{location}/attributes/{attribute}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AttributeAsAttributeName
    
    
    public AttributeName AttributeAsAttributeName { get; set; }

[AttributeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeName)-typed view over the [Attribute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues#Google_Cloud_ApiHub_V1_AttributeValues_Attribute) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AttributeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeName)` |   
  
### EnumValues
    
    
    public AttributeValues.Types.EnumAttributeValues EnumValues { get; set; }

The attribute values associated with a resource in case attribute data type is enum.

**Property Value**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types)[EnumAttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types.EnumAttributeValues)` |   
  
### JsonValues
    
    
    public AttributeValues.Types.StringAttributeValues JsonValues { get; set; }

The attribute values associated with a resource in case attribute data type is JSON.

**Property Value**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types)[StringAttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types.StringAttributeValues)` |   
  
### StringValues
    
    
    public AttributeValues.Types.StringAttributeValues StringValues { get; set; }

The attribute values associated with a resource in case attribute data type is string.

**Property Value**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types)[StringAttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types.StringAttributeValues)` |   
  
### UriValues
    
    
    public AttributeValues.Types.StringAttributeValues UriValues { get; set; }

The attribute values associated with a resource in case attribute data type is URL, URI or IP, like gs://bucket-name/object-name.

**Property Value**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types)[StringAttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.Types.StringAttributeValues)` |   
  
### ValueCase
    
    
    public AttributeValues.ValueOneofCase ValueCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues)[ValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.AttributeValues.ValueOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
