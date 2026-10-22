---
url: https://docs.cloud.google.com/chronicle/docs/administration/rbac/
title: Configure legacy RBAC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:17.426018+00:00
---

# Configure legacy RBAC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/administration/rbac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure legacy RBAC

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Role-based access control (RBAC) enables an administrator to tailor access to Google Security Operations features based on an employee's role in your organization.

**Important:** This document describes the Google SecOps roles and groups available in the _Google SecOps RBAC_ feature that don't use IAM for feature access control. If you migrated your instance to IAM, or if you're onboarding to Google SecOps on or after October 6, 2025, see [Configure feature access control using IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access) and [Google SecOps permissions in IAM](https://docs.cloud.google.com/chronicle/docs/reference/feature-rbac-permissions-roles).

## Before you begin

RBAC reads the group information from the SAML response from the following case-insensitive default attribute names:

  * `group`
  * `idpgroup group`
  * `memberof`



If you use a custom attribute name, it must be provided to your Google Security Operations first to enable you to modify your RBAC settings.

## Modify RBAC settings

To navigate to the RBAC profile and settings pages, click **Settings** in the navigation bar.

## Profile

The **Profile** page displays the information from the user's profile (user ID, group ID, roles assigned) and some additional information about their organization (customer ID, Google Cloud project number, Google Cloud project ID).

### Customer ID

Your customer ID is located in the **Organization Details** section of the **Profile** page.

### Update the time zone

You can update the time zone as follows:

  1. Locate the **Time Settings** section on your profile and click **Edit**.

  2. Select the appropriate time zone for your location.


**Note:** Some user interface elements display only UTC time, such as the time values on the prevalence graph in Domain view, which are labeled as **UTC**. Similarly, downloaded results are always displayed in UTC, regardless of the configured time zone.

## Users & Groups

The **Users & Groups** page enables an administrator to configure RBAC.

  1. Click the **Users & Groups** link in the left navigation pane. A list of users and groups are displayed on the **Users and groups** page with the columns: **User/Group** , **Type** , and **Assigned role**.

  2. Click **Assign new** to open the **Assign role** dialog. From this dialog you can complete the following tasks:

     * Assign a new user or users to a role.
     * Assign a new group or groups to a role.

The available roles are:

     * Default
     * ViewerWithNoDetectAccess
     * Viewer
     * Editor
     * Administrator

Once you have added your user or group IDs and selected the appropriate role from the **ASSIGN ROLE** drop-down menu, click **ASSIGN**.

As you assign roles, be aware of the following:

     * When adding users or groups, make sure they exist in your identity provider (IdP). When deleting users or groups, make sure you retain at least one user or group that has the Administrator role and is in your IdP; otherwise, you'll lose administrator access.
     * User and group IdP IDs are case sensitive.
     * You can't change the assigned role of an existing user or group using this dialog. See the steps that follow for how to change roles and delete users and groups.
     * Google Security Operations manages the mapping between users and groups and roles.
     * Use caution if the user or group ID contains special characters that, depending on the text source, might use UTF-8 encoding. Once you click **Assign** , Google recommends that you verify that the new assignment has been saved correctly.
  3. You can change the role of an existing user or group by selecting a new role from the drop-down menu corresponding to that user or group in the **Assigned role** column.

**Note:** If the administrator has changed a user's role, the user might need to refresh their browser to view the changes.
  4. You can change the default role assigned to new users and groups from the role drop-down menu in the top right corner.

  5. You can delete a user or a group by clicking on the trash-can icon which appears on the far right side of the user or group row as you hold the pointer over it.

If you delete users and groups that are administrators, and the only remaining administrators are not in your IDP, you will lose administrator access.

### Roles




Roles are associated with a set of product permissions. Assigning a role to a user grants the user the permissions associated with that role.

Google Security Operations includes the following predefined roles:

  * Administrator—Manages the role-based access control policies for your enterprise. Can also edit or view any Google Security Operations page.
  * Editor—Can edit Google Security Operations pages, including the ability to create and edit rules for the Detection Engine.
  * Viewer—Can view any Google Security Operations page, but cannot make any changes.
  * ViewerWithNoDetectAccess—Can view all Google Security Operations pages that don't include detections (principally the Rules and Reference Lists pages).



RBAC applications include the following:

  * Create and assign roles based on the job responsibilities.
  * Create and assign roles based on tenancies or organizations.
  * Assign temporary roles to analysts for investigating an issue.



### Permissions

Permissions provide the authorization needed to perform a single controlled action in Google Security Operations, including (see the user interface for the complete list of permissions):

  * View rule
  * Modify rule
  * Edit feedback
  * Edit reference list
  * View RBAC permissions



If a user does not have permissions for an action, the associated feature is disabled. For example, if the user has the Viewer role, they are unable to create a new rule (the **New** button is disabled in the Rules Editor), duplicate a rule (the **Duplicate** option is disabled), or modify an existing rule.

To view the roles and permissions available to users and groups, complete the following:

  1. Click the **Roles** link in the left navigation pane.

  2. Select a role from the Roles column to view the permissions granted for that role. The permissions associated with each role cannot be changed.




The default role for newly added users and groups is Viewer. If you select one of the other roles (for example, Editor), the **Set as default** control becomes available. This lets you to make that role the default instead.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
