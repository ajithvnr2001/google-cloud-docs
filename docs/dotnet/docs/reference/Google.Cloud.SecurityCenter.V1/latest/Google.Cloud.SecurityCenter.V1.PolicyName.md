---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName
title: Google Cloud Security Command Center v1 API - Class PolicyName (3.28.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:29.113115+00:00
---

# Google Cloud Security Command Center v1 API - Class PolicyName (3.28.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1 API - Class PolicyName (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class PolicyName : IResourceName, IEquatable<PolicyName>

Reference documentation and code samples for the Google Cloud Security Command Center v1 API class PolicyName.

Resource name for the `Policy` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PolicyName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1)

## Assembly

Google.Cloud.SecurityCenter.V1.dll

## Constructors 

### PolicyName(string, string)
    
    
    public PolicyName(string organizationId, string constraintNameId)

Constructs a new instance of a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) class from the component parts of pattern `organizations/{organization}/policies/{constraint_name}`

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
  
## Properties 

### ConstraintNameId
    
    
    public string ConstraintNameId { get; }

The `ConstraintName` ID. May be `null`, depending on which resource name is contained by this instance.

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
  
### IsKnownPattern
    
    
    public bool IsKnownPattern { get; }

Whether this instance contains a resource name with a known pattern.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
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
    
    
    public PolicyName.ResourceNameType Type { get; }

The [PolicyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string organizationId, string constraintNameId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `organizations/{organization}/policies/{constraint_name}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `organizations/{organization}/policies/{constraint_name}`.  
  
### FormatFolderConstraintName(string, string)
    
    
    public static string FormatFolderConstraintName(string folderId, string constraintNameId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `folders/{folder}/policies/{constraint_name}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `folders/{folder}/policies/{constraint_name}`.  
  
### FormatOrganizationConstraintName(string, string)
    
    
    public static string FormatOrganizationConstraintName(string organizationId, string constraintNameId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `organizations/{organization}/policies/{constraint_name}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `organizations/{organization}/policies/{constraint_name}`.  
  
### FormatProjectConstraintName(string, string)
    
    
    public static string FormatProjectConstraintName(string projectId, string constraintNameId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `projects/{project}/policies/{constraint_name}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with pattern `projects/{project}/policies/{constraint_name}`.  
  
### FromFolderConstraintName(string, string)
    
    
    public static PolicyName FromFolderConstraintName(string folderId, string constraintNameId)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with the pattern `folders/{folder}/policies/{constraint_name}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) constructed from the provided ids.  
  
### FromOrganizationConstraintName(string, string)
    
    
    public static PolicyName FromOrganizationConstraintName(string organizationId, string constraintNameId)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with the pattern `organizations/{organization}/policies/{constraint_name}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) constructed from the provided ids.  
  
### FromProjectConstraintName(string, string)
    
    
    public static PolicyName FromProjectConstraintName(string projectId, string constraintNameId)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) with the pattern `projects/{project}/policies/{constraint_name}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`constraintNameId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `ConstraintName` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static PolicyName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static PolicyName Parse(string policyName)

Parses the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) instance.

**Parameter**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)` | The parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/policies/{constraint_name}`
  * `folders/{folder}/policies/{constraint_name}`
  * `projects/{project}/policies/{constraint_name}`



### Parse(string, bool)
    
    
    public static PolicyName Parse(string policyName, bool allowUnparsed)

Parses the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName#Google_Cloud_SecurityCenter_V1_PolicyName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)` | The parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/policies/{constraint_name}`
  * `folders/{folder}/policies/{constraint_name}`
  * `projects/{project}/policies/{constraint_name}`



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

### TryParse(string, out PolicyName)
    
    
    public static bool TryParse(string policyName, out PolicyName result)

Tries to parse the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) instance.

**Parameters**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)`  
When this method returns, the parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/policies/{constraint_name}`
  * `folders/{folder}/policies/{constraint_name}`
  * `projects/{project}/policies/{constraint_name}`



### TryParse(string, bool, out PolicyName)
    
    
    public static bool TryParse(string policyName, bool allowUnparsed, out PolicyName result)

Tries to parse the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName#Google_Cloud_SecurityCenter_V1_PolicyName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)`  
When this method returns, the parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following:

  * `organizations/{organization}/policies/{constraint_name}`
  * `folders/{folder}/policies/{constraint_name}`
  * `projects/{project}/policies/{constraint_name}`



Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(PolicyName, PolicyName)
    
    
    public static bool operator ==(PolicyName a, PolicyName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)`  
The first resource name to compare, or null.  
`b` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(PolicyName, PolicyName)
    
    
    public static bool operator !=(PolicyName a, PolicyName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)`  
The first resource name to compare, or null.  
`b` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.PolicyName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
