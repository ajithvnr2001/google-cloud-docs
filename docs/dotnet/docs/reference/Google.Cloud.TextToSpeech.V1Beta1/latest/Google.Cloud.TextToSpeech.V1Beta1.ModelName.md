---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName
title: Google Cloud Text-to-Speech v1beta1 API - Class ModelName (2.0.0-beta18) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:32.004406+00:00
---

# Google Cloud Text-to-Speech v1beta1 API - Class ModelName (2.0.0-beta18)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Text-to-Speech v1beta1 API - Class ModelName (2.0.0-beta18) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta18 (latest)  2.0.0-beta17  1.0.0-beta04 
    
    
    public sealed class ModelName : IResourceName, IEquatable<ModelName>

Reference documentation and code samples for the Google Cloud Text-to-Speech v1beta1 API class ModelName.

Resource name for the `Model` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ModelName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.TextToSpeech.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1)

## Assembly

Google.Cloud.TextToSpeech.V1Beta1.dll

## Constructors 

### ModelName(string, string, string)
    
    
    public ModelName(string projectId, string locationId, string modelId)

Constructs a new instance of a [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) class from the component parts of pattern `projects/{project}/locations/{location}/models/{model}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
  
## Properties 

### IsKnownPattern
    
    
    public bool IsKnownPattern { get; }

Whether this instance contains a resource name with a known pattern.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LocationId
    
    
    public string LocationId { get; }

The `Location` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ModelId
    
    
    public string ModelId { get; }

The `Model` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ModelName.ResourceNameType Type { get; }

The [ModelName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string modelId)

Formats the IDs into the string representation of this [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) with pattern `projects/{project}/locations/{location}/models/{model}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) with pattern `projects/{project}/locations/{location}/models/{model}`.  
  
### FormatProjectLocationModel(string, string, string)
    
    
    public static string FormatProjectLocationModel(string projectId, string locationId, string modelId)

Formats the IDs into the string representation of this [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) with pattern `projects/{project}/locations/{location}/models/{model}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) with pattern `projects/{project}/locations/{location}/models/{model}`.  
  
### FromProjectLocationModel(string, string, string)
    
    
    public static ModelName FromProjectLocationModel(string projectId, string locationId, string modelId)

Creates a [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) with the pattern `projects/{project}/locations/{location}/models/{model}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)` | A new instance of [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ModelName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)` | A new instance of [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) containing the provided `unparsedResourceName`.  
  
### GetHashCode()
    
    
    public override int GetHashCode()

Returns a hash code for this resource name.

**Returns**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
**Overrides**

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

### Parse(string)
    
    
    public static ModelName Parse(string modelName)

Parses the given resource name string into a new [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) instance.

**Parameter**  
---  
**Name** | **Description**  
`modelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)` | The parsed [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}`



### Parse(string, bool)
    
    
    public static ModelName Parse(string modelName, bool allowUnparsed)

Parses the given resource name string into a new [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`modelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName#Google_Cloud_TextToSpeech_V1Beta1_ModelName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)` | The parsed [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}`



Or may be in any format if `allowUnparsed` is `true`.

### ToString()
    
    
    public override string ToString()

The string representation of the resource name.

**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of the resource name.  
**Overrides**

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

### TryParse(string, out ModelName)
    
    
    public static bool TryParse(string modelName, out ModelName result)

Tries to parse the given resource name string into a new [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) instance.

**Parameters**  
---  
**Name** | **Description**  
`modelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)`  
When this method returns, the parsed [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}`



### TryParse(string, bool, out ModelName)
    
    
    public static bool TryParse(string modelName, bool allowUnparsed, out ModelName result)

Tries to parse the given resource name string into a new [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`modelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName#Google_Cloud_TextToSpeech_V1Beta1_ModelName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)`  
When this method returns, the parsed [ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ModelName, ModelName)
    
    
    public static bool operator ==(ModelName a, ModelName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)`  
The first resource name to compare, or null.  
`b` | `[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ModelName, ModelName)
    
    
    public static bool operator !=(ModelName a, ModelName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)`  
The first resource name to compare, or null.  
`b` | `[ModelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.ModelName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
