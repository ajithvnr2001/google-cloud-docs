---
url: https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts/
title: Overview of consolidating accounts \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:07.150251+00:00
---

# Overview of consolidating accounts  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Overview of consolidating accounts Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

If your organization isn't already using [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/), some of your employees might be using [consumer accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account) to access Google services. A consumer account is owned and managed by the individual who created the account. Your organization therefore [has no control](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts#consumer_accounts) over the configuration, security, and lifecycle of these consumer accounts.

This document describes how to consolidate existing consumer accounts so that you achieve the following results:

  * Only [managed user accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account) are used to access Google services.
  * Your organization has full control over the configuration, security, and lifecycle of user accounts.
  * If you [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), all user accounts have a matching identity in your external identity provider (IdP) and can be used for single sign-on.



## Before you begin

Before you consolidate your consumer accounts, make sure that you [identify a suitable onboarding plan](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans) and complete the prerequisites for consolidating your existing user accounts.

When you consolidate existing user accounts, you might need to collaborate between multiple teams and stakeholders in your organization, including the following:

  * Administrators of your external IdP, if you use one.
  * Administrators of your email system.
  * Users responsible for managing access to Google services used in your organization, such as Google Marketing Platform, Google Ads, or Google Play.



If you use [separate Cloud Identity or Google Workspace organizations for staging and production](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning#use_a_separate_staging_organization), we recommend that you perform a test run of the consolidation process first:

  * For each class of existing consumer accounts that you need to consolidate, create a test user account that uses a similar configuration. When you assign email addresses to these test user accounts, choose email addresses that match one of the domains of your staging account.
  * Perform the consolidation process by using the test user accounts and your staging Google Workspace or Cloud Identity account.



Performing a test run lets you familiarize yourself with the process before you apply it in your production environment. It also helps you identify potential issues before you apply them to thousands of users.

## Consolidation process

The consolidation process consists of the following streams:

  * Migrating consumer accounts to Cloud Identity or Google Workspace.
  * Evicting consumer accounts that you don't want to keep.
  * Identifying and removing access for Gmail accounts.
  * Sanitizing Gmail accounts that use a corporate email address as an alternate address.



Depending on the sets of existing accounts that [you have identified](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts), some of these streams might not apply to you.

The following flow chart illustrates the consolidation process. The streams, indicated by parallel lines, are independent of one another so you can do them in parallel.

![Consolidation process showing different streams of migration.](https://docs.cloud.google.com/static/architecture/identity/images/consolidation-process.svg)

The diagram shows this flow:

  1. Identify a set of consumer accounts to migrate. If you have a large number of consumer accounts, it's best to do the migration in batches. Start with a small batch of approximately 10 users, and then make your batches larger in subsequent migrations.
  2. Announce to affected users your intent to transfer consumer accounts. Make sure that users understand both the importance and consequences of accepting or declining a transfer request.

For an example of what an announcement email message might look like, see [Advance communication for user account migration](https://docs.cloud.google.com/architecture/identity/example-announcement).

  3. Migrate the selected consumer accounts by using the [transfer tool for unmanaged users](https://admin.google.com/ac/unmanaged). This process is described in more detail in [Migrating consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts).

  4. Wait for most of the users (a _quorum_) to accept or decline transfer requests, and resend transfer requests if necessary. You can see a user has responded by looking at the [transfer tool for unmanaged users](https://admin.google.com/ac/unmanaged).

  5. If you're using an external IdP, some of the migrated user accounts might end up without a matching identity in the external IdP. [Reconcile these orphaned managed user accounts](https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts) to ensure that all managed user accounts have a matching identity in the external IdP.

  6. [Evict all consumer accounts](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts) that you don't want to migrate.

  7. Search your [Identity and Access Management (IAM) policies](https://docs.cloud.google.com/iam/docs/overview#cloud-iam-policy) for Gmail accounts (search for `*@gmail.com` entries). Revoke access to these accounts and provide affected users with managed user accounts as replacements. In order to minimize impact on users, make sure that these managed user accounts have the same or similar access to resources as previous Gmail accounts.

  8. If there are Gmail accounts that use a corporate email address as their alternate email address, [sanitize these Gmail accounts](https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts).




## Best practices

We recommend the following best practices when you are consolidating existing user accounts:

  * If you are migrating from an external email system to Google Workspace, remember that consumer accounts might use an email address that is also subject to migration. To ensure that the owners of these consumer accounts continue to receive email, don't change [DNS MX records](https://support.google.com/a/answer/174125) until after you migrate all affected consumer accounts.
  * After you complete the consolidation, consider [provisioning all users and limiting authentication by single sign-on](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating) to block new consumer account sign-ups.



## What's next

  * Find out how to [migrate consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts) and how to [evict unwanted consumer accounts](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts).
  * Learn how you can [sanitize Gmail accounts](https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts).
  * See how to [reconcile orphaned managed user accounts](https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
