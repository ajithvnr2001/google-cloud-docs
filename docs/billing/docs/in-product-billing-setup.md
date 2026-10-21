---
url: https://docs.cloud.google.com/billing/docs/in-product-billing-setup/
title: Learn about the in-product Cloud Billing setup \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:16.716646+00:00
---

# Learn about the in-product Cloud Billing setup  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/in-product-billing-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Learn about the in-product Cloud Billing setup Stay organized with collections  Save and categorize content based on your preferences. 

Supported Google products and services let you set up or link a Cloud Billing account directly within their application interface. This streamlined flow, referred to as _in-product Cloud Billing setup_ , lets you enable billing capabilities for your Google product or service without leaving your current workflow.

This document explains the account features and billing status associated with this setup type.

## How in-product Cloud Billing setup works

With the appropriate permissions, you can initiate a Cloud Billing setup directly from supported product interfaces.

Depending on the product you are using, this setup might result in a **Paid account** or a **Starter Tier**. For more information about Cloud Billing accounts and their billable status, see [Cloud Billing account types](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types).

### Setup for the Starter Tier

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Starter Tier** is an onboarding path to Google Cloud that [supported Google products](https://docs.cloud.google.com/docs/starter-tier#supported-products) provide. The Starter Tier provisions your resources in a Google-managed project and doesn't require a Cloud Billing account or credit card. For information on this deployment experience, see [Learn about the Google Cloud Starter Tier](https://docs.cloud.google.com/docs/starter-tier).

### Setup for Paid accounts

When you use the in-product billing setup in supported products, such as [Google AI Studio](https://ai.google.dev/aistudio), you enable billing on your project by either creating a new Cloud Billing account or linking your project to an existing Cloud Billing account. Enabling billing through the in-product billing setup lets you immediately unlock paid features, higher quotas, and enterprise capabilities without leaving your current workflow.

For those products, the [billable status](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) of the Cloud Billing account is **Paid account** and you are charged for your product usage. The following are key details of this configuration:

  * When you configure a paid Cloud Billing account, you become a Google Cloud customer. Your Google user account is no longer eligible for the [Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial) but you might be eligible for a complimentary welcome credit to explore other Google Cloud products.
  * With a paid billing account, you are billed for your product usage based on the [charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle) of your Cloud Billing account.
  * When compared to free tier or free trial offers, using a paid billing account lets you access more features and higher quotas for your workflow.
  * You don't need to manually upgrade your Cloud Billing account later. You are ready for production workloads immediately.
  * You have access to [the entire Google Cloud platform](https://cloud.google.com/products).
  * When exploring other Google Cloud products, you might be eligible for [Free Tier usage](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier) of select Google Cloud products, up to specified monthly limits.



Because your Cloud Billing account is immediately activated as a **Paid account** when you use the in-product billing setup, your product usage is charged to the payment method connected to your Cloud Billing account. These charges include your usage of other Google Cloud products that is no longer covered by the welcome credit and usage that exceeds the [Google Cloud Free Tier usage limits](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier-usage-limits). For more information on how these conditions apply, see About charges and free offers for paid billing accounts.

For information about products and services that support the in-product **Paid account** setup, see Supported products.

#### Charging cycles

Depending on the product and your account status, your Cloud Billing account is set up with one or more of the following charging cycles that determine when you pay for your resource usage:

  * **Postpay** : For most Google Cloud services, you use resources first and costs accrue to be paid later. You are charged automatically at the end of your [billing cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle) or when your accrued costs reach a specific threshold amount. This cycle applies to all services unless a product specifically requires a **Prepay** cycle.
  * **Prepay** : For specific services, such as the Gemini API in AI Studio, you purchase credits in advance to access paid tiers. These prepay credits are stored in a separate balance and are deducted as you use the service. You pay manually when you load credits into your account, or you can set up _auto-reload_ to add prepay credits automatically and keep your services running. Prepay credits are non-refundable and expire after one year of purchase. If this balance is exhausted, the specific service requiring prepayment stops working until you add more credits.



A single Cloud Billing account can support both charging cycles simultaneously. For example, you might have a **Prepay** balance for Gemini API costs and maintain a **Postpay** cycle for your other Google Cloud resources.

#### Adding **Prepay** to an existing **Postpay** account

If your existing Cloud Billing account is configured for a **Postpay** cycle, you can add **Prepay** capabilities directly through the in-product setup flow of supported products. This lets you purchase credits in advance for specific services without needing to create a separate Cloud Billing account.

During the in-product setup to add **Prepay** to an existing account, you are presented with a mandatory confirmation screen explaining that your selected Cloud Billing account will be modified.

The system must modify your account state _before_ you submit your prepayment. Therefore, canceling the process after confirming the modification but before completing the prepayment setup might result in temporary service disruptions for projects already linked to that Cloud Billing account. Ensure you are ready to complete the prepayment process before confirming the transition. If you encounter issues, see Services disrupted after canceling a **Prepay** setup.

If you are eligible and manually switch from a **Prepay** cycle to a **Postpay** cycle, any remaining prepay credit balance is automatically refunded to the original payment method used for the prepayment. However, if you close your Cloud Billing account for any other reason, any remaining prepay credits are forfeited and aren't refunded.

## About charges and free offers for paid billing accounts

The in-product Cloud Billing setup might affect the application of charges and free offers of your product if the Cloud Billing account is configured as a **Paid account**. This section describes how these offers apply to paid billing accounts that are set up through in-product flows.

### Welcome credit

Cloud Billing accounts set up using the in-product flow on specific services and products might be eligible for a $300 welcome credit to help you explore [the Google Cloud platform](https://cloud.google.com/products).

**Important:** Credit exclusions apply to specific products. For example, a product's usage might be excluded from welcome credit coverage if it already offers a comprehensive free plan. For more information on credit eligibility, see the product-specific billing documentation.

The welcome credit offers benefits comparable to the standard [Google Cloud Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features#free-trial) credit, including the amount, restrictions, and validity period. However, it is subject to additional guidelines:

  * The $300 welcome credit is added to your configured **Paid account**, which is active after setup.
  * For eligible accounts, the welcome credit supports the discovery and onboarding of additional Google Cloud services, with [restrictions](https://docs.cloud.google.com/free/docs/free-cloud-features#during-free-trial).
  * Unlike a [_Free trial account_](https://docs.cloud.google.com/free/docs/free-cloud-features#confirm-billing-account), you are billed for Google Cloud usage when you exceed [Free Tier usage limits](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier-usage-limits) or exhaust your welcome credit.
  * The welcome credit doesn't cover usage for products explicitly excluded from the program, such as [Gemini API in AI Studio](https://ai.google.dev/aistudio). Usage for these products is charged to your Cloud Billing account based on your [charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle), but your welcome credit remains available for [other eligible services](https://docs.cloud.google.com/free/docs/free-cloud-features#during-free-trial).



### Google Cloud Free Tier and free product usage

The [Google Cloud Free Tier](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier) gives you free use of select Google Cloud products, up to specified limits. On a **Paid account** configured or linked with and in-product setup, Google Cloud products with a Free Tier continue to offer [free usage up to their specified limits](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier-usage-limits).

Additionally, other Google products offer [product-specific free trials](https://docs.cloud.google.com/free/docs/free-cloud-features#product-free-trials) or [other free offers](https://docs.cloud.google.com/free/docs/free-cloud-features#adjacent-products) available outside of the Google Cloud platform. You are billed for usage of resources from products or services that don't have active free offers or aren't covered by the welcome credit.

Billing is based on your specific [account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle). Your usage is charged when it exceeds the product's free offer limits or when the available welcome credit is exhausted.

**Important:** Switching to a **Paid account** might end free usage for specific products outside Google Cloud. We recommend reviewing your Google product's billing documentation to confirm how charges apply when linking a Cloud Billing account.

## Supported products

The following table lists the Google products and services that support in-product Cloud Billing setup:

Product | Description | Cloud Billing account billable status | Charging cycles | The welcome credit and free offers  
---|---|---|---|---  
[Google AI Studio](https://ai.google.dev/gemini-api/docs/billing) |  Create a Cloud Billing account directly from the AI Studio interface to manage API keys, access higher rate limits for Gemini API models, and pay for usage beyond the free tier. |  **Paid account** |  **Prepay for usage** of the Gemini API **Postpay for usage** of other Google Cloud services |  The welcome credit excludes Gemini API usage  
**Note:** Additional requirements or restrictions might apply to your product or service. For more information, see the product documentation.

## Monitor your costs

The tools available to help you monitor your costs depend on your charging cycle.

### Prepay

For Gemini API in AI Studio, if you configure a **Paid account** that requires you to **prepay** for usage, you can monitor your usage and available credit in the [Google AI Studio interface](https://aistudio.google.com/usage) in **Dashboard** > **Usage and Limits**.

### Postpay

If you configure a **Paid account** and incur **postpay** usage charges, we recommend the following Cloud Billing tools to help you monitor your spending:

  * [Create budgets and set up budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets).
  * [Analyze billing data and cost trends with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports).
  * [View and manage cost anomalies](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies).



## Troubleshoot in-product billing setup

This section describes issues that you might encounter during the in-product billing setup and their resolutions.

### Services disrupted after canceling a **Prepay** setup

**Issue:** You initiated the in-product flow to add **Prepay** capabilities to an existing **Postpay** Cloud Billing account, but you closed the window or canceled the process before completing the prepayment setup. Other projects linked to that same Cloud Billing account lose access to services that require prepayment, such as the Gemini API in AI Studio.

**Cause:** During the transition flow, the infrastructure to enable prepayment capabilities is created on your account immediately after you accept the confirmation dialog. If you don't complete the subsequent prepayment steps, the configuration enters an _unchargeable_ state. Because this state applies at the billing account level, it restricts access for all [projects linked to that specific Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked) that rely on **Prepay** services.

**Resolution:** Because the account state was already modified, there is no automatic remedy if you abandon the payment flow. To restore service to your linked projects, do one of the following:

  * **Complete the setup:** Return to the integrating product, such as Google AI Studio, restart the billing setup flow, and complete the full process for prepayment. After the payment is processed, the **Prepay** configuration becomes active and services are restored.
  * **Contact Support:** If you don't want to proceed with the **Prepay** model and need to revert your account entirely back to **Postpay** , [contact Cloud Billing Support](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues) to manually reset your account state.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
