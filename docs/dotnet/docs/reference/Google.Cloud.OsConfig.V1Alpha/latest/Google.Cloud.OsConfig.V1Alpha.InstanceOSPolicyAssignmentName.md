---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName
title: Google Cloud OS Config v1alpha API - Class InstanceOSPolicyAssignmentName (2.0.0-alpha07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:46.644702+00:00
---

# Google Cloud OS Config v1alpha API - Class InstanceOSPolicyAssignmentName (2.0.0-alpha07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Config v1alpha API - Class InstanceOSPolicyAssignmentName (2.0.0-alpha07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)
  * [ 2.0.0-alpha06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/2.0.0-alpha06/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/1.0.0-alpha04/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)


    
    
    public sealed class InstanceOSPolicyAssignmentName : IResourceName, IEquatable<InstanceOSPolicyAssignmentName>

Reference documentation and code samples for the Google Cloud OS Config v1alpha API class InstanceOSPolicyAssignmentName.

Resource name for the `InstanceOSPolicyAssignment` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InstanceOSPolicyAssignmentName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.OsConfig.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha)

## Assembly

Google.Cloud.OsConfig.V1Alpha.dll

## Constructors 

### InstanceOSPolicyAssignmentName(string, string, string, string)
    
    
    public InstanceOSPolicyAssignmentName(string projectId, string locationId, string instanceId, string assignmentId)

Constructs a new instance of a [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) class from the component parts of pattern `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Instance` ID. Must not be `null` or empty.  
`assignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Assignment` ID. Must not be `null` or empty.  
  
## Properties 

### AssignmentId
    
    
    public string AssignmentId { get; }

The `Assignment` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceId
    
    
    public string InstanceId { get; }

The `Instance` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public InstanceOSPolicyAssignmentName.ResourceNameType Type { get; }

The [InstanceOSPolicyAssignmentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string instanceId, string assignmentId)

Formats the IDs into the string representation of this [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) with pattern `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Instance` ID. Must not be `null` or empty.  
`assignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Assignment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) with pattern `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`.  
  
### FormatProjectLocationInstanceAssignment(string, string, string, string)
    
    
    public static string FormatProjectLocationInstanceAssignment(string projectId, string locationId, string instanceId, string assignmentId)

Formats the IDs into the string representation of this [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) with pattern `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Instance` ID. Must not be `null` or empty.  
`assignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Assignment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) with pattern `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`.  
  
### FromProjectLocationInstanceAssignment(string, string, string, string)
    
    
    public static InstanceOSPolicyAssignmentName FromProjectLocationInstanceAssignment(string projectId, string locationId, string instanceId, string assignmentId)

Creates a [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) with the pattern `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`instanceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Instance` ID. Must not be `null` or empty.  
`assignmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Assignment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)` | A new instance of [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static InstanceOSPolicyAssignmentName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)` | A new instance of [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static InstanceOSPolicyAssignmentName Parse(string instanceOSPolicyAssignmentName)

Parses the given resource name string into a new [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) instance.

**Parameter**  
---  
**Name** | **Description**  
`instanceOSPolicyAssignmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)` | The parsed [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`



### Parse(string, bool)
    
    
    public static InstanceOSPolicyAssignmentName Parse(string instanceOSPolicyAssignmentName, bool allowUnparsed)

Parses the given resource name string into a new [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`instanceOSPolicyAssignmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName#Google_Cloud_OsConfig_V1Alpha_InstanceOSPolicyAssignmentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)` | The parsed [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`

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

### TryParse(string, out InstanceOSPolicyAssignmentName)
    
    
    public static bool TryParse(string instanceOSPolicyAssignmentName, out InstanceOSPolicyAssignmentName result)

Tries to parse the given resource name string into a new [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceOSPolicyAssignmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
When this method returns, the parsed [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`



### TryParse(string, bool, out InstanceOSPolicyAssignmentName)
    
    
    public static bool TryParse(string instanceOSPolicyAssignmentName, bool allowUnparsed, out InstanceOSPolicyAssignmentName result)

Tries to parse the given resource name string into a new [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`instanceOSPolicyAssignmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName#Google_Cloud_OsConfig_V1Alpha_InstanceOSPolicyAssignmentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
When this method returns, the parsed [InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/instances/{instance}/osPolicyAssignments/{assignment}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(InstanceOSPolicyAssignmentName, InstanceOSPolicyAssignmentName)
    
    
    public static bool operator ==(InstanceOSPolicyAssignmentName a, InstanceOSPolicyAssignmentName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
The first resource name to compare, or null.  
`b` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(InstanceOSPolicyAssignmentName, InstanceOSPolicyAssignmentName)
    
    
    public static bool operator !=(InstanceOSPolicyAssignmentName a, InstanceOSPolicyAssignmentName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
The first resource name to compare, or null.  
`b` | `[InstanceOSPolicyAssignmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsConfig.V1Alpha/latest/Google.Cloud.OsConfig.V1Alpha.InstanceOSPolicyAssignmentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
