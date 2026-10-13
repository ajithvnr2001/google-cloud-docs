---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName
title: Device Streaming v1 API - Class DeviceSessionName (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:09.508011+00:00
---

# Device Streaming v1 API - Class DeviceSessionName (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Device Streaming v1 API - Class DeviceSessionName (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class DeviceSessionName : IResourceName, IEquatable<DeviceSessionName>

Reference documentation and code samples for the Device Streaming v1 API class DeviceSessionName.

Resource name for the `DeviceSession` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeviceSessionName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.DeviceStreaming.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1)

## Assembly

Google.Cloud.DeviceStreaming.V1.dll

## Constructors 

### DeviceSessionName(string, string)
    
    
    public DeviceSessionName(string projectId, string deviceSessionId)

Constructs a new instance of a [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) class from the component parts of pattern `projects/{project}/deviceSessions/{device_session}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`deviceSessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeviceSession` ID. Must not be `null` or empty.  
  
## Properties 

### DeviceSessionId
    
    
    public string DeviceSessionId { get; }

The `DeviceSession` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public DeviceSessionName.ResourceNameType Type { get; }

The [DeviceSessionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string projectId, string deviceSessionId)

Formats the IDs into the string representation of this [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) with pattern `projects/{project}/deviceSessions/{device_session}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`deviceSessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeviceSession` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) with pattern `projects/{project}/deviceSessions/{device_session}`.  
  
### FormatProjectDeviceSession(string, string)
    
    
    public static string FormatProjectDeviceSession(string projectId, string deviceSessionId)

Formats the IDs into the string representation of this [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) with pattern `projects/{project}/deviceSessions/{device_session}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`deviceSessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeviceSession` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) with pattern `projects/{project}/deviceSessions/{device_session}`.  
  
### FromProjectDeviceSession(string, string)
    
    
    public static DeviceSessionName FromProjectDeviceSession(string projectId, string deviceSessionId)

Creates a [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) with the pattern `projects/{project}/deviceSessions/{device_session}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`deviceSessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeviceSession` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)` | A new instance of [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static DeviceSessionName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)` | A new instance of [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static DeviceSessionName Parse(string deviceSessionName)

Parses the given resource name string into a new [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) instance.

**Parameter**  
---  
**Name** | **Description**  
`deviceSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)` | The parsed [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/deviceSessions/{device_session}`



### Parse(string, bool)
    
    
    public static DeviceSessionName Parse(string deviceSessionName, bool allowUnparsed)

Parses the given resource name string into a new [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`deviceSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName#Google_Cloud_DeviceStreaming_V1_DeviceSessionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)` | The parsed [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/deviceSessions/{device_session}`



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

### TryParse(string, out DeviceSessionName)
    
    
    public static bool TryParse(string deviceSessionName, out DeviceSessionName result)

Tries to parse the given resource name string into a new [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) instance.

**Parameters**  
---  
**Name** | **Description**  
`deviceSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)`  
When this method returns, the parsed [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/deviceSessions/{device_session}`



### TryParse(string, bool, out DeviceSessionName)
    
    
    public static bool TryParse(string deviceSessionName, bool allowUnparsed, out DeviceSessionName result)

Tries to parse the given resource name string into a new [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`deviceSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName#Google_Cloud_DeviceStreaming_V1_DeviceSessionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)`  
When this method returns, the parsed [DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/deviceSessions/{device_session}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(DeviceSessionName, DeviceSessionName)
    
    
    public static bool operator ==(DeviceSessionName a, DeviceSessionName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)`  
The first resource name to compare, or null.  
`b` | `[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(DeviceSessionName, DeviceSessionName)
    
    
    public static bool operator !=(DeviceSessionName a, DeviceSessionName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)`  
The first resource name to compare, or null.  
`b` | `[DeviceSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeviceStreaming.V1/latest/Google.Cloud.DeviceStreaming.V1.DeviceSessionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
