---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName
title: Artifact Registry v1beta2 API - Class TagName (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:27.192911+00:00
---

# Artifact Registry v1beta2 API - Class TagName (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Artifact Registry v1beta2 API - Class TagName (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/2.0.0-beta05/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/1.0.0-beta06/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)


    
    
    public sealed class TagName : IResourceName, IEquatable<TagName>

Reference documentation and code samples for the Artifact Registry v1beta2 API class TagName.

Resource name for the `Tag` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TagName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.ArtifactRegistry.V1Beta2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2)

## Assembly

Google.Cloud.ArtifactRegistry.V1Beta2.dll

## Constructors 

### TagName(string, string, string, string, string)
    
    
    public TagName(string projectId, string locationId, string repositoryId, string packageId, string tagId)

Constructs a new instance of a [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) class from the component parts of pattern `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`packageId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Package` ID. Must not be `null` or empty.  
`tagId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Tag` ID. Must not be `null` or empty.  
  
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
  
### PackageId
    
    
    public string PackageId { get; }

The `Package` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### RepositoryId
    
    
    public string RepositoryId { get; }

The `Repository` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TagId
    
    
    public string TagId { get; }

The `Tag` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public TagName.ResourceNameType Type { get; }

The [TagName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string repositoryId, string packageId, string tagId)

Formats the IDs into the string representation of this [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`packageId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Package` ID. Must not be `null` or empty.  
`tagId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Tag` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`.  
  
### FormatProjectLocationRepositoryPackageTag(string, string, string, string, string)
    
    
    public static string FormatProjectLocationRepositoryPackageTag(string projectId, string locationId, string repositoryId, string packageId, string tagId)

Formats the IDs into the string representation of this [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`packageId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Package` ID. Must not be `null` or empty.  
`tagId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Tag` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`.  
  
### FromProjectLocationRepositoryPackageTag(string, string, string, string, string)
    
    
    public static TagName FromProjectLocationRepositoryPackageTag(string projectId, string locationId, string repositoryId, string packageId, string tagId)

Creates a [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) with the pattern `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`packageId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Package` ID. Must not be `null` or empty.  
`tagId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Tag` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)` | A new instance of [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static TagName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)` | A new instance of [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static TagName Parse(string tagName)

Parses the given resource name string into a new [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) instance.

**Parameter**  
---  
**Name** | **Description**  
`tagName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)` | The parsed [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`



### Parse(string, bool)
    
    
    public static TagName Parse(string tagName, bool allowUnparsed)

Parses the given resource name string into a new [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`tagName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName#Google_Cloud_ArtifactRegistry_V1Beta2_TagName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)` | The parsed [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`

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

### TryParse(string, out TagName)
    
    
    public static bool TryParse(string tagName, out TagName result)

Tries to parse the given resource name string into a new [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) instance.

**Parameters**  
---  
**Name** | **Description**  
`tagName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)`  
When this method returns, the parsed [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`



### TryParse(string, bool, out TagName)
    
    
    public static bool TryParse(string tagName, bool allowUnparsed, out TagName result)

Tries to parse the given resource name string into a new [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`tagName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName#Google_Cloud_ArtifactRegistry_V1Beta2_TagName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)`  
When this method returns, the parsed [TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/repositories/{repository}/packages/{package}/tags/{tag}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(TagName, TagName)
    
    
    public static bool operator ==(TagName a, TagName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)`  
The first resource name to compare, or null.  
`b` | `[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(TagName, TagName)
    
    
    public static bool operator !=(TagName a, TagName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)`  
The first resource name to compare, or null.  
`b` | `[TagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.TagName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
