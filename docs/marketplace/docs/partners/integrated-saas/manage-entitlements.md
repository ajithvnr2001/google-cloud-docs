---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements/
title: Manage customer entitlements for your SaaS product \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:42.094030+00:00
---

# Manage customer entitlements for your SaaS product  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Manage customer entitlements for your SaaS product Stay organized with collections  Save and categorize content based on your preferences. 

When customers choose a pricing plan for your software, Google creates an _entitlement_ , which indicates that the customer has bought your product from Cloud Marketplace. This section reviews how to create and manage entitlements for your customers using the Partner Procurement API.

For more details on managing entitlements, visit the [reference documentation](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements).

## Before you begin

  * Set up access to the Cloud Commerce Partner Procurement API, as described in [ Integrate your app](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup).



If you've turned on multiple orders of the same product, the Partner Procurement API can send multiple events with the event type `ENTITLEMENT_ACTIVE` for the same value of `ACCOUNT_ID`, each with a unique `ENTITLEMENT_ID` representing a different offer. This means that you must ensure that your app's event handling logic can respond to the `ENTITLEMENT_ID` instead of the `ACCOUNT_ID` or the `PRODUCT_ID`.

You must ensure that your frontend integration can handle the new `orders` object included in the JWT payload. For more information, see [Integrate your app's frontend](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration).

For more information about turning on multiple orders of the same product, see [Turn on multiple orders of the same product](https://docs.cloud.google.com/marketplace/docs/partners/offers/multiple-offers).

## Approve an entitlement

When a customer chooses a pricing plan, Cloud Marketplace creates an entitlement and sends the following Pub/Sub message to your app:
    
    
    {
      "eventId": "...",
      "eventType": "ENTITLEMENT_CREATION_REQUESTED",
      "providerId": "YOUR_PARTNER_ID",
      "entitlement": {
        "id": "ENTITLEMENT_ID",
        "updateTime": "...",
        "newPendingOfferDuration": "P2Y3M",   // Contract duration for offer-based entitlements
      },
    }

where ENTITLEMENT_ID is an ID created by Cloud Marketplace. If the offer has a specified duration, that duration is provided in years and months. If the offer has a specified end date, instead of a duration, the field indicating the duration is empty.

In your system, update the user's account to reflect that they have purchased a plan. Then, to approve the entitlement, make an `HTTP POST` request to the Partner Procurement API, and send the ENTITLEMENT_ID that you're approving:
    
    
    POST v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID:approve
    

## Reject an entitlement

To reject an entitlement, make an `HTTP POST` request to the Partner Procurement API, and use the `reject` method in your request:
    
    
    POST v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID:reject
    

To give a reason for rejecting the entitlement in the request body, use the following format:
    
    
    {
      "reason": "..."
    }

## Change an entitlement plan

Depending on how you set up your pricing plans, your customers might be able to change their plan. If a customer selects a new pricing plan, you receive a Pub/Sub message, in the following format:
    
    
    {
      "eventId": "...",
      "eventType": "ENTITLEMENT_PLAN_CHANGE_REQUESTED",
      "providerId": "YOUR_PARTNER_ID",
      "entitlement": {
        "id": "ENTITLEMENT_ID",
        "newPendingPlan": "ultimate",   // New plan
        "updateTime": "...",
        "newPendingOfferDuration": "P2Y3M",   // Contract duration for the new offer, for offer-based entitlements
        "newProduct": "test-product.cloud.goog"
        "newPendingOffer": "projects/1234567/services/test-product.cloud.goog/standardOffers/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
      },
    }

If the offer has a specified duration, that duration is provided in years and months. If the offer has a specified end date, instead of a duration, the field indicating the duration is empty.

To approve the plan change, make the following `HTTP POST` request to the Partner Procurement API:
    
    
    POST v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID:approvePlanChange
    

The request body must have the plan that is being approved:
    
    
    {
      "pendingPlanName": PLAN_NAME
    }
    

After the change is approved, you receive another Pub/Sub message when the change takes effect. In the message, the `eventType` field changes to `ENTITLEMENT_PLAN_CHANGED`. To check the status of a plan, make the following `HTTP GET` request to the Partner Procurement API.
    
    
    GET v1/providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID
    

The response is similar to the following, with the `state` field indicating whether the new plan is active, or whether the plan change is still pending:
    
    
    {
      "name": "providers/YOUR_PARTNER_ID/entitlements/ENTITLEMENT_ID",
      "provider": "YOUR_PARTNER_ID",
      "account": "USER_ACCOUNT_ID",
      "product": "example-server",
      "plan": "pro",
      "state": "ENTITLEMENT_PENDING_PLAN_CHANGE",
      "newPendingPlan": "ultimate",
      ...
    }

## Cancel an entitlement

If a user decides to cancel their entitlement, you receive a Pub/Sub notification. Similar to changing a plan, the actual cancellation might take effect at the end of the current billing cycle.

The notification is in the following format:
    
    
    {
      "eventId": "...",
      // If the entitlement is canceled at the end of the month,
      // eventType is ENTITLEMENT_PENDING_CANCELLATION
      "eventType": "ENTITLEMENT_CANCELLED",
      "providerId": "YOUR_PARTNER_ID",
      "entitlement": {
        "id": "ENTITLEMENT_ID",
        "updateTime": "..."
      },
    }

## Delete an entitlement

If a user makes a direct request to Google support, or if they leave the Google platform, their entitlements are immediately canceled, and their entitlement and accounts are deleted after a 60 day grace period. To protect the user's privacy, you must delete their data from your servers when you're notified.

When the entitlements are canceled and the account is deleted, you receive notifications similar to the following:
    
    
    {
      "eventId": "...",
      "eventType": "ENTITLEMENT_DELETED",
      "providerId": "YOUR_PARTNER_ID",
      "entitlement": {
        "id": "ENTITLEMENT_ID",
        "updateTime": "...",
      },
    }
    
    
    {
      "eventId": "...",
      "eventType": "ACCOUNT_DELETED",
      "providerId": "YOUR_PARTNER_ID",
      "account": {
        "id": "USER_ACCOUNT_ID",
        "updateTime": "...",
      },
    }

## Entitlement state transitions

The following table shows how an entitlement transitions between states based on different events.

Current State | Triggering Event | New State | Notes  
---|---|---|---  
(None) | `ENTITLEMENT_CREATION_REQUESTED` | `ENTITLEMENT_ACTIVATION_REQUESTED` | The customer selects a plan.  
`ENTITLEMENT_ACTIVATION_REQUESTED` | Provider approves the entitlement | `ENTITLEMENT_ACTIVE` | The entitlement becomes active.  
`ENTITLEMENT_ACTIVATION_REQUESTED` | Provider rejects the entitlement | `ENTITLEMENT_CANCELLED` | The entitlement is not created.  
`ENTITLEMENT_ACTIVE` | `ENTITLEMENT_PLAN_CHANGE_REQUESTED` | `ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL` or `ENTITLEMENT_PENDING_PLAN_CHANGE` | The customer requests a plan change.  
`ENTITLEMENT_ACTIVE` | `ENTITLEMENT_CANCELLING` | `ENTITLEMENT_PENDING_CANCELLATION` | The customer cancels their plan, effective at the end of the term.  
`ENTITLEMENT_ACTIVE` | `ENTITLEMENT_CANCELLED` | `ENTITLEMENT_CANCELLED` | The customer cancels their plan immediately.  
`ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL` | Provider approves the plan change | `ENTITLEMENT_PENDING_PLAN_CHANGE` or `ENTITLEMENT_ACTIVE` | If the current plan requires the billing cycle to complete, it goes to pending. Otherwise, it becomes active.  
`ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL` | Provider rejects the plan change | `ENTITLEMENT_ACTIVE` | The entitlement reverts to the old plan.  
`ENTITLEMENT_PENDING_PLAN_CHANGE` | `ENTITLEMENT_PLAN_CHANGED` | `ENTITLEMENT_ACTIVE` | The billing cycle completes, and the new plan takes effect.  
`ENTITLEMENT_PENDING_PLAN_CHANGE` | `ENTITLEMENT_OFFER_ENDED` followed by `ENTITLEMENT_PLAN_CHANGED` | `ENTITLEMENT_PENDING_CANCELLATION` | The customer accepted a private offer resulting in a plan change, and the transition takes effect.  
`ENTITLEMENT_PENDING_CANCELLATION` | `ENTITLEMENT_CANCELLED` | `ENTITLEMENT_CANCELLED` | The billing cycle completes, and the entitlement is fully canceled.  
`ENTITLEMENT_PENDING_CANCELLATION` | `ENTITLEMENT_CANCELLATION_REVERTED` | `ENTITLEMENT_ACTIVE` | The pending cancellation was reverted by the customer.  
  
## List of event types for account tasks

The following is a list of the `eventType`s that your app might receive in Pub/Sub messages:

eventType| Description| ACCOUNT_CREATION_REQUESTED| Deprecated  
---|---  
ACCOUNT_ACTIVE| Indicates that the customer's account has been created.  
ACCOUNT_DELETED| Indicates that the customer's account was deleted from Google Cloud systems.  
ENTITLEMENT_CREATION_REQUESTED| Indicates that a customer selected one of your pricing plans.  
ENTITLEMENT_OFFER_ACCEPTED| Indicates that an offer was accepted by a customer. Includes the scheduled start time of the offer, if there is one. This event is sent for both private offers and standard offers (public purchases).  
ENTITLEMENT_ACTIVE| Indicates that a customer's chosen plan is now active.  
ENTITLEMENT_PLAN_CHANGE_REQUESTED| Indicates that a customer chose a new plan.  
ENTITLEMENT_PLAN_CHANGED| Indicates that a customer's plan change is approved and the changes have taken effect.  
ENTITLEMENT_PLAN_CHANGE_CANCELLED| Indicates that a customer's plan change was canceled, either because it wasn't approved, or because they switched back to their old plan.  
ENTITLEMENT_PENDING_CANCELLATION| Indicates that a customer canceled their plan, and the cancellation is pending until the end of the billing cycle. This state is also applicable when a customer on an existing plan (public or private offer) accepted a private offer resulting in a plan change. After receiving the events `ENTITLEMENT_PLAN_CHANGE_REQUESTED` and `ENTITLEMENT_OFFER_ENDED`, when the event `ENTITLEMENT_PLAN_CHANGED` is received, the entitlement is in this state.  
ENTITLEMENT_CANCELLATION_REVERTED| Indicates that a customer's pending cancellation was reverted. Note that cancellations cannot be reverted after they are final.  
ENTITLEMENT_CANCELLED| Indicates that a customer's plan was canceled.  
ENTITLEMENT_CANCELLING| Indicates that a customer's plan is in the process of being canceled.  
ENTITLEMENT_RENEWED| Indicates that a customer's entitlement was renewed for another term. You don't need to take any action to complete the renewal.  
ENTITLEMENT_OFFER_ENDED| Indicates that a customer's private offer has ended. If the customer's entitlement was canceled, a separate `ENTITLEMENT_CANCELLED` event is triggered. If the customer's entitlement is still active, their plan reverts to non-discounted pricing.  
ENTITLEMENT_DELETED| Indicates that information about a customer's plan was deleted from Cloud Marketplace.  
  
[ Previous arrow_back  Manage user accounts  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-user-accounts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
