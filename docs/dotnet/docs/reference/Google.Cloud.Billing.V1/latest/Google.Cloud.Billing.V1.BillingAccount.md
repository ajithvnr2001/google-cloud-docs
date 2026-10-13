---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount
title: Google Cloud Billing v1 API - Class BillingAccount (3.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:21.776803+00:00
---

# Google Cloud Billing v1 API - Class BillingAccount (3.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Billing v1 API - Class BillingAccount (3.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.9.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.8.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.7.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.6.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.5.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.4.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.3.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.2.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.1.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/3.0.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/2.3.0/Google.Cloud.Billing.V1.BillingAccount)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/2.2.0/Google.Cloud.Billing.V1.BillingAccount)


    
    
    public sealed class BillingAccount : IMessage<BillingAccount>, IEquatable<BillingAccount>, IDeepCloneable<BillingAccount>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Billing v1 API class BillingAccount.

A billing account in the [Google Cloud Console](https://console.cloud.google.com/). You can assign a billing account to one or more projects.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BillingAccount

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BillingAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BillingAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BillingAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Billing.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1)

## Assembly

Google.Cloud.Billing.V1.dll

## Constructors 

### BillingAccount()
    
    
    public BillingAccount()

### BillingAccount(BillingAccount)
    
    
    public BillingAccount(BillingAccount other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BillingAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount)`  
  
  
## Properties 

### BillingAccountName
    
    
    public BillingAccountName BillingAccountName { get; set; }

[BillingAccountName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.BillingAccountName.html)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Billing.V1/latest/Google.Cloud.Billing.V1.BillingAccount#Google_Cloud_Billing_V1_BillingAccount_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BillingAccountName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.BillingAccountName.html)` |   
  
### CurrencyCode
    
    
    public string CurrencyCode { get; set; }

Optional. The currency in which the billing account is billed and charged, represented as an ISO 4217 code such as `USD`.

Billing account currency is determined at the time of billing account creation and cannot be updated subsequently, so this field should not be set on update requests. In addition, a subaccount always matches the currency of its parent billing account, so this field should not be set on subaccount creation requests. Clients can read this field to determine the currency of an existing billing account.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

The display name given to the billing account, such as `My Billing Account`. This name is displayed in the Google Cloud Console.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MasterBillingAccount
    
    
    public string MasterBillingAccount { get; set; }

If this account is a [subaccount](https://cloud.google.com/billing/docs/concepts), then this will be the resource name of the parent billing account that it is being resold through. Otherwise this will be empty.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name of the billing account. The resource name has the form `billingAccounts/{billing_account_id}`. For example, `billingAccounts/012345-567890-ABCDEF` would be the resource name for billing account `012345-567890-ABCDEF`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Open
    
    
    public bool Open { get; set; }

Output only. True if the billing account is open, and will therefore be charged for any usage on associated projects. False if the billing account is closed, and therefore projects associated with it are unable to use paid services.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Output only. The billing account's parent resource identifier. Use the `MoveBillingAccount` method to update the account's parent resource if it is a organization. Format:

  * `organizations/{organization_id}`, for example, `organizations/12345678`
  * `billingAccounts/{billing_account_id}`, for example, `billingAccounts/012345-567890-ABCDEF`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
