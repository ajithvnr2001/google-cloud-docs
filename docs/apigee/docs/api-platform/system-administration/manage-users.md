---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users/
title: Manage users in the Apigee UI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:15:07.034606+00:00
---

# Manage users in the Apigee UI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage users in the Apigee UI Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic describes how to add users to an environment, remove users from an environment, and update user roles in an environment, using the Apigee UI.

## About role scope

You can add users to Apigee organizations using the Google Cloud console. When you do this, the user is granted the same access to all environments in the organization. However, you can refine each user's access by using the Apigee UI.

The Apigee UI lets you assign roles to users that are specific to a given environment. Instead of each user having the same role in all environments of an organization, you can assign a specific role or roles for that user for each environment.

When you first configure Apigee and create the Google Cloud project to which the Apigee organization is bound, you typically add a few users with different roles like `API Admin` and `Environment Admin`. Because these users are defined at the Cloud Project project level, they can access _all_ environments with the roles granted.

If you grant access using the Apigee UI, you can set roles of existing users at the _environment level_.

**Note:** Before you can add a new user (and specify environment-specific access for that new user) in the Apigee UI, you must grant that user access to the Google Cloud project, as described in [Managing access in Google Cloud](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-access). 

Roles you assign in the Google Cloud project apply to all environments. Roles you assign in the UI apply only to the selected environment.

The roles list displays only predefined roles.

**Note:** Roles assigned to specific environments, as explained in this topic, only affect resources that are under the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) that includes Apigee Environment resources. You can identify which resources are in the Environment resource hierarchy by examining the [Apigee API documentation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments). For example, the `organizations.environments.deployments` resource is in the `Environments` resource hierarchy. 

For all other permissions for Apigee resource access, see [Managing access in Google Cloud](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-access). 

## Add user accounts in the Apigee UI

To specify user permissions for an environment:

  1. Ensure that you have already added the user to your Google Cloud project. For information on adding users to a Google Cloud project, see [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access). 
  2. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

**Note:** If you see the message below at the top of the UI, you need to [provision your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) before proceeding further. 

![Welcome to Apigee page.](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/welcome-to-apigee.png)

After you have provisioned Apigee, close the UI and then reopen it.

  3. Select the environment you wish to edit from the list of available environments.
  4. Click the **Access** tab on the **Environment details** page. 

The UI displays a list of current user accounts and roles for the selected environment.

  5. Click **+Grant Access**. 

The **Grant Access** pane displays.

  6. Enter the user's email account in the first field. This email address is typically one of the following: 
     * An individual [Google account](https://support.google.com/accounts/answer/27441) (for example, `fred@gmail.com`). All Gmail accounts are Google accounts, but you can also register email addresses with different domains as Google accounts.
     * A Google Group alias. For example, `address@googlegroups.com`.
     * A service account. For example, `address@example.gserviceaccount.com`.
     * A Google Workspace domain. For example, `address@example.com`, where `example.com` is a domain that you used when you signed up for Google Cloud services.
  7. Select a role from the **Role(s)** list and click **OK**. You can add more than one role for each user. For details on available roles, see [Apigee roles](https://cloud.google.com/iam/docs/roles-permissions/apigee) and [IAM permissions reference](https://cloud.google.com/iam/docs/permissions-reference). 
  8. Click **Grant**.
  9. Repeat this process for each environment for which you want to specify the user's role.

You can remove a user account from an environment using the UI, but that user account will still have the access that it was granted in the [Google Cloud console](https://console.cloud.google.com) unless you also remove the user from the Console by default.




## Remove user accounts

Removing a user at the environment level does not remove the user at the Google Cloud project level. As a result, the user can still access all environments with their Google Cloud project level permissions.

To revoke the user's access entirely, you must remove them from the Google Cloud project as described in [Revoking Access to Google Cloud Platform](https://cloud.google.com/security/data-loss-prevention/revoking-user-access).

To remove a user from an environment:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the environment name you wish to edit from the list of available environments.
  3. Click the **Access** tab on the **Environment details** page. 

The UI displays a list of current user accounts and roles for the selected environment.

  4. In the user's row, click  more_vert  **Actions** , and select **Remove**. 

The UI displays a confirmation dialog box.

  5. Click **Remove Access**. 

The UI removes that user from the environment.

**Note:** Removing a user at the environment level does not remove the user at the Google Cloud project level. To remove a user entirely, you must also remove that user from the Google Cloud project by using the Console, as described in [Revoking Access to Google Cloud Platform](https://cloud.google.com/security/data-loss-prevention/revoking-user-access). 



## Change user roles in the Apigee UI

You can change a user's role on a per-environment basis by using the Apigee UI. This includes adding additional roles to a user account or removing one or more roles from the user account.

To change a user's roles for an environment:

  1. In the Google Cloud console, go to the **Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the environment name you wish to edit from the list of available environments.
  3. Click the **Access** tab on the **Environment details** page. 

The UI displays a list of current user accounts and roles for the selected environment.

  4. In the user's row, click  more_vert  **Actions** , and select **Edit**. 

The UI displays the **Manage Roles** pane.

  5. Do one of the following: 
     1. **To remove a role:** Clear the checkbox next to that role.
     2. **To add another role:** Select the checkbox next to the role you wish to add.
  6. Click **OK**.
  7. Click **Update**. 

The UI applies your changes to the user in that environment.

**Note:** Changing roles at the environment level does not affect the user's roles at the Google Cloud project level. For information on changing roles at the Google Cloud project level, see [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
  *[Google Cloud]: Google Cloud
