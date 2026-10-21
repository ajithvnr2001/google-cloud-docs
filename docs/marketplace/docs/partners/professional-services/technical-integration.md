---
url: https://docs.cloud.google.com/marketplace/docs/partners/professional-services/technical-integration/
title: Complete your professional services product's technical integration \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:48:13.568847+00:00
---

# Complete your professional services product's technical integration  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/professional-services/technical-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Complete your professional services product's technical integration Stay organized with collections  Save and categorize content based on your preferences. 

If your professional services product includes usage in its pricing, you must complete technical integration with Google Cloud Marketplace before you publish your product. If none of your product's pricing models include usage, technical integration is optional and you can skip it.

## Before you begin

  * Set up access to the Cloud Commerce Partner Procurement API, as described in [ Integrate your app](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup).
  * If you chose a usage-based pricing scheme, verify that your Partner Engineer has created a service that you can report usage against. This service displays in the **Service domain** field of the [ **Billing Integration** section](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/backend-integration#backend-integration) of Producer Portal.



## Access your product's technical integration in Producer Portal

To access all of the information you need to integrate your product with Cloud Marketplace from one location, such as your service accounts and plan level identifiers, you can use the **Technical integration** section of Producer Portal.

The direct link to Producer Portal is:
    
    
    https://console.cloud.google.com/producer-portal?project=YOUR_PROJECT_ID
    

**Note:** If you don't see the link, or can't access the URL, verify that you've selected the correct project. If you still can't access the URL, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to request assistance, and include the word "Marketplace" in your description. For more information about Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support).

To access the **Technical integration** section:

  1. In the list of products, click the name of your product.

  2. From the **Overview** page of your product, go to the **Technical integration** section.




## Create and link service accounts in Producer Portal

You can use the **Billing integration** section of the **Technical integration** tab in Producer Portal to create and link the service accounts that you use to interact with the Partner APIs and to get information about users' purchases.

In the following steps, you can use existing service accounts, or create new service accounts. If you create a new service account, specify the service account's name in the **Service account name** field and the service account's ID in the **Service account ID** field, and then click **Create and link**. For detailed steps to create a service account, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

To link your service accounts:

  1. From your product's **Overview** page in Producer Portal, go to the **Billing integration** section of the **Technical integration** tab.

  2. To integrate with the Partner Procurement API, under **Link a service account to call Procurement API** , click **Add service account**. You can enter an existing service account into the field, or create a new service account.

  3. To integrate with Pub/Sub, under **Link a service account to subscribe to Pub/Sub topic** , click **Add service account**. You can enter an existing service account into the field, or create a new service account. Grant the [Pub/Sub Editor](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.editor) Identity and Access Management (IAM) role to the service account that you link.

  4. To integrate with the Service Control API, under **Add`roles/servicemanagement.serviceController` to a service account**, click **Add service account**. You can enter an existing service account into the field, or create a new service account.




## What's next

  * [Publish](https://docs.cloud.google.com/marketplace/docs/partners/professional-services/publish) your professional services product.



[ Previous arrow_back  Choose and submit your pricing model  ](https://docs.cloud.google.com/marketplace/docs/partners/professional-services/choose-pricing)

[ Next Publish your product  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/professional-services/publish)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
