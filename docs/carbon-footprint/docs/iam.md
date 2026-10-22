---
url: https://docs.cloud.google.com/carbon-footprint/docs/iam/
title: Cloud Billing IAM permissions and roles \u00a0|\u00a0 Carbon Footprint \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:17.546737+00:00
---

# Cloud Billing IAM permissions and roles  |  Carbon Footprint  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/carbon-footprint/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Carbon Footprint ](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Billing IAM permissions and roles

This page describes how you use [Cloud Billing IAM](https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) and project-based [IAM](https://docs.cloud.google.com/iam) roles and permissions to control access to Carbon Footprint data.

## Overview

[Cloud Billing IAM](https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) and project-based [IAM](https://docs.cloud.google.com/iam) [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions) and [roles](https://docs.cloud.google.com/iam/docs/overview#roles) determine your ability to access data through the Google Cloud console and [data export](https://docs.cloud.google.com/carbon-footprint/docs/export).

A role is a collection of permissions. You can't grant a permission to a principal (user or service account) directly; instead, you grant principals a role. When you grant a role to a principal, you grant them all the permissions that the role contains. You can grant multiple roles to the same principal.

To access Carbon Footprint data associated with a billing account, a billing account administrator must grant you one or more Cloud Billing IAM roles, on the billing account, that contain the appropriate carbon data permission.

To learn how to grant these roles, see [Update user permissions for a Cloud Billing account](https://cloud.google.com/billing/docs/how-to/grant-access-to-billing#update-cloud-billing-permissions).

**Caution:** These permissions must be granted from the Billing account settings page, not the project-level IAM page. If you don't know who your administrator is, see [Find a Billing Account Administrator](https://cloud.google.com/billing/docs/how-to/find-billing-account-administrator). 

## Permissions

The following table lists the [Cloud Billing IAM](https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) permissions associated with Carbon Footprint.

Permission | Description  
---|---  
`billing.accounts.getCarbonInformation` | View Carbon Footprint of a billing account.  
  
## Predefined roles

The following table describes [Cloud Billing IAM](https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) roles associated with Carbon Footprint, and lists the permissions that are contained in each role.

Role | Description | Permissions  
---|---|---  
Carbon Footprint Viewer  
(`roles/billing.carbonViewer`) | Can list billing accounts and view carbon information. Cannot see detailed billing data. | `billing.accounts.list``billing.accounts.get``billing.accounts.getCarbonInformation`  
Billing Account Administrator  
(`roles/billing.admin`) | Provides access to see and manage all aspects of billing accounts, including carbon information. | See [Cloud Billing IAM roles documentation](https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) for complete list of permissions of this role.   
Includes but not limited to:  
`billing.accounts.list``billing.accounts.get``billing.accounts.getCarbonInformation`  
Billing Account Viewer  
(`roles/billing.viewer`) | View billing account cost and pricing information, transactions, and billing and commitment recommendations, including carbon information. | See [Cloud Billing IAM roles documentation](https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) for complete list of permissions of this role.   
Includes but not limited to:  
`billing.accounts.list``billing.accounts.get``billing.accounts.getCarbonInformation`  
Account Hierarchy Manager  
(`roles/billing.linkAdmin`) | Authorized to manage billing account hierarchy. | See [Cloud Billing IAM roles documentation](https://cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) for complete list of permissions of this role.   
Includes but not limited to:  
`billing.accounts.list``billing.accounts.get``billing.accounts.getCarbonInformation`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
