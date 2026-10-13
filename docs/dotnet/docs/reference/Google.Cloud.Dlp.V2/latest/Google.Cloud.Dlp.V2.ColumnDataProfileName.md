---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName
title: Google Cloud Data Loss Prevention v2 API - Class ColumnDataProfileName (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:17.420169+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class ColumnDataProfileName (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class ColumnDataProfileName (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class ColumnDataProfileName : IResourceName, IEquatable<ColumnDataProfileName>

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class ColumnDataProfileName.

Resource name for the `ColumnDataProfile` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ColumnDataProfileName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### ColumnDataProfileName(string, string, string)
    
    
    public ColumnDataProfileName(string organizationId, string locationId, string columnDataProfileId)

Constructs a new instance of a [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) class from the component parts of pattern `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`columnDataProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ColumnDataProfile` ID. Must not be `null` or empty.  
  
## Properties 

### ColumnDataProfileId
    
    
    public string ColumnDataProfileId { get; }

The `ColumnDataProfile` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ColumnDataProfileName.ResourceNameType Type { get; }

The [ColumnDataProfileName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string organizationId, string locationId, string columnDataProfileId)

Formats the IDs into the string representation of this [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with pattern `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`columnDataProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ColumnDataProfile` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with pattern `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`.  
  
### FormatOrganizationLocationColumnDataProfile(string, string, string)
    
    
    public static string FormatOrganizationLocationColumnDataProfile(string organizationId, string locationId, string columnDataProfileId)

Formats the IDs into the string representation of this [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with pattern `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`columnDataProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ColumnDataProfile` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with pattern `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`.  
  
### FormatProjectLocationColumnDataProfile(string, string, string)
    
    
    public static string FormatProjectLocationColumnDataProfile(string projectId, string locationId, string columnDataProfileId)

Formats the IDs into the string representation of this [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with pattern `projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`columnDataProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ColumnDataProfile` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with pattern `projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`.  
  
### FromOrganizationLocationColumnDataProfile(string, string, string)
    
    
    public static ColumnDataProfileName FromOrganizationLocationColumnDataProfile(string organizationId, string locationId, string columnDataProfileId)

Creates a [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with the pattern `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`columnDataProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ColumnDataProfile` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)` | A new instance of [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) constructed from the provided ids.  
  
### FromProjectLocationColumnDataProfile(string, string, string)
    
    
    public static ColumnDataProfileName FromProjectLocationColumnDataProfile(string projectId, string locationId, string columnDataProfileId)

Creates a [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) with the pattern `projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`columnDataProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ColumnDataProfile` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)` | A new instance of [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ColumnDataProfileName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)` | A new instance of [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ColumnDataProfileName Parse(string columnDataProfileName)

Parses the given resource name string into a new [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) instance.

**Parameter**  
---  
**Name** | **Description**  
`columnDataProfileName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)` | The parsed [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`
  * `projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`



### Parse(string, bool)
    
    
    public static ColumnDataProfileName Parse(string columnDataProfileName, bool allowUnparsed)

Parses the given resource name string into a new [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`columnDataProfileName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName#Google_Cloud_Dlp_V2_ColumnDataProfileName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)` | The parsed [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`
  * `projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`



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

### TryParse(string, out ColumnDataProfileName)
    
    
    public static bool TryParse(string columnDataProfileName, out ColumnDataProfileName result)

Tries to parse the given resource name string into a new [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) instance.

**Parameters**  
---  
**Name** | **Description**  
`columnDataProfileName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)`  
When this method returns, the parsed [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`
  * `projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`



### TryParse(string, bool, out ColumnDataProfileName)
    
    
    public static bool TryParse(string columnDataProfileName, bool allowUnparsed, out ColumnDataProfileName result)

Tries to parse the given resource name string into a new [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`columnDataProfileName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName#Google_Cloud_Dlp_V2_ColumnDataProfileName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)`  
When this method returns, the parsed [ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/columnDataProfiles/{column_data_profile}`
  * `projects/{project}/locations/{location}/columnDataProfiles/{column_data_profile}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ColumnDataProfileName, ColumnDataProfileName)
    
    
    public static bool operator ==(ColumnDataProfileName a, ColumnDataProfileName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)`  
The first resource name to compare, or null.  
`b` | `[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ColumnDataProfileName, ColumnDataProfileName)
    
    
    public static bool operator !=(ColumnDataProfileName a, ColumnDataProfileName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)`  
The first resource name to compare, or null.  
`b` | `[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
