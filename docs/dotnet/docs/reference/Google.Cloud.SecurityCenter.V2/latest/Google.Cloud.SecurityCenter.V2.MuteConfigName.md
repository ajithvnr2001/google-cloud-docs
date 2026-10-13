---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName
title: Security Command Center v2 API - Class MuteConfigName (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:36.792724+00:00
---

# Security Command Center v2 API - Class MuteConfigName (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class MuteConfigName (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class MuteConfigName : IResourceName, IEquatable<MuteConfigName>

Reference documentation and code samples for the Security Command Center v2 API class MuteConfigName.

Resource name for the `MuteConfig` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MuteConfigName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### MuteConfigName(string, string)
    
    
    public MuteConfigName(string organizationId, string muteConfigId)

Constructs a new instance of a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) class from the component parts of pattern `organizations/{organization}/muteConfigs/{mute_config}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
  
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
  
### MuteConfigId
    
    
    public string MuteConfigId { get; }

The `MuteConfig` ID. May be `null`, depending on which resource name is contained by this instance.

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
    
    
    public MuteConfigName.ResourceNameType Type { get; }

The [MuteConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string organizationId, string muteConfigId)

Formats the IDs into the string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `organizations/{organization}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `organizations/{organization}/muteConfigs/{mute_config}`.  
  
### FormatFolderLocationMuteConfig(string, string, string)
    
    
    public static string FormatFolderLocationMuteConfig(string folderId, string locationId, string muteConfigId)

Formats the IDs into the string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `folders/{folder}/locations/{location}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `folders/{folder}/locations/{location}/muteConfigs/{mute_config}`.  
  
### FormatFolderMuteConfig(string, string)
    
    
    public static string FormatFolderMuteConfig(string folderId, string muteConfigId)

Formats the IDs into the string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `folders/{folder}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `folders/{folder}/muteConfigs/{mute_config}`.  
  
### FormatOrganizationLocationMuteConfig(string, string, string)
    
    
    public static string FormatOrganizationLocationMuteConfig(string organizationId, string locationId, string muteConfigId)

Formats the IDs into the string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `organizations/{organization}/locations/{location}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `organizations/{organization}/locations/{location}/muteConfigs/{mute_config}`.  
  
### FormatOrganizationMuteConfig(string, string)
    
    
    public static string FormatOrganizationMuteConfig(string organizationId, string muteConfigId)

Formats the IDs into the string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `organizations/{organization}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `organizations/{organization}/muteConfigs/{mute_config}`.  
  
### FormatProjectLocationMuteConfig(string, string, string)
    
    
    public static string FormatProjectLocationMuteConfig(string projectId, string locationId, string muteConfigId)

Formats the IDs into the string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `projects/{project}/locations/{location}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `projects/{project}/locations/{location}/muteConfigs/{mute_config}`.  
  
### FormatProjectMuteConfig(string, string)
    
    
    public static string FormatProjectMuteConfig(string projectId, string muteConfigId)

Formats the IDs into the string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `projects/{project}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with pattern `projects/{project}/muteConfigs/{mute_config}`.  
  
### FromFolderLocationMuteConfig(string, string, string)
    
    
    public static MuteConfigName FromFolderLocationMuteConfig(string folderId, string locationId, string muteConfigId)

Creates a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with the pattern `folders/{folder}/locations/{location}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | A new instance of [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) constructed from the provided ids.  
  
### FromFolderMuteConfig(string, string)
    
    
    public static MuteConfigName FromFolderMuteConfig(string folderId, string muteConfigId)

Creates a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with the pattern `folders/{folder}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | A new instance of [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) constructed from the provided ids.  
  
### FromOrganizationLocationMuteConfig(string, string, string)
    
    
    public static MuteConfigName FromOrganizationLocationMuteConfig(string organizationId, string locationId, string muteConfigId)

