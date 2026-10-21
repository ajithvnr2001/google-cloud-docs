---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/billing/v1/billing-v1/
title: KRM API billing.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:22.207920+00:00
---

# KRM API billing.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/billing/v1/billing-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API billing.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## billing.gdc.goog/v1

Contains API Schema definitions for Billing Account related APIs.

Package v1 contains API Schema definitions for the billing.gdc.goog v1 API group

### BillingAccount

Represents a Billing Account. The identifier of the `BillingAccount` will be the "namespaced name", . It will appear on the Invoices for this Billing Account, and be on the selectors for querying billing data in Dashboards.   
Limited access: This field might not be available as it may not be accredited for use in your deployment. You can access it when it's approved.

_Appears in:_ \- BillingAccountList

Field | Description  
---|---  
`apiVersion` _string_ | `billing.gdc.goog/v1`  
`kind` _string_ | `BillingAccount`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BillingAccountSpec_ |   
`status` _BillingAccountStatus_ |   
  
### BillingAccountBinding

Represents the link between a Billing Account and a Project or the Organization. Limited access: This field might not be available as it may not be accredited for use in your deployment. You can access it when it's approved.

_Appears in:_ \- BillingAccountBindingList

Field | Description  
---|---  
`apiVersion` _string_ | `billing.gdc.goog/v1`  
`kind` _string_ | `BillingAccountBinding`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BillingAccountBindingSpec_ |   
`status` _BillingAccountBindingStatus_ |   
  
### BillingAccountBindingList

Contains a list of BillingAccountBinding

Field | Description  
---|---  
`apiVersion` _string_ | `billing.gdc.goog/v1`  
`kind` _string_ | `BillingAccountBindingList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BillingAccountBinding array_ |   
  
### BillingAccountBindingSpec

Defines the spec of a BillingAccountBinding.

_Appears in:_ \- BillingAccountBinding

Field | Description  
---|---  
`billingAccountRef` _NamespacedName_ | The Billing Account to use. Required.  
  
### BillingAccountBindingStatus

Shows the status of the BillingAccountBinding.

_Appears in:_ \- BillingAccountBinding

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions contains the latest time and state when Billing Platform processed the binding. If the `Effective` condition is `true`, the binding in the `ObservedGeneration` of the object is effective, otherwise, the previous binding, or no binding is effective.  
`bindingHistory` _BindingHistoryRecord array_ | BindingHistory keeps an append-only ledger of all past active billing account bindings.  
  
### BillingAccountList

Contains a list of BillingAccounts

Field | Description  
---|---  
`apiVersion` _string_ | `billing.gdc.goog/v1`  
`kind` _string_ | `BillingAccountList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BillingAccount array_ |   
  
### BillingAccountSpec

Defines the metadata of a Billing Account.

_Appears in:_ \- BillingAccount

Field | Description  
---|---  
`displayName` _string_ | A human readable name or description of this Billing Account. This name will be a selector for querying billing data in dashboards.  
`paymentSystemConfig` _PaymentSystemConfig_ | The link to an external payment account.  
  
### BillingAccountStatus

Provides the status of a BillingAccount.

_Appears in:_ \- BillingAccount

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions contains the latest time and state when Billing Platform processes the BillingAccount.  
  
### BindingHistoryRecord

BindingHistoryRecord represents a historic binding point of a billing account to a project or organization.

_Appears in:_ \- BillingAccountBindingStatus

Field | Description  
---|---  
`billingAccountRef` _NamespacedName_ |   
`effectiveTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ |   
  
### Money

Money represents an amount of money with its currency type.

_Appears in:_ \- Price \- PriceTier

Field | Description  
---|---  
`currencyCode` _string_ |   
`units` _integer_ | Units is the whole units of the amount. For example if `CurrencyCode` is `"USD"`, then 1 unit is one US dollar.  
`nanos` _integer_ | Nanos is the number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `Units` is positive, `nanos` must be positive or zero. If `Units` is zero, `nanos` can be positive, zero, or negative. If `Units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `Units`=-1 and `Nanos`=-750,000,000.  
  
