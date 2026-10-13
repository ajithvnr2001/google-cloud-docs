---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName
title: Vertex AI v1beta1 API - Class RagDataSchemaName (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:16.634159+00:00
---

# Vertex AI v1beta1 API - Class RagDataSchemaName (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class RagDataSchemaName (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class RagDataSchemaName : IResourceName, IEquatable<RagDataSchemaName>

Reference documentation and code samples for the Vertex AI v1beta1 API class RagDataSchemaName.

Resource name for the `RagDataSchema` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RagDataSchemaName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### RagDataSchemaName(string, string, string, string)
    
    
    public RagDataSchemaName(string projectId, string locationId, string ragCorpusId, string ragDataSchemaId)

Constructs a new instance of a [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) class from the component parts of pattern `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`ragCorpusId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagCorpus` ID. Must not be `null` or empty.  
`ragDataSchemaId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagDataSchema` ID. Must not be `null` or empty.  
  
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
  
### RagCorpusId
    
    
    public string RagCorpusId { get; }

The `RagCorpus` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RagDataSchemaId
    
    
    public string RagDataSchemaId { get; }

The `RagDataSchema` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public RagDataSchemaName.ResourceNameType Type { get; }

The [RagDataSchemaName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string ragCorpusId, string ragDataSchemaId)

Formats the IDs into the string representation of this [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) with pattern `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`ragCorpusId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagCorpus` ID. Must not be `null` or empty.  
`ragDataSchemaId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagDataSchema` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) with pattern `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`.  
  
### FormatProjectLocationRagCorpusRagDataSchema(string, string, string, string)
    
    
    public static string FormatProjectLocationRagCorpusRagDataSchema(string projectId, string locationId, string ragCorpusId, string ragDataSchemaId)

Formats the IDs into the string representation of this [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) with pattern `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`ragCorpusId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagCorpus` ID. Must not be `null` or empty.  
`ragDataSchemaId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagDataSchema` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) with pattern `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`.  
  
### FromProjectLocationRagCorpusRagDataSchema(string, string, string, string)
    
    
    public static RagDataSchemaName FromProjectLocationRagCorpusRagDataSchema(string projectId, string locationId, string ragCorpusId, string ragDataSchemaId)

Creates a [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) with the pattern `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`ragCorpusId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagCorpus` ID. Must not be `null` or empty.  
`ragDataSchemaId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `RagDataSchema` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)` | A new instance of [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static RagDataSchemaName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)` | A new instance of [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static RagDataSchemaName Parse(string ragDataSchemaName)

Parses the given resource name string into a new [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) instance.

**Parameter**  
---  
**Name** | **Description**  
`ragDataSchemaName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)` | The parsed [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`



### Parse(string, bool)
    
    
    public static RagDataSchemaName Parse(string ragDataSchemaName, bool allowUnparsed)

Parses the given resource name string into a new [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`ragDataSchemaName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName#Google_Cloud_AIPlatform_V1Beta1_RagDataSchemaName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)` | The parsed [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`



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

### TryParse(string, out RagDataSchemaName)
    
    
    public static bool TryParse(string ragDataSchemaName, out RagDataSchemaName result)

Tries to parse the given resource name string into a new [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) instance.

**Parameters**  
---  
**Name** | **Description**  
`ragDataSchemaName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)`  
When this method returns, the parsed [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`



### TryParse(string, bool, out RagDataSchemaName)
    
    
    public static bool TryParse(string ragDataSchemaName, bool allowUnparsed, out RagDataSchemaName result)

Tries to parse the given resource name string into a new [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`ragDataSchemaName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName#Google_Cloud_AIPlatform_V1Beta1_RagDataSchemaName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)`  
When this method returns, the parsed [RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}/ragDataSchemas/{rag_data_schema}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(RagDataSchemaName, RagDataSchemaName)
    
    
    public static bool operator ==(RagDataSchemaName a, RagDataSchemaName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)`  
The first resource name to compare, or null.  
`b` | `[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(RagDataSchemaName, RagDataSchemaName)
    
    
    public static bool operator !=(RagDataSchemaName a, RagDataSchemaName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)`  
The first resource name to compare, or null.  
`b` | `[RagDataSchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.RagDataSchemaName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
