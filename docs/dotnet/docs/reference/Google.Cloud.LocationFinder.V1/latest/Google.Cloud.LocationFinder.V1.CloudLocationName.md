---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName
title: Cloud Location Finder v1 API - Class CloudLocationName (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:55.788079+00:00
---

# Cloud Location Finder v1 API - Class CloudLocationName (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Location Finder v1 API - Class CloudLocationName (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class CloudLocationName : IResourceName, IEquatable<CloudLocationName>

Reference documentation and code samples for the Cloud Location Finder v1 API class CloudLocationName.

Resource name for the `CloudLocation` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudLocationName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.LocationFinder.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1)

## Assembly

Google.Cloud.LocationFinder.V1.dll

## Constructors 

### CloudLocationName(string, string, string)
    
    
    public CloudLocationName(string projectId, string locationId, string cloudLocationId)

Constructs a new instance of a [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) class from the component parts of pattern `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudLocationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudLocation` ID. Must not be `null` or empty.  
  
## Properties 

### CloudLocationId
    
    
    public string CloudLocationId { get; }

The `CloudLocation` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public CloudLocationName.ResourceNameType Type { get; }

The [CloudLocationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string cloudLocationId)

Formats the IDs into the string representation of this [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) with pattern `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudLocationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudLocation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) with pattern `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`.  
  
### FormatProjectLocationCloudLocation(string, string, string)
    
    
    public static string FormatProjectLocationCloudLocation(string projectId, string locationId, string cloudLocationId)

Formats the IDs into the string representation of this [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) with pattern `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudLocationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudLocation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) with pattern `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`.  
  
### FromProjectLocationCloudLocation(string, string, string)
    
    
    public static CloudLocationName FromProjectLocationCloudLocation(string projectId, string locationId, string cloudLocationId)

Creates a [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) with the pattern `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`cloudLocationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `CloudLocation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` | A new instance of [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static CloudLocationName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` | A new instance of [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static CloudLocationName Parse(string cloudLocationName)

Parses the given resource name string into a new [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) instance.

**Parameter**  
---  
**Name** | **Description**  
`cloudLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` | The parsed [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`



### Parse(string, bool)
    
    
    public static CloudLocationName Parse(string cloudLocationName, bool allowUnparsed)

Parses the given resource name string into a new [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`cloudLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName#Google_Cloud_LocationFinder_V1_CloudLocationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)` | The parsed [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`



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

### TryParse(string, out CloudLocationName)
    
    
    public static bool TryParse(string cloudLocationName, out CloudLocationName result)

Tries to parse the given resource name string into a new [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) instance.

**Parameters**  
---  
**Name** | **Description**  
`cloudLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
When this method returns, the parsed [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`



### TryParse(string, bool, out CloudLocationName)
    
    
    public static bool TryParse(string cloudLocationName, bool allowUnparsed, out CloudLocationName result)

Tries to parse the given resource name string into a new [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`cloudLocationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName#Google_Cloud_LocationFinder_V1_CloudLocationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
When this method returns, the parsed [CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/cloudLocations/{cloud_location}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(CloudLocationName, CloudLocationName)
    
    
    public static bool operator ==(CloudLocationName a, CloudLocationName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
The first resource name to compare, or null.  
`b` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(CloudLocationName, CloudLocationName)
    
    
    public static bool operator !=(CloudLocationName a, CloudLocationName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
The first resource name to compare, or null.  
`b` | `[CloudLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.LocationFinder.V1/latest/Google.Cloud.LocationFinder.V1.CloudLocationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
