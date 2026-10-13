---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName
title: Memorystore v1 API - Class SharedRegionalCertificateAuthorityName (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:42.372318+00:00
---

# Memorystore v1 API - Class SharedRegionalCertificateAuthorityName (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1 API - Class SharedRegionalCertificateAuthorityName (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta09 
    
    
    public sealed class SharedRegionalCertificateAuthorityName : IResourceName, IEquatable<SharedRegionalCertificateAuthorityName>

Reference documentation and code samples for the Memorystore v1 API class SharedRegionalCertificateAuthorityName.

Resource name for the `SharedRegionalCertificateAuthority` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SharedRegionalCertificateAuthorityName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Memorystore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1)

## Assembly

Google.Cloud.Memorystore.V1.dll

## Constructors 

### SharedRegionalCertificateAuthorityName(string, string)
    
    
    public SharedRegionalCertificateAuthorityName(string projectId, string locationId)

Constructs a new instance of a [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) class from the component parts of pattern `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
  
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
  
### Type
    
    
    public SharedRegionalCertificateAuthorityName.ResourceNameType Type { get; }

The [SharedRegionalCertificateAuthorityName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string projectId, string locationId)

Formats the IDs into the string representation of this [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) with pattern `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) with pattern `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`.  
  
### FormatProjectLocation(string, string)
    
    
    public static string FormatProjectLocation(string projectId, string locationId)

Formats the IDs into the string representation of this [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) with pattern `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) with pattern `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`.  
  
### FromProjectLocation(string, string)
    
    
    public static SharedRegionalCertificateAuthorityName FromProjectLocation(string projectId, string locationId)

Creates a [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) with the pattern `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)` | A new instance of [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static SharedRegionalCertificateAuthorityName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)` | A new instance of [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static SharedRegionalCertificateAuthorityName Parse(string sharedRegionalCertificateAuthorityName)

Parses the given resource name string into a new [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) instance.

**Parameter**  
---  
**Name** | **Description**  
`sharedRegionalCertificateAuthorityName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)` | The parsed [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`



### Parse(string, bool)
    
    
    public static SharedRegionalCertificateAuthorityName Parse(string sharedRegionalCertificateAuthorityName, bool allowUnparsed)

Parses the given resource name string into a new [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`sharedRegionalCertificateAuthorityName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName#Google_Cloud_Memorystore_V1_SharedRegionalCertificateAuthorityName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)` | The parsed [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`



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

### TryParse(string, out SharedRegionalCertificateAuthorityName)
    
    
    public static bool TryParse(string sharedRegionalCertificateAuthorityName, out SharedRegionalCertificateAuthorityName result)

Tries to parse the given resource name string into a new [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) instance.

**Parameters**  
---  
**Name** | **Description**  
`sharedRegionalCertificateAuthorityName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)`  
When this method returns, the parsed [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`



### TryParse(string, bool, out SharedRegionalCertificateAuthorityName)
    
    
    public static bool TryParse(string sharedRegionalCertificateAuthorityName, bool allowUnparsed, out SharedRegionalCertificateAuthorityName result)

Tries to parse the given resource name string into a new [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`sharedRegionalCertificateAuthorityName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName#Google_Cloud_Memorystore_V1_SharedRegionalCertificateAuthorityName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)`  
When this method returns, the parsed [SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(SharedRegionalCertificateAuthorityName, SharedRegionalCertificateAuthorityName)
    
    
    public static bool operator ==(SharedRegionalCertificateAuthorityName a, SharedRegionalCertificateAuthorityName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)`  
The first resource name to compare, or null.  
`b` | `[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(SharedRegionalCertificateAuthorityName, SharedRegionalCertificateAuthorityName)
    
    
    public static bool operator !=(SharedRegionalCertificateAuthorityName a, SharedRegionalCertificateAuthorityName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)`  
The first resource name to compare, or null.  
`b` | `[SharedRegionalCertificateAuthorityName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1/latest/Google.Cloud.Memorystore.V1.SharedRegionalCertificateAuthorityName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
