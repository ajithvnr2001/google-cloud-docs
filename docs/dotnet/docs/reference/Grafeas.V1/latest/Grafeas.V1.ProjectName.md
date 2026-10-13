---
url: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName
title: Grafeas v1 API - Class ProjectName (3.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:48.641709+00:00
---

# Grafeas v1 API - Class ProjectName (3.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Grafeas v1 API - Class ProjectName (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ProjectName : IResourceName, IEquatable<ProjectName>

Reference documentation and code samples for the Grafeas v1 API class ProjectName.

Resource name for the `Project` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProjectName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Grafeas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1)

## Assembly

Grafeas.V1.dll

## Constructors 

### ProjectName(string)
    
    
    public ProjectName(string projectId)

Constructs a new instance of a [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) class from the component parts of pattern `projects/{project}`

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
  
## Properties 

### IsKnownPattern
    
    
    public bool IsKnownPattern { get; }

Whether this instance contains a resource name with a known pattern.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ProjectName.ResourceNameType Type { get; }

The [ProjectName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string)
    
    
    public static string Format(string projectId)

Formats the IDs into the string representation of this [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) with pattern `projects/{project}`.

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) with pattern `projects/{project}`.  
  
### FormatProject(string)
    
    
    public static string FormatProject(string projectId)

Formats the IDs into the string representation of this [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) with pattern `projects/{project}`.

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) with pattern `projects/{project}`.  
  
### FromProject(string)
    
    
    public static ProjectName FromProject(string projectId)

Creates a [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) with the pattern `projects/{project}`.

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)` | A new instance of [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ProjectName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)` | A new instance of [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ProjectName Parse(string projectName)

Parses the given resource name string into a new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) instance.

**Parameter**  
---  
**Name** | **Description**  
`projectName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)` | The parsed [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}`



### Parse(string, bool)
    
    
    public static ProjectName Parse(string projectName, bool allowUnparsed)

Parses the given resource name string into a new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`projectName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName#Grafeas_V1_ProjectName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)` | The parsed [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}`



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

### TryParse(string, out ProjectName)
    
    
    public static bool TryParse(string projectName, out ProjectName result)

Tries to parse the given resource name string into a new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) instance.

**Parameters**  
---  
**Name** | **Description**  
`projectName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)`  
When this method returns, the parsed [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}`



### TryParse(string, bool, out ProjectName)
    
    
    public static bool TryParse(string projectName, bool allowUnparsed, out ProjectName result)

Tries to parse the given resource name string into a new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`projectName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName#Grafeas_V1_ProjectName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)`  
When this method returns, the parsed [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ProjectName, ProjectName)
    
    
    public static bool operator ==(ProjectName a, ProjectName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)`  
The first resource name to compare, or null.  
`b` | `[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ProjectName, ProjectName)
    
    
    public static bool operator !=(ProjectName a, ProjectName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)`  
The first resource name to compare, or null.  
`b` | `[ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Grafeas.V1/latest/Grafeas.V1.ProjectName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
