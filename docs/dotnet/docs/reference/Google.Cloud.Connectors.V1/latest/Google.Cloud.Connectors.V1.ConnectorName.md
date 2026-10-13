---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName
title: Integration Connectors v1 API - Class ConnectorName (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:42.389152+00:00
---

# Integration Connectors v1 API - Class ConnectorName (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Integration Connectors v1 API - Class ConnectorName (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.3.0/Google.Cloud.Connectors.V1.ConnectorName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.2.0/Google.Cloud.Connectors.V1.ConnectorName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.1.0/Google.Cloud.Connectors.V1.ConnectorName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/1.0.0/Google.Cloud.Connectors.V1.ConnectorName)


    
    
    public sealed class ConnectorName : IResourceName, IEquatable<ConnectorName>

Reference documentation and code samples for the Integration Connectors v1 API class ConnectorName.

Resource name for the `Connector` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConnectorName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Connectors.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1)

## Assembly

Google.Cloud.Connectors.V1.dll

## Constructors 

### ConnectorName(string, string, string, string)
    
    
    public ConnectorName(string projectId, string locationId, string providerId, string connectorId)

Constructs a new instance of a [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) class from the component parts of pattern `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`providerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Provider` ID. Must not be `null` or empty.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Connector` ID. Must not be `null` or empty.  
  
## Properties 

### ConnectorId
    
    
    public string ConnectorId { get; }

The `Connector` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### ProviderId
    
    
    public string ProviderId { get; }

The `Provider` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public ConnectorName.ResourceNameType Type { get; }

The [ConnectorName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string providerId, string connectorId)

Formats the IDs into the string representation of this [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) with pattern `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`providerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Provider` ID. Must not be `null` or empty.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Connector` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) with pattern `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`.  
  
### FormatProjectLocationProviderConnector(string, string, string, string)
    
    
    public static string FormatProjectLocationProviderConnector(string projectId, string locationId, string providerId, string connectorId)

Formats the IDs into the string representation of this [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) with pattern `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`providerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Provider` ID. Must not be `null` or empty.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Connector` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) with pattern `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`.  
  
### FromProjectLocationProviderConnector(string, string, string, string)
    
    
    public static ConnectorName FromProjectLocationProviderConnector(string projectId, string locationId, string providerId, string connectorId)

Creates a [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) with the pattern `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`providerId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Provider` ID. Must not be `null` or empty.  
`connectorId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Connector` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)` | A new instance of [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static ConnectorName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)` | A new instance of [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static ConnectorName Parse(string connectorName)

Parses the given resource name string into a new [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) instance.

**Parameter**  
---  
**Name** | **Description**  
`connectorName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)` | The parsed [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`



### Parse(string, bool)
    
    
    public static ConnectorName Parse(string connectorName, bool allowUnparsed)

Parses the given resource name string into a new [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`connectorName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName#Google_Cloud_Connectors_V1_ConnectorName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)` | The parsed [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`

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

### TryParse(string, out ConnectorName)
    
    
    public static bool TryParse(string connectorName, out ConnectorName result)

Tries to parse the given resource name string into a new [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) instance.

**Parameters**  
---  
**Name** | **Description**  
`connectorName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)`  
When this method returns, the parsed [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`



### TryParse(string, bool, out ConnectorName)
    
    
    public static bool TryParse(string connectorName, bool allowUnparsed, out ConnectorName result)

Tries to parse the given resource name string into a new [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`connectorName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName#Google_Cloud_Connectors_V1_ConnectorName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)`  
When this method returns, the parsed [ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/providers/{provider}/connectors/{connector}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(ConnectorName, ConnectorName)
    
    
    public static bool operator ==(ConnectorName a, ConnectorName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)`  
The first resource name to compare, or null.  
`b` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(ConnectorName, ConnectorName)
    
    
    public static bool operator !=(ConnectorName a, ConnectorName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)`  
The first resource name to compare, or null.  
`b` | `[ConnectorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Connectors.V1/latest/Google.Cloud.Connectors.V1.ConnectorName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
