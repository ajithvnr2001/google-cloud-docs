---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName
title: Dataproc Metastore v1 API - Class BackupName (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:49.530624+00:00
---

# Dataproc Metastore v1 API - Class BackupName (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1 API - Class BackupName (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.9.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.8.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.7.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.6.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.5.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.4.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.3.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.2.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.1.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.0.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.1.0/Google.Cloud.Metastore.V1.BackupName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.0.0/Google.Cloud.Metastore.V1.BackupName)


    
    
    public sealed class BackupName : IResourceName, IEquatable<BackupName>

Reference documentation and code samples for the Dataproc Metastore v1 API class BackupName.

Resource name for the `Backup` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackupName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Metastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1)

## Assembly

Google.Cloud.Metastore.V1.dll

## Constructors 

### BackupName(string, string, string, string)
    
    
    public BackupName(string projectId, string locationId, string serviceId, string backupId)

Constructs a new instance of a [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) class from the component parts of pattern `projects/{project}/locations/{location}/services/{service}/backups/{backup}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Backup` ID. Must not be `null` or empty.  
  
## Properties 

### BackupId
    
    
    public string BackupId { get; }

The `Backup` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### ServiceId
    
    
    public string ServiceId { get; }

The `Service` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public BackupName.ResourceNameType Type { get; }

The [BackupName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string serviceId, string backupId)

Formats the IDs into the string representation of this [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) with pattern `projects/{project}/locations/{location}/services/{service}/backups/{backup}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Backup` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) with pattern `projects/{project}/locations/{location}/services/{service}/backups/{backup}`.  
  
### FormatProjectLocationServiceBackup(string, string, string, string)
    
    
    public static string FormatProjectLocationServiceBackup(string projectId, string locationId, string serviceId, string backupId)

Formats the IDs into the string representation of this [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) with pattern `projects/{project}/locations/{location}/services/{service}/backups/{backup}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Backup` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) with pattern `projects/{project}/locations/{location}/services/{service}/backups/{backup}`.  
  
### FromProjectLocationServiceBackup(string, string, string, string)
    
    
    public static BackupName FromProjectLocationServiceBackup(string projectId, string locationId, string serviceId, string backupId)

Creates a [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) with the pattern `projects/{project}/locations/{location}/services/{service}/backups/{backup}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`backupId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Backup` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)` | A new instance of [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static BackupName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)` | A new instance of [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static BackupName Parse(string backupName)

Parses the given resource name string into a new [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) instance.

**Parameter**  
---  
**Name** | **Description**  
`backupName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)` | The parsed [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/backups/{backup}`



### Parse(string, bool)
    
    
    public static BackupName Parse(string backupName, bool allowUnparsed)

Parses the given resource name string into a new [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`backupName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName#Google_Cloud_Metastore_V1_BackupName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)` | The parsed [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/backups/{backup}`

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

### TryParse(string, out BackupName)
    
    
    public static bool TryParse(string backupName, out BackupName result)

Tries to parse the given resource name string into a new [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) instance.

**Parameters**  
---  
**Name** | **Description**  
`backupName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)`  
When this method returns, the parsed [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/backups/{backup}`



### TryParse(string, bool, out BackupName)
    
    
    public static bool TryParse(string backupName, bool allowUnparsed, out BackupName result)

Tries to parse the given resource name string into a new [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`backupName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName#Google_Cloud_Metastore_V1_BackupName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)`  
When this method returns, the parsed [BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/backups/{backup}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(BackupName, BackupName)
    
    
    public static bool operator ==(BackupName a, BackupName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)`  
The first resource name to compare, or null.  
`b` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(BackupName, BackupName)
    
    
    public static bool operator !=(BackupName a, BackupName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)`  
The first resource name to compare, or null.  
`b` | `[BackupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.BackupName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
