---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/duplicate-accounts-troubleshooting/
title: Troubleshooting duplicate accounts on email change \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:14:26.030236+00:00
---

# Troubleshooting duplicate accounts on email change  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/duplicate-accounts-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting duplicate accounts on email change Stay organized with collections  Save and categorize content based on your preferences. 

This guide helps you troubleshoot and resolve duplicate user accounts that Looker creates when an existing user's primary email address changes in your Identity Provider (IdP), such as Azure Active Directory (Azure AD).

Before you begin troubleshooting, you must determine whether your instance is a Looker (original) instance (hosted or self-hosted) or a Looker (Google Cloud core) instance, because they support different user merging options:

  * **Looker (original)** : Supports local email and password credentials. This option lets you merge users by email matching when unique IdP identifiers change.
  * **Looker (Google Cloud core)** : Doesn't support local email and password login or email credentials. Because of this, you cannot merge users by using the email and password credentials option in Looker (Google Cloud core).



## Looker (original) instances

Use the following decision tree to troubleshoot email changes on Looker (original) instances:

The following sections describe the scenarios in the tree in further detail.

### Configure identity provider settings

To prevent duplicate accounts when users' email addresses change, you can configure your IdP to assert an immutable unique identifier:

  1. In your IdP (such as Azure AD), find the unique identifier mapping settings (for example, the **Unique User Identifier (Name ID)** attribute for SAML or the `sub` claim for OIDC).
  2. Configure this attribute to map to an immutable user attribute (such as an employee ID or a database UUID) instead of a mutable email address.
  3. Save the configurations. Because the unique identifier remains constant when the email address changes, Looker recognizes the existing user and updates their email automatically on their next sign-in without creating a duplicate account.



### Prevent duplicates

If you use a mutable email address as the unique identifier on Looker (original), and you cannot change it to an immutable attribute, you must follow these steps to configure Looker to merge users based on email matching:

  1. In the Looker Admin panel, go to **Admin > SAML** or **Admin > OpenID Connect**.
  2. Go to the **Merge Users Using** option and select the box for **Looker Email/Password**.
  3. Before the user signs in with their new email address, you must create a Looker email credential on their existing user account that matches the new email address. Use the Looker API endpoint `create_user_credentials_email`: `POST /api/4.0/users/<var>USER_ID</var>/credentials_email` Specify the new email address in the request body.
  4. Have the user sign in. Looker will match the new email declared by the IdP with the pre-created email credential and merge their accounts.



### Clean up duplicates

If the email address has already changed and duplicate user accounts exist, follow these steps to clean up and merge the accounts:

  1. In the Looker Admin panel, go to **Admin > Users** and identify the user's original account and the duplicate account.
  2. Determine if the duplicate account has user-generated content or schedules that you need to retain. If so, follow the steps in the Migrate duplicate content section.
  3. In the Looker SAML or OIDC settings, verify that **Merge Users Using** has **Looker Email/Password** enabled.
  4. Delete the duplicate user account.
  5. In the Looker API, create a Looker email credential on the original user account that uses the new email address: `POST /api/4.0/users/<var>USER_ID</var>/credentials_email`
  6. Instruct the user to sign in using SAML or OIDC. Looker will merge their login credentials into the original user account.



### Migrate duplicate content

If the duplicate account contains user-generated content, personal folder items, Looks, dashboards, or schedules, you can migrate these to the original account before deleting the duplicate:

  1. Use the Looker API to retrieve the list of content and schedules that's associated with the duplicate user ID.
  2. Call the update endpoints (such as `update_dashboard`, `update_look`, or `update_schedule_plan`) to change the owner of these resources to the original user ID.
  3. Alternatively, you can use tools like the Looker open-source Admin Power Pack to perform bulk migrations of user content.
  4. Once you transfer the content, proceed with deleting the duplicate user account.



## Looker (Google Cloud core) instances

Looker (Google Cloud core) doesn't support email credentials or email and password merging. Use the following decision tree to handle email changes on Looker (Google Cloud core):

The following sections describe the scenarios in the tree in further detail.

### Pre-migration steps

If you're preparing to migrate from a Looker (original) instance to Looker (Google Cloud core), you must follow these steps to convert users to a Core-supported authentication method (such as Google OAuth) first:

  1. Enable Google OAuth on your Looker (original) instance.
  2. Enable **Merge Users Using** with **Looker Email/Password** enabled under the Google OAuth settings.
  3. Instruct all users to sign in using Google OAuth on the Looker (original) instance to merge their accounts before the migration.
  4. Perform the migration to Looker (Google Cloud core).



### Post-migration steps

If the migration to Looker (Google Cloud core) has completed and duplicate accounts still exist, perform one of the following tasks:

  * **If the Looker (original) instance is still accessible** : Contact Google Cloud Support to restore the instance, perform the Google OAuth merge steps on the original instance, and then re-perform the migration to Looker (Google Cloud core).
  * **If the Looker (original) instance isn't accessible** : You must manually migrate user-generated content by using Looker API scripts from the users' old accounts to their new accounts, and then delete the old or duplicate accounts.



## Final review and support

If you're still unable to resolve the duplicate accounts issue, [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
