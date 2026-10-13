---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName
title: Vertex AI v1beta1 API - Class AutoMLDatasetName (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:33.627121+00:00
---

# Vertex AI v1beta1 API - Class AutoMLDatasetName (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class AutoMLDatasetName (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class AutoMLDatasetName : IResourceName, IEquatable<AutoMLDatasetName>

Reference documentation and code samples for the Vertex AI v1beta1 API class AutoMLDatasetName.

Resource name for the `AutoMLDataset` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutoMLDatasetName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### AutoMLDatasetName(string, string, string)
    
    
    public AutoMLDatasetName(string projectId, string locationId, string datasetId)

Constructs a new instance of a [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) class from the component parts of pattern `projects/{project}/locations/{location}/datasets/{dataset}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
  
## Properties 

### DatasetId
    
    
    public string DatasetId { get; }

The `Dataset` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
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
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public AutoMLDatasetName.ResourceNameType Type { get; }

The [AutoMLDatasetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string datasetId)

Formats the IDs into the string representation of this [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}`.  
  
### FormatProjectLocationDataset(string, string, string)
    
    
    public static string FormatProjectLocationDataset(string projectId, string locationId, string datasetId)

Formats the IDs into the string representation of this [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}`.  
  
### FromProjectLocationDataset(string, string, string)
    
    
    public static AutoMLDatasetName FromProjectLocationDataset(string projectId, string locationId, string datasetId)

Creates a [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) with the pattern `projects/{project}/locations/{location}/datasets/{dataset}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)` | A new instance of [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static AutoMLDatasetName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)` | A new instance of [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static AutoMLDatasetName Parse(string autoMLDatasetName)

Parses the given resource name string into a new [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) instance.

**Parameter**  
---  
**Name** | **Description**  
`autoMLDatasetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)` | The parsed [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}`



### Parse(string, bool)
    
    
    public static AutoMLDatasetName Parse(string autoMLDatasetName, bool allowUnparsed)

Parses the given resource name string into a new [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`autoMLDatasetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName#Google_Cloud_AIPlatform_V1Beta1_AutoMLDatasetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)` | The parsed [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}`



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

### TryParse(string, out AutoMLDatasetName)
    
    
    public static bool TryParse(string autoMLDatasetName, out AutoMLDatasetName result)

Tries to parse the given resource name string into a new [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) instance.

**Parameters**  
---  
**Name** | **Description**  
`autoMLDatasetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)`  
When this method returns, the parsed [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}`



### TryParse(string, bool, out AutoMLDatasetName)
    
    
    public static bool TryParse(string autoMLDatasetName, bool allowUnparsed, out AutoMLDatasetName result)

Tries to parse the given resource name string into a new [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`autoMLDatasetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName#Google_Cloud_AIPlatform_V1Beta1_AutoMLDatasetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)`  
When this method returns, the parsed [AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(AutoMLDatasetName, AutoMLDatasetName)
    
    
    public static bool operator ==(AutoMLDatasetName a, AutoMLDatasetName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)`  
The first resource name to compare, or null.  
`b` | `[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(AutoMLDatasetName, AutoMLDatasetName)
    
    
    public static bool operator !=(AutoMLDatasetName a, AutoMLDatasetName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)`  
The first resource name to compare, or null.  
`b` | `[AutoMLDatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.AutoMLDatasetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
