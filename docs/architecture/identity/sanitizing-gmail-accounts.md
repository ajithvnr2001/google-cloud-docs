---
url: https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts/
title: Sanitize Gmail accounts \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:20.973400+00:00
---

# Sanitize Gmail accounts  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Sanitize Gmail accounts Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

This document describes how to _sanitize_ existing Gmail accounts by deliberately removing any corporate email addresses from them. If your company hasn't been using [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/), it's possible that some of your employees have been using Gmail accounts to access Google services. Some of these Gmail accounts might use a corporate email address such as `alice@example.com` as an [alternate email address](https://support.google.com/accounts/answer/176347).

Consider sanitizing a Gmail account if either of the following conditions is true:

  * You want the owner of the Gmail account to switch to a [managed user account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account).
  * You want the Gmail account to stop using a corporate email address as an alternate address. This might be because the account belongs to a former employee or because you don't recognize the owner of the account.



Removing the corporate email address from a Gmail account can mitigate a social engineering risk: if a Gmail account uses a seemingly trustworthy email address like `alice@example.com` as an alternate address, then the owner of the account might be able to convince employees or business partners to grant them access to resources they shouldn't be allowed to access.

## Before you begin

To sanitize a Gmail account, you must meet all of the following prerequisites:

  * You have [identified a suitable onboarding plan](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans) and have completed all activities that your plan defines as prerequisites for consolidating your existing user accounts.
  * You have created a [Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#cloud_identity_or_g_suite_account).



Each Gmail account that you plan to sanitize must meet the following criteria:

  * One of the [alternate email addresses](https://support.google.com/accounts/answer/176347) of the Gmail account corresponds to one of the domains that you've added to your Cloud Identity or Google Workspace account. Both primary and secondary domains qualify, but alias domains are not supported.

**Note:** The [transfer tool for unmanaged users](https://admin.google.com/ac/unmanaged) doesn't find Gmail users, regardless of the alternate email addresses they use.

## Process

Sanitizing Gmail accounts works like [migrating consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts), but it is based on the idea that you deliberately create a conflicting account.

The following diagram illustrates the process. Rectangular boxes on the **Administrator** side denote actions that a Cloud Identity or Google Workspace administrator takes; rectangular boxes on the **User account owner** side denote actions that only the owner of a consumer account can perform.

![The sanitizing process.](https://docs.cloud.google.com/static/architecture/identity/images/sanitizing-process.svg)

The sequence of steps differs slightly depending on whether you want the owner of the Gmail account to switch to a managed user account or whether you simply want the account to give up its corporate email address.

### Encourage a switch to a managed account

If you want a user to switch to a managed account, create a user account for that user in Cloud Identity or Google Workspace. For the primary email address, use the email address that's used as an alternate email address by the Gmail account. For example, if the Gmail user `bob@gmail.com` has specified `bob@example.com` as an alternate email address, use `bob@example.com` as the primary email address for the Cloud Identity or Google Workspace user.

The owner of the affected account has two ways to sign in—by using the Gmail address or by using the corporate email address. If the owner signs in by using the Gmail address, they see the following message, indicating that the corporate email address has been disassociated from the user account:

![Message that your account has changed.](https://docs.cloud.google.com/static/architecture/identity/images/sanitizing-your-account-has-changed.png)

The account owner sees this message only once. If the owner instead signs in by using the corporate email address, they see a ballot screen:

![Ballot screen.](https://docs.cloud.google.com/static/architecture/identity/images/ballot-screen.png)

If they select **Organizational Google Workspace account** , they must authenticate using the credentials of the newly created user account in Cloud Identity or Google Workspace. If they use [an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), this process involves single sign-on. Because the user account in Cloud Identity or Google Workspace is new, none of the Gmail account's data is transferred.

If they select **Individual Google account** , they continue with their Gmail account, but they see the following message indicating that the corporate email address is being disassociated from the user account:

![Address gets disassociated.](https://docs.cloud.google.com/static/architecture/identity/images/primary-address.png)

After confirming, they are shown another message:

![Message showing that the primary address has changed.](https://docs.cloud.google.com/static/architecture/identity/images/primary-address-has-changed.png)

### Force an account to give up its corporate email address

You can force an account to give up its corporate email address as follows:

  1. Create a user account in Cloud Identity or Google Workspace that has the corresponding corporate email address. Because you don't want the managed user account to ever be used, assign a random password.
  2. Delete the user account that you just created.



By creating a conflicting account and immediately deleting the managed account, you leave the consumer account in a state where the owner has to rename the account.

The owner of the affected account has two ways to sign in—by using the Gmail address or by using the corporate email address:

  * If the owner signs in by using the Gmail address, they see the following message, indicating that the corporate email address has been disassociated from the user account:

![Corporate email address has been disassociated from the user account.](https://docs.cloud.google.com/static/architecture/identity/images/disassociated-address.png)

  * If they instead sign in by using the corporate email address, they see the following message:

![Message after signing in with corporate email address.](https://docs.cloud.google.com/static/architecture/identity/images/alternate-address.png)

After confirming, they are shown another message:

![New primary address.](https://docs.cloud.google.com/static/architecture/identity/images/account-changes-again.png)

All configuration and data that was created by using this consumer account is unaffected by the renaming process. But for subsequent attempts to sign in, the user must use the Gmail address because the corporate address is no longer associated with the user account.




## Best practices

We recommend the following best practices when you are sanitizing Gmail accounts:

  * Prevent other users from assigning a corporate email address to their Gmail accounts by [proactively provisioning user accounts to Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Prevent new Gmail accounts from being granted access to Google Cloud resources by using an organizational policy to [restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).

  * Prevent Gmail accounts from being given access to Google Marketing Platform by using a [policy that restricts sharing by domain](https://support.google.com/marketingplatform/answer/9014058).




## What's next

  * Review how you can [assess existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).
  * Learn how to [evict unwanted consumer accounts](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
