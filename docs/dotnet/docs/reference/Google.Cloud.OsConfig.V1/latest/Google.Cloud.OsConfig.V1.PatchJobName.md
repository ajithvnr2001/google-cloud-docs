---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName
title: Google Cloud OS Config v1 API - Class PatchJobName (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:27.964517+00:00
---

# Google Cloud OS Config v1 API - Class PatchJobName (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Config v1 API - Class PatchJobName (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/2.5.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/2.4.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/2.3.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/2.2.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/2.1.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/2.0.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 1.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/1.8.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/1.7.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/1.6.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/1.5.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/1.4.0/Google.Cloud.OsConfig.V1.PatchJobName)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/1.3.0/Google.Cloud.OsConfig.V1.PatchJobName)


    
    
    public sealed class PatchJobName : IResourceName, IEquatable<PatchJobName>

Reference documentation and code samples for the Google Cloud OS Config v1 API class PatchJobName.

Resource name for the `PatchJob` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PatchJobName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.OsConfig.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1)

## Assembly

Google.Cloud.OsConfig.V1.dll

## Constructors 

### PatchJobName(string, string)
    
    
    public PatchJobName(string projectId, string patchJobId)

Constructs a new instance of a [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) class from the component parts of pattern `projects/{project}/patchJobs/{patch_job}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`patchJobId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PatchJob` ID. Must not be `null` or empty.  
  
## Properties 

### IsKnownPattern
    
    
    public bool IsKnownPattern { get; }

Whether this instance contains a resource name with a known pattern.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PatchJobId
    
    
    public string PatchJobId { get; }

The `PatchJob` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public PatchJobName.ResourceNameType Type { get; }

The [PatchJobName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string projectId, string patchJobId)

Formats the IDs into the string representation of this [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) with pattern `projects/{project}/patchJobs/{patch_job}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`patchJobId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PatchJob` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) with pattern `projects/{project}/patchJobs/{patch_job}`.  
  
### FormatProjectPatchJob(string, string)
    
    
    public static string FormatProjectPatchJob(string projectId, string patchJobId)

Formats the IDs into the string representation of this [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) with pattern `projects/{project}/patchJobs/{patch_job}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`patchJobId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PatchJob` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) with pattern `projects/{project}/patchJobs/{patch_job}`.  
  
### FromProjectPatchJob(string, string)
    
    
    public static PatchJobName FromProjectPatchJob(string projectId, string patchJobId)

Creates a [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) with the pattern `projects/{project}/patchJobs/{patch_job}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`patchJobId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PatchJob` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)` | A new instance of [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static PatchJobName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)` | A new instance of [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) containing the provided `unparsedResourceName` .  
  
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
    
    
    public static PatchJobName Parse(string patchJobName)

Parses the given resource name string into a new [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) instance.

**Parameter**  
---  
**Name** | **Description**  
`patchJobName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)` | The parsed [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/patchJobs/{patch_job}`



### Parse(string, bool)
    
    
    public static PatchJobName Parse(string patchJobName, bool allowUnparsed)

Parses the given resource name string into a new [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`patchJobName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName#Google_Cloud_OsConfig_V1_PatchJobName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)` | The parsed [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/patchJobs/{patch_job}`

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

### TryParse(string, out PatchJobName)
    
    
    public static bool TryParse(string patchJobName, out PatchJobName result)

Tries to parse the given resource name string into a new [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) instance.

**Parameters**  
---  
**Name** | **Description**  
`patchJobName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)`  
When this method returns, the parsed [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/patchJobs/{patch_job}`



### TryParse(string, bool, out PatchJobName)
    
    
    public static bool TryParse(string patchJobName, bool allowUnparsed, out PatchJobName result)

Tries to parse the given resource name string into a new [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`patchJobName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName#Google_Cloud_OsConfig_V1_PatchJobName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)`  
When this method returns, the parsed [PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/patchJobs/{patch_job}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(PatchJobName, PatchJobName)
    
    
    public static bool operator ==(PatchJobName a, PatchJobName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)`  
The first resource name to compare, or null.  
`b` | `[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(PatchJobName, PatchJobName)
    
    
    public static bool operator !=(PatchJobName a, PatchJobName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)`  
The first resource name to compare, or null.  
`b` | `[PatchJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1/latest/Google.Cloud.OsConfig.V1.PatchJobName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
