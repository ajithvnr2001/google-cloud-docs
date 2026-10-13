---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName
title: Cloud Build v1 API - Class SubscriptionName (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:14.892620+00:00
---

# Cloud Build v1 API - Class SubscriptionName (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v1 API - Class SubscriptionName (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SubscriptionName : IResourceName, IEquatable<SubscriptionName>

Reference documentation and code samples for the Cloud Build v1 API class SubscriptionName.

Resource name for the `Subscription` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SubscriptionName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.CloudBuild.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1)

## Assembly

Google.Cloud.CloudBuild.V1.dll

## Constructors 

### SubscriptionName(string, string)
    
    
    public SubscriptionName(string projectId, string subscriptionId)

Constructs a new instance of a [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) class from the component parts of pattern `projects/{project}/subscriptions/{subscription}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`subscriptionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Subscription` ID. Must not be `null` or empty.  
  
## Properties 

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
  
### SubscriptionId
    
    
    public string SubscriptionId { get; }

The `Subscription` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public SubscriptionName.ResourceNameType Type { get; }

The [SubscriptionName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string projectId, string subscriptionId)

Formats the IDs into the string representation of this [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) with pattern `projects/{project}/subscriptions/{subscription}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`subscriptionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Subscription` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) with pattern `projects/{project}/subscriptions/{subscription}`.  
  
### FormatProjectSubscription(string, string)
    
    
    public static string FormatProjectSubscription(string projectId, string subscriptionId)

Formats the IDs into the string representation of this [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) with pattern `projects/{project}/subscriptions/{subscription}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`subscriptionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Subscription` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) with pattern `projects/{project}/subscriptions/{subscription}`.  
  
### FromProjectSubscription(string, string)
    
    
    public static SubscriptionName FromProjectSubscription(string projectId, string subscriptionId)

Creates a [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) with the pattern `projects/{project}/subscriptions/{subscription}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`subscriptionId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Subscription` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)` | A new instance of [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static SubscriptionName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)` | A new instance of [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static SubscriptionName Parse(string subscriptionName)

Parses the given resource name string into a new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) instance.

**Parameter**  
---  
**Name** | **Description**  
`subscriptionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)` | The parsed [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/subscriptions/{subscription}`



### Parse(string, bool)
    
    
    public static SubscriptionName Parse(string subscriptionName, bool allowUnparsed)

Parses the given resource name string into a new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`subscriptionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName#Google_Cloud_CloudBuild_V1_SubscriptionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)` | The parsed [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/subscriptions/{subscription}`



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

### TryParse(string, out SubscriptionName)
    
    
    public static bool TryParse(string subscriptionName, out SubscriptionName result)

Tries to parse the given resource name string into a new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) instance.

**Parameters**  
---  
**Name** | **Description**  
`subscriptionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)`  
When this method returns, the parsed [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/subscriptions/{subscription}`



### TryParse(string, bool, out SubscriptionName)
    
    
    public static bool TryParse(string subscriptionName, bool allowUnparsed, out SubscriptionName result)

Tries to parse the given resource name string into a new [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`subscriptionName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName#Google_Cloud_CloudBuild_V1_SubscriptionName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)`  
When this method returns, the parsed [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `projects/{project}/subscriptions/{subscription}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(SubscriptionName, SubscriptionName)
    
    
    public static bool operator ==(SubscriptionName a, SubscriptionName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)`  
The first resource name to compare, or null.  
`b` | `[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(SubscriptionName, SubscriptionName)
    
    
    public static bool operator !=(SubscriptionName a, SubscriptionName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)`  
The first resource name to compare, or null.  
`b` | `[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V1/latest/Google.Cloud.CloudBuild.V1.SubscriptionName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
