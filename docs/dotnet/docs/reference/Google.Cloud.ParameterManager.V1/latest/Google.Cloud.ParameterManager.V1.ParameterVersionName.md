---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName
title: Parameter Manager v1 API - Class ParameterVersionName (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:51.369729+00:00
---

# Parameter Manager v1 API - Class ParameterVersionName (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Parameter Manager v1 API - Class ParameterVersionName (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class ParameterVersionName : IResourceName, IEquatable<ParameterVersionName>

Reference documentation and code samples for the Parameter Manager v1 API class ParameterVersionName.

Resource name for the `ParameterVersion` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ParameterVersionName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1)

## Assembly

Google.Cloud.ParameterManager.V1.dll

## Constructors 

### ParameterVersionName(string, string, string, string)
    
    
    public ParameterVersionName(string projectId, string locationId, string parameterId, string parameterVersionId)

Constructs a new instance of a [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) class from the component parts of pattern `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`parameterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Parameter` ID. Must not be `null` or empty.  
`parameterVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ParameterVersion` ID. Must not be `null` or empty.  
  
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
  
### ParameterId
    
    
    public string ParameterId { get; }

The `Parameter` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParameterVersionId
    
    
    public string ParameterVersionId { get; }

The `ParameterVersion` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public ParameterVersionName.ResourceNameType Type { get; }

The [ParameterVersionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string parameterId, string parameterVersionId)

Formats the IDs into the string representation of this [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) with pattern `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`parameterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Parameter` ID. Must not be `null` or empty.  
`parameterVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ParameterVersion` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) with pattern `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`.  
  
### FormatProjectLocationParameterParameterVersion(string, string, string, string)
    
    
    public static string FormatProjectLocationParameterParameterVersion(string projectId, string locationId, string parameterId, string parameterVersionId)

Formats the IDs into the string representation of this [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) with pattern `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`parameterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Parameter` ID. Must not be `null` or empty.  
`parameterVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ParameterVersion` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) with pattern `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`.  
  
### FromProjectLocationParameterParameterVersion(string, string, string, string)
    
    
    public static ParameterVersionName FromProjectLocationParameterParameterVersion(string projectId, string locationId, string parameterId, string parameterVersionId)

Creates a [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) with the pattern `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`parameterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Parameter` ID. Must not be `null` or empty.  
`parameterVersionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ParameterVersion` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)` | A new instance of [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ParameterVersionName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)` | A new instance of [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ParameterVersionName Parse(string parameterVersionName)

Parses the given resource name string into a new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) instance.

**Parameter**  
---  
**Name** | **Description**  
`parameterVersionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)` | The parsed [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`



### Parse(string, bool)
    
    
    public static ParameterVersionName Parse(string parameterVersionName, bool allowUnparsed)

Parses the given resource name string into a new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`parameterVersionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName#Google_Cloud_ParameterManager_V1_ParameterVersionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)` | The parsed [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`



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

### TryParse(string, out ParameterVersionName)
    
    
    public static bool TryParse(string parameterVersionName, out ParameterVersionName result)

Tries to parse the given resource name string into a new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) instance.

**Parameters**  
---  
**Name** | **Description**  
`parameterVersionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)`  
When this method returns, the parsed [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`



### TryParse(string, bool, out ParameterVersionName)
    
    
    public static bool TryParse(string parameterVersionName, bool allowUnparsed, out ParameterVersionName result)

Tries to parse the given resource name string into a new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`parameterVersionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName#Google_Cloud_ParameterManager_V1_ParameterVersionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)`  
When this method returns, the parsed [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/parameters/{parameter}/versions/{parameter_version}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ParameterVersionName, ParameterVersionName)
    
    
    public static bool operator ==(ParameterVersionName a, ParameterVersionName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)`  
The first resource name to compare, or null.  
`b` | `[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ParameterVersionName, ParameterVersionName)
    
    
    public static bool operator !=(ParameterVersionName a, ParameterVersionName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)`  
The first resource name to compare, or null.  
`b` | `[ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
