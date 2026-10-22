---
url: https://docs.cloud.google.com/iam/docs/user-identities/
title: Identities for users \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:59.732646+00:00
---

# Identities for users  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/user-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Identities for users Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the ways that you can configure identities for users in your organization so that they can access Google Cloud. It doesn't discuss the identities that your customers use to authenticate to your application. To learn about how to authenticate customers to your application, see the [Identity Platform documentation](https://docs.cloud.google.com/identity-platform/docs), which discusses customer identity and access management (CIAM).

For users to access Google Cloud, they need an identity that Google Cloud can recognize. There are several ways to configure identities so that Google Cloud can recognize them:

  * Create Cloud Identity or Google Workspace accounts
  * Set up one of the following federated identity strategies: 
    * Federation using Cloud Identity or Google Workspace
    * Workforce Identity Federation



## Cloud Identity or Google Workspace accounts

You can use Cloud Identity or Google Workspace to create [managed user accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account). These accounts are called _managed accounts_ because you control their lifecycle and configuration. Users with these accounts can authenticate to Google Cloud and be authorized to use Google Cloud resources.

Cloud Identity and Google Workspace share a common technical platform. Both products offer similar features for managing users, groups, and authentication.

Only Cloud Identity or Google Workspace managed Super Admin accounts can invite users with unmanaged [consumer accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account) to transfer their consumer accounts to managed accounts.

To get started with Cloud Identity or Google Workspace, you can do the following:

  * To learn more about using Cloud Identity and Google Workspace to create identities for your users, see [Google for organizations](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_for_organizations).
  * Learn how to [set up Cloud Identity](https://support.google.com/cloudidentity/topic/7555414).
  * Learn how to [set up Google Workspace](https://support.google.com/a/answer/6365252).



## Federated user identities

You can federate identities to allow users to use their existing identity and credentials to sign in to Google services. There are several methods to federate identities in Google Cloud.

### Federation using Cloud Identity or Google Workspace

When you federate identities with Cloud Identity or Google Workspace, users aren't prompted to enter a password when they try to access Google services. Instead, you can redirect them to an [external identity provider (IdP)](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp) to authenticate.

To use this type of identity federation, a user must have an [external identity](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_identities) in the external IdP and a corresponding Google Account in Cloud Identity or Google Workspace, typically with the same email address. You can keep these accounts synchronized by using a tool like [Google Cloud Directory Sync (GCDS)](https://tools.google.com/dlpage/dirsync/) or by provisioning accounts using an [external authoritative source](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_authoritative_source). For example, you could set up account provisioning with [Microsoft Entra ID](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory) or [Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).

To learn more about federation using Cloud Identity or Google Workspace, see [Single sign-on](https://docs.cloud.google.com/architecture/identity/single-sign-on).

### Workforce Identity Federation

Workforce Identity Federation lets you use an external identity provider (IdP) to authenticate and authorize a workforce—a group of _users_ , such as employees, partners, and contractors—using IAM, so that the users can access Google Cloud services. With Workforce Identity Federation you don't need to synchronize user identities from your existing IdP to Google Cloud identities, as you would with Cloud Identity's [Google Cloud Directory Sync (GCDS)](https://tools.google.com/dlpage/dirsync/). Workforce Identity Federation extends Google Cloud's identity capabilities to support syncless, attribute-based single sign-on.

To learn more about Workforce Identity Federation, see [Workforce Identity Federation overview](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

## What's next

  * Learn about the ways to [authenticate to Google APIs with user credentials](https://docs.cloud.google.com/docs/authentication#user-accounts).
  * Learn how to [grant users access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
