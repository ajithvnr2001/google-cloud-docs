---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName
title: Cloud Billing Budget v1beta1 API - Class BudgetName (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:11.975906+00:00
---

# Cloud Billing Budget v1beta1 API - Class BudgetName (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Billing Budget v1beta1 API - Class BudgetName (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/2.0.0-beta06/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/1.0.0-beta05/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)


    
    
    public sealed class BudgetName : IResourceName, IEquatable<BudgetName>

Reference documentation and code samples for the Cloud Billing Budget v1beta1 API class BudgetName.

Resource name for the `Budget` resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BudgetName

## Implements

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)

## Inherited Members

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

## Namespace

[Google.Cloud.Billing.Budgets.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1)

## Assembly

Google.Cloud.Billing.Budgets.V1Beta1.dll

## Constructors 

### BudgetName(string, string)
    
    
    public BudgetName(string billingAccountId, string budgetId)

Constructs a new instance of a [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) class from the component parts of pattern `billingAccounts/{billing_account}/budgets/{budget}`

**Parameters**  
---  
**Name** | **Description**  
`billingAccountId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BillingAccount` ID. Must not be `null` or empty.  
`budgetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Budget` ID. Must not be `null` or empty.  
  
## Properties 

### BillingAccountId
    
    
    public string BillingAccountId { get; }

The `BillingAccount` ID. Will not be `null`, unless this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BudgetId
    
    
    public string BudgetId { get; }

The `Budget` ID. Will not be `null`, unless this instance contains an unparsed resource name.

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
  
### Type
    
    
    public BudgetName.ResourceNameType Type { get; }

The [BudgetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName.ResourceNameType) of the contained resource name.

**Property Value**  
---  
**Type** | **Description**  
`[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)[ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName.ResourceNameType)` |   
  
### UnparsedResource
    
    
    public UnparsedResourceName UnparsedResource { get; }

The contained [UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html). Only non-`null` if this instance contains an unparsed resource name.

**Property Value**  
---  
**Type** | **Description**  
`[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)` |   
  
## Methods 

### Format(string, string)
    
    
    public static string Format(string billingAccountId, string budgetId)

Formats the IDs into the string representation of this [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) with pattern `billingAccounts/{billing_account}/budgets/{budget}`.

**Parameters**  
---  
**Name** | **Description**  
`billingAccountId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BillingAccount` ID. Must not be `null` or empty.  
`budgetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Budget` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) with pattern `billingAccounts/{billing_account}/budgets/{budget}`.  
  
### FormatBillingAccountBudget(string, string)
    
    
    public static string FormatBillingAccountBudget(string billingAccountId, string budgetId)

Formats the IDs into the string representation of this [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) with pattern `billingAccounts/{billing_account}/budgets/{budget}`.

**Parameters**  
---  
**Name** | **Description**  
`billingAccountId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BillingAccount` ID. Must not be `null` or empty.  
`budgetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Budget` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` | The string representation of this [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) with pattern `billingAccounts/{billing_account}/budgets/{budget}`.  
  
### FromBillingAccountBudget(string, string)
    
    
    public static BudgetName FromBillingAccountBudget(string billingAccountId, string budgetId)

Creates a [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) with the pattern `billingAccounts/{billing_account}/budgets/{budget}` .

**Parameters**  
---  
**Name** | **Description**  
`billingAccountId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `BillingAccount` ID. Must not be `null` or empty.  
`budgetId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The `Budget` ID. Must not be `null` or empty.  
**Returns**  
---  
**Type** | **Description**  
`[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)` | A new instance of [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) constructed from the provided ids.  
  
### FromUnparsed(UnparsedResourceName)
    
    
    public static BudgetName FromUnparsed(UnparsedResourceName unparsedResourceName)

Creates a [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) containing an unparsed resource name.

**Parameter**  
---  
**Name** | **Description**  
`unparsedResourceName` | `[UnparsedResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.UnparsedResourceName.html)`  
The unparsed resource name. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)` | A new instance of [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) containing the provided `unparsedResourceName`.  
  
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
    
    
    public static BudgetName Parse(string budgetName)

Parses the given resource name string into a new [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) instance.

**Parameter**  
---  
**Name** | **Description**  
`budgetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)` | The parsed [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `billingAccounts/{billing_account}/budgets/{budget}`



### Parse(string, bool)
    
    
    public static BudgetName Parse(string budgetName, bool allowUnparsed)

Parses the given resource name string into a new [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`budgetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName#Google_Cloud_Billing_Budgets_V1Beta1_BudgetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
**Returns**  
---  
**Type** | **Description**  
`[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)` | The parsed [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) if successful.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `billingAccounts/{billing_account}/budgets/{budget}`

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

### TryParse(string, out BudgetName)
    
    
    public static bool TryParse(string budgetName, out BudgetName result)

Tries to parse the given resource name string into a new [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) instance.

**Parameters**  
---  
**Name** | **Description**  
`budgetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`result` | `[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)`  
When this method returns, the parsed [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `billingAccounts/{billing_account}/budgets/{budget}`



### TryParse(string, bool, out BudgetName)
    
    
    public static bool TryParse(string budgetName, bool allowUnparsed, out BudgetName result)

Tries to parse the given resource name string into a new [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName) instance; optionally allowing an unparseable resource name.

**Parameters**  
---  
**Name** | **Description**  
`budgetName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The resource name in string form. Must not be `null`.  
`allowUnparsed` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
If `true` will successfully store an unparseable resource name into the [UnparsedResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName#Google_Cloud_Billing_Budgets_V1Beta1_BudgetName_UnparsedResource) property; otherwise will throw an [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception) if an unparseable resource name is specified.  
`result` | `[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)`  
When this method returns, the parsed [BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName), or `null` if parsing failed.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | `true` if the name was parsed successfully; `false` otherwise.  
**Remarks**

To parse successfully, the resource name must be formatted as one of the following: 

  * `billingAccounts/{billing_account}/budgets/{budget}`

Or may be in any format if `allowUnparsed` is `true`.

## Operators 

### operator ==(BudgetName, BudgetName)
    
    
    public static bool operator ==(BudgetName a, BudgetName b)

Determines whether two specified resource names have the same value.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)`  
The first resource name to compare, or null.  
`b` | `[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is the same as the value of `b`; otherwise, false.  
  
### operator !=(BudgetName, BudgetName)
    
    
    public static bool operator !=(BudgetName a, BudgetName b)

Determines whether two specified resource names have different values.

**Parameters**  
---  
**Name** | **Description**  
`a` | `[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)`  
The first resource name to compare, or null.  
`b` | `[BudgetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.Budgets.V1Beta1/latest/Google.Cloud.Billing.Budgets.V1Beta1.BudgetName)`  
The second resource name to compare, or null.  
**Returns**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` | true if the value of `a` is different from the value of `b`; otherwise, false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
