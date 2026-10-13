---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName
title: Vertex AI v1 API - Class AnnotationSpecName (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:55.238701+00:00
---

# Vertex AI v1 API - Class AnnotationSpecName (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class AnnotationSpecName (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AnnotationSpecName : IResourceName, IEquatable<AnnotationSpecName>

Reference documentation and code samples for the Vertex AI v1 API class AnnotationSpecName.

Resource name for the `AnnotationSpec` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnnotationSpecName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.AIPlatform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Constructors 

### AnnotationSpecName(string, string, string, string)
    
    
    public AnnotationSpecName(string projectId, string locationId, string datasetId, string annotationSpecId)

Constructs a new instance of a [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) class from the component parts of pattern `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
`annotationSpecId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AnnotationSpec` ID. Must not be `null` or empty.  
  
## Properties 

### AnnotationSpecId
    
    
    public string AnnotationSpecId { get; }

The `AnnotationSpec` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
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
    
    
    public AnnotationSpecName.ResourceNameType Type { get; }

The [AnnotationSpecName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string datasetId, string annotationSpecId)

Formats the IDs into the string representation of this [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
`annotationSpecId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AnnotationSpec` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`.  
  
### FormatProjectLocationDatasetAnnotationSpec(string, string, string, string)
    
    
    public static string FormatProjectLocationDatasetAnnotationSpec(string projectId, string locationId, string datasetId, string annotationSpecId)

Formats the IDs into the string representation of this [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
`annotationSpecId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AnnotationSpec` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) with pattern `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`.  
  
### FromProjectLocationDatasetAnnotationSpec(string, string, string, string)
    
    
    public static AnnotationSpecName FromProjectLocationDatasetAnnotationSpec(string projectId, string locationId, string datasetId, string annotationSpecId)

Creates a [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) with the pattern `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`datasetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Dataset` ID. Must not be `null` or empty.  
`annotationSpecId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AnnotationSpec` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)` | A new instance of [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static AnnotationSpecName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)` | A new instance of [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static AnnotationSpecName Parse(string annotationSpecName)

Parses the given resource name string into a new [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) instance.

**Parameter**  
---  
**Name** | **Description**  
`annotationSpecName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)` | The parsed [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`



### Parse(string, bool)
    
    
    public static AnnotationSpecName Parse(string annotationSpecName, bool allowUnparsed)

Parses the given resource name string into a new [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`annotationSpecName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName#Google_Cloud_AIPlatform_V1_AnnotationSpecName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)` | The parsed [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`



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

### TryParse(string, out AnnotationSpecName)
    
    
    public static bool TryParse(string annotationSpecName, out AnnotationSpecName result)

Tries to parse the given resource name string into a new [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) instance.

**Parameters**  
---  
**Name** | **Description**  
`annotationSpecName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)`  
When this method returns, the parsed [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`



### TryParse(string, bool, out AnnotationSpecName)
    
    
    public static bool TryParse(string annotationSpecName, bool allowUnparsed, out AnnotationSpecName result)

Tries to parse the given resource name string into a new [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`annotationSpecName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName#Google_Cloud_AIPlatform_V1_AnnotationSpecName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)`  
When this method returns, the parsed [AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/datasets/{dataset}/annotationSpecs/{annotation_spec}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(AnnotationSpecName, AnnotationSpecName)
    
    
    public static bool operator ==(AnnotationSpecName a, AnnotationSpecName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)`  
The first resource name to compare, or null.  
`b` | `[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(AnnotationSpecName, AnnotationSpecName)
    
    
    public static bool operator !=(AnnotationSpecName a, AnnotationSpecName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)`  
The first resource name to compare, or null.  
`b` | `[AnnotationSpecName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.AnnotationSpecName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
