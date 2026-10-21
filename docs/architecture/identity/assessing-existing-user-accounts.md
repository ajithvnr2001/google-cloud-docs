---
url: https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts/
title: Assess existing user accounts \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:00.905872+00:00
---

# Assess existing user accounts  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Assess existing user accounts Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

Google supports these types of user accounts:

  * [Managed user accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account) are under the full control of a [Cloud Identity](https://docs.cloud.google.com/identity) or [Google Workspace](https://workspace.google.com/) administrator.
  * [Consumer accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#consumer_account) are fully owned and managed by the people who created them. In the context of Google Workspace, they are called _unmanaged personal accounts_.
  * [Unmanaged work accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#unmanaged_account) (unmanaged teams) are self-service business accounts that are created by employees who sign up for services like Google Workspace Essentials or Google Cloud.



A core tenet of identity management is to have a single place to manage identities across your organization:

  * If you [use Google as your identity provider (IdP)](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_google_as_idp), then Cloud Identity or Google Workspace should be the single place to manage identities. Employees should rely exclusively on user accounts that you manage in Cloud Identity or Google Workspace.

  * If you [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), then that provider should be the single place to manage identities. The external IdP needs to provision and manage user accounts in Cloud Identity or Google Workspace, and employees should rely exclusively on these managed user accounts when they use Google services.




If employees use consumer user accounts, then the premise of having a single place to manage identities is compromised: consumer accounts aren't managed by Cloud Identity, Google Workspace, or your external IdP. Therefore, you must identify the consumer user accounts that you want to convert to managed accounts, as explained in the [authentication overview](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#managed_user_account).

To convert consumer accounts to managed accounts using the transfer tool, described later in this document, you must have a Cloud Identity or Google Workspace identity with a Super Admin role.

This document helps you to understand and assess the following:

  * Which existing user accounts that your organization's employees might be using and how to identify those accounts.
  * Which risks might be associated with these existing user accounts.



## Example scenario

To illustrate the different sets of user accounts that employees might be using, this document uses an example scenario for a company named _Example Organization_. Example Organization has six employees and former employees who have all been using Google services such as Google Google Docs and Google Ads. Example Organization now intends to consolidate their identity management and establish their external IdP as the single place to manage identities. Each employee has an identity in the external IdP, and that identity matches the employee's email address.

There are two consumer user accounts, Carol and Chuck, that use an `example.com` email address:

  * Carol created a consumer account using her corporate email address (`carol@example.com`).
  * Chuck, a former employee, created a consumer account using his corporate email address (`chuck@example.com`).



Two employees, Glen and Grace, decided to use Gmail accounts:

  * Glen signed up for a Gmail account (`glen@gmail.com)`, which he uses to access private and corporate documents and other Google services.
  * Grace also uses a Gmail account (`grace@gmail.com`), but she added her corporate email address, `grace@example.com`, as an alternate email address.



Finally, two employees, Mary and Mike, are already using Cloud Identity:

  * Mary has a Cloud Identity user account (`mary@example.com`).
  * Mike is the administrator of the Cloud Identity account and created a user (`admin@example.com`) for himself.



The following diagram illustrates the different sets of user accounts:

![The sets of user accounts.](https://docs.cloud.google.com/static/architecture/identity/images/sets-of-user-accounts.svg)

To establish the external IdP as the single place to manage identities, you must link the identities of the existing Google user accounts to the identities in the external IdP. The following diagram therefore adds an account set that depicts the identities in the external IdP.

![User account set for identities in the external IdP.](https://docs.cloud.google.com/static/architecture/identity/images/account-set-for-external-idp.svg)

Recall that if employees want to establish an external IdP as the single place to manage identities, they must rely exclusively on managed user accounts, and that the external IdP must control those user accounts.

In this scenario, only Mary meets these requirements. She uses a Cloud Identity user, which is a managed user account, and her user account's identity matches her identity in the external IdP. All other employees either use consumer accounts, or the identity of their accounts doesn't match their identity in the external IdP. The risks and implications of not meeting the requirements are different for each of these users. Each user represents a different set of user accounts that might require further investigation.

## User account sets to investigate

The following sections examine potentially problematic sets of user accounts.

### Consumer accounts

This set of user accounts consists of accounts for which either of the following is true:

  * They were created by employees using the **Sign up** feature offered by many Google services.
  * They use a corporate email address as their identity.



In the example scenario, this description fits Carol and Chuck.

A consumer account that's used for business purposes and that uses a corporate email address can pose a risk to your business, such as the following:

  * You cannot control the lifecycle of the consumer account. An employee who leaves the company might continue to use the user account to access corporate resources or to generate corporate expenses.

Even if you revoke access to all resources, the account might still pose a social engineering risk. Because the user account uses a seemingly trustworthy identity like `chuck@example.com`, the former employee might be able to convince current employees or business partners to grant access to resources again.

Similarly, a former employee might use the user account to perform activities that aren't in line with your organization's policies, which could put your company's reputation at risk.

  * You cannot enforce security policies like MFA verification or password complexity rules on the account.

  * You cannot restrict which [geographic location Google Docs and Google Drive](https://support.google.com/a/answer/7630496) data is stored in, which might be a compliance risk.

  * You cannot restrict which Google services can be accessed by using this user account.




If ExampleOrganization decides to [use Google as their IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_google_as_idp), then the best way for them to deal with consumer accounts is to either [migrate them to Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts) or to [evict them](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts) by forcing the owners to rename the user account.

If ExampleOrganization decides to [use an external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), they need to further distinguish between the following:

  * Consumer accounts that have a matching identity in the external IdP.
  * Consumer accounts that don't have a matching identity in the external IdP.



The following two sections look at these two subclasses in detail.

#### Consumer accounts with a matching identity in the external IdP

This set of user accounts consists of accounts that match all of the following:

  * They were created by employees.
  * They use a corporate email address as the primary email address.
  * Their identity matches an identity in the external IdP.



In the example scenario, this description fits Carol.

![Accounts with a matching identity in the external IdP.](https://docs.cloud.google.com/static/architecture/identity/images/accounts-matching-ids-in-external-idp.svg)

The fact that these consumer accounts have a matching identity in your external IdP suggests that these user accounts belong to current employees and should be retained. You should therefore consider [migrating these accounts to Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts).

You can identify consumer accounts that have matching identity in the external IdP as follows:

  1. [Add and verify all domains](https://support.google.com/a/answer/7502379) to Cloud Identity or Google Workspace that you suspect might have been used for consumer account signups. In particular, the list of domains in Cloud Identity or Google Workspace should include all domains that your email system supports.
  2. In the Google Admin console, go to **Directory** > **Unmanaged users** : 
     * To identify consumer accounts and download a CSV report, select **Personal accounts**. For details, see [Transfer unmanaged personal accounts](https://knowledge.workspace.google.com/admin/users/find-and-add-unmanaged-users).
     * To identify unmanaged work accounts and teams, select **Work accounts**. For details, see [Transfer unmanaged work accounts](https://knowledge.workspace.google.com/p/unmanaged-work-accounts).
  3. To find consumer accounts that have a counterpart, compare the CSV report with the identities in your external IdP.



#### Consumer accounts without a matching identity in the external IdP

This set of user accounts consists of accounts that match all of the following:

  * They were created by employees.
  * They use a corporate email address as their identity.
  * Their identity does _not_ match any identity in the external IdP.



In the example scenario, this description fits Chuck.

![Accounts without a matching identity in the external IdP.](https://docs.cloud.google.com/static/architecture/identity/images/accounts-not-matching-ids-in-external-idp.svg)

There can be several causes for consumer accounts without a matching identity in the external IdP, including the following:

  * The employee who created the account might have left the company, so the corresponding identity no longer exists in the external IdP.
  * There might be a mismatch between the email address used for the consumer account sign-up and the identity known in the external IdP. Mismatches like these can occur if your email system allows variations in email addresses such as the following:

    * Using alternate domains. For example, `johndoe@example.org` and `johndoe@example.com` might be aliases for the same mailbox, but the user might only be known as `johndoe@example.com` in your IdP.
    * Using alternate handles. For example `johndoe@example.com` and `john.doe@example.com` might also refer to the same mailbox, but your IdP might recognize only one spelling.
    * Using different casing. For example, the variants `johndoe@example.com` and `JohnDoe@example.com` might not be recognized as the same user.



You can handle consumer accounts that don't have a matching identity in the external IdP in the following ways:

  * You can [migrate the consumer account to Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts) and then [reconcile](https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts) any mismatches caused by alternate domains, handles, or casing.

  * If you think the user account is illegitimate or shouldn't be used anymore, you can [evict the consumer account](https://docs.cloud.google.com/architecture/identity/evicting-consumer-accounts) by forcing the owner to rename it.




You can identify consumer accounts without a matching identity in the external IdP as follows:

  1. [Add and verify all domains](https://support.google.com/a/answer/7502379) to Cloud Identity or Google Workspace that you suspect might have been used for consumer account signups. In particular, the list of domains in Cloud Identity or Google Workspace should include all domains that your email system supports as aliases.
  2. In the Google Admin console, go to **Directory** > **Unmanaged users** : 
     * To identify consumer accounts and download a CSV report, select **Personal accounts**. For details, see [Transfer unmanaged personal accounts](https://knowledge.workspace.google.com/admin/users/find-and-add-unmanaged-users).
     * To identify unmanaged work accounts and teams, select **Work accounts** For details, see [Transfer unmanaged work accounts](https://knowledge.workspace.google.com/p/unmanaged-work-accounts).
  3. To find consumer accounts that lack a counterpart, compare the CSV report with the identities in your external IdP.



### Managed accounts without a matching identity in the external IdP

This set of user accounts consists of accounts that match all of the following:

  * They were manually created by a Cloud Identity or Google Workspace administrator.
  * Their identity doesn't match any identity in the external IdP.



In the example scenario, this description fits Mike, who used the identity `admin@example.com` for his managed account.

![Manually created accounts whose identity doesn't match any identity in the external IdP.](https://docs.cloud.google.com/static/architecture/identity/images/manually-created-accounts-not-matching-ids-in-idp.svg)

The potential causes for managed accounts without a matching identity in the external IdP are similar to those for consumer accounts without a matching identity in the external IdP:

  * The employee for whom the account was created might have left the company, so the corresponding identity no longer exists in the external IdP.
  * The corporate email address that matches the identity in the external IdP might have been [set as an alternate email address](https://support.google.com/accounts/answer/176347/) or alias rather than as the primary email address.
  * The email address that's used for the user account in Cloud Identity or Google Workspace might not match the identity known in the external IdP. Neither Cloud Identity nor Google Workspace verifies that the email address used as the identity exists. A mismatch can therefore not only occur because of alternate domains, alternate handles, or different casing, but also because of a typo or other human error.



Regardless of their cause, managed accounts without a matching identity in the external IdP are a risk because they can become subject to [inadvertent reuse and name squatting](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#make_cloud_identity_or_g_suite_identities_a_subset_of_the_identities). We recommend that you [reconcile these accounts](https://docs.cloud.google.com/architecture/identity/reconciling-orphaned-managed-user-accounts).

You can identify consumer accounts without a matching identity in the external IdP as follows:

  1. Using the [Admin Console](https://workspace.google.com/dashboard) or the [Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/users/list), export the list of user accounts in Cloud Identity or Google Workspace.
  2. Compare the list of accounts with the identities in your external IdP and find accounts that lack a counterpart.



### Gmail accounts used for corporate purposes

This set of user accounts consists of accounts that match the following:

  * They were created by employees.
  * They use a `gmail.com` email address as their identity.
  * Their identities don't match any identity in the external IdP.



In the example scenario, this description fits Grace and Glen.

![Employee-created Gmail accounts whose identities don't match any identity in the external IdP.](https://docs.cloud.google.com/static/architecture/identity/images/employee-gmail-accounts-not-matching-ids-in-external-idp.svg)

Gmail accounts that are used for corporate purposes are subject to similar risks as consumer accounts without matching identity in external IdP:

  * You cannot control the lifecycle of the consumer account. An employee who leaves the company might continue to use the user account to access corporate resources or to generate corporate expenses.
  * You cannot enforce security policies like MFA verification or password complexity rules on the account.



The best way to deal with Gmail accounts is therefore to revoke access for those user accounts to all corporate resources and provide affected employees with new managed user accounts as replacements.

Because Gmail accounts use `gmail.com` as their domain, there is no clear affiliation with your organization. The lack of a clear affiliation implies that there is no systematic way—other than scrubbing existing access control policies—to identify Gmail accounts that have been used for corporate purposes.

### Gmail accounts with a corporate email address as alternate email

This set of user accounts consists of accounts that match all of the following:

  * They were created by employees.
  * They use a `gmail.com` email address as their identity.
  * They use a corporate email address [as an alternate email address](https://support.google.com/accounts/answer/176347/).
  * Their identities don't match any identity in the external IdP.



In the example scenario, this description fits Grace.

![Gmail accounts with a corporate email address as alternate email.](https://docs.cloud.google.com/static/architecture/identity/images/gmail-accounts-with-corporate-address-as-alternate.svg)

From a risk perspective, Gmail accounts that use a corporate email address as an alternate email address are equivalent to consumer accounts without a matching identity in the external IdP. Because these accounts use a seemingly trustworthy corporate email address as their second identity, they are subject to the risk of social engineering.

If you want to maintain the access rights and some of the data associated with the Gmail account, you can ask the owner [to remove Gmail from the user account](https://docs.cloud.google.com/architecture/identity/removing-gmail-from-consumer-accounts) so that you can then [migrate them to Cloud Identity or Google Workspace](https://docs.cloud.google.com/architecture/identity/migrating-consumer-accounts).

The best way to handle Gmail accounts that use a corporate email address as an alternate email address is to [sanitize them](https://docs.cloud.google.com/architecture/identity/sanitizing-gmail-accounts). When you sanitize an account, you force the owner to give up the corporate email address by creating a managed user account with that same corporate email address. Additionally, we recommend that you revoke access to all corporate resources and provide the affected employees with the new managed user accounts as replacements.

## What's next

  * Learn more about [the different types of user accounts on Google Cloud](https://docs.cloud.google.com/architecture/identity/overview-google-authentication).
  * Review [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * For Google Workspace and Cloud Identity administrators: 
    * Review [Resolve duplicate account errors](https://knowledge.workspace.google.com/p/duplicate-account-errors).
    * Learn how to [Transfer unmanaged personal accounts](https://knowledge.workspace.google.com/admin/users/find-and-add-unmanaged-users).
    * Learn how to [Transfer unmanaged work accounts](https://knowledge.workspace.google.com/p/unmanaged-work-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
