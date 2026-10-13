---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName
title: Google AutoML v1 API - Class ModelEvaluationName (3.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:50.863400+00:00
---

# Google AutoML v1 API - Class ModelEvaluationName (3.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google AutoML v1 API - Class ModelEvaluationName (3.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.6.0 (latest)  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ModelEvaluationName : IResourceName, IEquatable<ModelEvaluationName>

Reference documentation and code samples for the Google AutoML v1 API class ModelEvaluationName.

Resource name for the `ModelEvaluation` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ModelEvaluationName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.AutoML.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1)

## Assembly

Google.Cloud.AutoML.V1.dll

## Constructors 

### ModelEvaluationName(string, string, string, string)
    
    
    public ModelEvaluationName(string projectId, string locationId, string modelId, string modelEvaluationId)

Constructs a new instance of a [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) class from the component parts of pattern `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
`modelEvaluationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ModelEvaluation` ID. Must not be `null` or empty.  
  
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
  
### ModelEvaluationId
    
    
    public string ModelEvaluationId { get; }

The `ModelEvaluation` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public ModelEvaluationName.ResourceNameType Type { get; }

The [ModelEvaluationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string modelId, string modelEvaluationId)

Formats the IDs into the string representation of this [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) with pattern `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
`modelEvaluationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ModelEvaluation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) with pattern `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`.  
  
### FormatProjectLocationModelModelEvaluation(string, string, string, string)
    
    
    public static string FormatProjectLocationModelModelEvaluation(string projectId, string locationId, string modelId, string modelEvaluationId)

Formats the IDs into the string representation of this [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) with pattern `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
`modelEvaluationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ModelEvaluation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) with pattern `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`.  
  
### FromProjectLocationModelModelEvaluation(string, string, string, string)
    
    
    public static ModelEvaluationName FromProjectLocationModelModelEvaluation(string projectId, string locationId, string modelId, string modelEvaluationId)

Creates a [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) with the pattern `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`modelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Model` ID. Must not be `null` or empty.  
`modelEvaluationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ModelEvaluation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)` | A new instance of [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ModelEvaluationName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)` | A new instance of [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ModelEvaluationName Parse(string modelEvaluationName)

Parses the given resource name string into a new [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) instance.

**Parameter**  
---  
**Name** | **Description**  
`modelEvaluationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)` | The parsed [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`



### Parse(string, bool)
    
    
    public static ModelEvaluationName Parse(string modelEvaluationName, bool allowUnparsed)

Parses the given resource name string into a new [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`modelEvaluationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName#Google_Cloud_AutoML_V1_ModelEvaluationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)` | The parsed [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`



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

### TryParse(string, out ModelEvaluationName)
    
    
    public static bool TryParse(string modelEvaluationName, out ModelEvaluationName result)

Tries to parse the given resource name string into a new [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) instance.

**Parameters**  
---  
**Name** | **Description**  
`modelEvaluationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)`  
When this method returns, the parsed [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`



### TryParse(string, bool, out ModelEvaluationName)
    
    
    public static bool TryParse(string modelEvaluationName, bool allowUnparsed, out ModelEvaluationName result)

Tries to parse the given resource name string into a new [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`modelEvaluationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName#Google_Cloud_AutoML_V1_ModelEvaluationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)`  
When this method returns, the parsed [ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/models/{model}/modelEvaluations/{model_evaluation}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ModelEvaluationName, ModelEvaluationName)
    
    
    public static bool operator ==(ModelEvaluationName a, ModelEvaluationName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)`  
The first resource name to compare, or null.  
`b` | `[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ModelEvaluationName, ModelEvaluationName)
    
    
    public static bool operator !=(ModelEvaluationName a, ModelEvaluationName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)`  
The first resource name to compare, or null.  
`b` | `[ModelEvaluationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
