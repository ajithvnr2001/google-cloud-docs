---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName
title: Network Connectivity v1alpha1 API - Class VpnTunnelName (2.0.0-alpha05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:54.413552+00:00
---

# Network Connectivity v1alpha1 API - Class VpnTunnelName (2.0.0-alpha05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1alpha1 API - Class VpnTunnelName (2.0.0-alpha05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)
  * [ 2.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/2.0.0-alpha04/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)
  * [ 1.0.0-alpha03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/1.0.0-alpha03/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)


    
    
    public sealed class VpnTunnelName : IResourceName, IEquatable<VpnTunnelName>

Reference documentation and code samples for the Network Connectivity v1alpha1 API class VpnTunnelName.

Resource name for the `VpnTunnel` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VpnTunnelName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Alpha1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1)

## Assembly

Google.Cloud.NetworkConnectivity.V1Alpha1.dll

## Constructors 

### VpnTunnelName(string, string, string)
    
    
    public VpnTunnelName(string projectId, string regionId, string resourceId)

Constructs a new instance of a [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) class from the component parts of pattern `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`resourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Resource` ID. Must not be `null` or empty.  
  
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
  
### ResourceId
    
    
    public string ResourceId { get; }

The `Resource` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public VpnTunnelName.ResourceNameType Type { get; }

The [VpnTunnelName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string regionId, string resourceId)

Formats the IDs into the string representation of this [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) with pattern `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`resourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Resource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) with pattern `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`.  
  
### FormatProjectRegionResource(string, string, string)
    
    
    public static string FormatProjectRegionResource(string projectId, string regionId, string resourceId)

Formats the IDs into the string representation of this [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) with pattern `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`resourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Resource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) with pattern `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`.  
  
### FromProjectRegionResource(string, string, string)
    
    
    public static VpnTunnelName FromProjectRegionResource(string projectId, string regionId, string resourceId)

Creates a [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) with the pattern `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`resourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Resource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)` | A new instance of [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static VpnTunnelName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)` | A new instance of [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static VpnTunnelName Parse(string vpnTunnelName)

Parses the given resource name string into a new [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) instance.

**Parameter**  
---  
**Name** | **Description**  
`vpnTunnelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)` | The parsed [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`



### Parse(string, bool)
    
    
    public static VpnTunnelName Parse(string vpnTunnelName, bool allowUnparsed)

Parses the given resource name string into a new [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`vpnTunnelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName#Google_Cloud_NetworkConnectivity_V1Alpha1_VpnTunnelName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)` | The parsed [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`

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

### TryParse(string, out VpnTunnelName)
    
    
    public static bool TryParse(string vpnTunnelName, out VpnTunnelName result)

Tries to parse the given resource name string into a new [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) instance.

**Parameters**  
---  
**Name** | **Description**  
`vpnTunnelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)`  
When this method returns, the parsed [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`



### TryParse(string, bool, out VpnTunnelName)
    
    
    public static bool TryParse(string vpnTunnelName, bool allowUnparsed, out VpnTunnelName result)

Tries to parse the given resource name string into a new [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`vpnTunnelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName#Google_Cloud_NetworkConnectivity_V1Alpha1_VpnTunnelName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)`  
When this method returns, the parsed [VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/regions/{region}/vpnTunnels/{resource_id}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(VpnTunnelName, VpnTunnelName)
    
    
    public static bool operator ==(VpnTunnelName a, VpnTunnelName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)`  
The first resource name to compare, or null.  
`b` | `[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(VpnTunnelName, VpnTunnelName)
    
    
    public static bool operator !=(VpnTunnelName a, VpnTunnelName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)`  
The first resource name to compare, or null.  
`b` | `[VpnTunnelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.VpnTunnelName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
