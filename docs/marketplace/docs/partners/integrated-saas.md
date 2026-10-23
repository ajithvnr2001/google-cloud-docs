---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/
title: Offering software as a service (SaaS) products \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:23.760697+00:00
---

# Offering software as a service (SaaS) products  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Offering software as a service (SaaS) products Stay organized with collections  Save and categorize content based on your preferences. 

Software as a service (SaaS) products on Cloud Marketplace are software products that run on Google Cloud, and are billed by Google. These require partner-managed infrastructure. This section describes the high-level steps that you must take to integrate your SaaS product with Cloud Marketplace.

## Before you begin

  * If you're new to offering software on Cloud Marketplace, [sign up to become a vendor](https://docs.cloud.google.com/marketplace/docs/partners/offer-products#initiate-onboarding). 
  * For your first (and all subsequent) listings you must complete the [Cloud Marketplace Onboarding Validation Form](https://docs.google.com/forms/d/e/1FAIpQLSesllyRR-HvLFZthYA8Cv4nQRUTOthHGgs-76DY9o2IntUL3A/viewform). 
  * To get access to Producer Portal, complete the _Cloud Marketplace Project Info Form_ , provided by the Cloud Marketplace team. 



## Product-specific requirements

If you want to publish a SaaS product, it must meet the following requirements:

  1. It must comply with the Cloud Marketplace [listing requirements](https://docs.cloud.google.com/marketplace/docs/partners/get-started#requirements_for_your_organization).

  2. It must not include professional services, hardware, or other non-software components that are billed through Cloud Marketplace.




## Checklist

  1. [Set up your SaaS product](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/set-up-environment), so that you can distribute your product and display it on Cloud Marketplace.

  2. [Review the available pricing options, and select a pricing model](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing). Pricing models take up to four business days to review. You can continue integrating your product while the pricing model is reviewed.

  3. [Integrate your product with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup). The integration includes modifying the frontend and backend of your software to create accounts for users, link the accounts to their Google accounts, and provide a way for users to sign in to your app using their Google credentials. For products whose architecture involves a data plane in the customer's Google Cloud project that connects to a control plane in your Google Cloud project, this involves [adding a consumption tracking label](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/partner-consumption-tracking) to track your product's associated consumption of Google Cloud resources.

  4. [Publish your product to Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/submitting). To publish your product, you submit various parts of your product for review. The Cloud Marketplace team reviews each submission and works with you to resolve any issues before approving it. When all of your submissions are approved, you can publish and launch the product within a few minutes.




## Integrating with App Lifecycle Manager

If you use App Lifecycle Manager to deploy and operate your SaaS product, you can also take advantage of streamlined validation and tenant onboarding. For more information, see [Integrate with App Lifecycle Manager](https://docs.cloud.google.com/marketplace/docs/partners/integrate-app-lifecycle-manager).

[ Next Set up your software as a service (SaaS) product for Google Cloud  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/set-up-environment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
