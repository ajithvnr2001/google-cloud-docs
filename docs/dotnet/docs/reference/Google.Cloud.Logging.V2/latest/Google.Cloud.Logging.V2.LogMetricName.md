---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName
title: Google Cloud Logging v2 API - Class LogMetricName (4.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:46.870573+00:00
---

# Google Cloud Logging v2 API - Class LogMetricName (4.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Logging v2 API - Class LogMetricName (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 4.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)
  * [ 4.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.4.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 4.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.3.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 4.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.2.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 4.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.1.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 4.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/4.0.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.6.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.5.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.4.0/Google.Cloud.Logging.V2.LogMetricName)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/3.3.0/Google.Cloud.Logging.V2.LogMetricName)


    
    
    public sealed class LogMetricName : IResourceName, IEquatable<LogMetricName>

Reference documentation and code samples for the Google Cloud Logging v2 API class LogMetricName.

Resource name for the `LogMetric` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LogMetricName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Logging.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2)

## Assembly

Google.Cloud.Logging.V2.dll

## Constructors 

### LogMetricName(string, string)
    
    
    public LogMetricName(string projectId, string metricId)

Constructs a new instance of a [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) class from the component parts of pattern `projects/{project}/metrics/{metric}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`metricId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Metric` ID. Must not be `null` or empty.  
  
## Properties 

### IsKnownPattern
    
    
    public bool IsKnownPattern { get; }

Whether this instance contains a resource name with a known pattern.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MetricId
    
    
    public string MetricId { get; }

The `Metric` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public LogMetricName.ResourceNameType Type { get; }

The [LogMetricName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string projectId, string metricId)

Formats the IDs into the string representation of this [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) with pattern `projects/{project}/metrics/{metric}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`metricId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Metric` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) with pattern `projects/{project}/metrics/{metric}`.  
  
### FormatProjectMetric(string, string)
    
    
    public static string FormatProjectMetric(string projectId, string metricId)

Formats the IDs into the string representation of this [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) with pattern `projects/{project}/metrics/{metric}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`metricId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Metric` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) with pattern `projects/{project}/metrics/{metric}`.  
  
### FromProjectMetric(string, string)
    
    
    public static LogMetricName FromProjectMetric(string projectId, string metricId)

Creates a [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) with the pattern `projects/{project}/metrics/{metric}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`metricId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Metric` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)` | A new instance of [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static LogMetricName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)` | A new instance of [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static LogMetricName Parse(string logMetricName)

Parses the given resource name string into a new [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) instance.

**Parameter**  
---  
**Name** | **Description**  
`logMetricName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)` | The parsed [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/metrics/{metric}`



### Parse(string, bool)
    
    
    public static LogMetricName Parse(string logMetricName, bool allowUnparsed)

Parses the given resource name string into a new [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`logMetricName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName#Google_Cloud_Logging_V2_LogMetricName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)` | The parsed [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/metrics/{metric}`

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

### TryParse(string, out LogMetricName)
    
    
    public static bool TryParse(string logMetricName, out LogMetricName result)

Tries to parse the given resource name string into a new [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) instance.

**Parameters**  
---  
**Name** | **Description**  
`logMetricName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)`  
When this method returns, the parsed [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/metrics/{metric}`



### TryParse(string, bool, out LogMetricName)
    
    
    public static bool TryParse(string logMetricName, bool allowUnparsed, out LogMetricName result)

Tries to parse the given resource name string into a new [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`logMetricName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName#Google_Cloud_Logging_V2_LogMetricName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)`  
When this method returns, the parsed [LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/metrics/{metric}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(LogMetricName, LogMetricName)
    
    
    public static bool operator ==(LogMetricName a, LogMetricName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)`  
The first resource name to compare, or null.  
`b` | `[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(LogMetricName, LogMetricName)
    
    
    public static bool operator !=(LogMetricName a, LogMetricName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)`  
The first resource name to compare, or null.  
`b` | `[LogMetricName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Logging.V2/latest/Google.Cloud.Logging.V2.LogMetricName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
