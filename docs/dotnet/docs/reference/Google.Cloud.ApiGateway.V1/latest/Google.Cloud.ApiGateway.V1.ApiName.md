---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName
title: API Gateway v1 API - Class ApiName (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:46.128009+00:00
---

# API Gateway v1 API - Class ApiName (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API Gateway v1 API - Class ApiName (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.1.0  1.0.0 
    
    
    public sealed class ApiName : IResourceName, IEquatable<ApiName>

Reference documentation and code samples for the API Gateway v1 API class ApiName.

Resource name for the `Api` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ApiName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.ApiGateway.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1)

## Assembly

Google.Cloud.ApiGateway.V1.dll

## Constructors 

### ApiName(string, string)
    
    
    public ApiName(string projectId, string apiId)

Constructs a new instance of a [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) class from the component parts of pattern `projects/{project}/locations/global/apis/{api}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`apiId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Api` ID. Must not be `null` or empty.  
  
## Properties 

### ApiId
    
    
    public string ApiId { get; }

The `Api` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public ApiName.ResourceNameType Type { get; }

The [ApiName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string projectId, string apiId)

Formats the IDs into the string representation of this [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) with pattern `projects/{project}/locations/global/apis/{api}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`apiId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Api` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) with pattern `projects/{project}/locations/global/apis/{api}`.  
  
### FormatProjectApi(string, string)
    
    
    public static string FormatProjectApi(string projectId, string apiId)

Formats the IDs into the string representation of this [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) with pattern `projects/{project}/locations/global/apis/{api}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`apiId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Api` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) with pattern `projects/{project}/locations/global/apis/{api}`.  
  
### FromProjectApi(string, string)
    
    
    public static ApiName FromProjectApi(string projectId, string apiId)

Creates a [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) with the pattern `projects/{project}/locations/global/apis/{api}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`apiId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Api` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)` | A new instance of [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ApiName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)` | A new instance of [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ApiName Parse(string apiName)

Parses the given resource name string into a new [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) instance.

**Parameter**  
---  
**Name** | **Description**  
`apiName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)` | The parsed [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/global/apis/{api}`



### Parse(string, bool)
    
    
    public static ApiName Parse(string apiName, bool allowUnparsed)

Parses the given resource name string into a new [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`apiName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName#Google_Cloud_ApiGateway_V1_ApiName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)` | The parsed [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/global/apis/{api}`



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

### TryParse(string, out ApiName)
    
    
    public static bool TryParse(string apiName, out ApiName result)

Tries to parse the given resource name string into a new [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) instance.

**Parameters**  
---  
**Name** | **Description**  
`apiName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)`  
When this method returns, the parsed [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/global/apis/{api}`



### TryParse(string, bool, out ApiName)
    
    
    public static bool TryParse(string apiName, bool allowUnparsed, out ApiName result)

Tries to parse the given resource name string into a new [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`apiName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName#Google_Cloud_ApiGateway_V1_ApiName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)`  
When this method returns, the parsed [ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/global/apis/{api}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ApiName, ApiName)
    
    
    public static bool operator ==(ApiName a, ApiName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)`  
The first resource name to compare, or null.  
`b` | `[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ApiName, ApiName)
    
    
    public static bool operator !=(ApiName a, ApiName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)`  
The first resource name to compare, or null.  
`b` | `[ApiName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiGateway.V1/latest/Google.Cloud.ApiGateway.V1.ApiName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
