---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName
title: Policy Simulator v1 API - Class FolderLocationName (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:40.688692+00:00
---

# Policy Simulator v1 API - Class FolderLocationName (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Policy Simulator v1 API - Class FolderLocationName (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.3.0/Google.Cloud.PolicySimulator.V1.FolderLocationName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.2.0/Google.Cloud.PolicySimulator.V1.FolderLocationName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.1.0/Google.Cloud.PolicySimulator.V1.FolderLocationName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.0.0/Google.Cloud.PolicySimulator.V1.FolderLocationName)


    
    
    public sealed class FolderLocationName : IResourceName, IEquatable<FolderLocationName>

Reference documentation and code samples for the Policy Simulator v1 API class FolderLocationName.

Resource name for the `FolderLocation` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FolderLocationName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.PolicySimulator.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1)

## Assembly

Google.Cloud.PolicySimulator.V1.dll

## Constructors 

### FolderLocationName(string, string)
    
    
    public FolderLocationName(string folderId, string locationId)

Constructs a new instance of a [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) class from the component parts of pattern `folders/{folder}/locations/{location}`

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
  
## Properties 

### FolderId
    
    
    public string FolderId { get; }

The `Folder` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### Type
    
    
    public FolderLocationName.ResourceNameType Type { get; }

The [FolderLocationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string folderId, string locationId)

Formats the IDs into the string representation of this [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) with pattern `folders/{folder}/locations/{location}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) with pattern `folders/{folder}/locations/{location}`.  
  
### FormatFolderLocation(string, string)
    
    
    public static string FormatFolderLocation(string folderId, string locationId)

Formats the IDs into the string representation of this [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) with pattern `folders/{folder}/locations/{location}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) with pattern `folders/{folder}/locations/{location}`.  
  
### FromFolderLocation(string, string)
    
    
    public static FolderLocationName FromFolderLocation(string folderId, string locationId)

Creates a [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) with the pattern `folders/{folder}/locations/{location}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)` | A new instance of [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static FolderLocationName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)` | A new instance of [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static FolderLocationName Parse(string folderLocationName)

Parses the given resource name string into a new [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) instance.

**Parameter**  
---  
**Name** | **Description**  
`folderLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)` | The parsed [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `folders/{folder}/locations/{location}`



### Parse(string, bool)
    
    
    public static FolderLocationName Parse(string folderLocationName, bool allowUnparsed)

Parses the given resource name string into a new [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`folderLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName#Google_Cloud_PolicySimulator_V1_FolderLocationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)` | The parsed [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `folders/{folder}/locations/{location}`

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

### TryParse(string, out FolderLocationName)
    
    
    public static bool TryParse(string folderLocationName, out FolderLocationName result)

Tries to parse the given resource name string into a new [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) instance.

**Parameters**  
---  
**Name** | **Description**  
`folderLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)`  
When this method returns, the parsed [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `folders/{folder}/locations/{location}`



### TryParse(string, bool, out FolderLocationName)
    
    
    public static bool TryParse(string folderLocationName, bool allowUnparsed, out FolderLocationName result)

Tries to parse the given resource name string into a new [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`folderLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName#Google_Cloud_PolicySimulator_V1_FolderLocationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)`  
When this method returns, the parsed [FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `folders/{folder}/locations/{location}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(FolderLocationName, FolderLocationName)
    
    
    public static bool operator ==(FolderLocationName a, FolderLocationName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)`  
The first resource name to compare, or null.  
`b` | `[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(FolderLocationName, FolderLocationName)
    
    
    public static bool operator !=(FolderLocationName a, FolderLocationName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)`  
The first resource name to compare, or null.  
`b` | `[FolderLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.FolderLocationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
