---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName
title: Gemini Enterprise for Customer Experience v1beta API - Class DeidentifyTemplateName (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:10.451539+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class DeidentifyTemplateName (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class DeidentifyTemplateName (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class DeidentifyTemplateName : IResourceName, IEquatable<DeidentifyTemplateName>

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class DeidentifyTemplateName.

Resource name for the `DeidentifyTemplate` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeidentifyTemplateName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### DeidentifyTemplateName(string, string, string)
    
    
    public DeidentifyTemplateName(string organizationId, string locationId, string deidentifyTemplateId)

Constructs a new instance of a [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) class from the component parts of pattern `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`deidentifyTemplateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeidentifyTemplate` ID. Must not be `null` or empty.  
  
## Properties 

### DeidentifyTemplateId
    
    
    public string DeidentifyTemplateId { get; }

The `DeidentifyTemplate` ID. May be `null`, depending on which resource name is contained by this instance.

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

The `Location` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrganizationId
    
    
    public string OrganizationId { get; }

The `Organization` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public DeidentifyTemplateName.ResourceNameType Type { get; }

The [DeidentifyTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string organizationId, string locationId, string deidentifyTemplateId)

Formats the IDs into the string representation of this [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with pattern `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`deidentifyTemplateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeidentifyTemplate` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with pattern `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`.  
  
### FormatOrganizationLocationDeidentifyTemplate(string, string, string)
    
    
    public static string FormatOrganizationLocationDeidentifyTemplate(string organizationId, string locationId, string deidentifyTemplateId)

Formats the IDs into the string representation of this [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with pattern `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`deidentifyTemplateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeidentifyTemplate` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with pattern `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`.  
  
### FormatProjectLocationDeidentifyTemplate(string, string, string)
    
    
    public static string FormatProjectLocationDeidentifyTemplate(string projectId, string locationId, string deidentifyTemplateId)

Formats the IDs into the string representation of this [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with pattern `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`deidentifyTemplateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeidentifyTemplate` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with pattern `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`.  
  
### FromOrganizationLocationDeidentifyTemplate(string, string, string)
    
    
    public static DeidentifyTemplateName FromOrganizationLocationDeidentifyTemplate(string organizationId, string locationId, string deidentifyTemplateId)

Creates a [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with the pattern `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`deidentifyTemplateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeidentifyTemplate` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)` | A new instance of [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) constructed from the provided ids.  
  
### FromProjectLocationDeidentifyTemplate(string, string, string)
    
    
    public static DeidentifyTemplateName FromProjectLocationDeidentifyTemplate(string projectId, string locationId, string deidentifyTemplateId)

Creates a [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) with the pattern `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`deidentifyTemplateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DeidentifyTemplate` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)` | A new instance of [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static DeidentifyTemplateName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)` | A new instance of [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static DeidentifyTemplateName Parse(string deidentifyTemplateName)

Parses the given resource name string into a new [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) instance.

**Parameter**  
---  
**Name** | **Description**  
`deidentifyTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)` | The parsed [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`
  * `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`



### Parse(string, bool)
    
    
    public static DeidentifyTemplateName Parse(string deidentifyTemplateName, bool allowUnparsed)

Parses the given resource name string into a new [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`deidentifyTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName#Google_Cloud_Ces_V1Beta_DeidentifyTemplateName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)` | The parsed [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`
  * `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`



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

### TryParse(string, out DeidentifyTemplateName)
    
    
    public static bool TryParse(string deidentifyTemplateName, out DeidentifyTemplateName result)

Tries to parse the given resource name string into a new [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) instance.

**Parameters**  
---  
**Name** | **Description**  
`deidentifyTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)`  
When this method returns, the parsed [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`
  * `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`



### TryParse(string, bool, out DeidentifyTemplateName)
    
    
    public static bool TryParse(string deidentifyTemplateName, bool allowUnparsed, out DeidentifyTemplateName result)

Tries to parse the given resource name string into a new [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`deidentifyTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName#Google_Cloud_Ces_V1Beta_DeidentifyTemplateName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)`  
When this method returns, the parsed [DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/locations/{location}/deidentifyTemplates/{deidentify_template}`
  * `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(DeidentifyTemplateName, DeidentifyTemplateName)
    
    
    public static bool operator ==(DeidentifyTemplateName a, DeidentifyTemplateName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)`  
The first resource name to compare, or null.  
`b` | `[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(DeidentifyTemplateName, DeidentifyTemplateName)
    
    
    public static bool operator !=(DeidentifyTemplateName a, DeidentifyTemplateName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)`  
The first resource name to compare, or null.  
`b` | `[DeidentifyTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DeidentifyTemplateName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
