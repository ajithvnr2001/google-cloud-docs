---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName
title: Google Cloud Recommender v1 API - Class InsightTypeName (3.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:45.375009+00:00
---

# Google Cloud Recommender v1 API - Class InsightTypeName (3.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Recommender v1 API - Class InsightTypeName (3.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.9.0 (latest)  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.8.0  2.7.0  2.6.0  2.5.0 
    
    
    public sealed class InsightTypeName : IResourceName, IEquatable<InsightTypeName>

Reference documentation and code samples for the Google Cloud Recommender v1 API class InsightTypeName.

Resource name for the `InsightType` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InsightTypeName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Recommender.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1)

## Assembly

Google.Cloud.Recommender.V1.dll

## Constructors 

### InsightTypeName(string, string, string)
    
    
    public InsightTypeName(string projectId, string locationId, string insightTypeId)

Constructs a new instance of a [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) class from the component parts of pattern `projects/{project}/locations/{location}/insightTypes/{insight_type}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
  
## Properties 

### BillingAccountId
    
    
    public string BillingAccountId { get; }

The `BillingAccount` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FolderId
    
    
    public string FolderId { get; }

The `Folder` ID. May be `null`, depending on which resource name is contained by this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InsightTypeId
    
    
    public string InsightTypeId { get; }

The `InsightType` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### OrganizationId
    
    
    public string OrganizationId { get; }

The `Organization` ID. May be `null`, depending on which resource name is contained by this instance.

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
    
    
    public InsightTypeName.ResourceNameType Type { get; }

The [InsightTypeName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string)
    
    
    public static string Format(string projectId, string locationId, string insightTypeId)

Formats the IDs into the string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `projects/{project}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `projects/{project}/locations/{location}/insightTypes/{insight_type}`.  
  
### FormatBillingAccountLocationInsightType(string, string, string)
    
    
    public static string FormatBillingAccountLocationInsightType(string billingAccountId, string locationId, string insightTypeId)

Formats the IDs into the string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `billingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`billingAccountId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BillingAccount` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `billingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}`.  
  
### FormatFolderLocationInsightType(string, string, string)
    
    
    public static string FormatFolderLocationInsightType(string folderId, string locationId, string insightTypeId)

Formats the IDs into the string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `folders/{folder}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `folders/{folder}/locations/{location}/insightTypes/{insight_type}`.  
  
### FormatOrganizationLocationInsightType(string, string, string)
    
    
    public static string FormatOrganizationLocationInsightType(string organizationId, string locationId, string insightTypeId)

Formats the IDs into the string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `organizations/{organization}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `organizations/{organization}/locations/{location}/insightTypes/{insight_type}`.  
  
### FormatProjectLocationInsightType(string, string, string)
    
    
    public static string FormatProjectLocationInsightType(string projectId, string locationId, string insightTypeId)

Formats the IDs into the string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `projects/{project}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with pattern `projects/{project}/locations/{location}/insightTypes/{insight_type}`.  
  
### FromBillingAccountLocationInsightType(string, string, string)
    
    
    public static InsightTypeName FromBillingAccountLocationInsightType(string billingAccountId, string locationId, string insightTypeId)

Creates a [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with the pattern `billingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`billingAccountId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BillingAccount` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)` | A new instance of [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) constructed from the provided ids.  
  
### FromFolderLocationInsightType(string, string, string)
    
    
    public static InsightTypeName FromFolderLocationInsightType(string folderId, string locationId, string insightTypeId)

Creates a [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with the pattern `folders/{folder}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)` | A new instance of [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) constructed from the provided ids.  
  
### FromOrganizationLocationInsightType(string, string, string)
    
    
    public static InsightTypeName FromOrganizationLocationInsightType(string organizationId, string locationId, string insightTypeId)

Creates a [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with the pattern `organizations/{organization}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)` | A new instance of [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) constructed from the provided ids.  
  
### FromProjectLocationInsightType(string, string, string)
    
    
    public static InsightTypeName FromProjectLocationInsightType(string projectId, string locationId, string insightTypeId)

Creates a [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) with the pattern `projects/{project}/locations/{location}/insightTypes/{insight_type}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`insightTypeId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `InsightType` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)` | A new instance of [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static InsightTypeName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)` | A new instance of [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static InsightTypeName Parse(string insightTypeName)

Parses the given resource name string into a new [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) instance.

**Parameter**  
---  
**Name** | **Description**  
`insightTypeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)` | The parsed [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/insightTypes/{insight_type}`
  * `billingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}`
  * `folders/{folder}/locations/{location}/insightTypes/{insight_type}`
  * `organizations/{organization}/locations/{location}/insightTypes/{insight_type}`



### Parse(string, bool)
    
    
    public static InsightTypeName Parse(string insightTypeName, bool allowUnparsed)

Parses the given resource name string into a new [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`insightTypeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName#Google_Cloud_Recommender_V1_InsightTypeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)` | The parsed [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/insightTypes/{insight_type}`
  * `billingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}`
  * `folders/{folder}/locations/{location}/insightTypes/{insight_type}`
  * `organizations/{organization}/locations/{location}/insightTypes/{insight_type}`



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

### TryParse(string, out InsightTypeName)
    
    
    public static bool TryParse(string insightTypeName, out InsightTypeName result)

Tries to parse the given resource name string into a new [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) instance.

**Parameters**  
---  
**Name** | **Description**  
`insightTypeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)`  
When this method returns, the parsed [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/insightTypes/{insight_type}`
  * `billingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}`
  * `folders/{folder}/locations/{location}/insightTypes/{insight_type}`
  * `organizations/{organization}/locations/{location}/insightTypes/{insight_type}`



### TryParse(string, bool, out InsightTypeName)
    
    
    public static bool TryParse(string insightTypeName, bool allowUnparsed, out InsightTypeName result)

Tries to parse the given resource name string into a new [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`insightTypeName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName#Google_Cloud_Recommender_V1_InsightTypeName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)`  
When this method returns, the parsed [InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/locations/{location}/insightTypes/{insight_type}`
  * `billingAccounts/{billing_account}/locations/{location}/insightTypes/{insight_type}`
  * `folders/{folder}/locations/{location}/insightTypes/{insight_type}`
  * `organizations/{organization}/locations/{location}/insightTypes/{insight_type}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(InsightTypeName, InsightTypeName)
    
    
    public static bool operator ==(InsightTypeName a, InsightTypeName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)`  
The first resource name to compare, or null.  
`b` | `[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(InsightTypeName, InsightTypeName)
    
    
    public static bool operator !=(InsightTypeName a, InsightTypeName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)`  
The first resource name to compare, or null.  
`b` | `[InsightTypeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.InsightTypeName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
