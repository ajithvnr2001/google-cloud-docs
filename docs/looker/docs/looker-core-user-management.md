---
url: https://docs.cloud.google.com/looker/docs/looker-core-user-management/
title: Manage users within Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:18.372235+00:00
---

# Manage users within Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-user-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Manage users within Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

As a Looker administrator, you can manage authentication methods and default Looker roles within your Looker (Google Cloud core) instance. Additionally, you can manage certain elements of user accounts within your Looker (Google Cloud core) instance. This ensures that the right individuals have appropriate access and permissions within your analytics application, keeping your data environment secure and organized.

## Required permission

In order to manage users within a Looker (Google Cloud core) instance, you must have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_permission_sets) within Looker.

## The Users page

The [**Admin > Users** page](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) within Looker displays active users within Looker (Google Cloud core) and lets you make certain edits to their accounts within Looker, such as editing the following account settings:

  * [locale](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#locale)
  * [number format](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#number_format)
  * [timezone](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#timezone)
  * [ability to create API keys](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys)
  * [Groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#groups)
  * [Looker roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#roles)



Users' names and email addresses must be edited within the identity provider that is used for authentication.

Unlike within Looker (original) instances, the following isn't available in the Looker (Google Cloud core) **Users** page:

  * [add users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#adding_users) (with the exception of service accounts)
  * [send setup link / send reset link](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#send_setup_link_send_reset_link)
  * [set up two-factor authentication](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#two-factor_secret)
  * [sudo](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#impersonating_sudoing_users) as a user



## Adding users to a Looker (Google Cloud core) instance

To add individual Looker (Google Cloud core) users, follow the procedure for your [authentication method](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication):

  * **Workforce Identity Federation:** Add users or groups within your external identity provider, and ensure that the appropriate [Looker (Google Cloud core) IAM role](https://docs.cloud.google.com/looker/docs/looker-core-access-control#iam-roles) is granted to the workforce pool principal or group in IAM. For more information, see [Use Workforce Identity Federation for Looker (Google Cloud core) user authentication](https://docs.cloud.google.com/looker/docs/looker-core-workforce-identity).
  * **Google OAuth:** Google OAuth is enabled by default. To add a user, grant their principal an appropriate [Looker (Google Cloud core) IAM role](https://docs.cloud.google.com/looker/docs/looker-core-access-control#iam-roles) by using IAM in the Google Cloud console.
  * **SAML or OpenID Connect (OIDC):** Add users within your configuration for the external identity provider. Google OAuth will remain available as a backup authentication method by default if another identity provider is configured.



Users' Looker accounts will be created upon first login. Individual users cannot be added on the **Users** page; however, API-only service accounts can be added on the **Users** page.

**Note:** Looker doesn't notify users that they have been added to the Looker (Google Cloud core) instance. You must notify users they have been added and provide login information, such as URL.

### Creating an API-only service account

Service accounts are the only accounts that can be created within a Looker (Google Cloud core) instance.

You can create [API-only accounts (often called _service accounts_)](https://docs.cloud.google.com/looker/docs/api-auth#managing_api_credentials) from the **Users** page within a Looker (Google Cloud core) instance. These accounts can be granted Admin Looker roles and Looker API credentials. However, these accounts can't log in to Looker (Google Cloud core) through the UI.

Service accounts use licenses according to the roles that they have. If a service account is granted multiple roles, it consumes one license from the highest tier available among those roles. For example, if a service account has both Viewer and Developer permissions, it uses a Developer license.

To add a service account, follow these steps:

  1. Click the **Add Service Accounts** button to open the **Adding a new Service Account** page.
  2. In the **Service Account Name** field, enter a name for the service account.
  3. The **Create default set of API credentials** switch is enabled by default. If you don't want API credentials created for the account, click the switch to disable this option.
  4. Select the [Groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) and [Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) to assign to the service account.
  5. Click the **Save** button.

**Note:** Service accounts within Looker (Google Cloud core) aren't the same as [Google service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) and aren't governed by IAM.

You can view and edit existing service accounts in the **Service Accounts** tab on the **Users** page. To edit a service account, click the service account row to display the **Edit User** page. From the **Edit User** page you can do the following:

  * Enable or disable the service account
  * Edit the service account name
  * Manage the service account [API keys](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#api_keys)
  * Assign different [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) and [Roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles)
  * Edit the [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) that are associated with the service account



## Removing access to Looker (Google Cloud core)

**Important:** We recommend that you remove access to a Looker (Google Cloud core) instance by applying changes to the authentication method rather than by disabling or deleting the user from the **Users** page.

To remove access to a Looker (Google Cloud core) instance, do one of the following:

  * **Workforce Identity Federation:** Revoke the user's or group's [Looker (Google Cloud core) IAM role](https://docs.cloud.google.com/looker/docs/looker-core-access-control#iam-roles) by using IAM in the Google Cloud console, or disable the user's account in your external identity provider.
  * **Google OAuth:** Revoke the user's [Looker (Google Cloud core) IAM role](https://docs.cloud.google.com/looker/docs/looker-core-access-control#iam-roles) by using IAM in the Google Cloud console.
  * **SAML or OpenID Connect (OIDC):** Update the configuration in the external identity provider that was used for authentication.



Although the user can no longer log in to the instance, the user account will still appear active on the **Users** page. To remove the user account from the **Users** page, [delete](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#deleting_users) the user within the Looker (Google Cloud core) instance.

Deleting users from a Looker (Google Cloud core) instance that is [associated with a Data Studio Pro subscription](https://docs.cloud.google.com/looker/docs/looker-core-lsp) reduces the number of complimentary Data Studio Pro licenses that may be allocated to your instance. If the number of complimentary Pro licenses that are allocated to your instance becomes less than the number of licenses that are in use, the difference will be converted immediately to paid licenses, subject to Data Studio Pro [pricing](https://cloud.google.com/data-studio#pricing).

## Selecting an authentication method for Looker (Google Cloud core) users

Setting up an OAuth client [might be required](https://docs.cloud.google.com/looker/docs/looker-core-create-oauth) as part of instance creation, and OAuth authentication is the backup authentication method for Looker (Google Cloud core). However, you can choose between several different primary authentication methods. The [User authentication methods for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-user-authentication) documentation page lists the available authentication methods.

## Setting a default Looker role within the Looker (Google Cloud core) instance

Before you add any users, you can set the default [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) that will be granted to user accounts with the Looker Instance User IAM role upon their first login to a Looker (Google Cloud core) instance. To set a default role, follow the steps provided in the documentation for your identity provider: [OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#setting_a_default_looker_role_within_the_instance), [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#default_groups_and_roles), or [OpenID Connect](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect#default_groups_and_roles).

## What's next

  * [Connect Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects)
  * [Configure a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-setup)
  * [Looker (Google Cloud core) admin settings](https://docs.cloud.google.com/looker/docs/looker-core-admin-looker)
  * [Administer a Looker (Google Cloud core) instance from the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-admin-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
