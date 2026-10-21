---
url: https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts/
title: Evict consumer accounts \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:10.000505+00:00
---

# Evict consumer accounts  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Evict consumer accounts Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

If you haven't been using [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/), it's possible that your organization's employees have been using consumer accounts to access Google services. Some of these consumer accounts might use a corporate email address such as `alice@example.com` as a primary or alternate email address.

This document describes how you can _evict_ , or get rid of, these types of consumer accounts by removing the corporate email address from them. Although the consumer accounts will still exist, removing the corporate email address helps you mitigate a social engineering risk—as long as a consumer account has a seemingly trustworthy email address like `alice@example.com`, the owner of the account might be able to convince current employees or business partners to grant them access to resources they shouldn't be allowed to access.

Alternatively, by [migrating consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts), you can keep these accounts and turn them into [managed accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account). But there might be some accounts that you don't want to migrate, such as the following:

  * Consumer accounts that are used by former employees.
  * Consumer accounts that are used by employees that are not supposed to access Google services.
  * Consumer accounts for which you cannot recognize the owner.



## Before you begin

To evict offending consumer accounts, you must satisfy the following prerequisites:

  * You have [identified a suitable onboarding plan](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans) and have completed all prerequisites for consolidating your existing user accounts.
  * You have created a [Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#cloud_identity_or_g_suite_account).



The primary or alternate email address of the consumer account must correspond to one of the domains that you have added to your Cloud Identity or Google Workspace account. Both primary and secondary domains qualify, but alias domains are not supported.

## Process

Evicting unwanted consumer accounts works similarly to [migrating consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts), but it is based on deliberately creating a conflicting account. The following diagram illustrates the process. Boxes on the **Administrator** side denote actions a Cloud Identity or Google Workspace administrator takes; rectangular boxes on the **User account owner** side denote actions only the owner of a consumer account can perform.

![Process for evicting unwanted consumer accounts.](https://docs.cloud.google.com/static/architecture/identity/images/eviction-process.svg)

#### Find unmanaged user accounts

You can use the [transfer tool for unmanaged users](https://admin.google.com/ac/unmanaged) to find consumer accounts that use a primary email address that matches one of the verified domains of your Cloud Identity or Google Workspace account.

#### Create a conflicting account

When you have identified a consumer account that you want to evict, do the following:

  1. Create a user account in Cloud Identity or Google Workspace that has the same corporate email address as the account you want to evict.

If the consumer account uses the corporate email address as the primary email address, the Admin Console warns you about an impending conflict. Because you are intentionally creating the conflicting account, select **Create new user**.

![Warning that user already exists.](https://docs.cloud.google.com/static/architecture/identity/images/user-already-exists.png)

Because you don't want the managed user account to ever be used, assign a random password.

  2. Delete the user account that you just created.




By creating a conflicting account and immediately deleting it, you force the owner to rename that user account. But you avoid that owner being shown a ballot screen that prompts them to choose between the managed and consumer account.

#### Rename the user account

For the owner of the evicted user account, the next time they sign in, they see the following message:

![Evicted owner sees the message that their account has changed.](https://docs.cloud.google.com/static/architecture/identity/images/account-has-changed.png)

As the screenshot suggests, they have three options for proceeding:

  * Convert the user account into a Gmail account.
  * Associate a different email address with the account.
  * Postpone the rename. This causes the user account to use a temporary `gtempaccount.com` email address in the meantime.



All configuration and data that was created by using this consumer account is unaffected by the rename.

## Best practices

We recommend the following best practices when you evict unwanted consumer accounts:

  * Ensure that affected users can no longer receive email on their (former) corporate email address. Otherwise, a user might be able to undo the rename and switch the primary email address back to the corporate email address.
  * Prevent other users from signing up for new consumer accounts by [proactively provisioning user accounts to Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).



## What's next

  * Review how you can [assess existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).
  * Learn how to [remove a corporate email address from a Gmail account](https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
