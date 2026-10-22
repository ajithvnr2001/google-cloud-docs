---
url: https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing/
title: Manage access to Cloud Billing accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:07.342387+00:00
---

# Manage access to Cloud Billing accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/grant-access-to-billing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Manage access to Cloud Billing accounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure access permissions for Cloud Billing accounts.

A Cloud Billing account is set up in Google Cloud and defines who pays for a given set of Google Cloud resources and Google Maps Platform APIs. A Cloud Billing account is connected to a Google payments profile. Access permissions for Cloud Billing and Google payments are configured in two different systems depending on what type of access you want to provide. 

If you need to configure access permissions for a Google payments profile, see [Manage Google payments users, permissions, and notification settings](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts). **Note:** Changing access permissions for Cloud Billing accounts is considered a sensitive action; in some cases, you might need to reauthenticate before you can initiate the action. For more information, see [Sensitive actions](https://docs.cloud.google.com/docs/authentication/reauthentication#sensitive-actions). 

## Cloud Billing account user permissions

Each Cloud Billing account needs at least one [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in). By default, the person who creates the Cloud Billing account is a Billing Account Administrator for that billing account. For redundancy, we recommend that you configure more than one administrator on each Cloud Billing account.

You can grant your users different levels of access to billing accounts, depending on what they need to do (for example, track spend, review cost anomalies, manage budgets, optimize costs, or review and pay invoices).

You don't directly give users permissions; instead, you grant them _roles_ , which have one or more permissions bundled within them. You can grant one or more roles on the same resource.

If you have an organization associated with your Google Cloud account, you can grant or limit access to Cloud Billing by setting an IAM policy at the organization level. You can also set Cloud Billing IAM policy on the Cloud Billing account level or limit billing access to a folder or project level.

### Before you begin

Familiarize yourself with the roles and permissions available in Cloud Billing.

  * For information about predefined billing roles and their permissions, see [Cloud Billing access control & permissions](https://docs.cloud.google.com/billing/docs/how-to/billing-access).
  * If the permissions available in the [predefined roles](https://docs.cloud.google.com/billing/docs/how-to/billing-access) don't fit your needs, create and use custom roles that grant more specific sets of permissions. For more information, see [Create custom roles for billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles).



### Permissions required for this task

To manage user permissions on a Cloud Billing account, you need a role that includes the following [permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * [`billing.accounts.getIamPolicy`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#policy) \- To view roles on account, including associated usernames.
  * [`billing.accounts.setIamPolicy`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#policy) \- To grant roles to principals on a Cloud Billing account.



To gain this permission using a predefined role, ask your administrator to grant you the following role on the Cloud Billing account:

  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access)



## Update user permissions for a Cloud Billing account

In the **Billing** section of the Google Cloud console, you can review, add, or remove Cloud Billing user permissions for each billing account that you administer.

### Access the Permissions panel for a Cloud Billing account

To manage permissions for a Cloud Billing account, access the account from the list of Cloud Billing accounts in the Google Cloud console **Billing account management** page:

![Billing account management page. Click to view larger image.](https://docs.cloud.google.com/static/billing/docs/images/ba-mgmt-acct-profile-panel.png)

![](https://docs.cloud.google.com/static/billing/docs/images/ba-mgmt-acct-profile-panel.png)

  1. Sign in to the **Manage billing accounts** page in the Google Cloud console.

[Sign in to Manage billing accounts](https://console.cloud.google.com/billing)

  2. Select the row of a Cloud Billing account to view the principals and permissions for the billing account in the info panel. If the panel isn't already visible, click **Show info panel** to open it.




Alternatively, you can access a Cloud Billing account's permissions on its **Account management** page:

![Account management page for a billing account. Click to view larger image.](https://docs.cloud.google.com/static/billing/docs/images/acct-mgmt-roles-info-panel.png)

![](https://docs.cloud.google.com/static/billing/docs/images/acct-mgmt-roles-info-panel.png)

  1. In the Google Cloud console, go to the **Account management** page for the Cloud Billing account.

[Go to Account management in Cloud Billing](https://console.cloud.google.com/billing/manage)

  2. At the prompt, choose the Cloud Billing account that you want to view.

  3. In the **Info** panel, review and edit the **Principals** and **Permissions** for the selected Cloud Billing account. If the panel isn't already visible, click **Show info panel** to open it.




### Update roles and principals in the Permissions panel

The **Permissions** panel is organized by role, along with the number of principals that have each role. For example, in your permissions panel, you might see the following:

  * Billing Account Administrator (2 principals)
  * Billing Account User (6 principals)
  * Billing Account Viewer (10 principals)



You can grant multiple roles to the same principal.

To view the list of principals assigned to a role, expand the **role node**.

To find a specific principal and see which roles are granted to that principal, use the  filter_list **Filter** and enter the email address of the principal.

To update Cloud Billing permissions, in the **Permissions** panel, do any of the following:

  * To add new principals and assign permissions:

    1. Click **Add principal**.
    2. In the **New principals** field, enter one or more email addresses for the principals that you want to add. You can add individuals, service accounts, or Google Groups as principals.
    3. Select a permission for the principals from **Select a role**.
    4. If needed, you can **Add another role** to grant additional permissions to the principals.
    5. When done, click **Save**.
  * To edit a principal's billing permissions:

    1. Use the  filter_list **Filter** to locate a specific principal or role.
    2. In the list, locate the principal that you want to edit.
    3. In the principal's row, click **Edit** edit.

The **Edit permissions** panel opens, specific to the selected principal and resource (Cloud Billing account) that you're viewing.

    4. In the **Edit permissions** panel, add, edit, and delete roles for the selected principal and resource.

    5. When done, click **Save**.

  * To revoke a role from a principal:

    1. Use the  filter_list **Filter** to locate a specific principal or role.
    2. In the list, locate the principal whose role you want to revoke.
    3. In the principal's row, click **Delete** delete.
    4. Confirm your action.

**Note:** This action revokes only a single role. The principal retains their other roles.



## Google payments user permissions

Each Google payments account needs at least one [_Admin with all permissions_](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#permissions), and one [_Primary Contact_](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts#primary-contact) (the person Google will contact with any payments-related alerts or questions). By default, the person who creates the Google payments account is both the _Admin with all permissions_ and the _Primary Contact_. For redundancy, we recommend that you set more than one Google payments administrator.

You can add users to any [Google payments _Organization_ profile](https://docs.cloud.google.com/billing/docs/concepts#payments_profile_types) that you manage, and grant different levels of access to your users depending on what they need to do (for example, manage payment methods or payments profile details). You can also configure user email preferences for receiving billing and payments emails.

Not all payments-related tasks require you to be a Google payments user to gain the permissions required to access and edit Google payments profile information. Certain Cloud Billing IAM permissions will grant _equivalent_ payments permissions. Specifically, Cloud Billing account users with the `billing.accounts.updatePaymentInfo` permission on their billing account can access and edit the associated Google payments profile and payments account directly from the Cloud Billing console, without needing additional permissions on the payments profile itself. This includes users with the [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) role (`roles/billing.admin`) and users granted this permission using a [custom role](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#payment_information).

For more information, see [Manage Google payments users, permissions, and notification settings](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts). 

## Related topics

\+ [Manage Google payments users, permissions, and notification settings](https://docs.cloud.google.com/billing/docs/how-to/modify-contacts)

  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)
  * [Cloud Billing API access control](https://docs.cloud.google.com/billing/v1/how-tos/access-control)
  * [Granting, changing, and revoking Access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
