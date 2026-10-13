---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName
title: Google Cloud Dataproc v1 API - Class SessionTemplateName (5.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:25.994896+00:00
---

# Google Cloud Dataproc v1 API - Class SessionTemplateName (5.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dataproc v1 API - Class SessionTemplateName (5.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.28.0 (latest)  5.27.0  5.26.0  5.25.0  5.24.0  5.23.0  5.22.0  5.21.0  5.20.0  5.19.0  5.18.0  5.17.0  5.16.0  5.15.0  5.14.0  5.13.0  5.12.0  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.0.0  3.4.0  3.3.0  3.2.0  3.1.0 
    
    
    public sealed class SessionTemplateName : IResourceName, IEquatable<SessionTemplateName>

Reference documentation and code samples for the Google Cloud Dataproc v1 API class SessionTemplateName.

Resource name for the `SessionTemplate` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SessionTemplateName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Dataproc.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1)

## Assembly

Google.Cloud.Dataproc.V1.dll

## Constructors 

### SessionTemplateName(string, string, string)
    
    
    public SessionTemplateName(string projectId, string locationId, string templateId)

Constructs a new instance of a [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) class from the component parts of pattern `projects/{project}/locations/{location}/sessionTemplates/{template}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Template` ID. Must not be `null` or empty.  
  
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
  
### TemplateId
    
    
    public string TemplateId { get; }

The `Template` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public SessionTemplateName.ResourceNameType Type { get; }

The [SessionTemplateName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string templateId)

Formats the IDs into the string representation of this [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) with pattern `projects/{project}/locations/{location}/sessionTemplates/{template}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Template` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) with pattern `projects/{project}/locations/{location}/sessionTemplates/{template}`.  
  
### FormatProjectLocationTemplate(string, string, string)
    
    
    public static string FormatProjectLocationTemplate(string projectId, string locationId, string templateId)

Formats the IDs into the string representation of this [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) with pattern `projects/{project}/locations/{location}/sessionTemplates/{template}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Template` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) with pattern `projects/{project}/locations/{location}/sessionTemplates/{template}`.  
  
### FromProjectLocationTemplate(string, string, string)
    
    
    public static SessionTemplateName FromProjectLocationTemplate(string projectId, string locationId, string templateId)

Creates a [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) with the pattern `projects/{project}/locations/{location}/sessionTemplates/{template}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`templateId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Template` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)` | A new instance of [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static SessionTemplateName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)` | A new instance of [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static SessionTemplateName Parse(string sessionTemplateName)

Parses the given resource name string into a new [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) instance.

**Parameter**  
---  
**Name** | **Description**  
`sessionTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)` | The parsed [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessionTemplates/{template}`



### Parse(string, bool)
    
    
    public static SessionTemplateName Parse(string sessionTemplateName, bool allowUnparsed)

Parses the given resource name string into a new [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`sessionTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName#Google_Cloud_Dataproc_V1_SessionTemplateName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)` | The parsed [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessionTemplates/{template}`



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

### TryParse(string, out SessionTemplateName)
    
    
    public static bool TryParse(string sessionTemplateName, out SessionTemplateName result)

Tries to parse the given resource name string into a new [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) instance.

**Parameters**  
---  
**Name** | **Description**  
`sessionTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)`  
When this method returns, the parsed [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessionTemplates/{template}`



### TryParse(string, bool, out SessionTemplateName)
    
    
    public static bool TryParse(string sessionTemplateName, bool allowUnparsed, out SessionTemplateName result)

Tries to parse the given resource name string into a new [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`sessionTemplateName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName#Google_Cloud_Dataproc_V1_SessionTemplateName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)`  
When this method returns, the parsed [SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sessionTemplates/{template}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(SessionTemplateName, SessionTemplateName)
    
    
    public static bool operator ==(SessionTemplateName a, SessionTemplateName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)`  
The first resource name to compare, or null.  
`b` | `[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(SessionTemplateName, SessionTemplateName)
    
    
    public static bool operator !=(SessionTemplateName a, SessionTemplateName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)`  
The first resource name to compare, or null.  
`b` | `[SessionTemplateName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataproc.V1/latest/Google.Cloud.Dataproc.V1.SessionTemplateName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
