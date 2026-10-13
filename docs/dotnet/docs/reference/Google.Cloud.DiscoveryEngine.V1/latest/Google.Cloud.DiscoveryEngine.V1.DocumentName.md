---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName
title: Discovery Engine v1 API - Class DocumentName (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:12.731482+00:00
---

# Discovery Engine v1 API - Class DocumentName (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class DocumentName (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public sealed class DocumentName : IResourceName, IEquatable<DocumentName>

Reference documentation and code samples for the Discovery Engine v1 API class DocumentName.

Resource name for the `Document` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DocumentName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Constructors 

### DocumentName(string, string, string, string, string)
    
    
    public DocumentName(string projectId, string locationId, string dataStoreId, string branchId, string documentId)

Constructs a new instance of a [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) class from the component parts of pattern `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`branchId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Branch` ID. Must not be `null` or empty.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Document` ID. Must not be `null` or empty.  
  
## Properties 

### BranchId
    
    
    public string BranchId { get; }

The `Branch` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CollectionId
    
    
    public string CollectionId { get; }

The `Collection` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataStoreId
    
    
    public string DataStoreId { get; }

The `DataStore` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DocumentId
    
    
    public string DocumentId { get; }

The `Document` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### ProjectId
    
    
    public string ProjectId { get; }

The `Project` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public DocumentName.ResourceNameType Type { get; }

The [DocumentName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string dataStoreId, string branchId, string documentId)

Formats the IDs into the string representation of this [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`branchId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Branch` ID. Must not be `null` or empty.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Document` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}` .  
  
### FormatProjectLocationCollectionDataStoreBranchDocument(string, string, string, string, string, string)
    
    
    public static string FormatProjectLocationCollectionDataStoreBranchDocument(string projectId, string locationId, string collectionId, string dataStoreId, string branchId, string documentId)

Formats the IDs into the string representation of this [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with pattern ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Collection` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`branchId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Branch` ID. Must not be `null` or empty.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Document` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with pattern ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}` .  
  
### FormatProjectLocationDataStoreBranchDocument(string, string, string, string, string)
    
    
    public static string FormatProjectLocationDataStoreBranchDocument(string projectId, string locationId, string dataStoreId, string branchId, string documentId)

Formats the IDs into the string representation of this [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`branchId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Branch` ID. Must not be `null` or empty.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Document` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}` .  
  
### FromProjectLocationCollectionDataStoreBranchDocument(string, string, string, string, string, string)
    
    
    public static DocumentName FromProjectLocationCollectionDataStoreBranchDocument(string projectId, string locationId, string collectionId, string dataStoreId, string branchId, string documentId)

Creates a [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with the pattern ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Collection` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`branchId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Branch` ID. Must not be `null` or empty.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Document` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)` | A new instance of [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) constructed from the provided ids.  
  
### FromProjectLocationDataStoreBranchDocument(string, string, string, string, string)
    
    
    public static DocumentName FromProjectLocationDataStoreBranchDocument(string projectId, string locationId, string dataStoreId, string branchId, string documentId)

Creates a [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) with the pattern `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`branchId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Branch` ID. Must not be `null` or empty.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Document` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)` | A new instance of [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static DocumentName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)` | A new instance of [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) containing the provided `unparsedResourceName` .  
  
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
    
    
    public static DocumentName Parse(string documentName)

Parses the given resource name string into a new [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) instance.

**Parameter**  
---  
**Name** | **Description**  
`documentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)` | The parsed [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`



### Parse(string, bool)
    
    
    public static DocumentName Parse(string documentName, bool allowUnparsed)

Parses the given resource name string into a new [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`documentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName#Google_Cloud_DiscoveryEngine_V1_DocumentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)` | The parsed [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`



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

### TryParse(string, out DocumentName)
    
    
    public static bool TryParse(string documentName, out DocumentName result)

Tries to parse the given resource name string into a new [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) instance.

**Parameters**  
---  
**Name** | **Description**  
`documentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)`  
When this method returns, the parsed [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`



### TryParse(string, bool, out DocumentName)
    
    
    public static bool TryParse(string documentName, bool allowUnparsed, out DocumentName result)

Tries to parse the given resource name string into a new [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`documentName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName#Google_Cloud_DiscoveryEngine_V1_DocumentName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)`  
When this method returns, the parsed [DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(DocumentName, DocumentName)
    
    
    public static bool operator ==(DocumentName a, DocumentName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)`  
The first resource name to compare, or null.  
`b` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(DocumentName, DocumentName)
    
    
    public static bool operator !=(DocumentName a, DocumentName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)`  
The first resource name to compare, or null.  
`b` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.DocumentName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
