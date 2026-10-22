---
url: https://docs.cloud.google.com/iam/docs/grant-role-console/
title: Quickstart: Grant roles in the Google Cloud console \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:53.005341+00:00
---

# Quickstart: Grant roles in the Google Cloud console  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/grant-role-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Grant an IAM role by using the Google Cloud console

Learn how to use the Google Cloud console to grant IAM roles to principals at the project level.

**Note:** If you're getting started with Google Cloud, you can grant the appropriate IAM roles to your organization administrator groups as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

See the following video for a quick walkthrough:

[![A video showing how to grant IAM roles to principals using the
Google Cloud console.](https://img.youtube.com/vi/Sdt-i-Q7tyA/0.jpg)](https://www.youtube.com/watch?v=Sdt-i-Q7tyA)

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/iam-admin/iam?walkthrough_id=iam--quickstart)

* * *

## Before you begin

### Create a Google Cloud project

For this quickstart, you need a new Google Cloud project.

**Warning:** If you use an existing project, then completing this quickstart will enable some users to access resources in that project.

  1. Ensure that you have the Project Creator IAM role (`roles/resourcemanager.projectCreator`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  2. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Click **Create project**.

  4. Name your project. Make a note of your generated project ID.

  5. Edit the other fields as needed.

  6. Click **Create**.




### Ensure that you have the required roles

Make sure that you have the following role or roles on the project: Project IAM Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



### Enable the APIs

Enable the IAM and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

## Grant an IAM role

Grant a principal the Logs Viewer role on the project.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. Select your new project.

  3. Click person_add **Grant access**.

  4. Enter an identifier for the principal. For example, `my-user@example.com`.

  5. From the **Select a role** drop-down menu, search for **Logs Viewer** , then click **Logs Viewer**.

  6. Click **Save**.

  7. Verify that the principal and the corresponding role are listed in the IAM page.




You have successfully granted an IAM role to a principal.

## Observe the effects of IAM roles

Verify that the principal you granted a role to can access the expected Google Cloud console pages by doing the following:

  1. Send the following URL to the principal to whom you granted the role in the preceding step:
         
         https://console.cloud.google.com/logs?project=PROJECT_ID
         

This URL takes the principal to the **Logs Explorer** page for your project.

  2. Verify that the principal is able to access and view the URL.




If the principal tries to access a different Google Cloud console page that they don't have access to, they see an error message.

## Grant additional roles to the same principal

Grant the principal the Compute Viewer role in addition to their Logs Viewer role.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate the row that contains the principal to whom you want to grant another role, and click **Edit principal** edit in that row.

  3. In the **Edit permissions** pane, click **Add another role**.

![](https://docs.cloud.google.com/static/iam/img/quickstart-roles-add.png)

![](https://docs.cloud.google.com/static/iam/img/quickstart-roles-add.png)

  4. From the **Select a role** drop-down menu, search for **Compute Viewer** , then click **Compute Viewer**. Click **Save**.

  5. Click **Save**.




The principal now has a second IAM role.

## Revoke IAM roles

Revoke the roles you granted to the principal in the preceding steps by doing the following:

  1. Locate the row that contains the principal that you granted roles to and click **Edit principal** edit in that row.

  2. In the **Edit permissions** pane, click the delete icon next to the Logs Viewer and Compute Viewer roles.

  3. Click **Save**.




You have now removed the principal from both of the roles. If they try to view the **Logs Explorer** page, they see the following error message:

`You don't have permissions to view logs.`

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Clean up by deleting the project that you created for this quickstart.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Learn the basics](https://docs.cloud.google.com/iam/docs/overview) of IAM.
  * Review the [list of all IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles).
  * Find out how to [manage access with IAM](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
