---
url: https://docs.cloud.google.com/bare-metal/docs/bms-configure-pam/
title: Configure Privileged Access Manager for evict operation \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:14.276682+00:00
---

# Configure Privileged Access Manager for evict operation  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-configure-pam/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Privileged Access Manager for evict operation

This page describes how to set up Privileged Access Manager to evict LUNs and storage volumes.

Privileged Access Manager ensures that critical operations on sensitive resources, like permanently deleting LUNs and storage volumes, are only performed with a valid justification and for a limited time. For more information, see [Privileged Access Manager overview](https://docs.cloud.google.com/iam/docs/pam-overview).

Only a project owner or an Identity and Access Management (IAM) administrator can create a custom role, set up Privileged Access Manager, create an entitlement, and approve or deny a grant request.

**Important:** We recommend that you grant temporary elevated access only to principals who are authorized to carry out the evict operation. Avoid granting access to everyone in your organization as it might result in accidental permanent deletion of your storage volumes.

## Before you begin

  * Create a custom IAM role with the following permissions:

    * `baremetalsolution.volumes.onDemandEvict`
    * `baremetalsolution.luns.onDemandEvict`

To learn how to create a custom role, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

  * [Set up Privileged Access Manager and grant required permissions](https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup).




## Create an entitlement

[Create an entitlement](https://docs.cloud.google.com/iam/docs/pam-create-entitlements) for Bare Metal Solution evict operation with the following information:

  * Custom role that you created for the evict operation in Before you begin.
  * Maximum duration for a grant. For example, 2 hours.
  * Approval Requirement: We recommended that you set mandatory approver requirement to authorize the request.



## Request Elevated Access

If you're a user who needs to perform evict operation, you can [request a grant](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#request-grant) against the Bare Metal Solution evict operation entitlement with a justification.

You can check your [grant request status](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access#check-status).

## Approve or deny grant

After you request a grant, the approver specified in the entitlement receives your grant request. Once the approver approves the request, your access is activated.

If you're an approver, to learn how to approve a grant, see [Approve or deny grants using Google Cloud console](https://docs.cloud.google.com/iam/docs/pam-approve-deny-grants#approve-deny-console).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
