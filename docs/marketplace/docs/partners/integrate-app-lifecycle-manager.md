---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrate-app-lifecycle-manager/
title: Integrate with App Lifecycle Manager \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:00.899466+00:00
---

# Integrate with App Lifecycle Manager  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrate-app-lifecycle-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Integrate with App Lifecycle Manager Stay organized with collections  Save and categorize content based on your preferences. 

[App Lifecycle Manager](https://cloud.google.com/products/saas-runtime) is a fully-managed service lifecycle management platform for deploying and operating Software as a Service (SaaS) at scale. App Lifecycle Manager simplifies and automates the complexities of infrastructure operations, which lets service producers focus on their business logic.

As a Google Cloud Marketplace partner offering a SaaS product, you can integrate with App Lifecycle Manager for streamlined validation and tenant onboarding.

## Intended audience

This documentation is intended for both the producers creating the SaaS integration and the consumers provisioning the resulting SaaS applications:

**Producer roles:**

  * **Producer Portal Admin:** Creates the Google Cloud Marketplace listing associated with your pricing SKUs. This role uses Producer Portal (accessed from the project where the Commerce Partner Procurement API is enabled) to create the listing after validation.
  * **SaaS Operator:** The App Lifecycle Manager administrator responsible for the actuation of tenant instances. This role is the overall administrator of SaaS Offerings and manages product offerings and feature sets.
  * **Producer Platform Administrator:** Responsible for the cloud platform running the SaaS, including managing the service management plane of the SaaS.
  * **Producer Platform Engineer:** Responsible for operating the SaaS platform.
  * **Architect:** Designs the SaaS on Google Cloud.
  * **SaaS Developer:** Develops the SaaS application.



**Consumer roles:**

  * **Marketplace Procurement Admin:** Has the IAM permissions within the consumer organization to procure Google Cloud Marketplace solutions.
  * **Consumer Cloud Architect:** Designs applications on the cloud within the consumer organization.
  * **Consumer Platform Administrator:** Manages applications on the cloud for the consumer.
  * **Application Developer:** Develops applications and determines the appropriate third-party service to use from Google Google Cloud Marketplace.



## Advantages of integrating with App Lifecycle Manager

Integrating your SaaS product with App Lifecycle Manager provides the following advantages when you publish your product on Google Cloud Marketplace:

  * **Accelerated consumption metering validation:** Integrating with App Lifecycle Manager lets you create a test tenant. This provides an accurate way to validate your directional consumption ratio and prove that your data plane runs on Google Cloud. This is the preferred way to programmatically validate your Google Cloud architecture and helps avoid delays in the approval process that can occur when using theoretical pricing estimators.
  * **One-click tenant deployment:** You can set up your product to onboard tenants directly from within the Google Cloud Marketplace interface. Customers can provision and configure your SaaS service without being redirected to different producer interfaces. You avoid the need to build, manage, and scale a separate web page or application to facilitate tenant provisioning.
  * **"Built with SaaS Runtime" category:** Your product can receive a "Built with App Lifecycle Manager" category filter on Google Cloud Marketplace. This highlights to consumers that your service runs using a first party Google Cloud service for hosting and managing their SaaS



## Validate your consumption using App Lifecycle Manager

During the validation process, the validation team evaluates the directional consumption ratio of your SaaS offering. Using App Lifecycle Manager is the validation team's preferred way to perform this consumption ratio validation, and it accelerates your approval process.

  1. Use App Lifecycle Manager to create a **SaaS Offering** , model your single-tenant or multi-tenant architecture, and deploy a test tenant on Google Cloud.
  2. Submit your validation request form to the validation team. Your request must include the following information: 
     * Your App Lifecycle Manager project ID
     * Your SaaS Offering



## Add the Built with App Lifecycle Manager category to your listing

**Note:** You cannot manually add this category. Only the validation team can add the **Built with SaaS Runtime** category to your product listing after verifying your use of App Lifecycle Manager.

## Set up one-click tenant onboarding

**Note:** This feature is not yet available. For the latest announcements, see [Google Cloud Marketplace release notes](https://docs.cloud.google.com/marketplace/docs/release-notes).

## What's next

  * Learn how to [Test your SaaS products](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/test-saas-product).
  * Learn how to [Publish your SaaS product](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/submitting).
  * Learn how to [Track your products' associated consumption](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/partner-consumption-tracking).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
