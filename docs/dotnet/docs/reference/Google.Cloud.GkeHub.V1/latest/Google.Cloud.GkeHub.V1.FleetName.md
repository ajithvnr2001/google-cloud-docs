---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName
title: GKE Hub v1 API - Class FleetName (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:43.070866+00:00
---

# GKE Hub v1 API - Class FleetName (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GKE Hub v1 API - Class FleetName (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.7.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.6.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.5.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.4.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.3.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.2.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.1.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.0.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.2.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.1.0/Google.Cloud.GkeHub.V1.FleetName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.0.0/Google.Cloud.GkeHub.V1.FleetName)


    
    
    public sealed class FleetName : IResourceName, IEquatable<FleetName>

Reference documentation and code samples for the GKE Hub v1 API class FleetName.

Resource name for the `Fleet` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FleetName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.GkeHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1)

## Assembly

Google.Cloud.GkeHub.V1.dll

## Constructors 

### FleetName(string, string, string)
    
    
    public FleetName(string projectId, string locationId, string fleetId)

Constructs a new instance of a [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) class from the component parts of pattern `projects/{project}/locations/{location}/fleets/{fleet}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`fleetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Fleet` ID. Must not be `null` or empty.  
  
## Properties 

### FleetId
    
    
    public string FleetId { get; }

The `Fleet` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### Type
    
    
    public FleetName.ResourceNameType Type { get; }

The [FleetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string fleetId)

Formats the IDs into the string representation of this [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with pattern `projects/{project}/locations/{location}/fleets/{fleet}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`fleetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Fleet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with pattern `projects/{project}/locations/{location}/fleets/{fleet}`.  
  
### FormatOrganizationLocationFleet(string, string, string)
    
    
    public static string FormatOrganizationLocationFleet(string organizationId, string locationId, string fleetId)

Formats the IDs into the string representation of this [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with pattern `organizations/{organization}/locations/{location}/fleets/{fleet}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`fleetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Fleet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with pattern `organizations/{organization}/locations/{location}/fleets/{fleet}`.  
  
### FormatProjectLocationFleet(string, string, string)
    
    
    public static string FormatProjectLocationFleet(string projectId, string locationId, string fleetId)

Formats the IDs into the string representation of this [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with pattern `projects/{project}/locations/{location}/fleets/{fleet}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`fleetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Fleet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with pattern `projects/{project}/locations/{location}/fleets/{fleet}`.  
  
### FromOrganizationLocationFleet(string, string, string)
    
    
    public static FleetName FromOrganizationLocationFleet(string organizationId, string locationId, string fleetId)

Creates a [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with the pattern `organizations/{organization}/locations/{location}/fleets/{fleet}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`fleetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Fleet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)` | A new instance of [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) constructed from the provided ids.  
  
### FromProjectLocationFleet(string, string, string)
    
    
    public static FleetName FromProjectLocationFleet(string projectId, string locationId, string fleetId)

Creates a [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) with the pattern `projects/{project}/locations/{location}/fleets/{fleet}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`fleetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Fleet` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)` | A new instance of [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static FleetName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)` | A new instance of [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static FleetName Parse(string fleetName)

Parses the given resource name string into a new [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) instance.

**Parameter**  
---  
**Name** | **Description**  
`fleetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)` | The parsed [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/fleets/{fleet}`
  * `organizations/{organization}/locations/{location}/fleets/{fleet}`



### Parse(string, bool)
    
    
    public static FleetName Parse(string fleetName, bool allowUnparsed)

Parses the given resource name string into a new [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`fleetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName#Google_Cloud_GkeHub_V1_FleetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)` | The parsed [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/fleets/{fleet}`
  * `organizations/{organization}/locations/{location}/fleets/{fleet}`

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

### TryParse(string, out FleetName)
    
    
    public static bool TryParse(string fleetName, out FleetName result)

Tries to parse the given resource name string into a new [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) instance.

**Parameters**  
---  
**Name** | **Description**  
`fleetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)`  
When this method returns, the parsed [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/fleets/{fleet}`
  * `organizations/{organization}/locations/{location}/fleets/{fleet}`



### TryParse(string, bool, out FleetName)
    
    
    public static bool TryParse(string fleetName, bool allowUnparsed, out FleetName result)

Tries to parse the given resource name string into a new [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`fleetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName#Google_Cloud_GkeHub_V1_FleetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)`  
When this method returns, the parsed [FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/fleets/{fleet}`
  * `organizations/{organization}/locations/{location}/fleets/{fleet}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(FleetName, FleetName)
    
    
    public static bool operator ==(FleetName a, FleetName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)`  
The first resource name to compare, or null.  
`b` | `[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(FleetName, FleetName)
    
    
    public static bool operator !=(FleetName a, FleetName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)`  
The first resource name to compare, or null.  
`b` | `[FleetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.FleetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
