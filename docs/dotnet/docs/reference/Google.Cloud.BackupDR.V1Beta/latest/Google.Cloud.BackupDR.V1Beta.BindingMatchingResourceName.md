---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName
title: Backup and DR Service v1beta API - Class BindingMatchingResourceName (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:22.476811+00:00
---

# Backup and DR Service v1beta API - Class BindingMatchingResourceName (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1beta API - Class BindingMatchingResourceName (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class BindingMatchingResourceName : IResourceName, IEquatable<BindingMatchingResourceName>

Reference documentation and code samples for the Backup and DR Service v1beta API class BindingMatchingResourceName.

Resource name for the `BindingMatchingResource` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BindingMatchingResourceName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.BackupDR.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta)

## Assembly

Google.Cloud.BackupDR.V1Beta.dll

## Constructors 

### BindingMatchingResourceName(string, string, string, string, string)
    
    
    public BindingMatchingResourceName(string projectId, string locationId, string autoProtectionPolicyId, string bindingId, string matchingResourceId)

Constructs a new instance of a [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) class from the component parts of pattern ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autoProtectionPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutoProtectionPolicy` ID. Must not be `null` or empty.  
`bindingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Binding` ID. Must not be `null` or empty.  
`matchingResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MatchingResource` ID. Must not be `null` or empty.  
  
## Properties 

### AutoProtectionPolicyId
    
    
    public string AutoProtectionPolicyId { get; }

The `AutoProtectionPolicy` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BindingId
    
    
    public string BindingId { get; }

The `Binding` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### MatchingResourceId
    
    
    public string MatchingResourceId { get; }

The `MatchingResource` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
    
    
    public BindingMatchingResourceName.ResourceNameType Type { get; }

The [BindingMatchingResourceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string, string, string, string)
    
    
    public static string Format(string projectId, string locationId, string autoProtectionPolicyId, string bindingId, string matchingResourceId)

Formats the IDs into the string representation of this [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) with pattern ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autoProtectionPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutoProtectionPolicy` ID. Must not be `null` or empty.  
`bindingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Binding` ID. Must not be `null` or empty.  
`matchingResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MatchingResource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) with pattern ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}` .  
  
### FormatProjectLocationAutoProtectionPolicyBindingMatchingResource(string, string, string, string, string)
    
    
    public static string FormatProjectLocationAutoProtectionPolicyBindingMatchingResource(string projectId, string locationId, string autoProtectionPolicyId, string bindingId, string matchingResourceId)

Formats the IDs into the string representation of this [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) with pattern ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autoProtectionPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutoProtectionPolicy` ID. Must not be `null` or empty.  
`bindingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Binding` ID. Must not be `null` or empty.  
`matchingResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MatchingResource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) with pattern ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}` .  
  
### FromProjectLocationAutoProtectionPolicyBindingMatchingResource(string, string, string, string, string)
    
    
    public static BindingMatchingResourceName FromProjectLocationAutoProtectionPolicyBindingMatchingResource(string projectId, string locationId, string autoProtectionPolicyId, string bindingId, string matchingResourceId)

Creates a [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) with the pattern ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}` .

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`locationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Location` ID. Must not be `null` or empty.  
`autoProtectionPolicyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `AutoProtectionPolicy` ID. Must not be `null` or empty.  
`bindingId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Binding` ID. Must not be `null` or empty.  
`matchingResourceId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `MatchingResource` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)` | A new instance of [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static BindingMatchingResourceName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)` | A new instance of [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static BindingMatchingResourceName Parse(string bindingMatchingResourceName)

Parses the given resource name string into a new [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) instance.

**Parameter**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)` | The parsed [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}`



### Parse(string, bool)
    
    
    public static BindingMatchingResourceName Parse(string bindingMatchingResourceName, bool allowUnparsed)

Parses the given resource name string into a new [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName#Google_Cloud_BackupDR_V1Beta_BindingMatchingResourceName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)` | The parsed [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}`



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

### TryParse(string, out BindingMatchingResourceName)
    
    
    public static bool TryParse(string bindingMatchingResourceName, out BindingMatchingResourceName result)

Tries to parse the given resource name string into a new [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) instance.

**Parameters**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)`  
When this method returns, the parsed [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}`



### TryParse(string, bool, out BindingMatchingResourceName)
    
    
    public static bool TryParse(string bindingMatchingResourceName, bool allowUnparsed, out BindingMatchingResourceName result)

Tries to parse the given resource name string into a new [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`bindingMatchingResourceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName#Google_Cloud_BackupDR_V1Beta_BindingMatchingResourceName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)`  
When this method returns, the parsed [BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * ` projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy}/bindings/{binding}/matchingResources/{matching_resource}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(BindingMatchingResourceName, BindingMatchingResourceName)
    
    
    public static bool operator ==(BindingMatchingResourceName a, BindingMatchingResourceName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)`  
The first resource name to compare, or null.  
`b` | `[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(BindingMatchingResourceName, BindingMatchingResourceName)
    
    
    public static bool operator !=(BindingMatchingResourceName a, BindingMatchingResourceName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)`  
The first resource name to compare, or null.  
`b` | `[BindingMatchingResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.BindingMatchingResourceName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
