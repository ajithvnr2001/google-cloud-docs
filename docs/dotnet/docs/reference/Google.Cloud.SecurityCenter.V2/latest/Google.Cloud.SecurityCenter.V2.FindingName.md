---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName
title: Security Command Center v2 API - Class FindingName (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:38.697414+00:00
---

# Security Command Center v2 API - Class FindingName (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class FindingName (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class FindingName : IResourceName, IEquatable<FindingName>

Reference documentation and code samples for the Security Command Center v2 API class FindingName.

Resource name for the `Finding` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FindingName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### FindingName(string, string, string)
    
    
    public FindingName(string organizationId, string sourceId, string findingId)

Constructs a new instance of a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) class from the component parts of pattern `organizations/{organization}/sources/{source}/findings/{finding}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
  
## Properties 

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
    
    
    public FindingName.ResourceNameType Type { get; }

The [FindingName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string organizationId, string sourceId, string findingId)

Formats the IDs into the string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}`.  
  
### FormatFolderSourceFinding(string, string, string)
    
    
    public static string FormatFolderSourceFinding(string folderId, string sourceId, string findingId)

Formats the IDs into the string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `folders/{folder}/sources/{source}/findings/{finding}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `folders/{folder}/sources/{source}/findings/{finding}`.  
  
### FormatFolderSourceLocationFinding(string, string, string, string)
    
    
    public static string FormatFolderSourceLocationFinding(string folderId, string sourceId, string locationId, string findingId)

Formats the IDs into the string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `folders/{folder}/sources/{source}/locations/{location}/findings/{finding}`.

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
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `folders/{folder}/sources/{source}/locations/{location}/findings/{finding}`.  
  
### FormatOrganizationSourceFinding(string, string, string)
    
    
    public static string FormatOrganizationSourceFinding(string organizationId, string sourceId, string findingId)

Formats the IDs into the string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `organizations/{organization}/sources/{source}/findings/{finding}`.  
  
### FormatOrganizationSourceLocationFinding(string, string, string, string)
    
    
    public static string FormatOrganizationSourceLocationFinding(string organizationId, string sourceId, string locationId, string findingId)

Formats the IDs into the string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}`.

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
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}`.  
  
### FormatProjectSourceFinding(string, string, string)
    
    
    public static string FormatProjectSourceFinding(string projectId, string sourceId, string findingId)

Formats the IDs into the string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `projects/{project}/sources/{source}/findings/{finding}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `projects/{project}/sources/{source}/findings/{finding}`.  
  
### FormatProjectSourceLocationFinding(string, string, string, string)
    
    
    public static string FormatProjectSourceLocationFinding(string projectId, string sourceId, string locationId, string findingId)

Formats the IDs into the string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `projects/{project}/sources/{source}/locations/{location}/findings/{finding}`.

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
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with pattern `projects/{project}/sources/{source}/locations/{location}/findings/{finding}`.  
  
### FromFolderSourceFinding(string, string, string)
    
    
    public static FindingName FromFolderSourceFinding(string folderId, string sourceId, string findingId)

Creates a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with the pattern `folders/{folder}/sources/{source}/findings/{finding}` .

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | A new instance of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) constructed from the provided ids.  
  
### FromFolderSourceLocationFinding(string, string, string, string)
    
    
    public static FindingName FromFolderSourceLocationFinding(string folderId, string sourceId, string locationId, string findingId)

Creates a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with the pattern `folders/{folder}/sources/{source}/locations/{location}/findings/{finding}`.

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
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | A new instance of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) constructed from the provided ids.  
  
### FromOrganizationSourceFinding(string, string, string)
    
    
    public static FindingName FromOrganizationSourceFinding(string organizationId, string sourceId, string findingId)

Creates a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with the pattern `organizations/{organization}/sources/{source}/findings/{finding}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | A new instance of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) constructed from the provided ids.  
  
### FromOrganizationSourceLocationFinding(string, string, string, string)
    
    
    public static FindingName FromOrganizationSourceLocationFinding(string organizationId, string sourceId, string locationId, string findingId)

Creates a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with the pattern `organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}`.

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
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | A new instance of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) constructed from the provided ids.  
  
### FromProjectSourceFinding(string, string, string)
    
    
    public static FindingName FromProjectSourceFinding(string projectId, string sourceId, string findingId)

Creates a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with the pattern `projects/{project}/sources/{source}/findings/{finding}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`sourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Source` ID. Must not be `null` or empty.  
`findingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Finding` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | A new instance of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) constructed from the provided ids.  
  
### FromProjectSourceLocationFinding(string, string, string, string)
    
    
    public static FindingName FromProjectSourceLocationFinding(string projectId, string sourceId, string locationId, string findingId)

Creates a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) with the pattern `projects/{project}/sources/{source}/locations/{location}/findings/{finding}`.

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
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | A new instance of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static FindingName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | A new instance of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static FindingName Parse(string findingName)

Parses the given resource name string into a new [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) instance.

**Parameter**  
---  
**Name** | **Description**  
`findingName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | The parsed [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}`
  * `organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}`
  * `folders/{folder}/sources/{source}/findings/{finding}`
  * `folders/{folder}/sources/{source}/locations/{location}/findings/{finding}`
  * `projects/{project}/sources/{source}/findings/{finding}`
  * `projects/{project}/sources/{source}/locations/{location}/findings/{finding}`



### Parse(string, bool)
    
    
    public static FindingName Parse(string findingName, bool allowUnparsed)

Parses the given resource name string into a new [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`findingName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName#Google_Cloud_SecurityCenter_V2_FindingName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)` | The parsed [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}`
  * `organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}`
  * `folders/{folder}/sources/{source}/findings/{finding}`
  * `folders/{folder}/sources/{source}/locations/{location}/findings/{finding}`
  * `projects/{project}/sources/{source}/findings/{finding}`
  * `projects/{project}/sources/{source}/locations/{location}/findings/{finding}`



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

### TryParse(string, out FindingName)
    
    
    public static bool TryParse(string findingName, out FindingName result)

Tries to parse the given resource name string into a new [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) instance.

**Parameters**  
---  
**Name** | **Description**  
`findingName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)`  
When this method returns, the parsed [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}`
  * `organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}`
  * `folders/{folder}/sources/{source}/findings/{finding}`
  * `folders/{folder}/sources/{source}/locations/{location}/findings/{finding}`
  * `projects/{project}/sources/{source}/findings/{finding}`
  * `projects/{project}/sources/{source}/locations/{location}/findings/{finding}`



### TryParse(string, bool, out FindingName)
    
    
    public static bool TryParse(string findingName, bool allowUnparsed, out FindingName result)

Tries to parse the given resource name string into a new [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`findingName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName#Google_Cloud_SecurityCenter_V2_FindingName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)`  
When this method returns, the parsed [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/sources/{source}/findings/{finding}`
  * `organizations/{organization}/sources/{source}/locations/{location}/findings/{finding}`
  * `folders/{folder}/sources/{source}/findings/{finding}`
  * `folders/{folder}/sources/{source}/locations/{location}/findings/{finding}`
  * `projects/{project}/sources/{source}/findings/{finding}`
  * `projects/{project}/sources/{source}/locations/{location}/findings/{finding}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(FindingName, FindingName)
    
    
    public static bool operator ==(FindingName a, FindingName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)`  
The first resource name to compare, or null.  
`b` | `[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(FindingName, FindingName)
    
    
    public static bool operator !=(FindingName a, FindingName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)`  
The first resource name to compare, or null.  
`b` | `[FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.FindingName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
