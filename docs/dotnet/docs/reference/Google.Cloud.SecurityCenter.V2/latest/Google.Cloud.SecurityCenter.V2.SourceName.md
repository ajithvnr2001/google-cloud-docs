---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName
title: Security Command Center v2 API - Class SourceName (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:59.566236+00:00
---

# Security Command Center v2 API - Class SourceName (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class SourceName (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SourceName : IResourceName, IEquatable<SourceName>

Reference documentation and code samples for the Security Command Center v2 API class SourceName.

Resource name for the `Source` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SourceName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### SourceName(string, string)
    
    
    public SourceName(string organizationId, string sourceId)

Constructs a new instance of a [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) class from the component parts of pattern `organizations/{organization}/sources/{source}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
  
## Properties 

### FolderId
    
    
    public string FolderId { get; }

The `Folder` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### OrganizationId
    
    
    public string OrganizationId { get; }

The `Organization` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceId
    
    
    public string SourceId { get; }

The `Source` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public SourceName.ResourceNameType Type { get; }

The [SourceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string organizationId, string sourceId)

Formats the IDs into the string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `organizations/{organization}/sources/{source}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `organizations/{organization}/sources/{source}`.  
  
### FormatFolderSource(string, string)
    
    
    public static string FormatFolderSource(string folderId, string sourceId)

Formats the IDs into the string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `folders/{folder}/sources/{source}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `folders/{folder}/sources/{source}` .  
  
### FormatOrganizationSource(string, string)
    
    
    public static string FormatOrganizationSource(string organizationId, string sourceId)

Formats the IDs into the string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `organizations/{organization}/sources/{source}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `organizations/{organization}/sources/{source}`.  
  
### FormatProjectSource(string, string)
    
    
    public static string FormatProjectSource(string projectId, string sourceId)

Formats the IDs into the string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `projects/{project}/sources/{source}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with pattern `projects/{project}/sources/{source}`.  
  
### FromFolderSource(string, string)
    
    
    public static SourceName FromFolderSource(string folderId, string sourceId)

Creates a [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with the pattern `folders/{folder}/sources/{source}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)` | A new instance of [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) constructed from the provided ids.  
  
### FromOrganizationSource(string, string)
    
    
    public static SourceName FromOrganizationSource(string organizationId, string sourceId)

Creates a [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with the pattern `organizations/{organization}/sources/{source}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)` | A new instance of [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) constructed from the provided ids.  
  
### FromProjectSource(string, string)
    
    
    public static SourceName FromProjectSource(string projectId, string sourceId)

Creates a [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) with the pattern `projects/{project}/sources/{source}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)` | A new instance of [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static SourceName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)` | A new instance of [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static SourceName Parse(string sourceName)

Parses the given resource name string into a new [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) instance.

**Parameter**  
---  
**Name** | **Description**  
`sourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)` | The parsed [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}`
  * `folders/{folder}/sources/{source}`
  * `projects/{project}/sources/{source}`



### Parse(string, bool)
    
    
    public static SourceName Parse(string sourceName, bool allowUnparsed)

Parses the given resource name string into a new [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`sourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName#Google_Cloud_SecurityCenter_V2_SourceName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)` | The parsed [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}`
  * `folders/{folder}/sources/{source}`
  * `projects/{project}/sources/{source}`



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

### TryParse(string, out SourceName)
    
    
    public static bool TryParse(string sourceName, out SourceName result)

Tries to parse the given resource name string into a new [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) instance.

**Parameters**  
---  
**Name** | **Description**  
`sourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)`  
When this method returns, the parsed [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}`
  * `folders/{folder}/sources/{source}`
  * `projects/{project}/sources/{source}`



### TryParse(string, bool, out SourceName)
    
    
    public static bool TryParse(string sourceName, bool allowUnparsed, out SourceName result)

Tries to parse the given resource name string into a new [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`sourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName#Google_Cloud_SecurityCenter_V2_SourceName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)`  
When this method returns, the parsed [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}`
  * `folders/{folder}/sources/{source}`
  * `projects/{project}/sources/{source}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(SourceName, SourceName)
    
    
    public static bool operator ==(SourceName a, SourceName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)`  
The first resource name to compare, or null.  
`b` | `[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(SourceName, SourceName)
    
    
    public static bool operator !=(SourceName a, SourceName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)`  
The first resource name to compare, or null.  
`b` | `[SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.SourceName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
