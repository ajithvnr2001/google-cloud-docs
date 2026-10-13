---
url: https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account/
title: Manage your Cloud Billing account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:19.399610+00:00
---

# Manage your Cloud Billing account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Manage your Cloud Billing account Stay organized with collections  Save and categorize content based on your preferences. 

This document directs you to resources that explain how to create, modify, close, and reopen a Cloud Billing account, as well as manage linked projects and payment settings.

## About Cloud Billing accounts

Cloud Billing accounts pay for usage costs in Google Cloud projects and Google Maps Platform projects. Cloud Billing accounts _don't_ pay for Google Workspace accounts. Google Workspace customers need a separate Google Workspace billing account.

You need a Cloud Billing account to use Google Cloud or Google Maps Platform. To use Google Cloud resources in a project, billing must be enabled on the project. Billing is enabled when the project is linked to an active Cloud Billing account.

**Caution:** Projects that aren't linked to an active Cloud Billing account can't use Google Cloud or Google Maps Platform services. This is true even if you only use [services that are free](https://docs.cloud.google.com/free/docs/gcp-free-tier).

## Pricing information

If you're looking for information about Google API pricing, refer to the documentation for the API you are using.

  * For information about Google Cloud pricing and the Google Cloud free trial, see [Google Cloud Pricing](https://cloud.google.com/pricing/).


  * For Google Maps Platform pricing, see [Google Maps Platform Pricing](https://mapsplatform.google.com/pricing/) or see [Google Maps Platform Billing](https://developers.google.com/maps/billing/gmp-billing).



## Set up a Cloud Billing account

The following sections explain how to set up a Cloud Billing account.

### Create a new Cloud Billing account

There are [two types of Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that you can create:

Billing account types  
---  
[Self-serve (or Online) account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account) | You can create self-serve accounts online, and manage the forms of payment you use to automatically pay for your Google Cloud and Google Maps Platform usage costs. [ Create a new, self-serve Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account)  
[ Invoiced (or Offline) account](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing) | If you prefer to have a Cloud Billing account that pays for your Google Cloud and Google Maps Platform usage costs with a monthly invoice, or multiple invoices when [ split invoicing](https://docs.cloud.google.com/billing/docs/how-to/split-invoice) applies, we must configure invoiced accounts for you. [ Apply for monthly invoiced billing](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing)  
  
### About authorization requests

When you create a new, self-serve Cloud Billing account, you might notice a $0.00 transaction from Google on your bank or credit card statement. These are authorization requests only, not actual charges.

  * Learn more [about authorization requests](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#bank-auth).

  * For information about verifying bank accounts, see [Verify your bank account](https://docs.cloud.google.com/billing/docs/how-to/verify-bank).

  * For information about adding backup methods of payment, see [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods).




### Verify your Google payments contact email address

To ensure you receive Cloud Billing-related and payments-related notifications, we might ask you to verify your email address on your Google payments profile.

  * Learn more about [how to verify your email address](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#verify-email-address).



## Modify your Cloud Billing account settings

After you create a Cloud Billing account and its associated Google payments profile, you can [change or update many account settings](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account).

This section lists a few of the settings you can update. For a more complete list, see [Modify your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account).

Account settings you can modify  
---  
[ Billing account name](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#rename_account) | The name of the billing account that displays in billing account selectors and tabular lists or reports that display the billing account name.  
[ Mailing addresses](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account#change_the_billing_address) | There are one or more mailing addresses associated with your billing account. The mailing addresses can include the legally registered business address, and the addresses where invoices are mailed.  
[ Projects linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project) | A Cloud Billing account defines who pays for a given set of resources, and it's [ linked to one or more projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked). Project usage is charged to the linked Cloud Billing account. You can [ change the Cloud Billing account linked to each of your projects](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).  
[ Payment methods for a self-serve billing account](https://docs.cloud.google.com/billing/docs/how-to/payment-methods) | Usage costs accrued for a self-serve Cloud Billing account are automatically charged to the payment instrument on file in the associated Google payments profile. These forms of payment typically include credit cards, debit cards, or bank accounts, depending on your [ country and currency](https://docs.cloud.google.com/billing/docs/resources/currency).  
[ Purchase Order number on invoices](https://docs.cloud.google.com/billing/docs/how-to/purchase-order) | For Cloud Billing accounts configured to be billed by a monthly invoice, you can set or modify the invoice purchase order number (also called IO number, CPE, or client code), an identifier that appears in the header of your invoices.  
  
## Close, reopen, or delete a Cloud Billing account

The following sections explain how to close, reopen, or delete a Cloud Billing account.

### Close a Cloud Billing account

You can close an active Cloud Billing account to stop all billable services in any [projects linked to the account](https://docs.cloud.google.com/billing/docs/how-to/view-linked), such as running VM instances or storage buckets. If your projects aren't linked to an active, valid Cloud Billing account, you can't use the products and services enabled in your projects. This is true even if your projects only use Google Cloud or Google Maps Platform [services that are free](https://docs.cloud.google.com/free/docs/gcp-free-tier).

  * Learn how to [close a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#close_a_billing_account).



**Tip** : Rather than closing your account, you can stop new charges from accruing in a Cloud Billing account using one of the following options:

  * [Disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) on each [project linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked)
  * [Link your projects to a different, active Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).



### Reopen a closed Cloud Billing account

If your Cloud Billing account is closed or inactive, you can reopen the account.

Before a Cloud Billing account can be reactivated, you must resolve any Google payments-related issues or suspensions. Follow the steps in the [resolving declined payments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#resolving_declined_payments) troubleshooter for assistance.

  * Learn how to [reopen a closed Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#reopen_a_closed_billing_account).



### Delete a Cloud Billing account

**Cloud Billing accounts can't be manually deleted.** Even if you close your Cloud Billing account, the Cloud Billing account information is retained for reporting and auditing purposes.

To stop charges, close the Cloud Billing account or [disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) on the [associated projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

#### Automatic deletion of orphaned accounts

A Cloud Billing account is orphaned if it has no active administrators. This can happen if the Google Accounts of all administrators are deleted. An orphaned account is not automatically closed or deleted, and charges continue on the attached payment method.

Google only schedules a Cloud Billing account for automatic deletion if all users on its IAM policy have had their Google Accounts permanently deleted and purged.

Google doesn't automatically delete an orphaned account if it meets any of the following criteria:

  * The account is associated with an active [Organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).
  * The account type is [Monthly Invoicing](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing).
  * The account is specially designated as a high-value or strategic account.



If you want to change the form of payment associated with your Cloud Billing account, you can [manage your payment methods](https://support.google.com/paymentscenter/topic/9023854) in the Google payments center.

## Related topics

  * [View projects linked to a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked)
  * [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project)
  * [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods)
  * [Resolve billing issues](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
  * [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
