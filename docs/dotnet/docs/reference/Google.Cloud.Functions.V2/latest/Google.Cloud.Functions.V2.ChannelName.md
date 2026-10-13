---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName
title: Cloud Functions v2 API - Class ChannelName (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:42.915388+00:00
---

# Cloud Functions v2 API - Class ChannelName (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2 API - Class ChannelName (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.7.0/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.6.0/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.5.0/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.4.0/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.3.0/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.2.0/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.1.0/Google.Cloud.Functions.V2.ChannelName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/1.0.0/Google.Cloud.Functions.V2.ChannelName)


    
    
    public sealed class ChannelName : IResourceName, IEquatable<ChannelName>

Reference documentation and code samples for the Cloud Functions v2 API class ChannelName.

Resource name for the `Channel` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ChannelName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Functions.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2)

## Assembly

Google.Cloud.Functions.V2.dll

## Constructors 

### ChannelName(string, string, string)
    
    
    public ChannelName(string projectId, string locationId, string channelId)

Constructs a new instance of a [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) class from the component parts of pattern `projects/{project}/locations/{location}/channels/{channel}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`channelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Channel` ID. Must not be `null` or empty.  
  
## Properties 

### ChannelId
    
    
    public string ChannelId { get; }

The `Channel` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public ChannelName.ResourceNameType Type { get; }

The [ChannelName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string channelId)

Formats the IDs into the string representation of this [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) with pattern `projects/{project}/locations/{location}/channels/{channel}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`channelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Channel` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) with pattern `projects/{project}/locations/{location}/channels/{channel}`.  
  
### FormatProjectLocationChannel(string, string, string)
    
    
    public static string FormatProjectLocationChannel(string projectId, string locationId, string channelId)

Formats the IDs into the string representation of this [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) with pattern `projects/{project}/locations/{location}/channels/{channel}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`channelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Channel` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) with pattern `projects/{project}/locations/{location}/channels/{channel}`.  
  
### FromProjectLocationChannel(string, string, string)
    
    
    public static ChannelName FromProjectLocationChannel(string projectId, string locationId, string channelId)

Creates a [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) with the pattern `projects/{project}/locations/{location}/channels/{channel}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`channelId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Channel` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)` | A new instance of [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ChannelName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)` | A new instance of [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ChannelName Parse(string channelName)

Parses the given resource name string into a new [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) instance.

**Parameter**  
---  
**Name** | **Description**  
`channelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)` | The parsed [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/channels/{channel}`



### Parse(string, bool)
    
    
    public static ChannelName Parse(string channelName, bool allowUnparsed)

Parses the given resource name string into a new [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`channelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName#Google_Cloud_Functions_V2_ChannelName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)` | The parsed [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/channels/{channel}`

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

### TryParse(string, out ChannelName)
    
    
    public static bool TryParse(string channelName, out ChannelName result)

Tries to parse the given resource name string into a new [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) instance.

**Parameters**  
---  
**Name** | **Description**  
`channelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)`  
When this method returns, the parsed [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/channels/{channel}`



### TryParse(string, bool, out ChannelName)
    
    
    public static bool TryParse(string channelName, bool allowUnparsed, out ChannelName result)

Tries to parse the given resource name string into a new [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`channelName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName#Google_Cloud_Functions_V2_ChannelName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)`  
When this method returns, the parsed [ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/channels/{channel}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ChannelName, ChannelName)
    
    
    public static bool operator ==(ChannelName a, ChannelName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)`  
The first resource name to compare, or null.  
`b` | `[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ChannelName, ChannelName)
    
    
    public static bool operator !=(ChannelName a, ChannelName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)`  
The first resource name to compare, or null.  
`b` | `[ChannelName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2/latest/Google.Cloud.Functions.V2.ChannelName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