Creates a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with the pattern `organizations/{organization}/locations/{location}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | A new instance of [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) constructed from the provided ids.  
  
### FromOrganizationMuteConfig(string, string)
    
    
    public static MuteConfigName FromOrganizationMuteConfig(string organizationId, string muteConfigId)

Creates a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with the pattern `organizations/{organization}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | A new instance of [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) constructed from the provided ids.  
  
### FromProjectLocationMuteConfig(string, string, string)
    
    
    public static MuteConfigName FromProjectLocationMuteConfig(string projectId, string locationId, string muteConfigId)

Creates a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with the pattern `projects/{project}/locations/{location}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | A new instance of [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) constructed from the provided ids.  
  
### FromProjectMuteConfig(string, string)
    
    
    public static MuteConfigName FromProjectMuteConfig(string projectId, string muteConfigId)

Creates a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) with the pattern `projects/{project}/muteConfigs/{mute_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`muteConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MuteConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | A new instance of [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static MuteConfigName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | A new instance of [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static MuteConfigName Parse(string muteConfigName)

Parses the given resource name string into a new [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) instance.

**Parameter**  
---  
**Name** | **Description**  
`muteConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | The parsed [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/muteConfigs/{mute_config}`
  * `organizations/{organization}/locations/{location}/muteConfigs/{mute_config}`
  * `folders/{folder}/muteConfigs/{mute_config}`
  * `folders/{folder}/locations/{location}/muteConfigs/{mute_config}`
  * `projects/{project}/muteConfigs/{mute_config}`
  * `projects/{project}/locations/{location}/muteConfigs/{mute_config}`



### Parse(string, bool)
    
    
    public static MuteConfigName Parse(string muteConfigName, bool allowUnparsed)

Parses the given resource name string into a new [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`muteConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName#Google_Cloud_SecurityCenter_V2_MuteConfigName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)` | The parsed [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/muteConfigs/{mute_config}`
  * `organizations/{organization}/locations/{location}/muteConfigs/{mute_config}`
  * `folders/{folder}/muteConfigs/{mute_config}`
  * `folders/{folder}/locations/{location}/muteConfigs/{mute_config}`
  * `projects/{project}/muteConfigs/{mute_config}`
  * `projects/{project}/locations/{location}/muteConfigs/{mute_config}`



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

### TryParse(string, out MuteConfigName)
    
    
    public static bool TryParse(string muteConfigName, out MuteConfigName result)

Tries to parse the given resource name string into a new [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) instance.

**Parameters**  
---  
**Name** | **Description**  
`muteConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)`  
When this method returns, the parsed [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/muteConfigs/{mute_config}`
  * `organizations/{organization}/locations/{location}/muteConfigs/{mute_config}`
  * `folders/{folder}/muteConfigs/{mute_config}`
  * `folders/{folder}/locations/{location}/muteConfigs/{mute_config}`
  * `projects/{project}/muteConfigs/{mute_config}`
  * `projects/{project}/locations/{location}/muteConfigs/{mute_config}`



### TryParse(string, bool, out MuteConfigName)
    
    
    public static bool TryParse(string muteConfigName, bool allowUnparsed, out MuteConfigName result)

Tries to parse the given resource name string into a new [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`muteConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName#Google_Cloud_SecurityCenter_V2_MuteConfigName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)`  
When this method returns, the parsed [MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/muteConfigs/{mute_config}`
  * `organizations/{organization}/locations/{location}/muteConfigs/{mute_config}`
  * `folders/{folder}/muteConfigs/{mute_config}`
  * `folders/{folder}/locations/{location}/muteConfigs/{mute_config}`
  * `projects/{project}/muteConfigs/{mute_config}`
  * `projects/{project}/locations/{location}/muteConfigs/{mute_config}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(MuteConfigName, MuteConfigName)
    
    
    public static bool operator ==(MuteConfigName a, MuteConfigName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)`  
The first resource name to compare, or null.  
`b` | `[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(MuteConfigName, MuteConfigName)
    
    
    public static bool operator !=(MuteConfigName a, MuteConfigName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)`  
The first resource name to compare, or null.  
`b` | `[MuteConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.MuteConfigName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
