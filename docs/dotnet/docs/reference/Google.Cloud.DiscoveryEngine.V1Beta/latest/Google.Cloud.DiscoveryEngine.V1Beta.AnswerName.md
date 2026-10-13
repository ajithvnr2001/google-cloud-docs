---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName
title: Discovery Engine v1beta API - Class AnswerName (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:45.662190+00:00
---

# Discovery Engine v1beta API - Class AnswerName (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class AnswerName (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class AnswerName : IResourceName, IEquatable<AnswerName>

Reference documentation and code samples for the Discovery Engine v1beta API class AnswerName.

Resource name for the `Answer` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnswerName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### AnswerName(string, string, string, string, string)
    
    
    public AnswerName(string projectId, string locationId, string dataStoreId, string sessionId, string answerId)

Constructs a new instance of a [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) class from the component parts of pattern `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
  
## Properties 

### AnswerId
    
    
    public string AnswerId { get; }

The `Answer` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### EngineId
    
    
    public string EngineId { get; }

The `Engine` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### SessionId
    
    
    public string SessionId { get; }

The `Session` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public AnswerName.ResourceNameType Type { get; }

The [AnswerName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string dataStoreId, string sessionId, string answerId)

Formats the IDs into the string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`.  
  
### FormatProjectLocationCollectionDataStoreSessionAnswer(string, string, string, string, string, string)
    
    
    public static string FormatProjectLocationCollectionDataStoreSessionAnswer(string projectId, string locationId, string collectionId, string dataStoreId, string sessionId, string answerId)

Formats the IDs into the string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}` .

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
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}` .  
  
### FormatProjectLocationCollectionEngineSessionAnswer(string, string, string, string, string, string)
    
    
    public static string FormatProjectLocationCollectionEngineSessionAnswer(string projectId, string locationId, string collectionId, string engineId, string sessionId, string answerId)

Formats the IDs into the string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern ` projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Collection` ID. Must not be `null` or empty.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Engine` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern ` projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}` .  
  
### FormatProjectLocationDataStoreSessionAnswer(string, string, string, string, string)
    
    
    public static string FormatProjectLocationDataStoreSessionAnswer(string projectId, string locationId, string dataStoreId, string sessionId, string answerId)

Formats the IDs into the string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with pattern `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`.  
  
### FromProjectLocationCollectionDataStoreSessionAnswer(string, string, string, string, string, string)
    
    
    public static AnswerName FromProjectLocationCollectionDataStoreSessionAnswer(string projectId, string locationId, string collectionId, string dataStoreId, string sessionId, string answerId)

Creates a [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with the pattern ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}` .

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
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)` | A new instance of [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) constructed from the provided ids.  
  
### FromProjectLocationCollectionEngineSessionAnswer(string, string, string, string, string, string)
    
    
    public static AnswerName FromProjectLocationCollectionEngineSessionAnswer(string projectId, string locationId, string collectionId, string engineId, string sessionId, string answerId)

Creates a [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with the pattern ` projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`collectionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Collection` ID. Must not be `null` or empty.  
`engineId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Engine` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)` | A new instance of [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) constructed from the provided ids.  
  
### FromProjectLocationDataStoreSessionAnswer(string, string, string, string, string)
    
    
    public static AnswerName FromProjectLocationDataStoreSessionAnswer(string projectId, string locationId, string dataStoreId, string sessionId, string answerId)

Creates a [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) with the pattern `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`dataStoreId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `DataStore` ID. Must not be `null` or empty.  
`sessionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Session` ID. Must not be `null` or empty.  
`answerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Answer` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)` | A new instance of [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static AnswerName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)` | A new instance of [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static AnswerName Parse(string answerName)

Parses the given resource name string into a new [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) instance.

**Parameter**  
---  
**Name** | **Description**  
`answerName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)` | The parsed [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}`



### Parse(string, bool)
    
    
    public static AnswerName Parse(string answerName, bool allowUnparsed)

Parses the given resource name string into a new [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`answerName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName#Google_Cloud_DiscoveryEngine_V1Beta_AnswerName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)` | The parsed [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}`



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

### TryParse(string, out AnswerName)
    
    
    public static bool TryParse(string answerName, out AnswerName result)

Tries to parse the given resource name string into a new [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) instance.

**Parameters**  
---  
**Name** | **Description**  
`answerName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)`  
When this method returns, the parsed [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}`



### TryParse(string, bool, out AnswerName)
    
    
    public static bool TryParse(string answerName, bool allowUnparsed, out AnswerName result)

Tries to parse the given resource name string into a new [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`answerName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName#Google_Cloud_DiscoveryEngine_V1Beta_AnswerName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)`  
When this method returns, the parsed [AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}`
  * ` projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(AnswerName, AnswerName)
    
    
    public static bool operator ==(AnswerName a, AnswerName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)`  
The first resource name to compare, or null.  
`b` | `[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(AnswerName, AnswerName)
    
    
    public static bool operator !=(AnswerName a, AnswerName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)`  
The first resource name to compare, or null.  
`b` | `[AnswerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AnswerName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
