---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName
title: Analytics Hub v1beta1 API - Class DataExchangeName (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:31:25.954442+00:00
---

# Analytics Hub v1beta1 API - Class DataExchangeName (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Analytics Hub v1beta1 API - Class DataExchangeName (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/2.0.0-beta06/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/1.0.0-beta01/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)


    
    
    public sealed class DataExchangeName : IResourceName, IEquatable<DataExchangeName>

Reference documentation and code samples for the Analytics Hub v1beta1 API class DataExchangeName.

Resource name for the `DataExchange` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DataExchangeName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.BigQuery.DataExchange.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1)

## Assembly

Google.Cloud.BigQuery.DataExchange.V1Beta1.dll

## Constructors 

### DataExchangeName(string, string, string)
    
    
    public DataExchangeName(string projectId, string locationId, string dataExchangeId)

Constructs a new instance of a [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) class from the component parts of pattern `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataExchangeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataExchange` ID. Must not be `null` or empty.  
  
## Properties 

### DataExchangeId
    
    
    public string DataExchangeId { get; }

The `DataExchange` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public DataExchangeName.ResourceNameType Type { get; }

The [DataExchangeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string dataExchangeId)

Formats the IDs into the string representation of this [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) with pattern `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataExchangeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataExchange` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) with pattern `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`.  
  
### FormatProjectLocationDataExchange(string, string, string)
    
    
    public static string FormatProjectLocationDataExchange(string projectId, string locationId, string dataExchangeId)

Formats the IDs into the string representation of this [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) with pattern `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataExchangeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataExchange` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) with pattern `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`.  
  
### FromProjectLocationDataExchange(string, string, string)
    
    
    public static DataExchangeName FromProjectLocationDataExchange(string projectId, string locationId, string dataExchangeId)

Creates a [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) with the pattern `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataExchangeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataExchange` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)` | A new instance of [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static DataExchangeName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)` | A new instance of [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static DataExchangeName Parse(string dataExchangeName)

Parses the given resource name string into a new [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) instance.

**Parameter**  
---  
**Name** | **Description**  
`dataExchangeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)` | The parsed [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`



### Parse(string, bool)
    
    
    public static DataExchangeName Parse(string dataExchangeName, bool allowUnparsed)

Parses the given resource name string into a new [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`dataExchangeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName#Google_Cloud_BigQuery_DataExchange_V1Beta1_DataExchangeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)` | The parsed [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`

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

### TryParse(string, out DataExchangeName)
    
    
    public static bool TryParse(string dataExchangeName, out DataExchangeName result)

Tries to parse the given resource name string into a new [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) instance.

**Parameters**  
---  
**Name** | **Description**  
`dataExchangeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)`  
When this method returns, the parsed [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`



### TryParse(string, bool, out DataExchangeName)
    
    
    public static bool TryParse(string dataExchangeName, bool allowUnparsed, out DataExchangeName result)

Tries to parse the given resource name string into a new [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`dataExchangeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName#Google_Cloud_BigQuery_DataExchange_V1Beta1_DataExchangeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)`  
When this method returns, the parsed [DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/dataExchanges/{data_exchange}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(DataExchangeName, DataExchangeName)
    
    
    public static bool operator ==(DataExchangeName a, DataExchangeName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)`  
The first resource name to compare, or null.  
`b` | `[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(DataExchangeName, DataExchangeName)
    
    
    public static bool operator !=(DataExchangeName a, DataExchangeName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)`  
The first resource name to compare, or null.  
`b` | `[DataExchangeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.DataExchangeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
