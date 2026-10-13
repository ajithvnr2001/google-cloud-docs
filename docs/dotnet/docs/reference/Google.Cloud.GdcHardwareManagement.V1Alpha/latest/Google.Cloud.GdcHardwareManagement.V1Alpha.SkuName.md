---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName
title: GDC Hardware Management v1alpha API - Class SkuName (1.0.0-alpha08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:16.019555+00:00
---

# GDC Hardware Management v1alpha API - Class SkuName (1.0.0-alpha08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GDC Hardware Management v1alpha API - Class SkuName (1.0.0-alpha08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-alpha08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)
  * [ 1.0.0-alpha07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/1.0.0-alpha07/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)


    
    
    public sealed class SkuName : IResourceName, IEquatable<SkuName>

Reference documentation and code samples for the GDC Hardware Management v1alpha API class SkuName.

Resource name for the `Sku` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SkuName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.GdcHardwareManagement.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha)

## Assembly

Google.Cloud.GdcHardwareManagement.V1Alpha.dll

## Constructors 

### SkuName(string, string, string)
    
    
    public SkuName(string projectId, string locationId, string skuId)

Constructs a new instance of a [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) class from the component parts of pattern `projects/{project}/locations/{location}/skus/{sku}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`skuId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Sku` ID. Must not be `null` or empty.  
  
## Properties 

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
  
### SkuId
    
    
    public string SkuId { get; }

The `Sku` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public SkuName.ResourceNameType Type { get; }

The [SkuName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string skuId)

Formats the IDs into the string representation of this [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) with pattern `projects/{project}/locations/{location}/skus/{sku}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`skuId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Sku` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) with pattern `projects/{project}/locations/{location}/skus/{sku}`.  
  
### FormatProjectLocationSku(string, string, string)
    
    
    public static string FormatProjectLocationSku(string projectId, string locationId, string skuId)

Formats the IDs into the string representation of this [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) with pattern `projects/{project}/locations/{location}/skus/{sku}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`skuId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Sku` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) with pattern `projects/{project}/locations/{location}/skus/{sku}`.  
  
### FromProjectLocationSku(string, string, string)
    
    
    public static SkuName FromProjectLocationSku(string projectId, string locationId, string skuId)

Creates a [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) with the pattern `projects/{project}/locations/{location}/skus/{sku}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`skuId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Sku` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)` | A new instance of [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static SkuName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)` | A new instance of [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static SkuName Parse(string skuName)

Parses the given resource name string into a new [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) instance.

**Parameter**  
---  
**Name** | **Description**  
`skuName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)` | The parsed [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/skus/{sku}`



### Parse(string, bool)
    
    
    public static SkuName Parse(string skuName, bool allowUnparsed)

Parses the given resource name string into a new [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`skuName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName#Google_Cloud_GdcHardwareManagement_V1Alpha_SkuName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)` | The parsed [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/skus/{sku}`



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

### TryParse(string, out SkuName)
    
    
    public static bool TryParse(string skuName, out SkuName result)

Tries to parse the given resource name string into a new [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) instance.

**Parameters**  
---  
**Name** | **Description**  
`skuName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)`  
When this method returns, the parsed [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/skus/{sku}`



### TryParse(string, bool, out SkuName)
    
    
    public static bool TryParse(string skuName, bool allowUnparsed, out SkuName result)

Tries to parse the given resource name string into a new [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`skuName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName#Google_Cloud_GdcHardwareManagement_V1Alpha_SkuName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)`  
When this method returns, the parsed [SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/skus/{sku}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(SkuName, SkuName)
    
    
    public static bool operator ==(SkuName a, SkuName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)`  
The first resource name to compare, or null.  
`b` | `[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(SkuName, SkuName)
    
    
    public static bool operator !=(SkuName a, SkuName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)`  
The first resource name to compare, or null.  
`b` | `[SkuName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.SkuName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
