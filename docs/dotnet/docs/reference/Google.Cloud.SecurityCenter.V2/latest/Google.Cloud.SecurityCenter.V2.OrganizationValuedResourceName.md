---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName
title: Security Command Center v2 API - Class OrganizationValuedResourceName (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:00.887788+00:00
---

# Security Command Center v2 API - Class OrganizationValuedResourceName (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class OrganizationValuedResourceName (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class OrganizationValuedResourceName : IResourceName, IEquatable<OrganizationValuedResourceName>

Reference documentation and code samples for the Security Command Center v2 API class OrganizationValuedResourceName.

Resource name for the `OrganizationValuedResource` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OrganizationValuedResourceName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### OrganizationValuedResourceName(string, string, string, string)
    
    
    public OrganizationValuedResourceName(string organizationId, string locationId, string simulationId, string valuedResourceId)

Constructs a new instance of a [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) class from the component parts of pattern ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`simulationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Simulation` ID. Must not be `null` or empty.  
`valuedResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ValuedResource` ID. Must not be `null` or empty.  
  
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
  
### OrganizationId
    
    
    public string OrganizationId { get; }

The `Organization` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SimulationId
    
    
    public string SimulationId { get; }

The `Simulation` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public OrganizationValuedResourceName.ResourceNameType Type { get; }

The [OrganizationValuedResourceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
### ValuedResourceId
    
    
    public string ValuedResourceId { get; }

The `ValuedResource` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string organizationId, string locationId, string simulationId, string valuedResourceId)

Formats the IDs into the string representation of this [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) with pattern ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}` .

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`simulationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Simulation` ID. Must not be `null` or empty.  
`valuedResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ValuedResource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) with pattern ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}` .  
  
### FormatOrganizationLocationSimulationValuedResource(string, string, string, string)
    
    
    public static string FormatOrganizationLocationSimulationValuedResource(string organizationId, string locationId, string simulationId, string valuedResourceId)

Formats the IDs into the string representation of this [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) with pattern ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}` .

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`simulationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Simulation` ID. Must not be `null` or empty.  
`valuedResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ValuedResource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) with pattern ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}` .  
  
### FromOrganizationLocationSimulationValuedResource(string, string, string, string)
    
    
    public static OrganizationValuedResourceName FromOrganizationLocationSimulationValuedResource(string organizationId, string locationId, string simulationId, string valuedResourceId)

Creates a [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) with the pattern ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}` .

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`simulationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Simulation` ID. Must not be `null` or empty.  
`valuedResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ValuedResource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)` | A new instance of [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static OrganizationValuedResourceName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)` | A new instance of [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static OrganizationValuedResourceName Parse(string organizationValuedResourceName)

Parses the given resource name string into a new [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) instance.

**Parameter**  
---  
**Name** | **Description**  
`organizationValuedResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)` | The parsed [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}`



### Parse(string, bool)
    
    
    public static OrganizationValuedResourceName Parse(string organizationValuedResourceName, bool allowUnparsed)

Parses the given resource name string into a new [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`organizationValuedResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName#Google_Cloud_SecurityCenter_V2_OrganizationValuedResourceName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)` | The parsed [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}`



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

### TryParse(string, out OrganizationValuedResourceName)
    
    
    public static bool TryParse(string organizationValuedResourceName, out OrganizationValuedResourceName result)

Tries to parse the given resource name string into a new [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) instance.

**Parameters**  
---  
**Name** | **Description**  
`organizationValuedResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)`  
When this method returns, the parsed [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}`



### TryParse(string, bool, out OrganizationValuedResourceName)
    
    
    public static bool TryParse(string organizationValuedResourceName, bool allowUnparsed, out OrganizationValuedResourceName result)

Tries to parse the given resource name string into a new [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`organizationValuedResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName#Google_Cloud_SecurityCenter_V2_OrganizationValuedResourceName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)`  
When this method returns, the parsed [OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` organizations/{organization}/locations/{location}/simulations/{simulation}/valuedResources/{valued_resource}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(OrganizationValuedResourceName, OrganizationValuedResourceName)
    
    
    public static bool operator ==(OrganizationValuedResourceName a, OrganizationValuedResourceName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)`  
The first resource name to compare, or null.  
`b` | `[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(OrganizationValuedResourceName, OrganizationValuedResourceName)
    
    
    public static bool operator !=(OrganizationValuedResourceName a, OrganizationValuedResourceName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)`  
The first resource name to compare, or null.  
`b` | `[OrganizationValuedResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.OrganizationValuedResourceName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
