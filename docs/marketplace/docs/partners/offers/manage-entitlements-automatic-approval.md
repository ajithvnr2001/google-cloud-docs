---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements-automatic-approval/
title: Manage entitlements for private offers with automatic offer approval \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:57.088785+00:00
---

# Manage entitlements for private offers with automatic offer approval  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements-automatic-approval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Manage entitlements for private offers with automatic offer approval Stay organized with collections  Save and categorize content based on your preferences. 

When a customer purchases a [private offer](https://docs.cloud.google.com/marketplace/docs/partners/offers), Google creates an _entitlement_ , which indicates that the customer has bought the offer from Cloud Marketplace.

This document reviews how to manage entitlements for your [private offers that have automatic offer approval turned on](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) by using the Partner Procurement API.

**Caution:** Once you turn on automatic offer approval for a SaaS product, you no longer receive `ENTITLEMENT_CREATION_REQUESTED` or `ENTITLEMENT_PLAN_CHANGE_REQUESTED` Pub/Sub messages for that SaaS product.

If you haven't turned on [automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for your software as a service (SaaS) product, you receive different Pub/Sub messages than those described in this document. For details of those Pub/Sub messages, refer to [Manage entitlements for private offers](https://docs.cloud.google.com/marketplace/docs/partners/offers/manage-entitlements).

For details on using the Partner Procurement API for private offers, visit the [reference documentation](https://docs.cloud.google.com/marketplace/docs/partners/offers/rest-resources).

**Note:** You can also perform some management tasks in Producer Portal when you view your list of offers.

## Verify when your customer's offers will become active

When you turn on [automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for a SaaS product, you receive different Pub/Sub messages than those you receive for SaaS products that don't have automatic approval turned on. Because SaaS products with automatic offer approval support scheduled start dates, after a private offer is accepted, you must verify when the offer is expected to begin, so that you can provision resources at the right time.

**Note:** If you've turned on automatic offer approval for SaaS products, you still must [approve your customer's account](https://docs.cloud.google.com/marketplace/docs/partners/offers/approve-offer) before an offer can take effect. If you don't approve your customer's account before the scheduled start date of their offer, that offer is automatically rejected, for both new offers and amendments to existing offers.

When a customer purchases a private offer, Cloud Marketplace creates an entitlement and sends the following Pub/Sub message to your product:
    
    
    {
      "eventId": "...",
      "eventType": "ENTITLEMENT_OFFER_ACCEPTED",
      "entitlement": {
      "id": "ENTITLEMENT_ID",
      "updateTime": "...",
      "newPendingOfferDuration": "", // Contract duration for the offer
      "newOfferStartTime": "...", // Starting time for the offer
      "newOfferEndTime": "...", // Ending time for the offer
      },
    }

In this example, ENTITLEMENT_ID is an ID created by Cloud Marketplace. The `newOfferStartTime` and `newOfferEndTime` fields are formatted as an [RFC 3339](https://tools.ietf.org/html/rfc3339) timestamp in UTC, such as `"2022-01-01T00:00:00Z"`. If you use the Partner Procurement API to [retrieve the entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/get), the API response also includes these `newOfferStartTime` and `newOfferEndTime` fields.

In your system, update the user's account to reflect that they've purchased the offer. Use the `newOfferStartTime` field to verify the time that the offer is expected to start, so that you can provision resources as needed.

When the offer reaches its start date and becomes active, you receive an additional Pub/Sub message with an `eventType` of `ENTITLEMENT_ACTIVE`.

## What's next

  * [Turn on automatic offer approval](https://docs.cloud.google.com/marketplace/docs/partners/offers/automatic-approval) for SaaS products that you offer.

  * [Create a private offer](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers) for a specific customer.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
