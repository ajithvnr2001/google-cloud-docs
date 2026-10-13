---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName
title: Google Cloud Tasks v2beta3 API - Class TaskName (3.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:12.478638+00:00
---

# Google Cloud Tasks v2beta3 API - Class TaskName (3.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2beta3 API - Class TaskName (3.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.0-beta09 (latest)  3.0.0-beta08  2.0.0-beta08 
    
    
    public sealed class TaskName : IResourceName, IEquatable<TaskName>

Reference documentation and code samples for the Google Cloud Tasks v2beta3 API class TaskName.

Resource name for the `Task` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TaskName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Tasks.V2Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3)

## Assembly

Google.Cloud.Tasks.V2Beta3.dll

## Constructors 

### TaskName(string, string, string, string)
    
    
    public TaskName(string projectId, string locationId, string queueId, string taskId)

Constructs a new instance of a [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) class from the component parts of pattern `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`queueId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Queue` ID. Must not be `null` or empty.  
`taskId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Task` ID. Must not be `null` or empty.  
  
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
  
### QueueId
    
    
    public string QueueId { get; }

The `Queue` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TaskId
    
    
    public string TaskId { get; }

The `Task` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public TaskName.ResourceNameType Type { get; }

The [TaskName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string queueId, string taskId)

Formats the IDs into the string representation of this [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) with pattern `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`queueId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Queue` ID. Must not be `null` or empty.  
`taskId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Task` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) with pattern `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`.  
  
### FormatProjectLocationQueueTask(string, string, string, string)
    
    
    public static string FormatProjectLocationQueueTask(string projectId, string locationId, string queueId, string taskId)

Formats the IDs into the string representation of this [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) with pattern `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`queueId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Queue` ID. Must not be `null` or empty.  
`taskId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Task` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) with pattern `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`.  
  
### FromProjectLocationQueueTask(string, string, string, string)
    
    
    public static TaskName FromProjectLocationQueueTask(string projectId, string locationId, string queueId, string taskId)

Creates a [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) with the pattern `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`queueId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Queue` ID. Must not be `null` or empty.  
`taskId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Task` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)` | A new instance of [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static TaskName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)` | A new instance of [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static TaskName Parse(string taskName)

Parses the given resource name string into a new [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) instance.

**Parameter**  
---  
**Name** | **Description**  
`taskName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)` | The parsed [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`



### Parse(string, bool)
    
    
    public static TaskName Parse(string taskName, bool allowUnparsed)

Parses the given resource name string into a new [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`taskName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName#Google_Cloud_Tasks_V2Beta3_TaskName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)` | The parsed [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`



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

### TryParse(string, out TaskName)
    
    
    public static bool TryParse(string taskName, out TaskName result)

Tries to parse the given resource name string into a new [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) instance.

**Parameters**  
---  
**Name** | **Description**  
`taskName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)`  
When this method returns, the parsed [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`



### TryParse(string, bool, out TaskName)
    
    
    public static bool TryParse(string taskName, bool allowUnparsed, out TaskName result)

Tries to parse the given resource name string into a new [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`taskName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName#Google_Cloud_Tasks_V2Beta3_TaskName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)`  
When this method returns, the parsed [TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/queues/{queue}/tasks/{task}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(TaskName, TaskName)
    
    
    public static bool operator ==(TaskName a, TaskName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)`  
The first resource name to compare, or null.  
`b` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(TaskName, TaskName)
    
    
    public static bool operator !=(TaskName a, TaskName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)`  
The first resource name to compare, or null.  
`b` | `[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
