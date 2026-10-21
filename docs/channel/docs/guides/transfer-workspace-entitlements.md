---
url: https://docs.cloud.google.com/channel/docs/guides/transfer-workspace-entitlements/
title: Transfer Google Workspace and Google Chrome entitlements using the Cloud Channel API \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:06:08.392289+00:00
---

# Transfer Google Workspace and Google Chrome entitlements using the Cloud Channel API  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/guides/transfer-workspace-entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)



Send feedback 

#  Transfer Google Workspace and Google Chrome entitlements using the Cloud Channel API Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you transfer entitlements for existing Google Workspace and Chrome accounts from their previous reseller. 

For help transferring customers in the Partner Sales Console, see our guides on transferring customers to a [reseller account](https://support.google.com/channelservices/answer/9547629) or a [Google account](https://support.google.com/channelservices/answer/9818236).

Google Workspace customers can only purchase entitlements from a single reseller.

During the transfer, existing entitlements are automatically canceled before they are created again under the new reseller. If a customer has commitment plan entitlements, those will start a new commitment term after the transfer.

## Before you begin

To manage entitlements for a customer, you need a customer-generated [transfer token](http://admin.google.com/TransferToken). Contact the customer and provide your [Reseller Public Identifier](https://support.google.com/channelservices/answer/9547629#zippy=%2Cfind-your-reseller-public-identifier-account-id) so they can generate a transfer token. After they create a token, the customer needs to send their transfer token back to you to complete the process. These tokens expire 14 days after creation. You also need the customer's domain or Cloud Identity ID.

When the customer creates their transfer token, they select the entitlements they want to transfer to their new reseller. You need to transfer all the selected entitlements during the process.

## Transfer steps

If you only have the customer's domain, you can use the Cloud Channel API to return their Cloud Identity ID. Call [checkCloudIdentityAccountsExist](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/checkCloudIdentityAccountsExist) with the customer's domain and, if the domain exists, the API will return the customer's Cloud Identity ID.

  1. With the customer's Cloud Identity ID, call [listTransferableSkus](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableSkus) to retrieve a list of the customer's [TransferableSku](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableSkus#TransferableSku) SKUs. Check each object's [transferEligibility](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableSkus#TransferEligibility) to make sure you can purchase the associated SKU.
  2. For each TransferableSku you can purchase, use the [listTransferableOffers](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableOffers) method to find its corresponding offers. At this point you should have the customer's transferable SKUs, their new offer IDs, and you should know if you can purchase these SKUs.
  3. Begin the transfer by using the [customers.import](https://docs.cloud.google.com/channel/docs/guides/channel/docs/reference/rest/v1/accounts.customers/import) method to import the customer's data.
  4. For each [TransferableOffer](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts/listTransferableOffers#TransferableOffer), create a new corresponding [Entitlement](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers.entitlements#Entitlement) object and call the [transferEntitlements](https://docs.cloud.google.com/channel/docs/reference/rest/v1/accounts.customers/transferEntitlements) method to perform the transfer. Each Entitlement needs an offer, commitmentSettings, and any required parameters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
