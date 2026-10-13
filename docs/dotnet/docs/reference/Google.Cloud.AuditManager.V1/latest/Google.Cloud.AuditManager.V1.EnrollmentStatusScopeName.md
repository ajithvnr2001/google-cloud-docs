---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName
title: Audit Manager v1 API - Class EnrollmentStatusScopeName (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:41.765576+00:00
---

# Audit Manager v1 API - Class EnrollmentStatusScopeName (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Audit Manager v1 API - Class EnrollmentStatusScopeName (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class EnrollmentStatusScopeName : IResourceName, IEquatable<EnrollmentStatusScopeName>

Reference documentation and code samples for the Audit Manager v1 API class EnrollmentStatusScopeName.

Resource name for the `EnrollmentStatusScope` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EnrollmentStatusScopeName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.AuditManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1)

## Assembly

Google.Cloud.AuditManager.V1.dll

## Constructors 

### EnrollmentStatusScopeName(string, string)
    
    
    public EnrollmentStatusScopeName(string folderId, string locationId)

Constructs a new instance of a [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) class from the component parts of pattern `folders/{folder}/locations/{location}`

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
  
### LocationId
    
    
    public string LocationId { get; }

The `Location` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrganizationId
    
    
    public string OrganizationId { get; }

The `Organization` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public EnrollmentStatusScopeName.ResourceNameType Type { get; }

The [EnrollmentStatusScopeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName.ResourceNameType)` |   
  
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

Formats the IDs into the string representation of this [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with pattern `folders/{folder}/locations/{location}`.

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
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with pattern `folders/{folder}/locations/{location}`.  
  
### FormatFolderLocation(string, string)
    
    
    public static string FormatFolderLocation(string folderId, string locationId)

Formats the IDs into the string representation of this [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with pattern `folders/{folder}/locations/{location}`.

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
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with pattern `folders/{folder}/locations/{location}`.  
  
### FormatOrganizationLocation(string, string)
    
    
    public static string FormatOrganizationLocation(string organizationId, string locationId)

Formats the IDs into the string representation of this [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with pattern `organizations/{organization}/locations/{location}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with pattern `organizations/{organization}/locations/{location}`.  
  
### FromFolderLocation(string, string)
    
    
    public static EnrollmentStatusScopeName FromFolderLocation(string folderId, string locationId)

Creates a [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with the pattern `folders/{folder}/locations/{location}` .

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
`[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)` | A new instance of [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) constructed from the provided ids.  
  
### FromOrganizationLocation(string, string)
    
    
    public static EnrollmentStatusScopeName FromOrganizationLocation(string organizationId, string locationId)

Creates a [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) with the pattern `organizations/{organization}/locations/{location}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)` | A new instance of [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static EnrollmentStatusScopeName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)` | A new instance of [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static EnrollmentStatusScopeName Parse(string enrollmentStatusScopeName)

Parses the given resource name string into a new [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) instance.

**Parameter**  
---  
**Name** | **Description**  
`enrollmentStatusScopeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)` | The parsed [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



### Parse(string, bool)
    
    
    public static EnrollmentStatusScopeName Parse(string enrollmentStatusScopeName, bool allowUnparsed)

Parses the given resource name string into a new [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`enrollmentStatusScopeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName#Google_Cloud_AuditManager_V1_EnrollmentStatusScopeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)` | The parsed [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



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

### TryParse(string, out EnrollmentStatusScopeName)
    
    
    public static bool TryParse(string enrollmentStatusScopeName, out EnrollmentStatusScopeName result)

Tries to parse the given resource name string into a new [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) instance.

**Parameters**  
---  
**Name** | **Description**  
`enrollmentStatusScopeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)`  
When this method returns, the parsed [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



### TryParse(string, bool, out EnrollmentStatusScopeName)
    
    
    public static bool TryParse(string enrollmentStatusScopeName, bool allowUnparsed, out EnrollmentStatusScopeName result)

Tries to parse the given resource name string into a new [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`enrollmentStatusScopeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName#Google_Cloud_AuditManager_V1_EnrollmentStatusScopeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)`  
When this method returns, the parsed [EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(EnrollmentStatusScopeName, EnrollmentStatusScopeName)
    
    
    public static bool operator ==(EnrollmentStatusScopeName a, EnrollmentStatusScopeName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)`  
The first resource name to compare, or null.  
`b` | `[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(EnrollmentStatusScopeName, EnrollmentStatusScopeName)
    
    
    public static bool operator !=(EnrollmentStatusScopeName a, EnrollmentStatusScopeName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)`  
The first resource name to compare, or null.  
`b` | `[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
