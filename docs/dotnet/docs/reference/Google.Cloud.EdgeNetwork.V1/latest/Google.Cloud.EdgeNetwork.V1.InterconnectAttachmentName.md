---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName
title: Distributed Cloud Edge Network v1 API - Class InterconnectAttachmentName (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:32.060153+00:00
---

# Distributed Cloud Edge Network v1 API - Class InterconnectAttachmentName (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network v1 API - Class InterconnectAttachmentName (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.5.0/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.4.0/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.3.0/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.2.0/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.1.0/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.0.0/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)


    
    
    public sealed class InterconnectAttachmentName : IResourceName, IEquatable<InterconnectAttachmentName>

Reference documentation and code samples for the Distributed Cloud Edge Network v1 API class InterconnectAttachmentName.

Resource name for the `InterconnectAttachment` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InterconnectAttachmentName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.EdgeNetwork.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1)

## Assembly

Google.Cloud.EdgeNetwork.V1.dll

## Constructors 

### InterconnectAttachmentName(string, string, string, string)
    
    
    public InterconnectAttachmentName(string projectId, string locationId, string zoneId, string interconnectAttachmentId)

Constructs a new instance of a [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) class from the component parts of pattern `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`zoneId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Zone` ID. Must not be `null` or empty.  
`interconnectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InterconnectAttachment` ID. Must not be `null` or empty.  
  
## Properties 

### InterconnectAttachmentId
    
    
    public string InterconnectAttachmentId { get; }

The `InterconnectAttachment` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public InterconnectAttachmentName.ResourceNameType Type { get; }

The [InterconnectAttachmentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
### ZoneId
    
    
    public string ZoneId { get; }

The `Zone` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string zoneId, string interconnectAttachmentId)

Formats the IDs into the string representation of this [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) with pattern `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`zoneId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Zone` ID. Must not be `null` or empty.  
`interconnectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InterconnectAttachment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) with pattern `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}` .  
  
### FormatProjectLocationZoneInterconnectAttachment(string, string, string, string)
    
    
    public static string FormatProjectLocationZoneInterconnectAttachment(string projectId, string locationId, string zoneId, string interconnectAttachmentId)

Formats the IDs into the string representation of this [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) with pattern `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`zoneId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Zone` ID. Must not be `null` or empty.  
`interconnectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InterconnectAttachment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) with pattern `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}` .  
  
### FromProjectLocationZoneInterconnectAttachment(string, string, string, string)
    
    
    public static InterconnectAttachmentName FromProjectLocationZoneInterconnectAttachment(string projectId, string locationId, string zoneId, string interconnectAttachmentId)

Creates a [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) with the pattern `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`zoneId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Zone` ID. Must not be `null` or empty.  
`interconnectAttachmentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InterconnectAttachment` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)` | A new instance of [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static InterconnectAttachmentName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)` | A new instance of [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static InterconnectAttachmentName Parse(string interconnectAttachmentName)

Parses the given resource name string into a new [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) instance.

**Parameter**  
---  
**Name** | **Description**  
`interconnectAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)` | The parsed [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}`



### Parse(string, bool)
    
    
    public static InterconnectAttachmentName Parse(string interconnectAttachmentName, bool allowUnparsed)

Parses the given resource name string into a new [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`interconnectAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName#Google_Cloud_EdgeNetwork_V1_InterconnectAttachmentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)` | The parsed [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}`

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

### TryParse(string, out InterconnectAttachmentName)
    
    
    public static bool TryParse(string interconnectAttachmentName, out InterconnectAttachmentName result)

Tries to parse the given resource name string into a new [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) instance.

**Parameters**  
---  
**Name** | **Description**  
`interconnectAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)`  
When this method returns, the parsed [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}`



### TryParse(string, bool, out InterconnectAttachmentName)
    
    
    public static bool TryParse(string interconnectAttachmentName, bool allowUnparsed, out InterconnectAttachmentName result)

Tries to parse the given resource name string into a new [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`interconnectAttachmentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName#Google_Cloud_EdgeNetwork_V1_InterconnectAttachmentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)`  
When this method returns, the parsed [InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/zones/{zone}/interconnectAttachments/{interconnect_attachment}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(InterconnectAttachmentName, InterconnectAttachmentName)
    
    
    public static bool operator ==(InterconnectAttachmentName a, InterconnectAttachmentName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)`  
The first resource name to compare, or null.  
`b` | `[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(InterconnectAttachmentName, InterconnectAttachmentName)
    
    
    public static bool operator !=(InterconnectAttachmentName a, InterconnectAttachmentName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)`  
The first resource name to compare, or null.  
`b` | `[InterconnectAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectAttachmentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
