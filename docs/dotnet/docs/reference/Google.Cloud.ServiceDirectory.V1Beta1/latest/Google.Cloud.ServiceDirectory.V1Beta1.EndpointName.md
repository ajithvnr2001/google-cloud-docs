---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName
title: Service Directory v1beta1 API - Class EndpointName (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:00.909376+00:00
---

# Service Directory v1beta1 API - Class EndpointName (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Directory v1beta1 API - Class EndpointName (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/2.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/1.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)


    
    
    public sealed class EndpointName : IResourceName, IEquatable<EndpointName>

Reference documentation and code samples for the Service Directory v1beta1 API class EndpointName.

Resource name for the `Endpoint` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > EndpointName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.ServiceDirectory.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1)

## Assembly

Google.Cloud.ServiceDirectory.V1Beta1.dll

## Constructors 

### EndpointName(string, string, string, string, string)
    
    
    public EndpointName(string projectId, string locationId, string namespaceId, string serviceId, string endpointId)

Constructs a new instance of a [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) class from the component parts of pattern `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`namespaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Namespace` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Endpoint` ID. Must not be `null` or empty.  
  
## Properties 

### EndpointId
    
    
    public string EndpointId { get; }

The `Endpoint` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### NamespaceId
    
    
    public string NamespaceId { get; }

The `Namespace` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public EndpointName.ResourceNameType Type { get; }

The [EndpointName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string namespaceId, string serviceId, string endpointId)

Formats the IDs into the string representation of this [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) with pattern `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`namespaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Namespace` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Endpoint` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) with pattern `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}` .  
  
### FormatProjectLocationNamespaceServiceEndpoint(string, string, string, string, string)
    
    
    public static string FormatProjectLocationNamespaceServiceEndpoint(string projectId, string locationId, string namespaceId, string serviceId, string endpointId)

Formats the IDs into the string representation of this [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) with pattern `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`namespaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Namespace` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Endpoint` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) with pattern `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}` .  
  
### FromProjectLocationNamespaceServiceEndpoint(string, string, string, string, string)
    
    
    public static EndpointName FromProjectLocationNamespaceServiceEndpoint(string projectId, string locationId, string namespaceId, string serviceId, string endpointId)

Creates a [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) with the pattern `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`namespaceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Namespace` ID. Must not be `null` or empty.  
`serviceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Service` ID. Must not be `null` or empty.  
`endpointId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Endpoint` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)` | A new instance of [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static EndpointName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)` | A new instance of [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) containing the provided `unparsedResourceName` .  
  
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
    
    
    public static EndpointName Parse(string endpointName)

Parses the given resource name string into a new [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) instance.

**Parameter**  
---  
**Name** | **Description**  
`endpointName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)` | The parsed [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}`



### Parse(string, bool)
    
    
    public static EndpointName Parse(string endpointName, bool allowUnparsed)

Parses the given resource name string into a new [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`endpointName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName#Google_Cloud_ServiceDirectory_V1Beta1_EndpointName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)` | The parsed [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}`

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

### TryParse(string, out EndpointName)
    
    
    public static bool TryParse(string endpointName, out EndpointName result)

Tries to parse the given resource name string into a new [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) instance.

**Parameters**  
---  
**Name** | **Description**  
`endpointName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)`  
When this method returns, the parsed [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}`



### TryParse(string, bool, out EndpointName)
    
    
    public static bool TryParse(string endpointName, bool allowUnparsed, out EndpointName result)

Tries to parse the given resource name string into a new [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`endpointName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName#Google_Cloud_ServiceDirectory_V1Beta1_EndpointName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)`  
When this method returns, the parsed [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}/endpoints/{endpoint}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(EndpointName, EndpointName)
    
    
    public static bool operator ==(EndpointName a, EndpointName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)`  
The first resource name to compare, or null.  
`b` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(EndpointName, EndpointName)
    
    
    public static bool operator !=(EndpointName a, EndpointName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)`  
The first resource name to compare, or null.  
`b` | `[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
