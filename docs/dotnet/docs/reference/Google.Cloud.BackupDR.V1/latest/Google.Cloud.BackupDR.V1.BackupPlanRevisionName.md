---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName
title: Backup and DR Service v1 API - Class BackupPlanRevisionName (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:50.545180+00:00
---

# Backup and DR Service v1 API - Class BackupPlanRevisionName (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1 API - Class BackupPlanRevisionName (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.0 (latest)  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.2.0  1.1.0  1.0.0-beta02 
    
    
    public sealed class BackupPlanRevisionName : IResourceName, IEquatable<BackupPlanRevisionName>

Reference documentation and code samples for the Backup and DR Service v1 API class BackupPlanRevisionName.

Resource name for the `BackupPlanRevision` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackupPlanRevisionName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.BackupDR.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1)

## Assembly

Google.Cloud.BackupDR.V1.dll

## Constructors 

### BackupPlanRevisionName(string, string, string, string)
    
    
    public BackupPlanRevisionName(string projectId, string locationId, string backupPlanId, string revisionId)

Constructs a new instance of a [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) class from the component parts of pattern `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`backupPlanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupPlan` ID. Must not be `null` or empty.  
`revisionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Revision` ID. Must not be `null` or empty.  
  
## Properties 

### BackupPlanId
    
    
    public string BackupPlanId { get; }

The `BackupPlan` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### RevisionId
    
    
    public string RevisionId { get; }

The `Revision` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public BackupPlanRevisionName.ResourceNameType Type { get; }

The [BackupPlanRevisionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string backupPlanId, string revisionId)

Formats the IDs into the string representation of this [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) with pattern `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`backupPlanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupPlan` ID. Must not be `null` or empty.  
`revisionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Revision` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) with pattern `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`.  
  
### FormatProjectLocationBackupPlanRevision(string, string, string, string)
    
    
    public static string FormatProjectLocationBackupPlanRevision(string projectId, string locationId, string backupPlanId, string revisionId)

Formats the IDs into the string representation of this [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) with pattern `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`backupPlanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupPlan` ID. Must not be `null` or empty.  
`revisionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Revision` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) with pattern `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`.  
  
### FromProjectLocationBackupPlanRevision(string, string, string, string)
    
    
    public static BackupPlanRevisionName FromProjectLocationBackupPlanRevision(string projectId, string locationId, string backupPlanId, string revisionId)

Creates a [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) with the pattern `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`backupPlanId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupPlan` ID. Must not be `null` or empty.  
`revisionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Revision` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)` | A new instance of [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static BackupPlanRevisionName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)` | A new instance of [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static BackupPlanRevisionName Parse(string backupPlanRevisionName)

Parses the given resource name string into a new [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) instance.

**Parameter**  
---  
**Name** | **Description**  
`backupPlanRevisionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)` | The parsed [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`



### Parse(string, bool)
    
    
    public static BackupPlanRevisionName Parse(string backupPlanRevisionName, bool allowUnparsed)

Parses the given resource name string into a new [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`backupPlanRevisionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName#Google_Cloud_BackupDR_V1_BackupPlanRevisionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)` | The parsed [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`



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

### TryParse(string, out BackupPlanRevisionName)
    
    
    public static bool TryParse(string backupPlanRevisionName, out BackupPlanRevisionName result)

Tries to parse the given resource name string into a new [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) instance.

**Parameters**  
---  
**Name** | **Description**  
`backupPlanRevisionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)`  
When this method returns, the parsed [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`



### TryParse(string, bool, out BackupPlanRevisionName)
    
    
    public static bool TryParse(string backupPlanRevisionName, bool allowUnparsed, out BackupPlanRevisionName result)

Tries to parse the given resource name string into a new [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`backupPlanRevisionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName#Google_Cloud_BackupDR_V1_BackupPlanRevisionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)`  
When this method returns, the parsed [BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(BackupPlanRevisionName, BackupPlanRevisionName)
    
    
    public static bool operator ==(BackupPlanRevisionName a, BackupPlanRevisionName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)`  
The first resource name to compare, or null.  
`b` | `[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(BackupPlanRevisionName, BackupPlanRevisionName)
    
    
    public static bool operator !=(BackupPlanRevisionName a, BackupPlanRevisionName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)`  
The first resource name to compare, or null.  
`b` | `[BackupPlanRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupPlanRevisionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-31 UTC."],[],[]] 
