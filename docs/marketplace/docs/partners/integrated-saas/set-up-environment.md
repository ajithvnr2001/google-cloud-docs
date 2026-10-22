---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/set-up-environment/
title: Setting up your software as a service (SaaS) product for Google Cloud \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:39.158174+00:00
---

# Setting up your software as a service (SaaS) product for Google Cloud  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/set-up-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Setting up your software as a service (SaaS) product for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to set up your Google Cloud environment and add your product's details to Cloud Marketplace.

## Setting up your Google Cloud environment

You must set up your Google Cloud environment so that you can distribute your SaaS product.

### Creating your workspace

We recommend that you create a new project in the [Google Cloud console](https://console.cloud.google.com/) primarily for your Cloud Marketplace products. For the project ID, use the format `PARTNER_NAME-public`. For information about creating projects, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

If you already have a project for your current Cloud Marketplace products, you can reuse that project and start creating your product in Producer Portal.

After you create your project, grant the following Identity and Access Management (IAM) roles at the project level:

  * To the group `cloud-commerce-marketplace-onboarding@twosync-src.google.com`, grant the following roles:

    * Project Editor (`roles/editor`)
    * Service Management Administrator (`roles/servicemanagement.admin`)
  * To the service account `cloud-commerce-producer@system.gserviceaccount.com`, grant the Config Editor (`roles/servicemanagement.configEditor`) role.




For steps to grant access to your project, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). Grant one of the following options to the service account `cloud-commerce-procurement@system.gserviceaccount.com`:

  * The Service Management Administrator role.
  * The Service Consumer role (`roles/servicemanagement.serviceConsumer`) and the Service Controller role (`roles/servicemanagement.serviceController`). This requires using the Google Cloud CLI, because these roles aren't visible in the UI.



For steps to grant access at the service level, see [Granting and revoking access to the API](https://docs.cloud.google.com/endpoints/docs/openapi/control-api-access).

## Submitting your product information

Before you begin setting up and integrating your product, we recommend that you complete the [Cloud Marketplace Project Info Form](https://docs.google.com/forms/d/e/1FAIpQLSfddn4mwKnqtLNQ-m7IgRZ-bgTz4BOsrEDWCf3XBjc_ogKNnA/viewform). You only need to complete this form once.

After you complete the form, your Partner Engineer gives you access to Producer Portal, and enables the Cloud Commerce Partner Procurement API and the Service Control API, which you use to integrate your product with Cloud Marketplace.

## Creating your product in the portal

You use Producer Portal to add your product information, which includes your marketing information, pricing plan, and other details.

After you complete the Cloud Marketplace Project Info Form from the Google Cloud Marketplace team, your Partner Engineer enables Producer Portal for you.

To publish your product to Cloud Marketplace, you use Producer Portal to submit the following details:

  * **Product Details** : Add listing and marketing information about your product.
  * **Pricing** : Specify your pricing model to determine how customers will pay for your product.
  * **Technical Integration** : Submit technical integration details for the SaaS product that you are offering through Google Cloud Marketplace.



You can submit these reviews individually, as you complete them. Some reviews might take up to two weeks for approval, so we recommend reviewing the requirements and getting started as early as possible.

**Note:** You can submit your Product Details and Pricing for review in any order. While you can work on your Technical Integration before your Pricing submission is approved, you must submit your Technical Integration for review after your Pricing submission is approved.

At this stage, you only need to create the entry for your product in Producer Portal. You add your marketing information in later steps.

The direct link to Producer Portal is:
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, see [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

To create your product:

  1. Click **Add product**.

  2. Under **Solution type** , select **SaaS**.

  3. Under **Product name** , name your product and review the **Product ID**. By default, the **Solution ID** is used in the URL for your Cloud Marketplace listing. You can also customize the URL for your listing later, when you add your product details.

**Caution:** The solution ID and solution type cannot be changed after the product is created. You can change your product name before you submit your product.
  4. Click **Create**. It might take a few seconds to create your product.




### Adding product details

The product details include your product listing on Cloud Marketplace, marketing information, and links to documentation. You use Producer Portal to add your product details.

To add product details, complete the following steps:

Go to the Producer Portal:
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, see [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

To add product details:

  1. In the list of products, click the solution ID that you created.

  2. On the **Overview** page of your product, go to the **Product details** section and click **Edit**.

  3. Complete the **Product info** tab of the **Product details** section. While completing **Product info** , you can add Category IDs. Category IDs let customers find your product under select categories or filters as they search Cloud Marketplace. You can select up to two Category IDs for a product.

**Note:** If you're adding a product that connects to Google Distributed Cloud, add the following text to your product info: "We recommend that you only purchase this product for a duration equal to or less than the shortest subscription length of your Google Distributed Cloud-connected devices."
  4. To add tutorials, documentation, and, optionally, additional license agreements, complete the **Documentation** tab of the **Product details** section.

  5. To add search metadata or keywords, or to customize the URL of the details page for your product, complete the **Product metadata** tab of the **Product details** section.


**Note:** Cloud Marketplace might require additional approvals for some categories of products. If you want to add your solution listing to a category that isn't listed in Producer Portal, submit a request using the [special category request form](https://docs.google.com/forms/d/1-VwD1yyr_w5yWYIbx0OFzQOp7XgSPpa6IgaWbltoR90/edit?resourcekey=0-93_HVNitkydC9bBb6oZiIg).

When you're ready to submit your product details for processing, click **Submit**. It takes approximately two to five days for the Partner Engineering team to review and approve your product details. You can start editing details now and submit the review later.

If you use App Lifecycle Manager to deploy and operate your SaaS product, you can also set up one-click tenant onboarding within your product details. For more information, see [Integrate with App Lifecycle Manager](https://docs.cloud.google.com/marketplace/docs/partners/integrate-app-lifecycle-manager).

[ Previous arrow_back  Overview and checklist  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas)

[ Next Choose and submit your pricing model  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/select-pricing)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
