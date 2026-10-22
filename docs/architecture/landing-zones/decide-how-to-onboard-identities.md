---
url: https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities/
title: Decide how to onboard identities to Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:20.825129+00:00
---

# Decide how to onboard identities to Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Decide how to onboard identities to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-02 UTC

This document describes identity provisioning options for Google Cloud and the decisions that you must make when you onboard your users to Cloud Identity or Google Workspace. This document also provides guidance on where to find more information on how to deploy each option.

This document is part of a series about [landing zones](https://docs.cloud.google.com/architecture/landing-zones), and is intended for architects and technical practitioners who are involved in managing identities for your organization and your Google Cloud deployment.

## Overview

To let your organization's users access your Google Cloud resources, you must provide a way for them to authenticate themselves. Google Cloud uses [Google Sign-In](https://account.google.com/) to authenticate users, which is the same identity provider (IdP) that other Google services such as Gmail or Google Ads use.

Although some users in your organization might already have a private Google user account, we strongly advise against letting them use their private accounts when they access Google Cloud. Instead, you can onboard your users to Cloud Identity or Google Workspace, which lets you control the lifecycle and security of user accounts.

Provisioning identities in Google Cloud is a complex topic and your exact strategy might require more detail than is in scope for this decision guide. For more best practices, planning, and deployment information, see [overview of identity and access management](https://docs.cloud.google.com/architecture/identity).

## Decision points for identity onboarding

To choose the best identity provisioning design for your organization, you must make the following decisions:

  * Your identity architecture

  * How to consolidate existing user accounts




## Decide on your identity architecture

Managing the lifecycle and security of user accounts plays an important role in securing your Google Cloud deployment. A key decision that you must make is the role that Google Cloud should play in relation to your existing identity management systems and applications. The options are as follows:

  * Use Google as your primary identity provider (IdP).
  * Use federation with an external identity provider.



The following sections provide more information about each option.

### Option 1: Use Google as your primary source for identities (no federation)

When you create user accounts directly in [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://workspace.google.com/), you can make Google your source of identities and primary IdP. Users can then use these identities and credentials to sign in to Google Cloud and other Google services.

Cloud Identity and Google Workspace provide a large selection of [ready-to-use integrations](https://workspace.google.com/marketplace) for popular third-party applications. You can also use standard protocols such as [SAML](https://support.google.com/a/answer/6087519), [OAuth](https://support.google.com/googleapi/answer/6158849), and [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect) to integrate your custom applications with Cloud Identity or Google Workspace.

Use this strategy when the following is true:

  * Your organization already has user identities provisioned in Google Workspace.
  * Your organization doesn't have an existing IdP.
  * Your organization has an existing IdP but wants to start quickly with a small subset of users and federate identities later.



Avoid this strategy when you have an existing IdP that you want to use as an authoritative source for identities.

For more information, see the following:

  * [Preparing your Google Workspace or Cloud Identity Account](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account)
  * [Using Google as an IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_google_as_an_idp)



### Option 2: Use Cloud Identity federation with an external identity provider

You can integrate Google Cloud with an existing external IdP by using federation. Identity federation establishes trust between two or more IdPs so that the multiple identities that a user might have in different identity management systems can be linked.

When you [federate a Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_identities) with an external IdP, you let users use their existing identity and credentials to sign in to Google Cloud and other Google services.

**Important:** Super administrator accounts always bypass single-sign-on (SSO). 

Use this strategy when the following is true:

  * You have an existing IdP such as Active Directory, Microsoft Entra ID, ForgeRock, Okta, or Ping Identity.
  * You want employees to use their existing identity and credentials to sign in to Google Cloud and other Google services such as Google Ads and Google Marketing Platform.



Avoid this strategy when your organization doesn't have an existing IdP.

For more information, see the following:

  * [External identities - Overview of Google identity management](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_identities)
  * [Reference architectures: Using an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp)
  * [Best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating)
  * [Federating Google Cloud with Active Directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction)
  * [Federating Google Cloud with Azure AD](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory)



### Option 3: Use Workforce Identity Federation with an external identity provider

[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) lets you federate a Google Cloud organization with an external identity provider directly. This type of federation doesn't involve Cloud Identity or Google Workspace.

Use this strategy when the following is true:

  * You don't want to federate with Cloud Identity.
  * You have an existing IdP.
  * Your Google services support Workforce Identity Federation.



Avoid this strategy when your organization doesn't have an existing IdP or your users require access to other Google services such as Google Workspace or Google Ads.

For more information, see the following:

  * [Architecture patterns for identity federation](https://docs.cloud.google.com/iam/docs/federated-identity-architectures)
  * [Best practices for using Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-workforce-identity-federation)



## Decide how to consolidate existing user accounts

If you haven't been using Cloud Identity or Google Workspace, it's possible that your organization's employees are using [consumer accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account) to access your Google services. Consumer accounts are accounts that are fully owned and managed by the people who created them. Because those accounts are not under your organization's control and might include both personal and corporate data, you must decide how to consolidate these accounts with other corporate accounts.

For details on consumer accounts, how to identify them, and what risk they might pose to your organization, see [Assessing existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).

The options for consolidating the accounts are as follows:

  * Consolidate a relevant subset of consumer accounts.
  * Consolidate all accounts through migration.
  * Consolidate all accounts through eviction, by not migrating accounts before creating new ones.



The following sections provide more information about each option.

### Option 1: Consolidate a relevant subset of consumer accounts

If you want to keep consumer accounts and manage them and their data under corporate policies, you must migrate them to Cloud Identity or Google Workspace. However, the process of consolidating consumer accounts can be time consuming. Therefore, we recommend that you first evaluate which subset of users are relevant for your planned Google Cloud deployment, and then consolidate only those user accounts.

Use this strategy when the following is true:

  * The [transfer tool for unmanaged user accounts](https://support.google.com/a/answer/6178640) shows many consumer user accounts in your domain, but only a subset of your users will use Google Cloud.
  * You want to save time in the consolidation process.



Avoid this strategy when the following is true:

  * You don't have consumer user accounts in your domain.
  * You want to ensure that all data from all consumer user accounts in your domain is consolidated to managed accounts before you start using Google Cloud.



For more information, see [Overview of consolidating accounts](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts).

### Option 2: Consolidate all accounts through migration

If you want to manage all user accounts in your domain, you can consolidate all consumer accounts by migrating them to managed accounts.

Use this strategy when the following is true:

  * The transfer tool for unmanaged user accounts shows only a few consumer accounts in your domain.
  * You want to restrict the use of consumer accounts in your organization.



Avoid this strategy when you want to save time in the consolidation process.

For more information, see [Migrating consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts).

### Option 3: Consolidate all accounts through eviction

You can evict consumer accounts in the following circumstances:

  * You want users who created consumer accounts to keep full control over their accounts and data.
  * You don't want to transfer any data to be managed by your organization.



To evict consumer accounts, create a managed user identity of the same name without migrating the user account first.

Use this strategy when the following is true:

  * You want to create new managed accounts for your users without transferring any of the data that exists in their consumer accounts.
  * You want to restrict the Google services that are available in your organization. You also want users to keep their data and keep using these services for the consumer accounts that they created.



Avoid this strategy when consumer accounts have been used for corporate purposes and might have access to corporate data.

For more information, see [Evicting consumer accounts](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts).

## Best practices for onboarding identities

After you choose your identity architecture and your method to consolidate existing consumer accounts, consider the following identity best practices.

### Select a suitable onboarding plan that works for your organization

Select a high-level plan to onboard your organization's identities to Cloud Identity or Google Workspace. For a selection of proven onboarding plans, along with guidance on how to select the plan that best suits your needs, see [Assessing onboarding plans](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans).

If you plan to use an external IdP and have identified user accounts that need to be migrated, you might have additional requirements. For more information, see [Assessing the impact of user account consolidation on federation](https://docs.cloud.google.com/architecture/identity/assessing-consolidation-impact-on-federation).

### Protect user accounts

After you've onboarded users to Cloud Identity or Google Workspace, you must put measures in place to help protect their accounts from abuse. For more information, see the following:

  * Implement [security best practices for Cloud Identity administrative accounts](https://support.google.com/a/answer/9011373).
  * Implement [2-Step Verification](https://knowledge.workspace.google.com/admin/security/protect-your-business-with-2-step-verification) and follow [best practices when combined with federating identities](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#multi-factor_authentication).
  * Export your [Google Workspace or Cloud Identity audit logs](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging) to Cloud Logging by [enabling data sharing](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs#share_audit_logs).



## What's next

  * [Decide your resource hierarchy](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy) (next document in this series).
  * Find out more about [how users, Cloud Identity accounts, and Google Cloud organizations relate](https://docs.cloud.google.com/architecture/identity/overview-google-authentication).
  * Review recommended [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).
  * Read about [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-02 UTC."],[],[]] 
