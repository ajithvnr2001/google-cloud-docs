---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName
title: Config Delivery v1 API - Class ResourceBundleName (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:04.789517+00:00
---

# Config Delivery v1 API - Class ResourceBundleName (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1 API - Class ResourceBundleName (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class ResourceBundleName : IResourceName, IEquatable<ResourceBundleName>

Reference documentation and code samples for the Config Delivery v1 API class ResourceBundleName.

Resource name for the `ResourceBundle` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceBundleName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.ConfigDelivery.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1)

## Assembly

Google.Cloud.ConfigDelivery.V1.dll

## Constructors 

### ResourceBundleName(string, string, string)
    
    
    public ResourceBundleName(string projectId, string locationId, string resourceBundleId)

Constructs a new instance of a [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) class from the component parts of pattern `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`resourceBundleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ResourceBundle` ID. Must not be `null` or empty.  
  
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
  
### ResourceBundleId
    
    
    public string ResourceBundleId { get; }

The `ResourceBundle` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ResourceBundleName.ResourceNameType Type { get; }

The [ResourceBundleName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string resourceBundleId)

Formats the IDs into the string representation of this [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) with pattern `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`resourceBundleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ResourceBundle` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) with pattern `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`.  
  
### FormatProjectLocationResourceBundle(string, string, string)
    
    
    public static string FormatProjectLocationResourceBundle(string projectId, string locationId, string resourceBundleId)

Formats the IDs into the string representation of this [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) with pattern `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`resourceBundleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ResourceBundle` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) with pattern `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`.  
  
### FromProjectLocationResourceBundle(string, string, string)
    
    
    public static ResourceBundleName FromProjectLocationResourceBundle(string projectId, string locationId, string resourceBundleId)

Creates a [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) with the pattern `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`resourceBundleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ResourceBundle` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)` | A new instance of [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ResourceBundleName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)` | A new instance of [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ResourceBundleName Parse(string resourceBundleName)

Parses the given resource name string into a new [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) instance.

**Parameter**  
---  
**Name** | **Description**  
`resourceBundleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)` | The parsed [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`



### Parse(string, bool)
    
    
    public static ResourceBundleName Parse(string resourceBundleName, bool allowUnparsed)

Parses the given resource name string into a new [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`resourceBundleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName#Google_Cloud_ConfigDelivery_V1_ResourceBundleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)` | The parsed [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`



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

### TryParse(string, out ResourceBundleName)
    
    
    public static bool TryParse(string resourceBundleName, out ResourceBundleName result)

Tries to parse the given resource name string into a new [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) instance.

**Parameters**  
---  
**Name** | **Description**  
`resourceBundleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)`  
When this method returns, the parsed [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`



### TryParse(string, bool, out ResourceBundleName)
    
    
    public static bool TryParse(string resourceBundleName, bool allowUnparsed, out ResourceBundleName result)

Tries to parse the given resource name string into a new [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`resourceBundleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName#Google_Cloud_ConfigDelivery_V1_ResourceBundleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)`  
When this method returns, the parsed [ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/resourceBundles/{resource_bundle}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ResourceBundleName, ResourceBundleName)
    
    
    public static bool operator ==(ResourceBundleName a, ResourceBundleName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)`  
The first resource name to compare, or null.  
`b` | `[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ResourceBundleName, ResourceBundleName)
    
    
    public static bool operator !=(ResourceBundleName a, ResourceBundleName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)`  
The first resource name to compare, or null.  
`b` | `[ResourceBundleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1/latest/Google.Cloud.ConfigDelivery.V1.ResourceBundleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
