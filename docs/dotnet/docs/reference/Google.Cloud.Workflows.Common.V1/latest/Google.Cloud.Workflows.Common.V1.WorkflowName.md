---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName
title: Google.Cloud.Workflows.Common.V1 - Class WorkflowName (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:25.844479+00:00
---

# Google.Cloud.Workflows.Common.V1 - Class WorkflowName (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Workflows.Common.V1 - Class WorkflowName (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/2.4.0/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/2.3.0/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/2.2.0/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/2.1.0/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/2.0.0/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/1.2.0/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/1.1.0/Google.Cloud.Workflows.Common.V1.WorkflowName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/1.0.0/Google.Cloud.Workflows.Common.V1.WorkflowName)


    
    
    public sealed class WorkflowName : IResourceName, IEquatable<WorkflowName>

Reference documentation and code samples for the Google.Cloud.Workflows.Common.V1 class WorkflowName.

Resource name for the `Workflow` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WorkflowName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Workflows.Common.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1)

## Assembly

Google.Cloud.Workflows.Common.V1.dll

## Constructors 

### WorkflowName(string, string, string)
    
    
    public WorkflowName(string projectId, string locationId, string workflowId)

Constructs a new instance of a [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) class from the component parts of pattern `projects/{project}/locations/{location}/workflows/{workflow}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workflowId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workflow` ID. Must not be `null` or empty.  
  
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
    
    
    public WorkflowName.ResourceNameType Type { get; }

The [WorkflowName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
### WorkflowId
    
    
    public string WorkflowId { get; }

The `Workflow` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string workflowId)

Formats the IDs into the string representation of this [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) with pattern `projects/{project}/locations/{location}/workflows/{workflow}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workflowId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workflow` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) with pattern `projects/{project}/locations/{location}/workflows/{workflow}`.  
  
### FormatProjectLocationWorkflow(string, string, string)
    
    
    public static string FormatProjectLocationWorkflow(string projectId, string locationId, string workflowId)

Formats the IDs into the string representation of this [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) with pattern `projects/{project}/locations/{location}/workflows/{workflow}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workflowId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workflow` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) with pattern `projects/{project}/locations/{location}/workflows/{workflow}`.  
  
### FromProjectLocationWorkflow(string, string, string)
    
    
    public static WorkflowName FromProjectLocationWorkflow(string projectId, string locationId, string workflowId)

Creates a [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) with the pattern `projects/{project}/locations/{location}/workflows/{workflow}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`workflowId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Workflow` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)` | A new instance of [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static WorkflowName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)` | A new instance of [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) containing the provided `unparsedResourceName` .  
  
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
    
    
    public static WorkflowName Parse(string workflowName)

Parses the given resource name string into a new [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) instance.

**Parameter**  
---  
**Name** | **Description**  
`workflowName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)` | The parsed [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/workflows/{workflow}`



### Parse(string, bool)
    
    
    public static WorkflowName Parse(string workflowName, bool allowUnparsed)

Parses the given resource name string into a new [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workflowName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName#Google_Cloud_Workflows_Common_V1_WorkflowName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)` | The parsed [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/workflows/{workflow}`

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

### TryParse(string, out WorkflowName)
    
    
    public static bool TryParse(string workflowName, out WorkflowName result)

Tries to parse the given resource name string into a new [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) instance.

**Parameters**  
---  
**Name** | **Description**  
`workflowName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)`  
When this method returns, the parsed [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/workflows/{workflow}`



### TryParse(string, bool, out WorkflowName)
    
    
    public static bool TryParse(string workflowName, bool allowUnparsed, out WorkflowName result)

Tries to parse the given resource name string into a new [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`workflowName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName#Google_Cloud_Workflows_Common_V1_WorkflowName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)`  
When this method returns, the parsed [WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/workflows/{workflow}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(WorkflowName, WorkflowName)
    
    
    public static bool operator ==(WorkflowName a, WorkflowName b)

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)`  
  
`b` | `[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### operator !=(WorkflowName, WorkflowName)
    
    
    public static bool operator !=(WorkflowName a, WorkflowName b)

**Parameters**  
---  
**Name** | **Description**  
`a` | `[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)`  
  
`b` | `[WorkflowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workflows.Common.V1/latest/Google.Cloud.Workflows.Common.V1.WorkflowName)`  
  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
