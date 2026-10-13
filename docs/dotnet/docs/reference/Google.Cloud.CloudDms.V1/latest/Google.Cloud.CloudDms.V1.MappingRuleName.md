---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName
title: Database Migration v1 API - Class MappingRuleName (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:21.947706+00:00
---

# Database Migration v1 API - Class MappingRuleName (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Migration v1 API - Class MappingRuleName (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.5.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.4.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.3.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.2.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.1.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.0.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.2.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.1.0/Google.Cloud.CloudDms.V1.MappingRuleName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.0.0/Google.Cloud.CloudDms.V1.MappingRuleName)


    
    
    public sealed class MappingRuleName : IResourceName, IEquatable<MappingRuleName>

Reference documentation and code samples for the Database Migration v1 API class MappingRuleName.

Resource name for the `MappingRule` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MappingRuleName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.CloudDms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1)

## Assembly

Google.Cloud.CloudDms.V1.dll

## Constructors 

### MappingRuleName(string, string, string, string)
    
    
    public MappingRuleName(string projectId, string locationId, string conversionWorkspaceId, string mappingRuleId)

Constructs a new instance of a [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) class from the component parts of pattern ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`conversionWorkspaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConversionWorkspace` ID. Must not be `null` or empty.  
`mappingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MappingRule` ID. Must not be `null` or empty.  
  
## Properties 

### ConversionWorkspaceId
    
    
    public string ConversionWorkspaceId { get; }

The `ConversionWorkspace` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### MappingRuleId
    
    
    public string MappingRuleId { get; }

The `MappingRule` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public MappingRuleName.ResourceNameType Type { get; }

The [MappingRuleName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string conversionWorkspaceId, string mappingRuleId)

Formats the IDs into the string representation of this [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) with pattern ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`conversionWorkspaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConversionWorkspace` ID. Must not be `null` or empty.  
`mappingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MappingRule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) with pattern ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}` .  
  
### FormatProjectLocationConversionWorkspaceMappingRule(string, string, string, string)
    
    
    public static string FormatProjectLocationConversionWorkspaceMappingRule(string projectId, string locationId, string conversionWorkspaceId, string mappingRuleId)

Formats the IDs into the string representation of this [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) with pattern ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`conversionWorkspaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConversionWorkspace` ID. Must not be `null` or empty.  
`mappingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MappingRule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) with pattern ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}` .  
  
### FromProjectLocationConversionWorkspaceMappingRule(string, string, string, string)
    
    
    public static MappingRuleName FromProjectLocationConversionWorkspaceMappingRule(string projectId, string locationId, string conversionWorkspaceId, string mappingRuleId)

Creates a [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) with the pattern ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`conversionWorkspaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConversionWorkspace` ID. Must not be `null` or empty.  
`mappingRuleId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MappingRule` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)` | A new instance of [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static MappingRuleName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)` | A new instance of [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static MappingRuleName Parse(string mappingRuleName)

Parses the given resource name string into a new [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) instance.

**Parameter**  
---  
**Name** | **Description**  
`mappingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)` | The parsed [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}`



### Parse(string, bool)
    
    
    public static MappingRuleName Parse(string mappingRuleName, bool allowUnparsed)

Parses the given resource name string into a new [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`mappingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName#Google_Cloud_CloudDms_V1_MappingRuleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)` | The parsed [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}`

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

### TryParse(string, out MappingRuleName)
    
    
    public static bool TryParse(string mappingRuleName, out MappingRuleName result)

Tries to parse the given resource name string into a new [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) instance.

**Parameters**  
---  
**Name** | **Description**  
`mappingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)`  
When this method returns, the parsed [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}`



### TryParse(string, bool, out MappingRuleName)
    
    
    public static bool TryParse(string mappingRuleName, bool allowUnparsed, out MappingRuleName result)

Tries to parse the given resource name string into a new [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`mappingRuleName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName#Google_Cloud_CloudDms_V1_MappingRuleName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)`  
When this method returns, the parsed [MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * ` projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}/mappingRules/{mapping_rule}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(MappingRuleName, MappingRuleName)
    
    
    public static bool operator ==(MappingRuleName a, MappingRuleName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)`  
The first resource name to compare, or null.  
`b` | `[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(MappingRuleName, MappingRuleName)
    
    
    public static bool operator !=(MappingRuleName a, MappingRuleName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)`  
The first resource name to compare, or null.  
`b` | `[MappingRuleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.MappingRuleName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
