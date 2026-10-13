---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName
title: Security Command Center v2 API - Class ExternalSystemName (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:59.597504+00:00
---

# Security Command Center v2 API - Class ExternalSystemName (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class ExternalSystemName (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ExternalSystemName : IResourceName, IEquatable<ExternalSystemName>

Reference documentation and code samples for the Security Command Center v2 API class ExternalSystemName.

Resource name for the `ExternalSystem` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExternalSystemName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### ExternalSystemName(string, string, string, string)
    
    
    public ExternalSystemName(string organizationId, string sourceId, string findingId, string externalsystemId)

Constructs a new instance of a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) class from the component parts of pattern `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
  
## Properties 

### ExternalsystemId
    
    
    public string ExternalsystemId { get; }

The `Externalsystem` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FindingId
    
    
    public string FindingId { get; }

The `Finding` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
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
  
### SourceId
    
    
    public string SourceId { get; }

The `Source` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ExternalSystemName.ResourceNameType Type { get; }

The [ExternalSystemName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string organizationId, string sourceId, string findingId, string externalsystemId)

Formats the IDs into the string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.  
  
### FormatFolderSourceFindingExternalsystem(string, string, string, string)
    
    
    public static string FormatFolderSourceFindingExternalsystem(string folderId, string sourceId, string findingId, string externalsystemId)

Formats the IDs into the string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `folders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `folders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.  
  
### FormatFolderSourceLocationFindingExternalsystem(string, string, string, string, string)
    
    
    public static string FormatFolderSourceLocationFindingExternalsystem(string folderId, string sourceId, string locationId, string findingId, string externalsystemId)

Formats the IDs into the string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern ` folders/{folder}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern ` folders/{folder}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .  
  
### FormatOrganizationSourceFindingExternalsystem(string, string, string, string)
    
    
    public static string FormatOrganizationSourceFindingExternalsystem(string organizationId, string sourceId, string findingId, string externalsystemId)

Formats the IDs into the string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.  
  
### FormatOrganizationSourceLocationFindingExternalsystem(string, string, string, string, string)
    
    
    public static string FormatOrganizationSourceLocationFindingExternalsystem(string organizationId, string sourceId, string locationId, string findingId, string externalsystemId)

Formats the IDs into the string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern ` organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern ` organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .  
  
### FormatProjectSourceFindingExternalsystem(string, string, string, string)
    
    
    public static string FormatProjectSourceFindingExternalsystem(string projectId, string sourceId, string findingId, string externalsystemId)

Formats the IDs into the string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `projects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern `projects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.  
  
### FormatProjectSourceLocationFindingExternalsystem(string, string, string, string, string)
    
    
    public static string FormatProjectSourceLocationFindingExternalsystem(string projectId, string sourceId, string locationId, string findingId, string externalsystemId)

Formats the IDs into the string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern ` projects/{project}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with pattern ` projects/{project}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .  
  
### FromFolderSourceFindingExternalsystem(string, string, string, string)
    
    
    public static ExternalSystemName FromFolderSourceFindingExternalsystem(string folderId, string sourceId, string findingId, string externalsystemId)

Creates a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with the pattern `folders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | A new instance of [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) constructed from the provided ids.  
  
### FromFolderSourceLocationFindingExternalsystem(string, string, string, string, string)
    
    
    public static ExternalSystemName FromFolderSourceLocationFindingExternalsystem(string folderId, string sourceId, string locationId, string findingId, string externalsystemId)

Creates a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with the pattern ` folders/{folder}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | A new instance of [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) constructed from the provided ids.  
  
### FromOrganizationSourceFindingExternalsystem(string, string, string, string)
    
    
    public static ExternalSystemName FromOrganizationSourceFindingExternalsystem(string organizationId, string sourceId, string findingId, string externalsystemId)

Creates a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with the pattern `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | A new instance of [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) constructed from the provided ids.  
  
### FromOrganizationSourceLocationFindingExternalsystem(string, string, string, string, string)
    
    
    public static ExternalSystemName FromOrganizationSourceLocationFindingExternalsystem(string organizationId, string sourceId, string locationId, string findingId, string externalsystemId)

Creates a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with the pattern ` organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | A new instance of [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) constructed from the provided ids.  
  
### FromProjectSourceFindingExternalsystem(string, string, string, string)
    
    
    public static ExternalSystemName FromProjectSourceFindingExternalsystem(string projectId, string sourceId, string findingId, string externalsystemId)

Creates a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with the pattern `projects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | A new instance of [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) constructed from the provided ids.  
  
### FromProjectSourceLocationFindingExternalsystem(string, string, string, string, string)
    
    
    public static ExternalSystemName FromProjectSourceLocationFindingExternalsystem(string projectId, string sourceId, string locationId, string findingId, string externalsystemId)

Creates a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) with the pattern ` projects/{project}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
`externalsystemId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Externalsystem` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | A new instance of [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ExternalSystemName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | A new instance of [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ExternalSystemName Parse(string externalSystemName)

Parses the given resource name string into a new [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) instance.

**Parameter**  
---  
**Name** | **Description**  
`externalSystemName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | The parsed [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `folders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` folders/{folder}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `projects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` projects/{project}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`



### Parse(string, bool)
    
    
    public static ExternalSystemName Parse(string externalSystemName, bool allowUnparsed)

Parses the given resource name string into a new [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`externalSystemName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName#Google_Cloud_SecurityCenter_V2_ExternalSystemName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)` | The parsed [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `folders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` folders/{folder}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `projects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` projects/{project}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`



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

### TryParse(string, out ExternalSystemName)
    
    
    public static bool TryParse(string externalSystemName, out ExternalSystemName result)

Tries to parse the given resource name string into a new [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) instance.

**Parameters**  
---  
**Name** | **Description**  
`externalSystemName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)`  
When this method returns, the parsed [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `folders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` folders/{folder}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `projects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` projects/{project}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`



### TryParse(string, bool, out ExternalSystemName)
    
    
    public static bool TryParse(string externalSystemName, bool allowUnparsed, out ExternalSystemName result)

Tries to parse the given resource name string into a new [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`externalSystemName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName#Google_Cloud_SecurityCenter_V2_ExternalSystemName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)`  
When this method returns, the parsed [ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `folders/{folder}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` folders/{folder}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`
  * `projects/{project}/sources/{source}/findings/{finding}/externalSystems/{externalsystem}`
  * ` projects/{project}/sources/{source}/locations/{location}/findings/{finding}/externalSystems/{externalsystem}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ExternalSystemName, ExternalSystemName)
    
    
    public static bool operator ==(ExternalSystemName a, ExternalSystemName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)`  
The first resource name to compare, or null.  
`b` | `[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ExternalSystemName, ExternalSystemName)
    
    
    public static bool operator !=(ExternalSystemName a, ExternalSystemName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)`  
The first resource name to compare, or null.  
`b` | `[ExternalSystemName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.ExternalSystemName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
