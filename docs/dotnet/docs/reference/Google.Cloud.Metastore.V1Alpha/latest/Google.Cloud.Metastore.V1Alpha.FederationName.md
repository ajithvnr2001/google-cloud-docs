---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName
title: Dataproc Metastore v1alpha API - Class FederationName (2.0.0-alpha12) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:29.593644+00:00
---

# Dataproc Metastore v1alpha API - Class FederationName (2.0.0-alpha12)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1alpha API - Class FederationName (2.0.0-alpha12) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha12 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)
  * [ 2.0.0-alpha11 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/2.0.0-alpha11/Google.Cloud.Metastore.V1Alpha.FederationName)
  * [ 1.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/1.0.0-alpha04/Google.Cloud.Metastore.V1Alpha.FederationName)


    
    
    public sealed class FederationName : IResourceName, IEquatable<FederationName>

Reference documentation and code samples for the Dataproc Metastore v1alpha API class FederationName.

Resource name for the `Federation` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FederationName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Metastore.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha)

## Assembly

Google.Cloud.Metastore.V1Alpha.dll

## Constructors 

### FederationName(string, string, string)
    
    
    public FederationName(string projectId, string locationId, string federationId)

Constructs a new instance of a [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) class from the component parts of pattern `projects/{project}/locations/{location}/federations/{federation}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Federation` ID. Must not be `null` or empty.  
  
## Properties 

### FederationId
    
    
    public string FederationId { get; }

The `Federation` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public FederationName.ResourceNameType Type { get; }

The [FederationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string federationId)

Formats the IDs into the string representation of this [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) with pattern `projects/{project}/locations/{location}/federations/{federation}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Federation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) with pattern `projects/{project}/locations/{location}/federations/{federation}`.  
  
### FormatProjectLocationFederation(string, string, string)
    
    
    public static string FormatProjectLocationFederation(string projectId, string locationId, string federationId)

Formats the IDs into the string representation of this [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) with pattern `projects/{project}/locations/{location}/federations/{federation}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Federation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) with pattern `projects/{project}/locations/{location}/federations/{federation}`.  
  
### FromProjectLocationFederation(string, string, string)
    
    
    public static FederationName FromProjectLocationFederation(string projectId, string locationId, string federationId)

Creates a [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) with the pattern `projects/{project}/locations/{location}/federations/{federation}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`federationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Federation` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)` | A new instance of [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static FederationName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)` | A new instance of [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static FederationName Parse(string federationName)

Parses the given resource name string into a new [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) instance.

**Parameter**  
---  
**Name** | **Description**  
`federationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)` | The parsed [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/federations/{federation}`



### Parse(string, bool)
    
    
    public static FederationName Parse(string federationName, bool allowUnparsed)

Parses the given resource name string into a new [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`federationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName#Google_Cloud_Metastore_V1Alpha_FederationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)` | The parsed [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/federations/{federation}`

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

### TryParse(string, out FederationName)
    
    
    public static bool TryParse(string federationName, out FederationName result)

Tries to parse the given resource name string into a new [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) instance.

**Parameters**  
---  
**Name** | **Description**  
`federationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)`  
When this method returns, the parsed [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/federations/{federation}`



### TryParse(string, bool, out FederationName)
    
    
    public static bool TryParse(string federationName, bool allowUnparsed, out FederationName result)

Tries to parse the given resource name string into a new [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`federationName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName#Google_Cloud_Metastore_V1Alpha_FederationName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)`  
When this method returns, the parsed [FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/federations/{federation}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(FederationName, FederationName)
    
    
    public static bool operator ==(FederationName a, FederationName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)`  
The first resource name to compare, or null.  
`b` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(FederationName, FederationName)
    
    
    public static bool operator !=(FederationName a, FederationName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)`  
The first resource name to compare, or null.  
`b` | `[FederationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1Alpha/latest/Google.Cloud.Metastore.V1Alpha.FederationName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