### PaymentSystemCloudBillingConfig

Stores the config for a Cloud Billing account.

_Appears in:_ \- PaymentSystemConfig

Field | Description  
---|---  
`accountID` _string_ | The Cloud Billing account ID.  
  
### PaymentSystemConfig

Stores the link to an external payment account. Fields are one-of.

_Appears in:_ \- BillingAccountSpec

Field | Description  
---|---  
`customConfig` _object (keys:string, values:string)_ | A link to a customized account defined by Infrastructure Operators (IO). To configure the customized account using `CustomConfig`: 

  * It should include a key `payment-config-type`, with value defined by IO.
  * It should list the names of identifiers of the account in keys, and values in values.

Example:   
"payment-config-type": "Example"   
"account-id": "test-account-id-1"  
`cloudBillingConfig` _PaymentSystemCloudBillingConfig_ | A link to a Cloud Billing account.  
  
### Price

Price represents the pricing details for a SKU at a specific point in time.

_Appears in:_ \- SKUDescription

Field | Description  
---|---  
`usageUnit` _string_ | The unit of usage in which price is defined. Eg: "10 TiB month".  
`effectiveTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | EffectiveTime represents the timestamp after which the Price becomes effective.  
`pricingStructure` _PricingStructure_ | PricingStructure defines the model to use. Defaults to "SINGLE_RATE" if not set. Can be "SINGLE_RATE" or "TIERED".  
`unitPrice` _Money_ | UnitPrice is the single, flat-rate price. Used when PricingStructure is "SINGLE_RATE".  
`tiers` _PriceTier array_ | Tiers is the list of pricing tiers. Used when PricingStructure is "TIERED".  
  
### PriceTier

PriceTier defines a single tier in a tiered pricing model.

_Appears in:_ \- Price

Field | Description  
---|---  
`fromUsage` _string_ | FromUsage is the start of the usage range (inclusive). For the first tier, this must be 0.  
`displayFromUsage` _string_ | DisplayFromUsage is an optional, human-readable string for UI display, e.g., "50 TB".  
`unitPrice` _Money_ | UnitPrice is the price per unit for this tier.  
  
### PricingStructure

_Underlying type:_ `string` PricingStructure defines the type of rate structure for a price entry.

_Appears in:_ \- Price

### SKUCategory

_Underlying type:_ `string` SKUCategory is the classification of a SKU into a category.

_Appears in:_ \- SKUDescription

### SKUDescription

SKUDescription is the Schema for the skudescriptions API.

_Appears in:_ \- SKUDescriptionList

Field | Description  
---|---  
`apiVersion` _string_ | `billing.gdc.goog/v1`  
`kind` _string_ | `SKUDescription`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`status` _SKUDescriptionStatus_ |   
`skuID` _string_ | SKUID is the unique ID for the SKU. Example: "AA95-CD31-42FE"  
`invoiceDescription` _string_ | InvoiceDescription is a human readable description of what the SKU is.  
`description` _string_ | Description is a a long human readable description of what the SKU is.  
`category` _SKUCategory_ | Category is the classification of a SKU into a similar grouping of SKUs.  
`deprecationTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | DeprecationTime represents the timestamp after which the SKU becomes deprecated.  
`pricingInfo` _Price array_ | PricingInfo contains a list of Price object, which represents the pricing history.  
  
### SKUDescriptionList

SKUDescriptionList contains a list of SKUDescription.

Field | Description  
---|---  
`apiVersion` _string_ | `billing.gdc.goog/v1`  
`kind` _string_ | `SKUDescriptionList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _SKUDescription array_ |   
  
### SKUDescriptionStatus

_Appears in:_ \- SKUDescription

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions contains the latest time and state when Billing Platform processes the SKUDescription.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
