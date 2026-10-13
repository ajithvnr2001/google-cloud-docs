---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName
title: Developer Connect v1 API - Class InsightsConfigName (1.0.0-beta04) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:10.504641+00:00
---

# Developer Connect v1 API - Class InsightsConfigName (1.0.0-beta04)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Developer Connect v1 API - Class InsightsConfigName (1.0.0-beta04) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta04 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/1.0.0-beta03/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)


    
    
    public sealed class InsightsConfigName : IResourceName, IEquatable<InsightsConfigName>

Reference documentation and code samples for the Developer Connect v1 API class InsightsConfigName.

Resource name for the `InsightsConfig` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InsightsConfigName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.DeveloperConnect.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1)

## Assembly

Google.Cloud.DeveloperConnect.V1.dll

## Constructors 

### InsightsConfigName(string, string, string)
    
    
    public InsightsConfigName(string projectId, string locationId, string insightsConfigId)

Constructs a new instance of a [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) class from the component parts of pattern `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightsConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightsConfig` ID. Must not be `null` or empty.  
  
## Properties 

### InsightsConfigId
    
    
    public string InsightsConfigId { get; }

The `InsightsConfig` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public InsightsConfigName.ResourceNameType Type { get; }

The [InsightsConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string insightsConfigId)

Formats the IDs into the string representation of this [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) with pattern `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightsConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightsConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) with pattern `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`.  
  
### FormatProjectLocationInsightsConfig(string, string, string)
    
    
    public static string FormatProjectLocationInsightsConfig(string projectId, string locationId, string insightsConfigId)

Formats the IDs into the string representation of this [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) with pattern `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightsConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightsConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) with pattern `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`.  
  
### FromProjectLocationInsightsConfig(string, string, string)
    
    
    public static InsightsConfigName FromProjectLocationInsightsConfig(string projectId, string locationId, string insightsConfigId)

Creates a [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) with the pattern `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightsConfigId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightsConfig` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)` | A new instance of [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static InsightsConfigName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)` | A new instance of [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static InsightsConfigName Parse(string insightsConfigName)

Parses the given resource name string into a new [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) instance.

**Parameter**  
---  
**Name** | **Description**  
`insightsConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)` | The parsed [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`



### Parse(string, bool)
    
    
    public static InsightsConfigName Parse(string insightsConfigName, bool allowUnparsed)

Parses the given resource name string into a new [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`insightsConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName#Google_Cloud_DeveloperConnect_V1_InsightsConfigName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)` | The parsed [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`

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

### TryParse(string, out InsightsConfigName)
    
    
    public static bool TryParse(string insightsConfigName, out InsightsConfigName result)

Tries to parse the given resource name string into a new [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) instance.

**Parameters**  
---  
**Name** | **Description**  
`insightsConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)`  
When this method returns, the parsed [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`



### TryParse(string, bool, out InsightsConfigName)
    
    
    public static bool TryParse(string insightsConfigName, bool allowUnparsed, out InsightsConfigName result)

Tries to parse the given resource name string into a new [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`insightsConfigName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName#Google_Cloud_DeveloperConnect_V1_InsightsConfigName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)`  
When this method returns, the parsed [InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/insightsConfigs/{insights_config}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(InsightsConfigName, InsightsConfigName)
    
    
    public static bool operator ==(InsightsConfigName a, InsightsConfigName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)`  
The first resource name to compare, or null.  
`b` | `[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(InsightsConfigName, InsightsConfigName)
    
    
    public static bool operator !=(InsightsConfigName a, InsightsConfigName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)`  
The first resource name to compare, or null.  
`b` | `[InsightsConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.InsightsConfigName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
