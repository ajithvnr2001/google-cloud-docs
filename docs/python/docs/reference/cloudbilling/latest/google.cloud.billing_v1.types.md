---
url: https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types
title: Package types (1.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:02.721709+00:00
---

# Package types (1.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.21.0 (latest)  1.20.0  1.19.0  1.18.0  1.17.0  1.16.3  1.15.0  1.14.1  1.13.6  1.12.1  1.11.5  1.10.1  1.9.1  1.8.0  1.7.3  1.6.1  1.5.1  1.4.1  1.3.4  1.2.1  1.1.1  1.0.0  0.1.0 

API documentation for `billing_v1.types` package.

## Classes 

### [AggregationInfo](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.AggregationInfo)

Represents the aggregation level and interval for pricing of a single SKU.

### [BillingAccount](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.BillingAccount)

A billing account in the `Google Cloud Console <https://console.cloud.google.com/>`__. You can assign a billing account to one or more projects.

### [Category](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.Category)

Represents the category hierarchy of a SKU.

### [CreateBillingAccountRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.CreateBillingAccountRequest)

Request message for `CreateBillingAccount`.

### [GeoTaxonomy](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.GeoTaxonomy)

Encapsulates the geographic taxonomy data for a sku.

### [GetBillingAccountRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.GetBillingAccountRequest)

Request message for `GetBillingAccount`.

### [GetProjectBillingInfoRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.GetProjectBillingInfoRequest)

Request message for `GetProjectBillingInfo`.

### [ListBillingAccountsRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListBillingAccountsRequest)

Request message for `ListBillingAccounts`.

### [ListBillingAccountsResponse](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListBillingAccountsResponse)

Response message for `ListBillingAccounts`.

### [ListProjectBillingInfoRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListProjectBillingInfoRequest)

Request message for `ListProjectBillingInfo`.

### [ListProjectBillingInfoResponse](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListProjectBillingInfoResponse)

Request message for `ListProjectBillingInfoResponse`.

### [ListServicesRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListServicesRequest)

Request message for `ListServices`.

### [ListServicesResponse](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListServicesResponse)

Response message for `ListServices`.

### [ListSkusRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListSkusRequest)

Request message for `ListSkus`.

### [ListSkusResponse](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListSkusResponse)

Response message for `ListSkus`.

### [MoveBillingAccountRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.MoveBillingAccountRequest)

Request message for `MoveBillingAccount` RPC.

### [PricingExpression](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.PricingExpression)

Expresses a mathematical pricing formula. For Example:-

`usage_unit: GBy` `tiered_rates:` `[start_usage_amount: 20, unit_price: $10]` `[start_usage_amount: 100, unit_price: $5]`

The above expresses a pricing formula where the first 20GB is free, the next 80GB is priced at $10 per GB followed by $5 per GB for additional usage.

### [PricingInfo](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.PricingInfo)

Represents the pricing information for a SKU at a single point of time.

### [ProjectBillingInfo](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ProjectBillingInfo)

Encapsulation of billing information for a Google Cloud Console project. A project has at most one associated billing account at a time (but a billing account can be assigned to multiple projects).

### [Service](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.Service)

Encapsulates a single service in Google Cloud Platform.

### [Sku](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.Sku)

Encapsulates a single SKU in Google Cloud

### [UpdateBillingAccountRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.UpdateBillingAccountRequest)

Request message for `UpdateBillingAccount`.

### [UpdateProjectBillingInfoRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.UpdateProjectBillingInfoRequest)

Request message for `UpdateProjectBillingInfo`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
