---
url: https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account/
title: Prepare your Google Workspace or Cloud Identity account \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:03.987972+00:00
---

# Prepare your Google Workspace or Cloud Identity account  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/preparing-your-g-suite-or-cloud-identity-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Prepare your Google Workspace or Cloud Identity account Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-11 UTC

This document describes how you can create a [Cloud Identity](https://workspace.google.com/signup/gcpidentity/welcome?&_ga=2.243199362.-1284715685.1569512141) or [Google Workspace](https://support.google.com/a/answer/53926) account and how you can prepare it for a production deployment.

## Before you begin

To prepare your Cloud Identity or Google Workspace account, you must do the following:

  * Select a target architecture for your production deployment based on our [reference architectures](https://docs.cloud.google.com/architecture/identity/reference-architectures).
  * Identify whether you need one or more additional Cloud Identity or Google Workspace accounts for production or staging purposes. For details on identifying the right number of accounts to use, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning).
  * [Identify a suitable onboarding plan](https://docs.cloud.google.com/architecture/identity/assessing-onboarding-plans) and have completed all the activities that your plan defines as prerequisites for consolidating your existing user accounts.



For each Cloud Identity or Google Workspace account that you must create, make sure of the following:

  * You have selected the DNS domain name to use as the [primary domain name](https://support.google.com/a/answer/182080). This domain name determines the name of the [associated Google Cloud organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#acquiring). You can use a [neutral domain name](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) as the primary domain name.
  * You have [selected any secondary](https://support.google.com/a/answer/7502379) DNS domain names that you want to add to the account. Make sure that you don't exceed a [total of 600 domains](https://support.google.com/a/answer/175747) per account.



To complete the sign-up process for a new Cloud Identity or Google Workspace account, you also need the following information:

  * A contact phone number and email address. Google uses this phone number and address to contact you in case of problems with your account.
  * An email address for the first super-admin user account. The email address must use the primary DNS domain and must not be used by an existing consumer account.

If you plan to set up federation later, select an email address that maps to a user in your external identity provider (IdP).




Creating a new Cloud Identity or Google Workspace account might require collaboration between multiple teams and stakeholders in your organization. These might include the following:

  * DNS administrators. To verify primary and secondary DNS domains, you need administrative access to both DNS zones.
  * If you use an external IdP, the administrators of your external IdP.
  * Future administrators of the Google Cloud organization.



## Process for preparing an account

The following flowchart illustrates the process of preparing your Cloud Identity or Google Workspace account. As the two sides of the diagram indicate, the process might require collaboration between different teams.

![Preparing your Cloud Identity or Google Workspace account.](https://docs.cloud.google.com/static/architecture/identity/images/preparing-an-account.svg)

  1. Sign up for Cloud Identity or Google Workspace. During the sign-up process, you must provide a contact phone number and email address, the primary domain that you want to use, and the username for the first super-admin user account.

**Note:** The sign-up process might fail if the primary DNS domain that you selected [is already in use by a different Cloud Identity or Google Workspace account](https://support.google.com/cloudidentity/answer/7332529).
  2. Verify the ownership of your primary domain by creating either a TXT or CNAME record in the corresponding DNS zone of your DNS server.

  3. Add any [secondary domains](https://support.google.com/a/answer/7502379) to the Cloud Identity or Google Workspace account.

  4. Verify ownership of the secondary domains by creating either TXT or CNAME records in the corresponding DNS zones of your DNS server.

  5. Protect your account by configuring security settings.

  6. Create a default configuration for user accounts.


**Note:** If you are signing up for Google Workspace and need to consolidate existing user accounts, don't update the DNS MX records of your primary domain yet. Doing so might cause the users of unmanaged accounts to not receive emails anymore.

### Secure access to your account

During the sign-up process, you create a first user in your Cloud Identity or Google Workspace account. This user account is assigned super-admin privileges and has full access to the Cloud Identity or Google Workspace account.

You need super-admin privileges in order to complete the initial configuration of your Cloud Identity or Google Workspace account. After you've completed the initial configuration, occurrences where you need super-admin privileges will be rare—but to ensure business continuity, it's important that you and other authorized personnel maintain super-admin access to the Cloud Identity or Google Workspace account:

To ensure this access, do the following:

  * Select a group of administrators that should have super-admin access to the Cloud Identity or Google Workspace account. It's best to keep the number of users small.
  * Create a set of [dedicated super-admin user accounts](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#use_dedicated_super-admin_users) for each administrator.
  * [Enforce Google 2-step authentication for these users](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#enforce_google_2-step_authentication_for_super-admins) and require them to [create backup codes](https://support.google.com/accounts/answer/1187538) so that they maintain access even if they lose their phone or USB key.
  * Instruct administrators to use the super-admin accounts only when necessary, and [discourage everyday use](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices#discourage_super_admin_account_usage) of those accounts.



For details on how to keep super-admin users secure, see [Super administrator account best practices](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices). And to make sure your account is properly secured, follow our [Security checklist for medium and large businesses](https://support.google.com/a/answer/7587183).

### Configure default settings for user accounts

Cloud Identity and Google Workspace support a number of settings that help you keep user accounts secure:

  * [Enforcing 2-step verification](https://support.google.com/a/answer/9176657).
  * [Controlling who can access Google Workspace and Google services](https://support.google.com/a/answer/182442).
  * [Allowing or disallowing access to apps that are less secure](https://support.google.com/a/answer/6260879).
  * [Assigning licenses for Cloud Identity Premium or Google Workspace](https://support.google.com/a/answer/1727173).
  * [Choosing a geographic location for your data](https://support.google.com/a/answer/7630496) and [controlling supplemental data storage](https://support.google.com/a/answer/6281927) (Google Workspace only).



To minimize administrative effort, it's best to configure these settings so that they are applied by default to new users. You can configure default settings on the following levels:

  1. **Global:** A global setting applies to all users but has the lowest priority.
  2. **Organizational unit (OU):** A setting configured for an OU applies to all users in the OU and to descendant OUs, and it overrides a global setting.
  3. **Group:** A setting configured by group applies to all members of the group and overrides OU and global settings.



### Create an OU structure

By creating a structure of [organizational units](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#organizational_unit), you can segment the user accounts of your Cloud Identity or Google Workspace account into discrete sets to make them easier to manage.

If you use Cloud Identity in combination with an [external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), creating custom organizational units might not be necessary. Instead, you can use a combination of global and group-specific settings:

  * Keep all user accounts in the default OU.
  * To control who is allowed to access certain Google services, create dedicated groups such as `Google Cloud Users and Google Ads Users` in your external IdP. Provision these groups to Cloud Identity and apply the right default settings to them. You can then control access by modifying group memberships in your external IdP.



If some or all of your users use Google Workspace, you are likely to require a custom OU structure because some of the Google Workspace–specific settings cannot be applied by group. If you use an external IdP, it's best to keep the OU structure simple, as follows:

  * Create a basic OU structure that lets you automatically [assign licenses](https://support.google.com/a/answer/1727173), [choose a geographic location for your data](https://support.google.com/a/answer/7630496), and [control supplemental data storage](https://support.google.com/a/answer/6281927). For all other settings, we recommend that you apply settings by group.
  * Configure your external IdP so that new users are automatically assigned to the right OU.
  * Create dedicated groups such as `Google Cloud Users and Google Ads Users` in your external IdP. Provision these groups to Google Workspace and apply the right default settings to them. You can then control access by modifying group memberships in your external IdP.



### Impact of the default OU on account migration

If you have identified [existing consumer accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts) that you plan to migrate to Cloud Identity or Google Workspace, the default OU plays a special role. If you migrate a consumer account to Cloud Identity or Google Workspace, that account is always placed into the default OU and not part of any groups.

To migrate a consumer account, you have to initiate an account transfer. This transfer has to be approved by the owner of the consumer account. As an administrator, you have limited control when the owner might give consent and you can therefore complete the transfer.

When the transfer is complete, all settings applied to the default OU take effect on the migrated user account. Make sure that these settings grant a base level of access to Google services so that the associated employee's ability to work is not impeded.

## Best practices

When you are preparing your Cloud Identity or Google Workspace account, follow these best practices:

  * If you use an [external IdP](https://docs.cloud.google.com/architecture/identity/reference-architectures#using_an_external_idp), then [ensure that the users in Cloud Identity or Google Workspace are a subset of the identities in your external IdP](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#make_cloud_identity_or_g_suite_identities_a_subset_of_the_identities_in_your_external_idp).
  * Consider shortening the [default session length](https://support.google.com/a/answer/7576830) and [session length used by Google Cloud](https://support.google.com/a/answer/9368756). When you use an external IdP, make sure that you [align the session length with your IdP](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating#align_the_length_of_google_sessions_and_idp_sessions).
  * [Export audit logs to BigQuery](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning#export_audit_logs_to_bigquery) to retain them beyond the default retention period.
  * To help keep your account safe, periodically review our [security checklist for medium and large businesses](https://support.google.com/a/answer/7587183).



## What's next

  * Read about how to [consolidate your existing user accounts](https://docs.cloud.google.com/architecture/identity/overview-consolidating-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-11 UTC."],[],[]] 
