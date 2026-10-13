---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName
title: AlloyDB v1 API - Class ServiceAttachmentName (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:24.620616+00:00
---

# AlloyDB v1 API - Class ServiceAttachmentName (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1 API - Class ServiceAttachmentName (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ServiceAttachmentName : IResourceName, IEquatable<ServiceAttachmentName>

Reference documentation and code samples for the AlloyDB v1 API class ServiceAttachmentName.

Resource name for the `ServiceAttachment` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceAttachmentName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1)

## Assembly

Google.Cloud.AlloyDb.V1.dll

## Constructors 

### ServiceAttachmentName(string, string, string)
    
    
    public ServiceAttachmentName(string projectId, string regionId, string serviceAttachmentId)

Constructs a new instance of a [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) class from the component parts of pattern `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`serviceAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ServiceAttachment` ID. Must not be `null` or empty.  
  
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
  
### RegionId
    
    
    public string RegionId { get; }

The `Region` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAttachmentId
    
    
    public string ServiceAttachmentId { get; }

The `ServiceAttachment` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ServiceAttachmentName.ResourceNameType Type { get; }

The [ServiceAttachmentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string regionId, string serviceAttachmentId)

Formats the IDs into the string representation of this [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) with pattern `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`serviceAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ServiceAttachment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) with pattern `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.  
  
### FormatProjectRegionServiceAttachment(string, string, string)
    
    
    public static string FormatProjectRegionServiceAttachment(string projectId, string regionId, string serviceAttachmentId)

Formats the IDs into the string representation of this [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) with pattern `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`serviceAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ServiceAttachment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) with pattern `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.  
  
### FromProjectRegionServiceAttachment(string, string, string)
    
    
    public static ServiceAttachmentName FromProjectRegionServiceAttachment(string projectId, string regionId, string serviceAttachmentId)

Creates a [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) with the pattern `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`serviceAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ServiceAttachment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)` | A new instance of [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ServiceAttachmentName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)` | A new instance of [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ServiceAttachmentName Parse(string serviceAttachmentName)

Parses the given resource name string into a new [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) instance.

**Parameter**  
---  
**Name** | **Description**  
`serviceAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)` | The parsed [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`



### Parse(string, bool)
    
    
    public static ServiceAttachmentName Parse(string serviceAttachmentName, bool allowUnparsed)

Parses the given resource name string into a new [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`serviceAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName#Google_Cloud_AlloyDb_V1_ServiceAttachmentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)` | The parsed [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`



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

### TryParse(string, out ServiceAttachmentName)
    
    
    public static bool TryParse(string serviceAttachmentName, out ServiceAttachmentName result)

Tries to parse the given resource name string into a new [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) instance.

**Parameters**  
---  
**Name** | **Description**  
`serviceAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)`  
When this method returns, the parsed [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`



### TryParse(string, bool, out ServiceAttachmentName)
    
    
    public static bool TryParse(string serviceAttachmentName, bool allowUnparsed, out ServiceAttachmentName result)

Tries to parse the given resource name string into a new [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`serviceAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName#Google_Cloud_AlloyDb_V1_ServiceAttachmentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)`  
When this method returns, the parsed [ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/serviceAttachments/{service_attachment}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ServiceAttachmentName, ServiceAttachmentName)
    
    
    public static bool operator ==(ServiceAttachmentName a, ServiceAttachmentName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)`  
The first resource name to compare, or null.  
`b` | `[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ServiceAttachmentName, ServiceAttachmentName)
    
    
    public static bool operator !=(ServiceAttachmentName a, ServiceAttachmentName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)`  
The first resource name to compare, or null.  
`b` | `[ServiceAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.ServiceAttachmentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
