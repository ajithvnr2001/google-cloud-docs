---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName
title: VMware Engine v1 API - Class ExternalAddressName (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:41.653618+00:00
---

# VMware Engine v1 API - Class ExternalAddressName (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  VMware Engine v1 API - Class ExternalAddressName (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.6.0/Google.Cloud.VmwareEngine.V1.ExternalAddressName)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.5.0/Google.Cloud.VmwareEngine.V1.ExternalAddressName)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.4.0/Google.Cloud.VmwareEngine.V1.ExternalAddressName)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.3.0/Google.Cloud.VmwareEngine.V1.ExternalAddressName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.2.0/Google.Cloud.VmwareEngine.V1.ExternalAddressName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.1.0/Google.Cloud.VmwareEngine.V1.ExternalAddressName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/1.0.0/Google.Cloud.VmwareEngine.V1.ExternalAddressName)


    
    
    public sealed class ExternalAddressName : IResourceName, IEquatable<ExternalAddressName>

Reference documentation and code samples for the VMware Engine v1 API class ExternalAddressName.

Resource name for the `ExternalAddress` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExternalAddressName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.VmwareEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1)

## Assembly

Google.Cloud.VmwareEngine.V1.dll

## Constructors 

### ExternalAddressName(string, string, string, string)
    
    
    public ExternalAddressName(string projectId, string locationId, string privateCloudId, string externalAddressId)

Constructs a new instance of a [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) class from the component parts of pattern ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`privateCloudId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PrivateCloud` ID. Must not be `null` or empty.  
`externalAddressId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ExternalAddress` ID. Must not be `null` or empty.  
  
## Properties 

### ExternalAddressId
    
    
    public string ExternalAddressId { get; }

The `ExternalAddress` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### PrivateCloudId
    
    
    public string PrivateCloudId { get; }

The `PrivateCloud` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public ExternalAddressName.ResourceNameType Type { get; }

The [ExternalAddressName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string privateCloudId, string externalAddressId)

Formats the IDs into the string representation of this [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) with pattern ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`privateCloudId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PrivateCloud` ID. Must not be `null` or empty.  
`externalAddressId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ExternalAddress` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) with pattern ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}` .  
  
### FormatProjectLocationPrivateCloudExternalAddress(string, string, string, string)
    
    
    public static string FormatProjectLocationPrivateCloudExternalAddress(string projectId, string locationId, string privateCloudId, string externalAddressId)

Formats the IDs into the string representation of this [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) with pattern ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`privateCloudId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PrivateCloud` ID. Must not be `null` or empty.  
`externalAddressId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ExternalAddress` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) with pattern ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}` .  
  
### FromProjectLocationPrivateCloudExternalAddress(string, string, string, string)
    
    
    public static ExternalAddressName FromProjectLocationPrivateCloudExternalAddress(string projectId, string locationId, string privateCloudId, string externalAddressId)

Creates a [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) with the pattern ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`privateCloudId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `PrivateCloud` ID. Must not be `null` or empty.  
`externalAddressId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ExternalAddress` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)` | A new instance of [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ExternalAddressName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)` | A new instance of [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ExternalAddressName Parse(string externalAddressName)

Parses the given resource name string into a new [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) instance.

**Parameter**  
---  
**Name** | **Description**  
`externalAddressName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)` | The parsed [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}`



### Parse(string, bool)
    
    
    public static ExternalAddressName Parse(string externalAddressName, bool allowUnparsed)

Parses the given resource name string into a new [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`externalAddressName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName#Google_Cloud_VmwareEngine_V1_ExternalAddressName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)` | The parsed [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}`

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

### TryParse(string, out ExternalAddressName)
    
    
    public static bool TryParse(string externalAddressName, out ExternalAddressName result)

Tries to parse the given resource name string into a new [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) instance.

**Parameters**  
---  
**Name** | **Description**  
`externalAddressName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)`  
When this method returns, the parsed [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}`



### TryParse(string, bool, out ExternalAddressName)
    
    
    public static bool TryParse(string externalAddressName, bool allowUnparsed, out ExternalAddressName result)

Tries to parse the given resource name string into a new [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`externalAddressName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName#Google_Cloud_VmwareEngine_V1_ExternalAddressName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)`  
When this method returns, the parsed [ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ExternalAddressName, ExternalAddressName)
    
    
    public static bool operator ==(ExternalAddressName a, ExternalAddressName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)`  
The first resource name to compare, or null.  
`b` | `[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ExternalAddressName, ExternalAddressName)
    
    
    public static bool operator !=(ExternalAddressName a, ExternalAddressName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)`  
The first resource name to compare, or null.  
`b` | `[ExternalAddressName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VmwareEngine.V1/latest/Google.Cloud.VmwareEngine.V1.ExternalAddressName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
