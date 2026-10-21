---
url: https://docs.cloud.google.com/channel/docs/guides/multiple-billing-account-starter/
title: Reseller account with multiple Google Workspace billing account Account Starter Guide \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:21:34.080858+00:00
---

# Reseller account with multiple Google Workspace billing account Account Starter Guide  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/guides/multiple-billing-account-starter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Reseller account with multiple Google Workspace billing account Account Starter Guide Stay organized with collections  Save and categorize content based on your preferences. 

This page is a starter guide focused on helping API partners understand how a reseller account with multiple Google Workspace billing accounts works. 

## About Google Workspace billing accounts

A Google Workspace billing account is used to pay for an entitlement. A Google Workspace billing account has a currency, region and legal entity; these attributes are immutable and cannot be changed.

## A reseller account with a single vs multiple Google Workspace billing accounts

A reseller account with a single Google Workspace billing account is defined as an account that only has a single Google Workspace billing account option for each Google Workspace SKU type. There are three Google Workspace SKU types: Google Workspace, Google Workspace Voice and Google Workspace Drive. This means that when you select a specific SKU type, there is only a single Google Workspace billing account that can be used and you do not need to specify the Google Workspace billing account when you are transacting on the Google Workspace subscription.

A reseller account with multiple Google Workspace billing accounts is when there are two or more Google Workspace billing account options for any of the Google Workspace SKU types. Given that there are two or more Google Workspace billing account options when purchasing a particular SKU, you need to specify the Google Workspace billing account. This means that you need to add a "Select Google Workspace billing account" step to your transaction flow. Note that the two or more Google Workspace billing account option could have the same or different currency; either way you will need to select the desired Google Workspace billing account when purchasing a Google Workspace subscription.

**Caution:** When working with a reseller account with multiple Google Workspace billing accounts, since there are two or more Google Workspace billing account choices when purchasing a Google Workspace subscription, API users must add a step in their transaction flow to select the desired Google Workspace billing account, otherwise the transaction will fail.

## Google Workspace billing account and Currency constraints

There are some Google Workspace billing account and currency constraints.

  1. All Google Workspace subscriptions for a customer must be paid by Google Workspace billing accounts in the same currency.
  2. For certain SKUs, the corresponding Subscriptions need to be paid for by the same Google Workspace billing account. For example, Google Workspace Business Subscriptions and Google Workspace Chrome Subscriptions must use the same Google Workspace billing account but Google Workspace Voice Subscriptions require a different Google Workspace billing account. The Google Workspace and Voice Google Workspace billing account must still have the same currency to satisfy condition 1.



## Transition from a reseller account with a single Google Workspace billing account to a reseller account with multiple Google Workspace billing account

For partners that already have a reseller account with a single Google Workspace billing account, you might notice that there is no Google Workspace billing account selection step in your transaction flows. The reason behind this is because for a given Google Workspace SKU type, there is only one eligible Google Workspace billing account so our system automatically selects that Google Workspace billing account for you. As mentioned above, in a multiple Google Workspace billing account setup, there will be cases where there are two or more Google Workspace billing account choices; this means partners will need to explicitly choose the desired Google Workspace billing account for a given transaction.

### Step-by-step instruction to convert your reseller account from a single Google Workspace billing account to a multiple Google Workspace billing account.

  1. Introduce a "Select Google Workspace billing account" step into your transaction process. At this point, you still have a reseller account with a single Google Workspace billing account. This means that there's only going to be one Google Workspace billing account choice during the "Select Google Workspace billing account" step. The benefit of doing this first is that it enables you add the "Select Google Workspace billing account" step into your transaction flow without any interruptions to day-to-day transact operations.
  2. Convert your reseller account from a single Google Workspace billing account to a reseller account with multiple Google Workspace billing accounts by adding a new Google Workspace billing account to your reseller console.
  3. That's it! Once the new Google Workspace billing account is added to your account, the account conversion has been completed. You will see more Google Workspace billing account options in the "Select Google Workspace billing account" step, just select the Google Workspace billing account you want to use and continue the process. [Detail step-by-step API integration guide](https://docs.cloud.google.com/channel/docs/guides/manage-entitlements)



## Default Google Workspace billing account logic under a reseller account with multiple Google Workspace billing account

Ideally, you have added the "Select Google Workspace billing account" step in your transaction workflow where you always select a Google Workspace billing account. This means that you won't need to rely on any default Google Workspace billing account selection logic.

**Caution:** In the rare but unfortunate case where a partner added a second Google Workspace billing account without introducing a "Select Google Workspace billing account" step in their transaction flow, you will run into transaction problem because our system won't know which Google Workspace billing account to choose when there are two or more Google Workspace billing account options.

To help mitigate these transactional issues, we introduced default Google Workspace billing account selection logic to make the API as backward compatible as possible.

**Caution:** The default Google Workspace billing account selection logic does not work for all scenarios, see below.

Here is the default logic for each SKU type

  * Google Workspace SKU type - We will default to the first Google Workspace billing account. For example, when you were in the single Google Workspace billing account state, you had one Google Workspace billing account, this will be the default Google Workspace billing account.
  * Google Workspace Voice SKU type - If there is only one Google Workspace Voice billing account, we default to this. Otherwise, you must choose a specific Google Workspace Voice billing account, otherwise we will throw an exception.
  * Google Workspace Drive SKU type - If there is only one Google Workspace Drive billing account, we default to this. Otherwise, you must specific a Google Workspace Drive billing account or else we will throw an exception.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
