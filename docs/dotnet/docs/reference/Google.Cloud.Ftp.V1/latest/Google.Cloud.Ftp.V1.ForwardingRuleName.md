---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName
title: Cloud FTP v1 API - Class ForwardingRuleName (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:16.315014+00:00
---

# Cloud FTP v1 API - Class ForwardingRuleName (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud FTP v1 API - Class ForwardingRuleName (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class ForwardingRuleName : IResourceName, IEquatable<ForwardingRuleName>

Reference documentation and code samples for the Cloud FTP v1 API class ForwardingRuleName.

Resource name for the `ForwardingRule` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ForwardingRuleName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Ftp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1)

## Assembly

Google.Cloud.Ftp.V1.dll

## Constructors 

### ForwardingRuleName(string, string, string)
    
    
    public ForwardingRuleName(string projectId, string regionId, string forwardingRuleId)

Constructs a new instance of a [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) class from the component parts of pattern `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`forwardingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ForwardingRule` ID. Must not be `null` or empty.  
  
## Properties 

### ForwardingRuleId
    
    
    public string ForwardingRuleId { get; }

The `ForwardingRule` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### RegionId
    
    
    public string RegionId { get; }

The `Region` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ForwardingRuleName.ResourceNameType Type { get; }

The [ForwardingRuleName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string regionId, string forwardingRuleId)

Formats the IDs into the string representation of this [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) with pattern `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`forwardingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ForwardingRule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) with pattern `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`.  
  
### FormatProjectRegionForwardingRule(string, string, string)
    
    
    public static string FormatProjectRegionForwardingRule(string projectId, string regionId, string forwardingRuleId)

Formats the IDs into the string representation of this [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) with pattern `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`forwardingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ForwardingRule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) with pattern `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`.  
  
### FromProjectRegionForwardingRule(string, string, string)
    
    
    public static ForwardingRuleName FromProjectRegionForwardingRule(string projectId, string regionId, string forwardingRuleId)

Creates a [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) with the pattern `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`regionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Region` ID. Must not be `null` or empty.  
`forwardingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ForwardingRule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)` | A new instance of [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ForwardingRuleName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)` | A new instance of [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ForwardingRuleName Parse(string forwardingRuleName)

Parses the given resource name string into a new [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) instance.

**Parameter**  
---  
**Name** | **Description**  
`forwardingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)` | The parsed [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`



### Parse(string, bool)
    
    
    public static ForwardingRuleName Parse(string forwardingRuleName, bool allowUnparsed)

Parses the given resource name string into a new [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`forwardingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName#Google_Cloud_Ftp_V1_ForwardingRuleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)` | The parsed [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`



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

### TryParse(string, out ForwardingRuleName)
    
    
    public static bool TryParse(string forwardingRuleName, out ForwardingRuleName result)

Tries to parse the given resource name string into a new [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) instance.

**Parameters**  
---  
**Name** | **Description**  
`forwardingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)`  
When this method returns, the parsed [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`



### TryParse(string, bool, out ForwardingRuleName)
    
    
    public static bool TryParse(string forwardingRuleName, bool allowUnparsed, out ForwardingRuleName result)

Tries to parse the given resource name string into a new [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`forwardingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName#Google_Cloud_Ftp_V1_ForwardingRuleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)`  
When this method returns, the parsed [ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ForwardingRuleName, ForwardingRuleName)
    
    
    public static bool operator ==(ForwardingRuleName a, ForwardingRuleName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)`  
The first resource name to compare, or null.  
`b` | `[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ForwardingRuleName, ForwardingRuleName)
    
    
    public static bool operator !=(ForwardingRuleName a, ForwardingRuleName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)`  
The first resource name to compare, or null.  
`b` | `[ForwardingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ftp.V1/latest/Google.Cloud.Ftp.V1.ForwardingRuleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
