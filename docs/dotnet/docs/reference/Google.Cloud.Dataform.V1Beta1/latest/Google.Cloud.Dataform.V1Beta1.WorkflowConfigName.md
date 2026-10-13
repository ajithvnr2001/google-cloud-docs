---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName
title: Dataform v1beta1 API - Class WorkflowConfigName (1.0.0-beta15) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:10.869706+00:00
---

# Dataform v1beta1 API - Class WorkflowConfigName (1.0.0-beta15)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1beta1 API - Class WorkflowConfigName (1.0.0-beta15) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta15 (latest)  1.0.0-beta14 
    
    
    public sealed class WorkflowConfigName : IResourceName, IEquatable<WorkflowConfigName>

Reference documentation and code samples for the Dataform v1beta1 API class WorkflowConfigName.

Resource name for the `WorkflowConfig` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WorkflowConfigName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Dataform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1)

## Assembly

Google.Cloud.Dataform.V1Beta1.dll

## Constructors 

### WorkflowConfigName(string, string, string, string)
    
    
    public WorkflowConfigName(string projectId, string locationId, string repositoryId, string workflowConfigId)

Constructs a new instance of a [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) class from the component parts of pattern `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`workflowConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkflowConfig` ID. Must not be `null` or empty.  
  
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
  
### RepositoryId
    
    
    public string RepositoryId { get; }

The `Repository` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public WorkflowConfigName.ResourceNameType Type { get; }

The [WorkflowConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
### WorkflowConfigId
    
    
    public string WorkflowConfigId { get; }

The `WorkflowConfig` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string repositoryId, string workflowConfigId)

Formats the IDs into the string representation of this [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`workflowConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkflowConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`.  
  
### FormatProjectLocationRepositoryWorkflowConfig(string, string, string, string)
    
    
    public static string FormatProjectLocationRepositoryWorkflowConfig(string projectId, string locationId, string repositoryId, string workflowConfigId)

Formats the IDs into the string representation of this [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`workflowConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkflowConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) with pattern `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`.  
  
### FromProjectLocationRepositoryWorkflowConfig(string, string, string, string)
    
    
    public static WorkflowConfigName FromProjectLocationRepositoryWorkflowConfig(string projectId, string locationId, string repositoryId, string workflowConfigId)

Creates a [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) with the pattern `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`repositoryId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Repository` ID. Must not be `null` or empty.  
`workflowConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `WorkflowConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)` | A new instance of [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static WorkflowConfigName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)` | A new instance of [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static WorkflowConfigName Parse(string workflowConfigName)

Parses the given resource name string into a new [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) instance.

**Parameter**  
---  
**Name** | **Description**  
`workflowConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)` | The parsed [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`



### Parse(string, bool)
    
    
    public static WorkflowConfigName Parse(string workflowConfigName, bool allowUnparsed)

Parses the given resource name string into a new [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workflowConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName#Google_Cloud_Dataform_V1Beta1_WorkflowConfigName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)` | The parsed [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`



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

### TryParse(string, out WorkflowConfigName)
    
    
    public static bool TryParse(string workflowConfigName, out WorkflowConfigName result)

Tries to parse the given resource name string into a new [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) instance.

**Parameters**  
---  
**Name** | **Description**  
`workflowConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)`  
When this method returns, the parsed [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`



### TryParse(string, bool, out WorkflowConfigName)
    
    
    public static bool TryParse(string workflowConfigName, bool allowUnparsed, out WorkflowConfigName result)

Tries to parse the given resource name string into a new [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workflowConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName#Google_Cloud_Dataform_V1Beta1_WorkflowConfigName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)`  
When this method returns, the parsed [WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/repositories/{repository}/workflowConfigs/{workflow_config}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(WorkflowConfigName, WorkflowConfigName)
    
    
    public static bool operator ==(WorkflowConfigName a, WorkflowConfigName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)`  
The first resource name to compare, or null.  
`b` | `[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(WorkflowConfigName, WorkflowConfigName)
    
    
    public static bool operator !=(WorkflowConfigName a, WorkflowConfigName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)`  
The first resource name to compare, or null.  
`b` | `[WorkflowConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.WorkflowConfigName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
