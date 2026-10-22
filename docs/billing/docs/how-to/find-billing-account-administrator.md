---
url: https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator/
title: Find a Billing Account Administrator \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:42.214942+00:00
---

# Find a Billing Account Administrator  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Find a Billing Account Administrator Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to identify the administrators and other principals within your organization who have Cloud Billing account permissions.

A [Billing Account Administrator role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) provides full _owner_ access to a Cloud Billing account. Billing Account Administrators can manage payment instruments, pay bills, configure billing data exports, view cost information, link and unlink projects, and manage user permissions on the billing account. Also, only Billing Account Administrators can contact Cloud Billing Support.

By default, the person who creates the Cloud Billing account is a Billing Account Administrator for the Cloud Billing account.

### Before you begin

To successfully view all the principals who have billing account permissions, you need basic permissions on the _Cloud Billing account_. Administrator-level permissions on other Google Cloud resources, such as Project Owner, don't grant you the permissions you need to see basic billing account information. On the Cloud Billing account, you need a role that includes the following [permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing):

  * `billing.accounts.get`
  * `billing.accounts.getIamPolicy`



These permissions are granted in many [predefined roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam), including:

  * Billing Account User
  * Billing Account Viewer
  * Billing Account Costs Manager
  * Billing Account Administrator



If you have some level of Cloud Billing account access, you can view basic information about the billing account, including viewing the **Info panel** to identify the administrators and other principals within your organization who have billing account permissions.

**Note:** Neither the [Billing Account Creator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.creator) role (which is granted at the Organization level) nor the [Project Billing Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.projectManager) role (which is granted on a project) include the permissions needed to access basic information about the billing account.

## View permissions for a Cloud Billing account in the Info panel

In the Billing section of the Google Cloud console, the **Info panel** is available on the **My Billing Accounts** page, and on the **Account management** page. In the **Info panel** , you can see the list of billing administrators and other [roles assigned on the Cloud Billing account](https://docs.cloud.google.com/iam/docs/roles-permissions/billing).

### View permissions on the My Billing Accounts page

You can view the **Info panel** on the Cloud Billing **My Billing Accounts** page.

![My Billing Accounts page showing the Info panel.](https://docs.cloud.google.com/static/billing/docs/images/my-billing-accounts-show-info-panel-with-permissions.png)Example of the My Billing Accounts page showing the Info panel for a selected billing account, with the Billing Account Administrator role node expanded. The numbers in this example correspond with the following steps. 

![](https://docs.cloud.google.com/static/billing/docs/images/my-billing-accounts-show-info-panel-with-permissions.png)

To access the **Info panel** on the **My Billing Accounts** page and view your Billing Account Administrators, do the following:

  1. In the Google Cloud console, go to the **My Billing Accounts** page in the **Billing** section.

[Go to My Billing Accounts](https://console.cloud.google.com/billing)

  2. If you have billing accounts for more than one organization, and you want to view accounts across all of your organizations, expand the **organization selector** and choose **None Selected**.

  3. By default, your list of billing accounts is filtered to show only _Active_ accounts.

     * To view a **complete list** of your billing accounts, active and closed, **remove** the _Status :**Active**_ filter.
     * To view a list of accounts filtered by _Closed_ accounts, **remove** the _Status :**Active**_ filter and **add** a _Status :**Closed**_ filter.
  4. **Select the row** of a Cloud Billing account to view the principals and permissions for the billing account in the **Info panel**. If the info panel isn't already visible, click **Show info panel** to open it.

  5. Expand (arrow_right) the **Billing Account Administrator role node** to view all the **principals** who are assigned as an administrator on the selected Cloud Billing account.




* * *

### View permissions on the Account management page

You can view the **Info panel** on the Cloud Billing **Account management** page. This option works well when you want to find the billing account administrators of a single, _active_ billing account that you know by name. If the billing account is closed or you're unsure of its name, locate the billing account and its permissions on the My Billing Account page Info panel.

![Account management page showing the Info panel.](https://docs.cloud.google.com/static/billing/docs/images/account-management-page-with-info-panel.png)Example of the Account management page showing the Info panel for a selected billing account, with the Billing Account Administrator role node expanded. 

![](https://docs.cloud.google.com/static/billing/docs/images/account-management-page-with-info-panel.png)

To access the **Info panel** on the **Account management** page and view your Billing Account Administrators, do the following:

  1. In the Google Cloud console, go to the **Account management** page for the **Cloud Billing account**.

[Go to Account management](https://console.cloud.google.com/billing/manage)

  2. At the prompt, **choose the Cloud Billing account** that you want to view.

The **Account management** page opens for the selected Cloud Billing account.

  3. In the **Info panel** , you can review the **Principals** and **Permissions** for the selected Cloud Billing account. If the panel isn't already visible, click **Show info panel** to open it.

  4. Expand (arrow_right) the **Billing Account Administrator role node** to view all the **principals** who are assigned as an administrator on the selected Cloud Billing account.




### About permissions in the Info panel

The **Permissions panel** is organized by role, along with the number of principals assigned to each role. For example, in your permissions panel, you might see:

  * Billing Account Administrator (2)
  * Billing Account User (6)
  * Billing Account Viewer (10)



To view the list of principals assigned to a role, expand the arrow_right *_role node_. Principals are users, groups, domains, or service accounts. The same principal can be assigned to multiple roles.

To find a _specific principal_ and see which roles are granted to that principal, use the  filter_list **Filter** and enter the email address of the principal.

[Learn more about principals in IAM](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity)

## What to do if you have no billing account access

If you don't have permissions to access the Cloud Billing account, and you need to locate your Billing Account Administrator, try the following options:

  * _Recommended_ : Locate someone at your company or organization who has some level of permissions to access the Cloud Billing account and ask them to look up the billing account administrators. For example, people who work on finance or accounting teams will typically have access to the Cloud Billing account.


  * _If all else fails_ : If you have no way to know who your Billing Account Administrators are and you (or your organization) have lost access to your Cloud Billing account and you need to regain access, you can contact Cloud Billing Support using the [**account recovery form**](https://support.google.com/cloud/contact/cloud_platform_access_recovery). 
    * For the team of specialists to provide assistance, you must meet all of the requirements specified on the form and submit all information requested. This includes providing the [billing account ID](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-id) and explaining how or why you lost access to the Cloud Billing account.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
