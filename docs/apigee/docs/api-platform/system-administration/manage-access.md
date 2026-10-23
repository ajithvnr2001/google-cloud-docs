---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-access/
title: Managing access in Google Cloud \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:34.772907+00:00
---

# Managing access in Google Cloud  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing access in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

After you receive a confirmation that your Apigee organization has been provisioned, you can add more user accounts to the Google Cloud project. You do this by using the IAM service in the Google Cloud console.

This section describes how to add new user accounts to your Google Cloud project and manage their access. These user accounts might have specialized roles, such as someone who creates analytics reports or someone who is responsible for deploying and undeploying API proxies. For description of Apigee roles, including API access details, see [ Manage users, roles, and permissions using the API](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users-roles).

**Note:** When you add new users to your project in the Google Cloud console, the new user can by default access _all_ environments in the organization. They are still limited in what they can do by their roles, though. To refine each user's access, override their roles at the environment level in the UI. 

For small projects, you might not add any new users. For larger projects, it's likely that you'll add at least one new principal for each Apigee role. Try to limit the number of Apigee Organization Admin roles you assign because this role has the highest level of permissions.

**To add a user and assign Apigee roles to it in your Google Cloud project:**

  1. In the Google Cloud console, go to the **IAM & Admin > IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

The Console displays the **Permissions** view:

![IAM permissions pane](https://docs.cloud.google.com/static/apigee/docs/api-platform/system-administration/images/iam-permission-pane.png)

  2. To add a new user, click **ADD**. The Console displays the **Add principals** view: 

![Add permissions dialog.](https://docs.cloud.google.com/static/apigee/docs/api-platform/system-administration/images/add-permissions-dialog.png)

  3. In the **New principals** field, enter the email address of the new user's account. 

The email address must be one of the following types:

     * A [Google account](https://support.google.com/accounts/answer/27441) (for example, _fred@gmail.com_). All Gmail accounts are Google accounts, but you can also register email addresses with different domains as Google accounts.
     * The name of a Google group. For example, _my-group@googlegroups.com_. If you add a Google group as a user, then all members of the group will have that role.
     * A service account. For example, _my-service-account@example.gserviceaccount.com_. (You do not need to add your service accounts here.)
     * A Google Workspace domain. For example, _address@example-domain.com_ , where example.com is a domain that you used when you signed up for Google Cloud services.

You can specify more than one email address in the **New principals** field and assign the same role to all of them. To assign different roles to different email addresses, perform steps 4 and 5 for each new principal.

  4. Assign at least one role to the new principals: 
     1. Expand the **Select a role** list.
     2. Select the role that you want to assign. To decide which roles to assign, see the descriptions in [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles).
     3. To assign an Apigee role, you can enter `Apigee` as a filter so that the list displays only Apigee roles, as the following example shows: 

![](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.3/images/apigee-roles-list-gcp.png)

     4. Repeat this process for each role you want to assign to the user.
**Note:** To enable granular control over your resources, you can specify resource conditions for each role. To understand how to specify resource conditions, see [Adding resource conditions in IAM policies](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/add-iam-conditions). If you don't specify any resource conditions for a role, the role will have blanket permissions on all the child resources. 
  5. Click **Save** to add the new user to the Google Cloud project with the assigned roles. 
  6. Repeat this process for each user that you want to add.



Google Cloud allows the project's new users to access all environments in the organization with the assigned permissions. To limit a user's access to certain environments, use the hybrid UI's, as described in [ Add user accounts in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users#add-user-accounts-in-the-hybrid-ui).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
