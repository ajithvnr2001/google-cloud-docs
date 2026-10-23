---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-user-accounts/
title: Manage user accounts for your SaaS product \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:50.294057+00:00
---

# Manage user accounts for your SaaS product  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-user-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  Manage user accounts for your SaaS product Stay organized with collections  Save and categorize content based on your preferences. 

At a high level, your app must handle the following scenario:

  1. A user makes a request or change in Cloud Marketplace, such as signing up for your product.

  2. Cloud Marketplace sends your app a notification through Pub/Sub, containing information about the request in the `eventType` field. For example, if a user changes their entitlement, the `eventType` is `ENTITLEMENT_PLAN_CHANGED`.

See the [full list of possible values for `eventType`](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements#eventtypes).

  3. To approve the request, your app sends an `HTTP POST` request to the Partner Procurement API.




The following sections describe the types of requests that users can make, and what your app must do to handle the requests.

For the API calls described in this section, use this endpoint:
    
    
    https://cloudcommerceprocurement.googleapis.com/
    

## Before you begin

  * Set up access to the Cloud Commerce Partner Procurement API, as described in [ Integrate your app](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/technical-integration-setup).



## Create an account for a new user

When a user first purchases your product, Cloud Marketplace creates an account resource that tracks the user's relationship with you. For subsequent purchases against products owned by you, same account resource will be reused. Whenever a user makes their first purchase of any of your products, if you've turned on account notifications for that product, then you're notified through the Pub/Sub topic created for you. The Pub/Sub message is in the following format:
    
    
    {
      "eventId": "...",
      "providerId": "YOUR_PARTNER_ID",
      "account": {
        "id": "USER_ACCOUNT_ID",
        "updateTime": "..."
      }
    }

where USER_ACCOUNT_ID is the account ID created by Cloud Marketplace and YOUR_PARTNER_ID is the partner ID assigned to you.

To find your partner ID:

  1. In the [Producer Portal](https://console.cloud.google.com/producer-portal), open your product.
  2. Go to the **Technical integration** section.
  3. In the **Provider identifier** field, your partner ID is the **Provider ID** value.



Simultaneously, Cloud Marketplace directs the user to your sign-up page, where they create an account in your system. For information about creating the sign-up page, see [Integrating your app's frontend](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/frontend-integration).

## Approve a user's account

After the user has successfully signed up, your app must call the Partner Procurement API and indicate that the account has been approved. Accounts are created in the `ACCOUNT_ACTIVE` state, but they have a `PENDING` entry in the `approvals` field called `signup`, which indicates that the user has not yet signed up. To approve the account after the user has signed up, use the following `HTTP POST` request:
    
    
    POST v1/providers/YOUR_PARTNER_ID/accounts/USER_ACCOUNT_ID:approve {'approvalName': 'signup'}
    

## Check the status of a user's account

To check the status of a linked account, use the following `HTTP GET` request:
    
    
    GET v1/providers/YOUR_PARTNER_ID/accounts/USER_ACCOUNT_ID
    

The response is in the following format:
    
    
    {
      "name": "providers/YOUR_PARTNER_ID/accounts/USER_ACCOUNT_ID",
      "provider": "acme-services",
      "state": "ACCOUNT_ACTIVE",
      "approvals": [{
        "name": "signup",
        "state": "APPROVED",
        "updateTime": "...",
      }],
      "updateTime": "...",
      "createTime": "..."
    }

For a list of possible account states, see the [`providers.accounts` API reference](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.accounts#state).

[ Next Manage customer entitlements  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/manage-entitlements)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
