---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName
title: Firestore Admin v1 API - Class BackupScheduleName (3.19.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:30.758070+00:00
---

# Firestore Admin v1 API - Class BackupScheduleName (3.19.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Firestore Admin v1 API - Class BackupScheduleName (3.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.19.0 (latest)  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class BackupScheduleName : IResourceName, IEquatable<BackupScheduleName>

Reference documentation and code samples for the Firestore Admin v1 API class BackupScheduleName.

Resource name for the `BackupSchedule` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackupScheduleName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Firestore.Admin.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1)

## Assembly

Google.Cloud.Firestore.Admin.V1.dll

## Constructors 

### BackupScheduleName(string, string, string)
    
    
    public BackupScheduleName(string projectId, string databaseId, string backupScheduleId)

Constructs a new instance of a [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) class from the component parts of pattern `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Database` ID. Must not be `null` or empty.  
`backupScheduleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupSchedule` ID. Must not be `null` or empty.  
  
## Properties 

### BackupScheduleId
    
    
    public string BackupScheduleId { get; }

The `BackupSchedule` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DatabaseId
    
    
    public string DatabaseId { get; }

The `Database` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public BackupScheduleName.ResourceNameType Type { get; }

The [BackupScheduleName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string databaseId, string backupScheduleId)

Formats the IDs into the string representation of this [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) with pattern `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Database` ID. Must not be `null` or empty.  
`backupScheduleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupSchedule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) with pattern `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`.  
  
### FormatProjectDatabaseBackupSchedule(string, string, string)
    
    
    public static string FormatProjectDatabaseBackupSchedule(string projectId, string databaseId, string backupScheduleId)

Formats the IDs into the string representation of this [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) with pattern `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Database` ID. Must not be `null` or empty.  
`backupScheduleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupSchedule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) with pattern `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`.  
  
### FromProjectDatabaseBackupSchedule(string, string, string)
    
    
    public static BackupScheduleName FromProjectDatabaseBackupSchedule(string projectId, string databaseId, string backupScheduleId)

Creates a [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) with the pattern `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`databaseId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Database` ID. Must not be `null` or empty.  
`backupScheduleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BackupSchedule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)` | A new instance of [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static BackupScheduleName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)` | A new instance of [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static BackupScheduleName Parse(string backupScheduleName)

Parses the given resource name string into a new [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) instance.

**Parameter**  
---  
**Name** | **Description**  
`backupScheduleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)` | The parsed [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`



### Parse(string, bool)
    
    
    public static BackupScheduleName Parse(string backupScheduleName, bool allowUnparsed)

Parses the given resource name string into a new [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`backupScheduleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName#Google_Cloud_Firestore_Admin_V1_BackupScheduleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)` | The parsed [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`



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

### TryParse(string, out BackupScheduleName)
    
    
    public static bool TryParse(string backupScheduleName, out BackupScheduleName result)

Tries to parse the given resource name string into a new [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) instance.

**Parameters**  
---  
**Name** | **Description**  
`backupScheduleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)`  
When this method returns, the parsed [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`



### TryParse(string, bool, out BackupScheduleName)
    
    
    public static bool TryParse(string backupScheduleName, bool allowUnparsed, out BackupScheduleName result)

Tries to parse the given resource name string into a new [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`backupScheduleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName#Google_Cloud_Firestore_Admin_V1_BackupScheduleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)`  
When this method returns, the parsed [BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(BackupScheduleName, BackupScheduleName)
    
    
    public static bool operator ==(BackupScheduleName a, BackupScheduleName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)`  
The first resource name to compare, or null.  
`b` | `[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(BackupScheduleName, BackupScheduleName)
    
    
    public static bool operator !=(BackupScheduleName a, BackupScheduleName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)`  
The first resource name to compare, or null.  
`b` | `[BackupScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.Admin.V1/latest/Google.Cloud.Firestore.Admin.V1.BackupScheduleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
