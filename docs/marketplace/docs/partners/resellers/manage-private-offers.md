---
url: https://docs.cloud.google.com/marketplace/docs/partners/resellers/manage-private-offers/
title: Manage your customers' private offers as a Cloud Marketplace reseller \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:31.229028+00:00
---

# Manage your customers' private offers as a Cloud Marketplace reseller  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/resellers/manage-private-offers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Manage your customers' private offers as a Cloud Marketplace reseller Stay organized with collections  Save and categorize content based on your preferences. 

After you accept a private offer plan from an independent sales vendor (ISV), you can use it to create private offers for your customers to purchase the ISV's Cloud Marketplace products at a discount. You can view the status of private offers that you've created for your customers by using the Partner Sales Console.

For more information about private offer plans, see [Private offer plans for Cloud Marketplace resellers](https://docs.cloud.google.com/marketplace/docs/partners/resellers/reseller-private-offer-plans). For detailed information about the Partner Sales Console, see the [Partner Sales Console help center](https://support.google.com/channelservices/answer/9789535).

## Before you begin

  * To access the Partner Sales Console, you and your team members must have the following Identity and Access Management (IAM) roles: 
    * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin), or a custom role with both `billing.accounts.get` and `billing.accounts.update` permissions on your reseller Cloud Billing accounts. This role must be assigned at the [Organizational level](https://docs.cloud.google.com/resource-manager/docs/access-control-org).
    * The _Google Cloud Reseller Admin_ role in the Partner Sales Console. For more information, see [Assign Google Cloud reseller roles and permissions](https://support.google.com/channelservices/answer/9805524).
  * To manage private offers as a reseller, you must have [accepted a private offer plan](https://docs.cloud.google.com/marketplace/docs/partners/resellers/reseller-private-offer-plans#accept-plan) from an ISV and used it to [create private offers](https://docs.cloud.google.com/marketplace/docs/partners/resellers/create-private-offers) for your customers.



## View the status of your resold customers' offers

To use the Partner Sales Console to view the status of your customers' private offers, complete the following steps:

  1. Sign in to the [Partner Sales Console](https://channelservices.cloud.google.com/).
  2. Click **Customers** , then click **Private offers**.



### Statuses for resold customers' offers

The following table shows possible statuses for private offers for resold customers:

**Offer status** | **Description**  
---|---  
Published | You published the offer, but the customer hasn't accepted it yet.  
Accepted | The customer accepted the offer, but the offer hasn't started yet.  
Active | The customer accepted the offer, and the offer has started.  
Expired | The specified due date for the offer passed, and the customer didn't accept the offer.  
Ended | The offer was accepted, became active, and ended when it passed its end date.  
Cancelled | You withdrew the offer.  
  
## Archive a resold customer's offer

In the Partner Sales Console, you can move private offers from the **Main** view to the **Archived** tab if they have one of the following statuses:

  * Active
  * Expired
  * Canceled
  * Ended
  * Unavailable



To archive an offer that you've made as a reseller, complete the following steps:

  1. Sign in to the [Partner Sales Console](https://channelservices.cloud.google.com/).
  2. Click **Customers**.
  3. Select the customer for the offer that you want to archive, and then click **Private offers**.
  4. Click **Archive**.



After you move an offer to the **Archived** tab, you can use that tab to continue accessing and managing the offer.

## What's next

  * [Request a reseller discount from an ISV](https://docs.cloud.google.com/marketplace/docs/partners/resellers/request-incentive) for their Cloud Marketplace products.

  * [Process requests from customers](https://docs.cloud.google.com/marketplace/docs/partners/resellers/process-entitlement-transfers) to change details of their orders.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
