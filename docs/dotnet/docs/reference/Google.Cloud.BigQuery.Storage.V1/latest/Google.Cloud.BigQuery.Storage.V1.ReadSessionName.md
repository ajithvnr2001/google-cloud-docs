---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName
title: Google BigQuery Storage v1 API - Class ReadSessionName (3.20.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:05.720035+00:00
---

# Google BigQuery Storage v1 API - Class ReadSessionName (3.20.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery Storage v1 API - Class ReadSessionName (3.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.20.0 (latest)  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class ReadSessionName : IResourceName, IEquatable<ReadSessionName>

Reference documentation and code samples for the Google BigQuery Storage v1 API class ReadSessionName.

Resource name for the `ReadSession` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReadSessionName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.BigQuery.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1)

## Assembly

Google.Cloud.BigQuery.Storage.V1.dll

## Constructors 

### ReadSessionName(string, string, string)
    
    
    public ReadSessionName(string projectId, string locationId, string sessionId)

Constructs a new instance of a [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) class from the component parts of pattern `projects/{project}/locations/{location}/sessions/{session}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
  
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
  
### SessionId
    
    
    public string SessionId { get; }

The `Session` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ReadSessionName.ResourceNameType Type { get; }

The [ReadSessionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string sessionId)

Formats the IDs into the string representation of this [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) with pattern `projects/{project}/locations/{location}/sessions/{session}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) with pattern `projects/{project}/locations/{location}/sessions/{session}`.  
  
### FormatProjectLocationSession(string, string, string)
    
    
    public static string FormatProjectLocationSession(string projectId, string locationId, string sessionId)

Formats the IDs into the string representation of this [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) with pattern `projects/{project}/locations/{location}/sessions/{session}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) with pattern `projects/{project}/locations/{location}/sessions/{session}`.  
  
### FromProjectLocationSession(string, string, string)
    
    
    public static ReadSessionName FromProjectLocationSession(string projectId, string locationId, string sessionId)

Creates a [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) with the pattern `projects/{project}/locations/{location}/sessions/{session}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)` | A new instance of [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ReadSessionName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)` | A new instance of [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ReadSessionName Parse(string readSessionName)

Parses the given resource name string into a new [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) instance.

**Parameter**  
---  
**Name** | **Description**  
`readSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)` | The parsed [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessions/{session}`



### Parse(string, bool)
    
    
    public static ReadSessionName Parse(string readSessionName, bool allowUnparsed)

Parses the given resource name string into a new [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`readSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName#Google_Cloud_BigQuery_Storage_V1_ReadSessionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)` | The parsed [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessions/{session}`



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

### TryParse(string, out ReadSessionName)
    
    
    public static bool TryParse(string readSessionName, out ReadSessionName result)

Tries to parse the given resource name string into a new [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) instance.

**Parameters**  
---  
**Name** | **Description**  
`readSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)`  
When this method returns, the parsed [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessions/{session}`



### TryParse(string, bool, out ReadSessionName)
    
    
    public static bool TryParse(string readSessionName, bool allowUnparsed, out ReadSessionName result)

Tries to parse the given resource name string into a new [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`readSessionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName#Google_Cloud_BigQuery_Storage_V1_ReadSessionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)`  
When this method returns, the parsed [ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessions/{session}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ReadSessionName, ReadSessionName)
    
    
    public static bool operator ==(ReadSessionName a, ReadSessionName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)`  
The first resource name to compare, or null.  
`b` | `[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ReadSessionName, ReadSessionName)
    
    
    public static bool operator !=(ReadSessionName a, ReadSessionName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)`  
The first resource name to compare, or null.  
`b` | `[ReadSessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.ReadSessionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
