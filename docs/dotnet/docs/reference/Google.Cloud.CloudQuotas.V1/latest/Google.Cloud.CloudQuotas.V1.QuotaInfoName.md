---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName
title: Cloud Quotas v1 API - Class QuotaInfoName (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:27.198908+00:00
---

# Cloud Quotas v1 API - Class QuotaInfoName (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class QuotaInfoName (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public sealed class QuotaInfoName : IResourceName, IEquatable<QuotaInfoName>

Reference documentation and code samples for the Cloud Quotas v1 API class QuotaInfoName.

Resource name for the `QuotaInfo` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QuotaInfoName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Constructors 

### QuotaInfoName(string, string, string, string)
    
    
    public QuotaInfoName(string projectId, string locationId, string serviceId, string quotaInfoId)

Constructs a new instance of a [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) class from the component parts of pattern `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
  
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
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaInfoId
    
    
    public string QuotaInfoId { get; }

The `QuotaInfo` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceId
    
    
    public string ServiceId { get; }

The `Service` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public QuotaInfoName.ResourceNameType Type { get; }

The [QuotaInfoName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string serviceId, string quotaInfoId)

Formats the IDs into the string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.  
  
### FormatFolderLocationServiceQuotaInfo(string, string, string, string)
    
    
    public static string FormatFolderLocationServiceQuotaInfo(string folderId, string locationId, string serviceId, string quotaInfoId)

Formats the IDs into the string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.  
  
### FormatOrganizationLocationServiceQuotaInfo(string, string, string, string)
    
    
    public static string FormatOrganizationLocationServiceQuotaInfo(string organizationId, string locationId, string serviceId, string quotaInfoId)

Formats the IDs into the string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.  
  
### FormatProjectLocationServiceQuotaInfo(string, string, string, string)
    
    
    public static string FormatProjectLocationServiceQuotaInfo(string projectId, string locationId, string serviceId, string quotaInfoId)

Formats the IDs into the string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with pattern `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.  
  
### FromFolderLocationServiceQuotaInfo(string, string, string, string)
    
    
    public static QuotaInfoName FromFolderLocationServiceQuotaInfo(string folderId, string locationId, string serviceId, string quotaInfoId)

Creates a [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with the pattern `folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)` | A new instance of [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) constructed from the provided ids.  
  
### FromOrganizationLocationServiceQuotaInfo(string, string, string, string)
    
    
    public static QuotaInfoName FromOrganizationLocationServiceQuotaInfo(string organizationId, string locationId, string serviceId, string quotaInfoId)

Creates a [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with the pattern `organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)` | A new instance of [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) constructed from the provided ids.  
  
### FromProjectLocationServiceQuotaInfo(string, string, string, string)
    
    
    public static QuotaInfoName FromProjectLocationServiceQuotaInfo(string projectId, string locationId, string serviceId, string quotaInfoId)

Creates a [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) with the pattern `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`quotaInfoId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `QuotaInfo` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)` | A new instance of [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static QuotaInfoName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)` | A new instance of [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static QuotaInfoName Parse(string quotaInfoName)

Parses the given resource name string into a new [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) instance.

**Parameter**  
---  
**Name** | **Description**  
`quotaInfoName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)` | The parsed [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`



### Parse(string, bool)
    
    
    public static QuotaInfoName Parse(string quotaInfoName, bool allowUnparsed)

Parses the given resource name string into a new [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`quotaInfoName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName#Google_Cloud_CloudQuotas_V1_QuotaInfoName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)` | The parsed [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`



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

### TryParse(string, out QuotaInfoName)
    
    
    public static bool TryParse(string quotaInfoName, out QuotaInfoName result)

Tries to parse the given resource name string into a new [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) instance.

**Parameters**  
---  
**Name** | **Description**  
`quotaInfoName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
When this method returns, the parsed [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`



### TryParse(string, bool, out QuotaInfoName)
    
    
    public static bool TryParse(string quotaInfoName, bool allowUnparsed, out QuotaInfoName result)

Tries to parse the given resource name string into a new [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`quotaInfoName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName#Google_Cloud_CloudQuotas_V1_QuotaInfoName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
When this method returns, the parsed [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `folders/{folder}/locations/{location}/services/{service}/quotaInfos/{quota_info}`
  * `organizations/{organization}/locations/{location}/services/{service}/quotaInfos/{quota_info}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(QuotaInfoName, QuotaInfoName)
    
    
    public static bool operator ==(QuotaInfoName a, QuotaInfoName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
The first resource name to compare, or null.  
`b` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(QuotaInfoName, QuotaInfoName)
    
    
    public static bool operator !=(QuotaInfoName a, QuotaInfoName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
The first resource name to compare, or null.  
`b` | `[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
