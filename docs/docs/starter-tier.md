---
url: https://docs.cloud.google.com/docs/starter-tier/
title: Learn about the Google Cloud Starter Tier \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:10.276574+00:00
---

# Learn about the Google Cloud Starter Tier  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/starter-tier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Learn about the Google Cloud Starter Tier Stay organized with collections  Save and categorize content based on your preferences. 

Supported Google products, such as [Google AI Studio](https://ai.google.dev/aistudio), offer a streamlined path to deploy applications to Google Cloud using the Starter Tier.

The Starter Tier lets an individual Google Account use a limited set of resources as part of the application deployment process. It offers essential capabilities to run your applications, and you don't need to enter billing information.

This document explains how Starter Tier resources are provisioned, how to manage your applications, and how to upgrade to a paid Cloud Billing account when you're ready to scale.

## How the Starter Tier works

When you deploy an application using the Starter Tier from a supported product, your resources and the underlying infrastructure required to run the application are automatically provisioned in a fully managed Google Cloud project. Google manages the project and project configuration on your behalf, so you can use the project without providing any billing information.

Because Google manages the underlying infrastructure, this environment requires no configuration and differs from standard Google Cloud projects in the following ways:

  * **No Cloud Billing account:** You don't need to provide a credit card or set up a Cloud Billing account to deploy your applications.
  * **Preconfigured environment:** Available Google Cloud regions, IAM roles, quotas, organization policies, and API enablements are strictly managed by Google.
  * **Separate Terms of Service:** Your Starter Tier resources aren't Google Cloud services and aren't controlled by the standard Google Cloud Terms of Service. Instead, your resources are governed by the [Starter Tier Additional Terms of Service](https://cloud.google.com/terms/starter-tier-additional-terms-of-service).



### Capabilities and limits

The Starter Tier helps you build and deploy functional applications with no upfront costs. If you have a [Google Account](https://myaccount.google.com/), you can automatically use a limited number of published applications and resources at no cost. This includes a free allowance for the underlying infrastructure required to run them.

Depending on the product you use to deploy your application, the Starter Tier enforces specific technical limits for the underlying infrastructure, such as maximum instances and storage. These limits help manage capacity and help prevent abuse or security risks. Additionally, all resources within your Starter Tier project are restricted to a limited set of geographic regions.

For detailed information on specific limits, quotas, and resources, see the product documentation. You can find links to this documentation in Supported products.

If you require service capabilities beyond the Starter Tier, you must upgrade your project to a standard Google Cloud project.

## Supported products

The following table lists the Google products that offer the Starter Tier deployment experience and the list of underlying resources that the Starter Tier provides for running your applications.

Product | Description | Starter Tier capabilities and underlying resources  
---|---|---  
[Google AI Studio](https://ai.google.dev/aistudio) |  Deploy functional web applications and agents directly from the AI Studio interface without providing a Cloud Billing account or credit card. For deployment instructions, see [Deploy from Google AI Studio](https://ai.google.dev/gemini-api/docs/aistudio-deploying). |  Provisions a bundled ecosystem of resources, including the following:

  * [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
  * [Firebase Authentication](https://firebase.google.com/docs/ai-assistance/ai-studio-integration)
  * [Firestore](https://firebase.google.com/docs/ai-assistance/ai-studio-integration#understand-shared-quota)
  * [Cloud SQL for PostgreSQL (developer edition)](https://docs.cloud.google.com/sql/docs/postgres/ai-assisted-coding-and-cloud-sql#starter-tier-and-pricing)

Google AI Studio also integrates with the following connected services:

  * [Google Maps Platform](https://developers.google.com/maps/ai/ai-studio) provides a Google AI Studio integration using a Demo Key to prototype location-aware applications at no cost.

  
  
Additional requirements or restrictions might apply to the product. For detailed limits, see the product documentation.

## Manage your Starter Tier resources

To help you focus on your application logs, metrics, and basic configuration, Google Cloud provides a simplified view of the Google Cloud console for your Starter Tier project. This tailored interface removes complex organizational controls and doesn't require billing information.

If you are a Starter Tier user, you can see your applications, view telemetry data, and manage your Starter Tier resources directly in the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

## Explore other Google Cloud products

Your Starter Tier applications run in an isolated, strictly managed environment. You can't enable other Google Cloud APIs within that same project.

If you navigate to the Google Cloud console and try to use a product or service that the Starter Tier doesn't support, you aren't automatically redirected to your fully managed Starter Tier project. Instead, you are directed to sign up for the Google Cloud [Free Trial](https://docs.cloud.google.com/free/docs/free-cloud-features) and create your own standard Google Cloud project, separate from your Google-managed Starter Tier project. This option lets you explore and evaluate Google Cloud at no cost in a different environment, without upgrading your Starter Tier applications to a paid plan.

Alternatively, if you want full access to Google Cloud from the same Starter Tier project you use, you must upgrade your Starter Tier project to a standard Google Cloud project, using the interface of the product you use to deploy your applications.

## Upgrade your Starter Tier project to a standard Google Cloud project

As your applications evolve, you might require capabilities beyond the Starter Tier, such as higher quotas, increased compute resources, access to additional Google Cloud regions, or access to the broader Google Cloud platform. To unlock these capabilities, you can convert your fully managed Starter Tier project into a standard Google Cloud project.

When you initiate this upgrade directly from the interface of the product you use to deploy your applications, such as Google AI Studio, you are prompted to accept the standard Terms of Service and set up a [Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account).

During the upgrade process, your project is converted to a standard Google Cloud project through a seamless transition:

  * There is no downtime for your applications.
  * Your application state, databases, and deployment URLs are preserved.
  * You gain full [IAM](https://docs.cloud.google.com/iam/docs/overview) control and ownership over the project.
  * You can enable any Google Cloud API.



After upgrading to a standard project, your resources are billed according to standard Google Cloud pricing against your connected Cloud Billing account, and the project becomes subject to the standard Google Cloud Terms of Service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
