---
url: https://docs.cloud.google.com/identity/docs/how-to/create-cloud-identity-user-accounts/
title: Create Cloud Identity user accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:43.370250+00:00
---

# Create Cloud Identity user accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/create-cloud-identity-user-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create Cloud Identity user accounts

Before you can manage users in Cloud Identity, you must create accounts for each user to be managed by Cloud Identity. An account provides users with a name and password for signing in to their Google services. Optionally, you can add more information to your users' profiles.

## Create one or more user accounts

  * [Add users individually](https://support.google.com/a/answer/33310) using your Google Admin console. ![alt
text](https://www.google.com/images/icons/feature/checkmark-lb16.png)**Easiest**
  * [Add several users at once](https://support.google.com/a/answer/40057) by uploading their names in a CSV file.



## Options for large organizations

  * Use [Google Cloud Directory Sync](https://support.google.com/a/answer/106368) to synchronize user data in your existing LDAP directory with your Google Account (syncs groups, contacts, and organizations, too).
  * Use the [Admin SDK Directory API](https://developers.google.com/admin-sdk/directory/) to provision a large number of users with data from your existing LDAP directory, such as Microsoft® Active Directory®. This API provides more flexibility than GCDS, but requires programming.



## Guidelines when creating accounts

**Important** : We recommend that you review and resolve any potential [conflicting accounts](https://knowledge.workspace.google.com/p/duplicate-account-errors) before you add users to your organization's new Cloud Identity account.

Other guidelines:

  * Each account's username becomes that person's login name and the first part of their email address. If your domain is **solarmora.com** , a user whose email is **jsmith@solarmora.com** has the username **jsmith**. If your organization's Cloud Identity account has multiple domain names associated with it, you specify which domain name to use when you create the Cloud Identity user account.
  * It can take up to 24 hours for a new user account to appear in the [searchable Directory](https://support.google.com/a/answer/1628008).



See also: [Name and password guidelines](https://support.google.com/a/answer/9193374).

## Do your users have existing Google Accounts?

If a user created a personal or unmanaged work Google Account using their work email address, it might result in an [account conflict](https://support.google.com/a/answer/7062710). If you create user accounts with the same username as existing personal or unmanaged work Google Accounts, then add them to your organization, they'll have the same address for their personal and Cloud Identity accounts. Two accounts can't share the same username.

For guidance on resolving conflicts and transferring accounts, see [Resolve duplicate account errors](https://knowledge.workspace.google.com/p/duplicate-account-errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
