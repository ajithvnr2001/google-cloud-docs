---
url: https://docs.cloud.google.com/iam/docs/groups-in-cloud-console/
title: Create and manage Google groups in the Google Cloud console \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:45.788244+00:00
---

# Create and manage Google groups in the Google Cloud console  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/groups-in-cloud-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Create and manage Google groups in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

Google groups can help you manage users at scale. Each member of a Google group inherits the Identity and Access Management (IAM) roles granted to that group. This inheritance means that you can use a group's membership to manage users' roles instead of granting IAM roles to individual users.

**Note:** You can't add [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) to Google groups unless the [external members](https://support.google.com/a/answer/167097#zippy=%2Ccan-external-users-participate-in-groups) option is turned on.

You can create and manage groups for your organization in the Google Cloud console.

## Required permissions

You need the following permissions to manage groups in the Google Cloud console.

### Group permissions

To create, view, edit, and delete groups, in the Google Cloud console or elsewhere, you need the appropriate group permissions. These permissions are managed by Google Workspace, not IAM. To gain these permissions, contact your Google Workspace administrator.

To learn about group permissions, see [Administrator privilege definitions](https://support.google.com/a/answer/1219251#groups) and [Set organization-wide policies for using groups](https://support.google.com/a/answer/167097#create-groups).

### IAM permissions

To get the permissions that you need to use the Google Cloud console to manage groups, ask your administrator to grant you the following IAM roles on the organization: 

  * [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`)
  * To view group membership change logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Viewing groups

To view the Google groups in your organization that you have access to, follow these steps:

  1. In the Google Cloud console, go to the **Groups** page.

[Go to the Groups page](https://console.cloud.google.com/iam-admin/groups)

  2. Select the organization whose groups you want to view.




The Google Cloud console displays all the groups in your organization that you can access.

**Note:** To check whether a group has access to your project and its resources, see [Viewing current access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#viewing-console).

## Creating a group

To create a group, follow these steps:

  1. In the Google Cloud console, go to the **Groups** page.

[Go to the Groups page](https://console.cloud.google.com/iam-admin/groups)

  2. Click add_box **Create**.

  3. Fill in your group's details, including the group's name, email address, and an optional description.

  4. To add members to the group, click add **Add member** , then enter the member's email and choose their [Google Groups role](https://support.google.com/groups/answer/2464975?ref_topic=2458761).

**Note:** When you add a member to a Google group, they inherit all IAM roles granted to that group, regardless of their Google Groups role.
  5. When you are finished, click **Submit** to create the group.




## Viewing and editing group details

To view and edit the details of a group, including the group name, description, and membership, follow these steps:

  1. In the Google Cloud console, go to the **Groups** page.

[Go to the Groups page](https://console.cloud.google.com/iam-admin/groups)

  2. Find the group whose details you want to view, click the **More** more_vert button in that row, and then click **View group details**.

  3. To edit the group name or description, type your new name or description in the **Group name** or **Group description** field and click **Save**.

  4. To edit the group's membership, do the following:

     * **To add members** : Click person **Add members** at the top of the page. Enter the names of the members you want to add, choose their [Google Groups roles](https://support.google.com/groups/answer/2464975?ref_topic=2458761), then click **Add** to add them to the group.

**Note:** When you add a member to a Google group, they inherit all IAM roles granted to that group, regardless of their Google Groups role.
     * **To remove members** : Select the checkboxes next to the names of the members you want to remove, then click delete **Remove members** at the top of the page.




## Managing a group in Google Groups

Some groups have features⁠—such as moderation settings, joining rules, and permissions for creating and viewing posts—that you cannot manage from the Google Cloud console. To manage these features, you need to open the group in Google Groups.

To open a group in Google Groups, follow these steps:

  1. In the Google Cloud console, go to the **Groups** page.

[Go to the Groups page](https://console.cloud.google.com/iam-admin/groups)

  2. Find the group that you want to manage, click the **More** more_vert button in that row, and then click **View in Google Groups** launch.




This action opens the group in Google Groups, where you can manage all of your group's features. For more information, see the [Google Groups help page](https://support.google.com/groups/).

## Deleting a group

**Warning:** Deleting a group is irreversible. To avoid unexpected access changes, revoke all IAM roles from the group, then wait at least 7 days before deleting it.

To delete a group, follow these steps:

  1. In the Google Cloud console, go to the **Groups** page.

[Go to the Groups page](https://console.cloud.google.com/iam-admin/groups)

  2. Find the group that you want to delete, click the **More** more_vert button in that row, and then click **Delete group**.

  3. Confirm that you want to delete the group by clicking **Confirm** in the confirmation dialog.




## View Google Workspace audit logs in Google Cloud

If [data sharing](https://support.google.com/a/answer/9320190) is enabled for your organization, Google Cloud will automatically generate audit logs for actions taken in Google Workspace. For example, it will generate audit logs when someone adds a user to your organization or when someone removes a user from a group. You can view and manage these logs in Cloud Logging.

To learn how to enable data sharing and how to view and manage Google Workspace audit logs, see [View and manage audit logs for Google Workspace](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs).

## What's next

  * Learn how to [grant, change, and revoke access for principals](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access), including Google groups.
  * Review other ways to [create groups](https://support.google.com/a/answer/33343).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
