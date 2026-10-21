---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/view-offer-status/
title: View the status of a private offer \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:58.008557+00:00
---

# View the status of a private offer  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/view-offer-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  View the status of a private offer Stay organized with collections  Save and categorize content based on your preferences. 

You can view the status of your private offers by using Producer Portal. For more information about private offers, see the [Private Offers documentation](https://docs.cloud.google.com/marketplace/docs/partners/offers).

## Before you begin

  * Your product must be integrated with and listed on Cloud Marketplace.

  * You must have [created at least one private offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers).

  * For the Google Cloud project where you manage your products, you must have the [Project Viewer](https://console.cloud.google.com/iam-admin/roles/details/roles%3Cviewer) (`roles/viewer`) role. If you don't have the role, request access from a Project Owner (`roles/owner`).

For information about managing your team's access, see [Configure access control for managing analytics and reports in Producer Portal](https://docs.cloud.google.com/marketplace/docs/partners/access-control#analytics-reports).




## View offer status

To view the status of your private offers, go to Producer Portal's **Private Offers** page in the Google Cloud console.
    
    
     https://console.cloud.google.com/producer-portal/private-offers
     

You see a table with all of your offers. To understand the state of each offer, view the offer's **Status** column:

**Offer status** | **Description**  
---|---  
Account pending approval | The account associated with this offer must be approved.  
Account rejected | The account associated with this offer was rejected.  
Activating | The new offer will be ready to use in a few minutes, or at its scheduled start time  
Active | Your customer is using this offer.  
Approval failed | An error has occurred, please re-approve this offer after the status changes.  
Approving | This offer's approval is being processed on our end. This should only take a few minutes.  
Canceled | The created offer is no longer available for the customer to accept, and the URL is no longer active.  
Created | You can now send this offer URL to your customer for purchase.  
Draft | This offer has been created but not finalized. You can continue to modify this offer until you finish it.  
Needs your approval | This offer has been accepted by the customer and is awaiting your confirmation.  
Offer expired | The customer did not accept this offer.  
Order expired | The end date for the contract has passed.  
Pending acceptance | The offer hasn't been accepted by the customer yet.  
Pending Google approval | Google is reviewing this offer before sending it out to the customer.  
Rejected | You turned down an offer that the customer accepted.  
Scheduled | You approved the replacement offer and it will become active on the contract start date  
Unavailable | The offer is a legacy offer that's no longer supported.  
  
## View the history of an offer

**Note:** To view the history of an offer, you must have the [Commerce Price Management Events Viewer](https://console.cloud.google.com/iam-admin/roles/details/roles%3Ccommercepricemanagement.eventsViewer) (`roles/commercepricemanagement.eventsViewer`) role for the Google Cloud project where you manage your products. If you don't have the role, request access from a Project Owner (`roles/owner`). For information about managing your team's access, see [Access control for viewing key events for private offers](https://docs.cloud.google.com/marketplace/docs/partners/access-control#view-offer-events).

To view a record of key events for an offer that you've published, complete the following steps:

  1. Go to Producer Portal's **Private Offers** page in the Google Cloud console.

  2. In the list of offers, click the offer ID of the offer that you want to view history for.




In the **Offer details** page, you see a **Key Events** widget that lists a historical record of statuses for that offer.

To download a copy of the offer at a particular step, click **Download PDF** from that particular step.

## What's next

The following articles describe additional ways that you can manage your customers' private offers:

  * [Approve an accepted offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/approve-offer).

  * [Modify an offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/modify-offer), which can include modifying pricing, contract duration, or acceptance date.

  * [Download an offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/download-offer) as a PDF.

  * [Cancel a published offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/cancel-offer).

  * [Archive an inactive offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/archive-offer).

  * [Cancel an active order](https://docs.cloud.google.com/marketplace/docs/partners/offers/cancel-active-order).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
