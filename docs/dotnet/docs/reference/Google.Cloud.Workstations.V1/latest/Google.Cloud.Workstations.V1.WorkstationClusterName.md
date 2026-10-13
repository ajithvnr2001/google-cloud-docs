---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName
title: Cloud Workstations v1 API - Class WorkstationClusterName (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:09.510637+00:00
---

# Cloud Workstations v1 API - Class WorkstationClusterName (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Workstations v1 API - Class WorkstationClusterName (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.0 (latest)  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class WorkstationClusterName : IResourceName, IEquatable<WorkstationClusterName>

Reference documentation and code samples for the Cloud Workstations v1 API class WorkstationClusterName.

Resource name for the `WorkstationCluster` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WorkstationClusterName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Workstations.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1)

## Assembly

Google.Cloud.Workstations.V1.dll

## Constructors 

### WorkstationClusterName(string, string, string)
    
    
    public WorkstationClusterName(string projectId, string locationId, string workstationClusterId)

Constructs a new instance of a [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) class from the component parts of pattern `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workstationClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkstationCluster` ID. Must not be `null` or empty.  
  
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
  
### Type
    
    
    public WorkstationClusterName.ResourceNameType Type { get; }

The [WorkstationClusterName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
### WorkstationClusterId
    
    
    public string WorkstationClusterId { get; }

The `WorkstationCluster` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string workstationClusterId)

Formats the IDs into the string representation of this [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) with pattern `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workstationClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkstationCluster` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) with pattern `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`.  
  
### FormatProjectLocationWorkstationCluster(string, string, string)
    
    
    public static string FormatProjectLocationWorkstationCluster(string projectId, string locationId, string workstationClusterId)

Formats the IDs into the string representation of this [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) with pattern `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workstationClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkstationCluster` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) with pattern `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`.  
  
### FromProjectLocationWorkstationCluster(string, string, string)
    
    
    public static WorkstationClusterName FromProjectLocationWorkstationCluster(string projectId, string locationId, string workstationClusterId)

Creates a [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) with the pattern `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workstationClusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkstationCluster` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)` | A new instance of [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static WorkstationClusterName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)` | A new instance of [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static WorkstationClusterName Parse(string workstationClusterName)

Parses the given resource name string into a new [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) instance.

**Parameter**  
---  
**Name** | **Description**  
`workstationClusterName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)` | The parsed [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`



### Parse(string, bool)
    
    
    public static WorkstationClusterName Parse(string workstationClusterName, bool allowUnparsed)

Parses the given resource name string into a new [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workstationClusterName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName#Google_Cloud_Workstations_V1_WorkstationClusterName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)` | The parsed [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`



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

### TryParse(string, out WorkstationClusterName)
    
    
    public static bool TryParse(string workstationClusterName, out WorkstationClusterName result)

Tries to parse the given resource name string into a new [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) instance.

**Parameters**  
---  
**Name** | **Description**  
`workstationClusterName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)`  
When this method returns, the parsed [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`



### TryParse(string, bool, out WorkstationClusterName)
    
    
    public static bool TryParse(string workstationClusterName, bool allowUnparsed, out WorkstationClusterName result)

Tries to parse the given resource name string into a new [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workstationClusterName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName#Google_Cloud_Workstations_V1_WorkstationClusterName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)`  
When this method returns, the parsed [WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/workstationClusters/{workstation_cluster}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(WorkstationClusterName, WorkstationClusterName)
    
    
    public static bool operator ==(WorkstationClusterName a, WorkstationClusterName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)`  
The first resource name to compare, or null.  
`b` | `[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(WorkstationClusterName, WorkstationClusterName)
    
    
    public static bool operator !=(WorkstationClusterName a, WorkstationClusterName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)`  
The first resource name to compare, or null.  
`b` | `[WorkstationClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationClusterName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-08 UTC."],[],[]] 
