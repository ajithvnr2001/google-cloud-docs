---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/send-offer/
title: Send a private offer to a customer \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:33.110651+00:00
---

# Send a private offer to a customer  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/send-offer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Send a private offer to a customer Stay organized with collections  Save and categorize content based on your preferences. 

This article describes how to send a private offer that you [created in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers) to a customer.

## Before you begin

Before you send your offer to a customer, you must have completed the following steps in Producer Portal:

  1. [Create a new offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers).

  2. [Add customer and product details](https://docs.cloud.google.com/marketplace/docs/partners/offers/add-offer-details) to the offer.

  3. [Set up pricing](https://docs.cloud.google.com/marketplace/docs/partners/offers/set-up-pricing-model) for your offer.

  4. [Specify the legal terms](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-eula) for your offer.

  5. [Review and publish](https://docs.cloud.google.com/marketplace/docs/partners/offers/review-offer) your offer.




## Send your offer to your customer

**Note:** If your offer's status is `Pending Google Approval`, Cloud Marketplace sends the offer to the customer automatically after Google approves it.

After you [publish your offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/review-offer#publish-offer), you must send the offer to the customer to view and purchase. A customer can purchase an offer only once.

**Note:** If you're offering a SaaS product, you must also [approve the accepted offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/approve-offer) after the customer completes their purchase.

Regardless of how you send the offer, verify that the customer has the correct IAM permissions for the Cloud Billing account that you included in the offer. To view and purchase the offer, the customer must have:

  * The [Billing Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) (`roles/billing.admin`) role _OR_

  * The Billing User (`roles/billing.user`) _AND_ Consumer Procurement Order Administrator (`roles/consumerprocurement.orderAdmin`) roles.




If your customer or your contact with your customer needs access, you should recommend that they reach out to an Organization Administrator or Billing Administrator.

You can send the offer in either of the following ways.

### Send the offer from Producer Portal

After you publish the offer, the **Share offer** dialog appears. To open the dialog later, go to the **Private offers** page in Producer Portal, and then, for your offer, click **Send offer**.

To send the offer by email from Producer Portal:

  1. In the **Share offer** dialog, click **Send email**.

  2. In the **Add customer email** field, enter the email addresses of the recipients. You can send the email to a maximum of ten recipients.

  3. Optional: To send a copy of the email to the sales contact that you specified for the offer, select **Send a copy to partner contact**. To send a copy to yourself, select **Send a copy to me**.

  4. Click **Send**.




Cloud Marketplace sends each recipient an email that contains a link to the offer. Recipients must have the permissions described earlier to view and purchase the offer.

### Send the offer URL yourself

To send the offer URL in your own email:

  1. In the **Share offer** dialog, click **Copy URL** , and then copy the offer URL.

  2. In your email, include the offer URL and the documentation [Accept a private offer](https://docs.cloud.google.com/marketplace/docs/offers/accepting-private-offer), which explains the process for Cloud Marketplace customers.




#### Example letter to a customer

The following example follows best practices for sending a private offer to a Cloud Marketplace customer:

> Dear _Customer Name_ ,
> 
> Thank you for working with _Organization Name_. Below, please find the private offer for _Product Name_ in Google Cloud:
> 
> _URL of Private Offer_
> 
> Please note that you can purchase this offer only once.
> 
> To view and purchase the offer, you must have specific IAM permissions for the associated Cloud Billing account. For details on requirements and how to accept the offer, see the Google Cloud Marketplace documentation for [accepting a private offer](https://docs.cloud.google.com/marketplace/docs/offers/accepting-private-offer). For additional support, you can also reach out to a Google Cloud Customer Engineer.
> 
> Please let us know if you have any questions about the offer. We look forward to working with you.
> 
> Sincerely,
> 
> _Signature_

## What's next

  * After your customer accepts the private offer, you must [approve the accepted offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/approve-offer).

  * To view the status of your private offer, or to take actions such as downloading the offer as a PDF or cancelling it before acceptance, visit [Manage your customers' private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-private-offers).

  * If you want to be able to configure future private offers to start on specific dates, consider [turning on auto-approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for your SaaS products.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
