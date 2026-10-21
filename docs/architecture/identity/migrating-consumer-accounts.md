---
url: https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts/
title: Migrate consumer accounts \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:03.341290+00:00
---

# Migrate consumer accounts  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate consumer accounts Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

This document describes how you can migrate [consumer accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account) to [managed user accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account) controlled by [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://gsuite.google.com/).

If your organization hasn't used Cloud Identity or Google Workspace before, it's possible that some of your employees are using consumer accounts to access Google services. Some of these consumer accounts might use a corporate email address such as `alice@example.com` as their primary email address.

Consumer accounts are owned and managed by the individuals who created them. Your organization therefore [has no control over the configuration, security, and lifecycle of these accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts#consumer_accounts).

## Before you begin

To migrate consumer accounts to Cloud Identity or Google Workspace, you must meet the following prerequisites:

  * You have [identified a suitable onboarding plan](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans) and have completed all prerequisites for consolidating your existing user accounts.
  * You have created a [Cloud Identity or Google Workspace account](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#cloud_identity_or_g_suite_account) and have [prepared the default organization unit (OU)](https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account) to grant appropriate access to migrated user accounts.



Each consumer account that you plan to migrate must meet the following criteria:

  * It can't be a Gmail account.
  * It must use a primary email address that corresponds to the primary or a secondary domain of your Cloud Identity or Google Workspace account. In the context of a consumer account migration, alternate email addresses and alias domains are ignored.
  * Its owner must be able to receive email on the account's primary email address.



Converting a consumer account to a managed account implies that the user who registered the consumer account passes control of the account and its associated data to your organization. Your organization might require employees to sign and adhere to an acceptable-email-use policy that disallows the use of corporate email addresses for private purposes. In this case, you can safely assume that the consumer account has been used only for business purposes. However, if your organization doesn't have such a policy or the policy allows certain personal use, the consumer account might be associated with a mixture of corporate and personal data. Given this uncertainty, you can't force the migration of a consumer account to a managed account—a migration therefore always requires the user's consent.

## Process

Migrating consumer accounts to managed accounts is a multi-step process that you must plan carefully. The following sections walk you through the process.

### Process overview

The goal of migrating is to convert a consumer account into a managed user account while maintaining both the identity of the account as reflected by its email address, and any data associated with the account.

During a migration like this, an account can be in one of four states, as the following state machine diagram shows.

![The four states of account migration.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-1-state-machine.svg)

When you add and verify a domain in Cloud Identity or Google Workspace, any consumer account that uses an email address with this domain becomes an _unmanaged account_. For the user, this has no impact; they can sign in and access their data as normal.

Adding a domain in Google Workspace or Cloud Identity affects only users whose email address matches this exact domain. For example, if you add `example.com`, the account `johndoe@example.com` is identified as an unmanaged account, while `johndoe@corp.example.com` is not unless you also add `corp.example.com` to the Cloud Identity or Google Workspace account.

The existence of unmanaged accounts is surfaced to you as the Cloud Identity or Google Workspace administrator. You can then ask the user to _transfer_ their account into a managed account.

![Transferring unmanaged accounts into managed accounts.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-3-transfer-account.svg)

In the preceding diagram, if the user `johndoe` consents to a transfer, the unmanaged account is converted to a managed account. The identity remains the same, but now Cloud Identity or Google Workspace controls the account, including all of its data.

![Control of a managed account passes to Cloud Identity or Google Workspace.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-4-convert-account.svg)

If the user `johndoe` doesn't consent to a data transfer, but you create an account in Cloud Identity or Google Workspace using the same email address, the result is a _conflicting account._ A conflicting account is actually two accounts—one consumer, one managed—that are associated with the same identity, as in the following diagram.

![A conflicting account with one consumer account and one managed account.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-5-conflicting-account.svg)

A user who signs in by using a conflicting account sees a screen prompting them to select either the managed account or the consumer account to resume the sign-on process.

**Important:** In the presence of a conflicting account, only the consumer account still has access to the original data, while only the managed account is under the control of your organization. The result reflects that the user never consented to transferring the data—however, it likely doesn't reflect the intent of your migration.

To avoid ending up with conflicting accounts, it's helpful to understand account states in more detail.

### Process in detail

The following state machine diagram illustrates account states in more detail. Rectangular boxes on the left denote actions a Cloud Identity or Google Workspace administrator can take; rectangular boxes on the right denote the activities only the owner of a consumer account can perform.

![State machine diagram of account states.](https://docs.cloud.google.com/static/architecture/identity/images/migration-process.png)

#### Find unmanaged user accounts

When signing up for Cloud Identity or Google Workspace, you must provide a domain name, which you're then asked to [verify ownership for](https://support.google.com/cloudidentity/answer/7331243). When you've completed the sign-up process, you can add and verify [secondary domains](https://support.google.com/a/answer/7502379).

By verifying a domain, you automatically initiate a search for consumer accounts that use this domain in their email address. Within about 12 hours, these accounts will be surfaced as unmanaged user accounts in the [transfer tool for unmanaged users](https://admin.google.com/ac/unmanaged).

The search for consumer accounts considers the primary domain registered in Cloud Identity or Google Workspace as well as any secondary domain that has been verified. The search tries to match these domains to the primary email address of any consumer accounts. In contrast, alias domains registered in Cloud Identity or Google Workspace as well as alternate email addresses of consumer accounts [aren't considered](https://support.google.com/a/answer/6178640?ref_topic=7042002).

Users of affected consumer accounts aren't made aware that you verified a domain or that you identified their account as an unmanaged account. They can continue to use their accounts as normal.

#### Initiate a transfer

In addition to showing you all unmanaged accounts, the [transfer tool for unmanaged users](https://admin.google.com/ac/unmanaged) lets you initiate an account transfer by sending an account transfer request. Initially, an account is listed as **Not yet invited** , indicating that no transfer request has been sent.

![Account listed as 'Not sent'.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-7-not-sent.png)

If you select a user and send an account transfer request, the user receives an email similar to the following. Meanwhile, the account switches to being listed as **Invited**.

![Account listed as 'Request Sent'.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-8-request-sent.png)

#### Accept or ignore a transfer

Having received the transfer request, an affected user might simply ignore it and continue to use the account as normal. In this case, you can send another request, repeating the procedure.

Until the user accepts the transfer request, the functionality of the unmanaged account is unimpaired—users are able to sign in and access their data. However, the process of migrating account data to Google Workspace or Cloud Identity is impeded as long as a user keeps ignoring a transfer request. To prevent this from happening, make sure that you communicate your migration plan to employees before you send the first transfer requests. Also make sure that employees are fully aware of the reasons and consequences of accepting or ignoring a transfer request.

Rather than ignoring the request, a user might also change the email address of the account. If the user changes the primary email address to use a domain that hasn't been verified by any Cloud Identity or Google Workspace account, this causes the account to become a consumer account again. Although the transfer tool might still temporarily list the user as an unmanaged account, you can no longer initiate an account transfer for such a renamed account.

#### Create a conflicting account

If at any point you create a user account in Cloud Identity or Google Workspace with the same email address as an unmanaged user account, the Admin Console warns you about an impending conflict:

![Creating a conflicting account.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-9-impending-conflict.png)

If you ignore this warning and create a user account anyway, this new account, together with the unmanaged account, becomes a _conflicting account_. Creating a conflicting account is useful if you want to [evict an unwanted consumer account](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts), but it's better to avoid it if your goal is to migrate a consumer account to Cloud Identity or Google Workspace.

Creating a conflicting account can happen unintentionally. After signing up for Cloud Identity or Google Workspace, you might decide to set up single sign-on with an external identity provider (IdP) such as Microsoft Entra ID (formerly Azure Active Directory) or Active Directory. When configured, the external IdP might automatically create accounts in Cloud Identity or Google Workspace for all users that you enabled single sign-on for, inadvertently creating conflicting accounts.

#### Use a conflicting account

Each time the user signs in using a conflicting account, they see a ballot screen like the following.

![Ballot screen that appears when a user tries to sign in to conflicting account.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-10-ballot-screen.png)

When they select the first option, the sign-in process continues using the managed part of the conflicting account. They are asked to provide the password that you set for the managed account, or if you configured single sign-on, they are redirected to an external IdP to authenticate. After they are authenticated, they can use the account like any other managed account—however, because none of the data has been transferred from the original consumer account, it's effectively a new account.

When choosing the second option in the ballot screen, the user is prompted to change the email address of the consumer part of the conflicting account.

![Prompt to change the consumer part of the conflicting account.](https://docs.cloud.google.com/static/architecture/identity/images/migrating-consumer-accounts-11-email-prompt.png)

By changing the email address, the user resolves the conflict by ensuring that the managed account and consumer account have different identities again. The result remains that they have one consumer account that has all their original data, and one managed account that doesn't have access to the original data.

The user can postpone renaming the account by clicking **Do this later**. This action turns the account into an _Evicted_ state. In this state, the user sees the same ballot screen every time they sign in, and the account is assigned a temporary `gtempaccount.com` email address until renamed.

Another way to resolve the conflict is to delete the managed account in Cloud Identity or Google Workspace, or if they use single sign-on, in the external IdP. This causes the ballot screen to not be shown the next time they sign in using the account, but the user still needs to change the email address of the account.

If the user changes the email address to a private email address, the account remains a consumer account. If the user decides to change the email address back to the original corporate email address, the account becomes an unmanaged account again.

#### Complete a transfer

If a user accepts the transfer, the account is surfaced in Cloud Identity or Google Workspace. The account is now considered a managed account, and all data associated with the original consumer account is transferred to the managed account.

If Cloud Identity or Google Workspace is not set up to use an external IdP for single sign-on, the user can sign in using their original password and continue to use the account as normal.

If you do use single sign-on, the user won't be able to sign in with their existing password anymore. Instead, they're sent to the sign-in page of your external IdP when attempting to sign in. For this to succeed, the external IdP must recognize the user and permit single sign-on. Otherwise, the account becomes locked out.

## Best practices

If you intend to migrate existing consumer accounts to either Cloud Identity or Google Workspace, plan and coordinate the migration steps in advance. Good planning avoids disrupting your users and minimizes the risk of inadvertently creating conflicting accounts.

Consider the following best practices when planning a consumer account migration:

  * If you [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), make sure that you configure user account provisioning and single sign-on in a way that does not impede consumer account migration.
  * Inform affected users ahead of a migration. Migrating consumer accounts to managed accounts requires users' consent and might also affect them personally if they have used accounts for private purposes. Therefore, it's crucial that you inform affected users about your migration plans.

Convey the following information to users before starting the migration:

    * Rationale and importance of the account migration.
    * Impact on personal data associated with existing accounts.
    * Timeframe in which users can expect to receive a transfer request.
    * Time window in which you expect users to approve a transfer.
    * Upcoming changes to the sign-in process after migration (only applies when using federation).
    * Instructions on how to transfer ownership of private Google Docs files to a personal account.

If you announce the migration by email, some users might assume it's a phishing attempt. To prevent this from happening, consider announcing the migration through a different medium as well.

For an example of an announcement email, see [Advance communication for user account migration](https://docs.cloud.google.com/architecture/identity/example-announcement).

  * [Initiate transfers in batches](https://support.google.com/a/answer/7044710). Begin with a small batch of approximately 10 users, and grow your batch size as you go.

  * Allow sufficient time for affected users to react to transfer requests. Keep in mind that some employees might be on vacation or parental leave and won't be able to react quickly.

  * Make sure that by consenting to a transfer, users don't lose access to data or Google services that they need.




## What's next

  * Review how you can [assess existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).
  * Learn how to [evict unwanted consumer accounts](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
