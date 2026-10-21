---
url: https://docs.cloud.google.com/architecture/identity/removing-gmail-from-consumer-accounts/
title: Remove Gmail from consumer accounts \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:24.397720+00:00
---

# Remove Gmail from consumer accounts  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/removing-gmail-from-consumer-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Remove Gmail from consumer accounts Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

This document describes how you can remove Gmail from an existing consumer account to enable the user account [to be migrated](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts) to Cloud Identity or Google Workspace.

If your organization doesn't use [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://workspace.google.com/), it's possible that some of your employees have been using Gmail accounts to access Google services. Some of these Gmail accounts might use a corporate email address such as `alice@example.com` as an [alternate email address](https://support.google.com/accounts/answer/176347).

Gmail accounts are owned and managed by the individuals who created them. Your organization therefore has no control over the configuration, security, and lifecycle of these accounts, which means they can't be migrated as is. By removing Gmail from affected consumer accounts, you allow the user accounts to be migrated to Cloud Identity or Google Workspace.

Consider removing Gmail from an existing consumer account if both of the following conditions apply:

  * You want to migrate the user account to [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/) and retain the user's settings and data.
  * You don't use the email functionality provided by Gmail.

**Note:** Because a Gmail account is owned and managed by the individual who created it, the account's owner must perform the steps to remove Gmail.

If you want to retain Gmail functionality, or if you want to avoid engaging the owner of a Gmail account, consider [sanitizing the Gmail account](https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts) instead.

## Before you begin

To remove Gmail from a user account, at least one of the alternate email addresses of the Gmail account must correspond to one of the domains that you've added to your Cloud Identity or Google Workspace account. Both primary and secondary domains qualify, but alias domains are not supported.

**Note:** If you are considering using the [transfer tool for unmanaged users](https://admin.google.com/ac/unmanaged), keep in mind that the tool doesn't find Gmail users, regardless of the alternate email addresses they use.

The following sections walk through the process of removing Gmail from a consumer account. **The steps must be performed by the owner of the Gmail account.**

## Export Gmail data

Before you remove Gmail from your user account, you must export your existing Gmail data. You won't be able to access that data after you remove Gmail from the account. (Non-Gmail data is not affected.)

For information about how to export your Gmail data, see [Download your data](https://support.google.com/accounts/answer/3024190).

## Remove the Gmail service

  1. In the Google Account dashboard, open the **Data & personalization** page.

[Go to Data & personalization](https://myaccount.google.com/data-and-personalization)

  2. Under **Download or delete your data** , select **Delete a service**.

  3. Click **Delete a service**. You might be prompted to enter your password again.

  4. Click the _delete_ icon next to the service you want to delete.

  5. In the **How you'll sign in to Google** dialog, select your corporate email address and click **Next**.

  6. Carefully read the explanations on the next screen. If you're sure you want to proceed, select **Yes** and click **Delete Gmail**.




It might take a few days until your corporate email address becomes the primary email address of the user account and the Gmail data is deleted. Although you won't be able to receive or send email using your `@gmail.com` email address anymore, the address remains associated with your user account and you can continue to use it to sign in.

## Migrate the user account

When the removal process has completed and the user account has been updated to use your corporate email address as the primary email address, your administrator can migrate the user account to Cloud Identity or Google Workspace like other consumer accounts. For more information, see [Migrating consumer accounts](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts)

## Best practices for administrators

We recommend the following best practices for working with Gmail accounts:

  * Prevent other users from assigning a corporate email address to their Gmail accounts by [proactively provisioning user accounts to Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#prevent_new_consumer_account_sign-ups).
  * Prevent new Gmail accounts from being granted access to Google Cloud resources by using an organizational policy to [restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).
  * Prevent Gmail accounts from being given access to Google Marketing Platform by using a [policy that restricts sharing by domain](https://support.google.com/looker-studio/answer/9699595).



## What's next

  * Review how to [assess existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).
  * Learn how to [sanitize Gmail accounts](https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
