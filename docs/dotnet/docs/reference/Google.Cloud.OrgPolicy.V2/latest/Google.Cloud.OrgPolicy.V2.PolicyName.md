---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName
title: Organization Policy v2 API - Class PolicyName (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:57.868682+00:00
---

# Organization Policy v2 API - Class PolicyName (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Organization Policy v2 API - Class PolicyName (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.8.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.7.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.6.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.5.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.4.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.3.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.2.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.1.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/2.0.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/1.2.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/1.1.0/Google.Cloud.OrgPolicy.V2.PolicyName)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/1.0.0/Google.Cloud.OrgPolicy.V2.PolicyName)


    
    
    public sealed class PolicyName : IResourceName, IEquatable<PolicyName>

Reference documentation and code samples for the Organization Policy v2 API class PolicyName.

Resource name for the `Policy` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PolicyName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.OrgPolicy.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2)

## Assembly

Google.Cloud.OrgPolicy.V2.dll

## Constructors 

### PolicyName(string, string)
    
    
    public PolicyName(string projectId, string policyId)

Constructs a new instance of a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) class from the component parts of pattern `projects/{project}/policies/{policy}`

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
  
## Properties 

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
  
### PolicyId
    
    
    public string PolicyId { get; }

The `Policy` ID. May be `null`, depending on which resource name is contained by this instance.

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

The [PolicyName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string projectId, string policyId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `projects/{project}/policies/{policy}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `projects/{project}/policies/{policy}`.  
  
### FormatFolderPolicy(string, string)
    
    
    public static string FormatFolderPolicy(string folderId, string policyId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `folders/{folder}/policies/{policy}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `folders/{folder}/policies/{policy}`.  
  
### FormatOrganizationPolicy(string, string)
    
    
    public static string FormatOrganizationPolicy(string organizationId, string policyId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `organizations/{organization}/policies/{policy}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `organizations/{organization}/policies/{policy}`.  
  
### FormatProjectPolicy(string, string)
    
    
    public static string FormatProjectPolicy(string projectId, string policyId)

Formats the IDs into the string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `projects/{project}/policies/{policy}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with pattern `projects/{project}/policies/{policy}`.  
  
### FromFolderPolicy(string, string)
    
    
    public static PolicyName FromFolderPolicy(string folderId, string policyId)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with the pattern `folders/{folder}/policies/{policy}`.

**Parameters**  
---  
**Name** | **Description**  
`folderId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Folder` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) constructed from the provided ids.  
  
### FromOrganizationPolicy(string, string)
    
    
    public static PolicyName FromOrganizationPolicy(string organizationId, string policyId)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with the pattern `organizations/{organization}/policies/{policy}`.

**Parameters**  
---  
**Name** | **Description**  
`organizationId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Organization` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) constructed from the provided ids.  
  
### FromProjectPolicy(string, string)
    
    
    public static PolicyName FromProjectPolicy(string projectId, string policyId)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) with the pattern `projects/{project}/policies/{policy}`.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Project` ID. Must not be `null` or empty.  
`policyId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Policy` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static PolicyName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)` | A new instance of [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) containing the provided `unparsedResourceName`.  
  
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

Parses the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) instance.

**Parameter**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)` | The parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/policies/{policy}`
  * `folders/{folder}/policies/{policy}`
  * `organizations/{organization}/policies/{policy}`



### Parse(string, bool)
    
    
    public static PolicyName Parse(string policyName, bool allowUnparsed)

Parses the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName#Google_Cloud_OrgPolicy_V2_PolicyName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)` | The parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/policies/{policy}`
  * `folders/{folder}/policies/{policy}`
  * `organizations/{organization}/policies/{policy}`

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

Tries to parse the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) instance.

**Parameters**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)`  
When this method returns, the parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/policies/{policy}`
  * `folders/{folder}/policies/{policy}`
  * `organizations/{organization}/policies/{policy}`



### TryParse(string, bool, out PolicyName)
    
    
    public static bool TryParse(string policyName, bool allowUnparsed, out PolicyName result)

Tries to parse the given resource name string into a new [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`policyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName#Google_Cloud_OrgPolicy_V2_PolicyName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)`  
When this method returns, the parsed [PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `projects/{project}/policies/{policy}`
  * `folders/{folder}/policies/{policy}`
  * `organizations/{organization}/policies/{policy}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(PolicyName, PolicyName)
    
    
    public static bool operator ==(PolicyName a, PolicyName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)`  
The first resource name to compare, or null.  
`b` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)`  
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
`a` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)`  
The first resource name to compare, or null.  
`b` | `[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OrgPolicy.V2/latest/Google.Cloud.OrgPolicy.V2.PolicyName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
