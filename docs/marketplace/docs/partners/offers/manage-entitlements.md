---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements/
title: Manage entitlements for private offers \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:57.014187+00:00
---

# Manage entitlements for private offers  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Manage entitlements for private offers Stay organized with collections  Save and categorize content based on your preferences. 

When a customer purchases a [private offer](https://docs.cloud.google.com/marketplace/docs/partners/offers), Google creates an _entitlement_ , which indicates that the customer has bought the offer from Cloud Marketplace.

This document reviews how to manage entitlements for your private offers by using Producer Portal and the Partner Procurement API. You can use Partner Procurement API to approve offer entitlements. For other offer entitlement management tasks, you must use the Partner Procurement API.

**Caution:** If you've turned on [automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for your software as a service (SaaS) product, you receive different Pub/Sub messages from those described in this document. You should instead refer to [Manage entitlements for private offers with automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements-automatic-approval).

## Approve entitlements by using Producer Portal

You can use Partner Procurement API to approve entitlements for private offers. To approve an entitlement, complete the following steps:

  1. In Producer Portal, go to the **Private Offers** page.

  2. Click **Manage your offers** more_vert.

**Note:** If you aren't able to approve the entitlement by using Partner Procurement API, verify that you've [approved the customer's account resource](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-accounts).



## Manage entitlements by using the Partner Procurement API

The following sections describe how to manage entitlements for private offers by using the Partner Procurement API.

For details on using the Partner Procurement API for private offers, visit the [reference documentation](https://docs.cloud.google.com/marketplace/docs/partners/offers/rest-resources).

### Approve an entitlement

When a customer purchases a private offer, Cloud Marketplace creates an entitlement and sends the following Pub/Sub message to your product:
    
    
    {
      "eventId": "...",
      "eventType": "ENTITLEMENT_CREATION_REQUESTED",
      "entitlement": {
      "id": "ENTITLEMENT_ID",
      "updateTime": "...",
      "newPendingOfferDuration": "P1Y6M", // Contract duration for the offer
      "newOfferEndTime": "", // Ending time for the offer
      },
    }

In this example, ENTITLEMENT_ID is an ID created by Cloud Marketplace.

If the offer was created with a duration, the message displays the duration in years and months, and the `newOfferEndTime` field is empty. If the offer was created with a specified ending time, the message displays the offer's end time, and the `newPendingOfferDuration` field is empty.

In your system, update the user's account to reflect that they've purchased the offer. Then, to approve the entitlement, make an `HTTP POST` request to the Partner Procurement API, and send the ENTITLEMENT_ID that you're approving:
    
    
    POST v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID:approve
    

**Caution:** If you don't approve your customer's entitlement before the scheduled start date of their offer, that offer is automatically rejected, for both new offers and amendments to existing offers.

### Reject an entitlement

To reject an entitlement, use the `reject` method in your `HTTP POST` request:
    
    
    POST v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID:reject
    

### Replace an active offer

Depending on how you set up your private offer, your customer might be able to replace their offer. If a customer selects a new private offer, you receive a Pub/Sub message, in the following format:
    
    
    {
      "eventId": "...",
      "eventType": "ENTITLEMENT_PLAN_CHANGE_REQUESTED",
      "entitlement": {
      "id": "ENTITLEMENT_ID",
      "newPendingPlan": "ultimate",   // New plan for the offer,
      "newPendingOffer": "OFFER2",    // New offer,
      "updateTime": "...",
      "newPendingOfferDuration": "P2Y",   // Contract duration for the new offer
      },
    }

In this example, OFFER2 is the replacement offer and ENTITLEMENT_ID is an ID created by Cloud Marketplace. The offer duration is provided in years and months.

To approve the offer replacement, make the following `HTTP POST` request to the Partner Procurement API:
    
    
    POST v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID:approvePlanChange
    

The request body must have the plan for the offer that is being approved:
    
    
    {
      "pendingPlanName": PLAN_NAME
    }

After the change is approved, you receive another Pub/Sub message when the change takes effect. In the message, the `eventType` field changes to `ENTITLEMENT_PLAN_CHANGED`. To check the status of a plan, make the following `HTTP GET` request to the Partner Procurement API:
    
    
    GET v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID
    

The response is similar to the following, with the state field indicating whether the new offer is active, or whether the offer change is still pending:
    
    
    {
      "name": "providers/PARTNER_ID/entitlements/ENTITLEMENT_ID",
      "provider": "PARTNER_ID",
      "account": "USER_ACCOUNT_ID",
      "product": "example-server",
      "Offer":   "OFFER1",
      "plan": "pro",
      "state": "ENTITLEMENT_PENDING_PLAN_CHANGE",
      "newPendingOffer": "OFFER2",
      "newPendingPlan": "ultimate",
      "newPendingOfferDuration": "P2Y",
      "newOfferEndTime": "",
      ...
    }

### Complete other entitlement tasks

For other entitlement tasks that aren't specific to private offers, refer to the Cloud Marketplace public documentation:

  * [Cancel an entitlement](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements#cancel_an_entitlement)
  * [Delete an entitlement](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements#delete_an_entitlement)



## List of event types for private offer account tasks

The following table includes `eventType`s that your product might receive in Pub/Sub messages for private offers.

For the full list, see [List of event types for account tasks](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements#eventtypes).

eventType  | **Description**  
---|---  
`ENTITLEMENT_OFFER_ENDED` | Indicates that a customer's private offer has ended. The offer either triggers an `ENTITLEMENT_CANCELLED` event or remains active with non-discounted pricing.  
  
## What's next

  * [Create a private offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers) for a specific customer.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
