---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers/
title: Create a private offer for a customer \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:18.078352+00:00
---

# Create a private offer for a customer  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Create a private offer for a customer Stay organized with collections  Save and categorize content based on your preferences. 

The following pages explain how to create and publish a new private offer. If you're creating a private offer to replace an active one, see [Modify a published offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/modify-offer) for information about replacement options.

As an alternative to using Producer Portal in the Google Cloud console, you can [create and manage private offers by using the API](https://docs.cloud.google.com/marketplace/docs/partners/offers/commerce-producer-api).

## Before you begin

  * Your product must be integrated with and listed on Cloud Marketplace.

  * You must have the customer's Cloud Billing account ID. If you don't have the ID, request it from your customer.

  * For the Google Cloud project where you manage your products, you must have the following Identity and Access Management (IAM) role(s):

    * Project Editor (`roles/editor`) _OR_
    * Commerce Producer Viewer (`roles/commerceproducer.viewer`) _AND_ Commerce Price Management Private Offers Admin (`roles/commercepricemanagement.privateOffersAdmin`)

If you don't have the roles, request access from a Project Owner (`roles/owner`). For information about managing your team's access, see [Configure access control for creating and managing private offers in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/access-control#create-manage-private).

  * If you want to add a custom end user license agreement (EULA) to your private offer, you must also have the Commerce Price Management Private Offers Admin (`roles/commercepricemanagement.privateOffersAdmin`) role, or equivalent permissions.

  * For SaaS products, make sure you have set up entitlements to track usage. For steps, see [Configure your SaaS product's backend for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/backend-integration).




## Create a private offer

You create private offers by using Producer Portal. The direct link to Producer Portal is:
    
    
    https://console.cloud.google.com/producer-portal?project=PUBLIC_PROJECT_ID
    

Replace PUBLIC_PROJECT_ID with the Google Cloud project that you use to manage your Cloud Marketplace products.

To create your private offer:

  1. In Producer Portal, navigate to the **Private Offers** page. The direct link is:
         
         https://console.cloud.google.com/producer-portal/private-offers
         

  2. On the **Private Offers** page, click **Create offer**.




## What's next

After creating the offer, you complete the following steps in Producer Portal:

  1. [Add product and customer details](https://docs.cloud.google.com/marketplace/docs/partners/offers/add-offer-details) to the offer.

  2. [Set up pricing](https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model) for your offer.

  3. [Specify the end user license agreement (EULA)](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-eula) for your offer.

  4. [Review and publish](https://docs.cloud.google.com/marketplace/docs/partners/offers/review-offer) your offer.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
