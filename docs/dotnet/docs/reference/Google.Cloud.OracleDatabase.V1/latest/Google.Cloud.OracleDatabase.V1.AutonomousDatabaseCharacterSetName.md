---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName
title: Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseCharacterSetName (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:28.626929+00:00
---

# Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseCharacterSetName (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud v1 API - Class AutonomousDatabaseCharacterSetName (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class AutonomousDatabaseCharacterSetName : IResourceName, IEquatable<AutonomousDatabaseCharacterSetName>

Reference documentation and code samples for the Oracle Database@Google Cloud v1 API class AutonomousDatabaseCharacterSetName.

Resource name for the `AutonomousDatabaseCharacterSet` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutonomousDatabaseCharacterSetName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.OracleDatabase.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1)

## Assembly

Google.Cloud.OracleDatabase.V1.dll

## Constructors 

### AutonomousDatabaseCharacterSetName(string, string, string)
    
    
    public AutonomousDatabaseCharacterSetName(string projectId, string locationId, string autonomousDatabaseCharacterSetId)

Constructs a new instance of a [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) class from the component parts of pattern ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autonomousDatabaseCharacterSetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutonomousDatabaseCharacterSet` ID. Must not be `null` or empty.  
  
## Properties 

### AutonomousDatabaseCharacterSetId
    
    
    public string AutonomousDatabaseCharacterSetId { get; }

The `AutonomousDatabaseCharacterSet` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public AutonomousDatabaseCharacterSetName.ResourceNameType Type { get; }

The [AutonomousDatabaseCharacterSetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string autonomousDatabaseCharacterSetId)

Formats the IDs into the string representation of this [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) with pattern ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autonomousDatabaseCharacterSetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutonomousDatabaseCharacterSet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) with pattern ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}` .  
  
### FormatProjectLocationAutonomousDatabaseCharacterSet(string, string, string)
    
    
    public static string FormatProjectLocationAutonomousDatabaseCharacterSet(string projectId, string locationId, string autonomousDatabaseCharacterSetId)

Formats the IDs into the string representation of this [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) with pattern ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autonomousDatabaseCharacterSetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutonomousDatabaseCharacterSet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) with pattern ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}` .  
  
### FromProjectLocationAutonomousDatabaseCharacterSet(string, string, string)
    
    
    public static AutonomousDatabaseCharacterSetName FromProjectLocationAutonomousDatabaseCharacterSet(string projectId, string locationId, string autonomousDatabaseCharacterSetId)

Creates a [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) with the pattern ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autonomousDatabaseCharacterSetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutonomousDatabaseCharacterSet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)` | A new instance of [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static AutonomousDatabaseCharacterSetName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)` | A new instance of [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static AutonomousDatabaseCharacterSetName Parse(string autonomousDatabaseCharacterSetName)

Parses the given resource name string into a new [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) instance.

**Parameter**  
---  
**Name** | **Description**  
`autonomousDatabaseCharacterSetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)` | The parsed [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}`



### Parse(string, bool)
    
    
    public static AutonomousDatabaseCharacterSetName Parse(string autonomousDatabaseCharacterSetName, bool allowUnparsed)

Parses the given resource name string into a new [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`autonomousDatabaseCharacterSetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName#Google_Cloud_OracleDatabase_V1_AutonomousDatabaseCharacterSetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)` | The parsed [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}`



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

### TryParse(string, out AutonomousDatabaseCharacterSetName)
    
    
    public static bool TryParse(string autonomousDatabaseCharacterSetName, out AutonomousDatabaseCharacterSetName result)

Tries to parse the given resource name string into a new [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) instance.

**Parameters**  
---  
**Name** | **Description**  
`autonomousDatabaseCharacterSetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)`  
When this method returns, the parsed [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}`



### TryParse(string, bool, out AutonomousDatabaseCharacterSetName)
    
    
    public static bool TryParse(string autonomousDatabaseCharacterSetName, bool allowUnparsed, out AutonomousDatabaseCharacterSetName result)

Tries to parse the given resource name string into a new [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`autonomousDatabaseCharacterSetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName#Google_Cloud_OracleDatabase_V1_AutonomousDatabaseCharacterSetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)`  
When this method returns, the parsed [AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(AutonomousDatabaseCharacterSetName, AutonomousDatabaseCharacterSetName)
    
    
    public static bool operator ==(AutonomousDatabaseCharacterSetName a, AutonomousDatabaseCharacterSetName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)`  
The first resource name to compare, or null.  
`b` | `[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(AutonomousDatabaseCharacterSetName, AutonomousDatabaseCharacterSetName)
    
    
    public static bool operator !=(AutonomousDatabaseCharacterSetName a, AutonomousDatabaseCharacterSetName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)`  
The first resource name to compare, or null.  
`b` | `[AutonomousDatabaseCharacterSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OracleDatabase.V1/latest/Google.Cloud.OracleDatabase.V1.AutonomousDatabaseCharacterSetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
