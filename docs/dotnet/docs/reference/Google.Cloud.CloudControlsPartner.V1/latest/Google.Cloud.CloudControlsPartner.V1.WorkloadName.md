---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName
title: Cloud Controls Partner v1 API - Class WorkloadName (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:05.657517+00:00
---

# Cloud Controls Partner v1 API - Class WorkloadName (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Controls Partner v1 API - Class WorkloadName (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/1.2.0/Google.Cloud.CloudControlsPartner.V1.WorkloadName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/1.1.0/Google.Cloud.CloudControlsPartner.V1.WorkloadName)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/1.0.0-beta02/Google.Cloud.CloudControlsPartner.V1.WorkloadName)


    
    
    public sealed class WorkloadName : IResourceName, IEquatable<WorkloadName>

Reference documentation and code samples for the Cloud Controls Partner v1 API class WorkloadName.

Resource name for the `Workload` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WorkloadName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.CloudControlsPartner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1)

## Assembly

Google.Cloud.CloudControlsPartner.V1.dll

## Constructors 

### WorkloadName(string, string, string, string)
    
    
    public WorkloadName(string organizationId, string locationId, string customerId, string workloadId)

Constructs a new instance of a [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) class from the component parts of pattern `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Customer` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
  
## Properties 

### CustomerId
    
    
    public string CustomerId { get; }

The `Customer` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### OrganizationId
    
    
    public string OrganizationId { get; }

The `Organization` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public WorkloadName.ResourceNameType Type { get; }

The [WorkloadName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
### WorkloadId
    
    
    public string WorkloadId { get; }

The `Workload` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string organizationId, string locationId, string customerId, string workloadId)

Formats the IDs into the string representation of this [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) with pattern `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Customer` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) with pattern `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`.  
  
### FormatOrganizationLocationCustomerWorkload(string, string, string, string)
    
    
    public static string FormatOrganizationLocationCustomerWorkload(string organizationId, string locationId, string customerId, string workloadId)

Formats the IDs into the string representation of this [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) with pattern `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Customer` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) with pattern `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`.  
  
### FromOrganizationLocationCustomerWorkload(string, string, string, string)
    
    
    public static WorkloadName FromOrganizationLocationCustomerWorkload(string organizationId, string locationId, string customerId, string workloadId)

Creates a [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) with the pattern `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`customerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Customer` ID. Must not be `null` or empty.  
`workloadId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workload` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)` | A new instance of [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static WorkloadName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)` | A new instance of [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) containing the provided `unparsedResourceName` .  
  
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
    
    
    public static WorkloadName Parse(string workloadName)

Parses the given resource name string into a new [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) instance.

**Parameter**  
---  
**Name** | **Description**  
`workloadName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)` | The parsed [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`



### Parse(string, bool)
    
    
    public static WorkloadName Parse(string workloadName, bool allowUnparsed)

Parses the given resource name string into a new [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workloadName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName#Google_Cloud_CloudControlsPartner_V1_WorkloadName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)` | The parsed [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`

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

### TryParse(string, out WorkloadName)
    
    
    public static bool TryParse(string workloadName, out WorkloadName result)

Tries to parse the given resource name string into a new [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) instance.

**Parameters**  
---  
**Name** | **Description**  
`workloadName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)`  
When this method returns, the parsed [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`



### TryParse(string, bool, out WorkloadName)
    
    
    public static bool TryParse(string workloadName, bool allowUnparsed, out WorkloadName result)

Tries to parse the given resource name string into a new [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workloadName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName#Google_Cloud_CloudControlsPartner_V1_WorkloadName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)`  
When this method returns, the parsed [WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(WorkloadName, WorkloadName)
    
    
    public static bool operator ==(WorkloadName a, WorkloadName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)`  
The first resource name to compare, or null.  
`b` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(WorkloadName, WorkloadName)
    
    
    public static bool operator !=(WorkloadName a, WorkloadName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)`  
The first resource name to compare, or null.  
`b` | `[WorkloadName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudControlsPartner.V1/latest/Google.Cloud.CloudControlsPartner.V1.WorkloadName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
