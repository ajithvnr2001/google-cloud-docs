---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName
title: Dataproc Metastore v1 API - Class MetadataImportName (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:36:00.678414+00:00
---

# Dataproc Metastore v1 API - Class MetadataImportName (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataproc Metastore v1 API - Class MetadataImportName (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.9.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.8.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.7.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.6.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.5.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.4.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.3.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.2.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.1.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/2.0.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.1.0/Google.Cloud.Metastore.V1.MetadataImportName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/1.0.0/Google.Cloud.Metastore.V1.MetadataImportName)


    
    
    public sealed class MetadataImportName : IResourceName, IEquatable<MetadataImportName>

Reference documentation and code samples for the Dataproc Metastore v1 API class MetadataImportName.

Resource name for the `MetadataImport` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MetadataImportName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Metastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1)

## Assembly

Google.Cloud.Metastore.V1.dll

## Constructors 

### MetadataImportName(string, string, string, string)
    
    
    public MetadataImportName(string projectId, string locationId, string serviceId, string metadataImportId)

Constructs a new instance of a [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) class from the component parts of pattern `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MetadataImport` ID. Must not be `null` or empty.  
  
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
  
### MetadataImportId
    
    
    public string MetadataImportId { get; }

The `MetadataImport` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### ServiceId
    
    
    public string ServiceId { get; }

The `Service` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public MetadataImportName.ResourceNameType Type { get; }

The [MetadataImportName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string serviceId, string metadataImportId)

Formats the IDs into the string representation of this [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) with pattern `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MetadataImport` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) with pattern `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`.  
  
### FormatProjectLocationServiceMetadataImport(string, string, string, string)
    
    
    public static string FormatProjectLocationServiceMetadataImport(string projectId, string locationId, string serviceId, string metadataImportId)

Formats the IDs into the string representation of this [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) with pattern `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MetadataImport` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) with pattern `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`.  
  
### FromProjectLocationServiceMetadataImport(string, string, string, string)
    
    
    public static MetadataImportName FromProjectLocationServiceMetadataImport(string projectId, string locationId, string serviceId, string metadataImportId)

Creates a [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) with the pattern `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`metadataImportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MetadataImport` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)` | A new instance of [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static MetadataImportName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)` | A new instance of [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static MetadataImportName Parse(string metadataImportName)

Parses the given resource name string into a new [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) instance.

**Parameter**  
---  
**Name** | **Description**  
`metadataImportName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)` | The parsed [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`



### Parse(string, bool)
    
    
    public static MetadataImportName Parse(string metadataImportName, bool allowUnparsed)

Parses the given resource name string into a new [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`metadataImportName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName#Google_Cloud_Metastore_V1_MetadataImportName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)` | The parsed [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`

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

### TryParse(string, out MetadataImportName)
    
    
    public static bool TryParse(string metadataImportName, out MetadataImportName result)

Tries to parse the given resource name string into a new [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) instance.

**Parameters**  
---  
**Name** | **Description**  
`metadataImportName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)`  
When this method returns, the parsed [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`



### TryParse(string, bool, out MetadataImportName)
    
    
    public static bool TryParse(string metadataImportName, bool allowUnparsed, out MetadataImportName result)

Tries to parse the given resource name string into a new [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`metadataImportName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName#Google_Cloud_Metastore_V1_MetadataImportName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)`  
When this method returns, the parsed [MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(MetadataImportName, MetadataImportName)
    
    
    public static bool operator ==(MetadataImportName a, MetadataImportName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)`  
The first resource name to compare, or null.  
`b` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(MetadataImportName, MetadataImportName)
    
    
    public static bool operator !=(MetadataImportName a, MetadataImportName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)`  
The first resource name to compare, or null.  
`b` | `[MetadataImportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Metastore.V1/latest/Google.Cloud.Metastore.V1.MetadataImportName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
