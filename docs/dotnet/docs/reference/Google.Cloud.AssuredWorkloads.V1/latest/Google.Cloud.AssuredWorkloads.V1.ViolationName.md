---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName
title: Assured Workloads v1 API - Class ViolationName (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:10.281632+00:00
---

# Assured Workloads v1 API - Class ViolationName (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Assured Workloads v1 API - Class ViolationName (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.6.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.5.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.4.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.3.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.2.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.1.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.0.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.1.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.0.0/Google.Cloud.AssuredWorkloads.V1.ViolationName)


    
    
    public sealed class ViolationName : IResourceName, IEquatable<ViolationName>

Reference documentation and code samples for the Assured Workloads v1 API class ViolationName.

Resource name for the `Violation` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ViolationName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.AssuredWorkloads.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1)

## Assembly

Google.Cloud.AssuredWorkloads.V1.dll

## Constructors 

### ViolationName(string, string, string, string)
    
    
    public ViolationName(string organizationId, string locationId, string workloadId, string violationId)

Constructs a new instance of a [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) class from the component parts of pattern `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
`violationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Violation` ID. Must not be `null` or empty.  
  
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
  
### Type
    
    
    public ViolationName.ResourceNameType Type { get; }

The [ViolationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
### ViolationId
    
    
    public string ViolationId { get; }

The `Violation` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WorkloadId
    
    
    public string WorkloadId { get; }

The `Workload` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string organizationId, string locationId, string workloadId, string violationId)

Formats the IDs into the string representation of this [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) with pattern `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
`violationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Violation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) with pattern `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`.  
  
### FormatOrganizationLocationWorkloadViolation(string, string, string, string)
    
    
    public static string FormatOrganizationLocationWorkloadViolation(string organizationId, string locationId, string workloadId, string violationId)

Formats the IDs into the string representation of this [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) with pattern `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
`violationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Violation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) with pattern `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`.  
  
### FromOrganizationLocationWorkloadViolation(string, string, string, string)
    
    
    public static ViolationName FromOrganizationLocationWorkloadViolation(string organizationId, string locationId, string workloadId, string violationId)

Creates a [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) with the pattern `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
`violationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Violation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)` | A new instance of [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ViolationName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)` | A new instance of [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ViolationName Parse(string violationName)

Parses the given resource name string into a new [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) instance.

**Parameter**  
---  
**Name** | **Description**  
`violationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)` | The parsed [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`



### Parse(string, bool)
    
    
    public static ViolationName Parse(string violationName, bool allowUnparsed)

Parses the given resource name string into a new [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`violationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName#Google_Cloud_AssuredWorkloads_V1_ViolationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)` | The parsed [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`

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

### TryParse(string, out ViolationName)
    
    
    public static bool TryParse(string violationName, out ViolationName result)

Tries to parse the given resource name string into a new [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) instance.

**Parameters**  
---  
**Name** | **Description**  
`violationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
When this method returns, the parsed [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`



### TryParse(string, bool, out ViolationName)
    
    
    public static bool TryParse(string violationName, bool allowUnparsed, out ViolationName result)

Tries to parse the given resource name string into a new [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`violationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName#Google_Cloud_AssuredWorkloads_V1_ViolationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
When this method returns, the parsed [ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ViolationName, ViolationName)
    
    
    public static bool operator ==(ViolationName a, ViolationName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
The first resource name to compare, or null.  
`b` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ViolationName, ViolationName)
    
    
    public static bool operator !=(ViolationName a, ViolationName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
The first resource name to compare, or null.  
`b` | `[ViolationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.ViolationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
