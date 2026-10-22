---
url: https://docs.cloud.google.com/colab/docs/manage-access-notebook/
title: Manage access to a Colab Enterprise notebook \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:11.618827+00:00
---

# Manage access to a Colab Enterprise notebook  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/manage-access-notebook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage access to a notebook

This page describes how you can grant and revoke access to a Colab Enterprise notebook (IPYNB file).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to manage access to a Colab Enterprise notebook, ask your administrator to grant you the Colab Enterprise Admin ([`roles/aiplatform.colabEnterpriseAdmin`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.colabEnterpriseAdmin)) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Grant access to a notebook

This section describes how to grant a principal access to a Colab Enterprise notebook.

**Important:** Users who have access to the notebook can see all output generated by code in the notebook. Users can see this output even if the output contains data from resources that they don't have access to. To prevent saved output from being shared, turn off notebook output saving.

To grant a principal access to a Colab Enterprise notebook, do the following:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Next to the notebook that you want to share, click the more_vert**Notebook actions** menu and select **Share**. 

  4. In the **Share permissions** window, click ![](https://docs.cloud.google.com/static/colab/images/icon-add-principal.png) **Add user/group**. 

  5. In the **Add user/group** dialog, in the **New principals** field, enter one or more principals with commas between them. 

  6. In the **Role** list, select one of the following roles:

     * [**Code Owner**](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeOwner): Can perform any action on the notebook, including deleting or sharing it. 
     * [**Code Editor**](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeEditor): Can edit the notebook. 
     * [**Code Viewer**](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeViewer): Can view the notebook. 
The principal must also have the [Notebook Runtime User (`roles/aiplatform.notebookRuntimeUser`)](https://docs.cloud.google.com/colab/docs/access-control#aiplatform.notebookRuntimeUser) role to run the notebook. 
  7. Click **Save**.




## Colab Enterprise principals are users, groups, or domains

You can grant access to users, groups, or domains. See the following table:

Principal | Example user account  
---|---  
Single user | `user@gmail.com`  
Google group | `admins@googlegroups.com`  
Google Workspace domain | `example.com`  
  
## Turn off notebook output saving

To prevent sharing saved notebook output with other users who have access to the notebook file, you can turn off notebook output saving.

When you turn off output saving for a selected notebook, Colab Enterprise deletes all output saved in the notebook file and doesn't save the output of subsequent runs.

However, users who have access to the notebook can still view its output in the following ways:

  * Run the notebook to view its current output. This output isn't saved.

  * View an archival version of the notebook and its output in revision history.




To turn off output saving for a selected notebook, do the following:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. To open a notebook, click its name.

  4. Click arrow_drop_down **Toggle header visibility** > **Edit** > **Notebook settings**. 

  5. In the **Notebook settings** window, select **Omit code cell output when saving this notebook**. 

  6. Click **Save**.

  7. Click **Reload**.




## Revoke access to a notebook

**Caution:** When a user creates a Colab Enterprise notebook, they are automatically granted the [Code Owner (`roles/dataform.codeOwner`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeOwner) role on that notebook. This is a resource-level role that is separate from any project-level roles. Removing a user's project-level IAM roles **doesn't** automatically remove their resource-level roles on notebooks they created. To fully revoke a user's access, you must remove both project-level and resource-level roles as described in this section. For more information, see [Security considerations](https://docs.cloud.google.com/colab/docs/access-control#security-considerations).

### Remove project-level access

To remove a principal's project-level access:

  1. In the Google Cloud console, go to the **IAM** page.

[ Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. Find the row containing the principal whose access you want to revoke. Then, click  edit **Edit principal** in that row.

**Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted.
  4. Click the **Delete** delete button for the role that you want to revoke, and then click **Save**.




### Remove resource-level access from a notebook

To remove a principal's resource-level access from a specific notebook:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Next to the notebook, click the more_vert**Notebook actions** menu and select **Share**. 

  4. In the **Share permissions** window, find the principal whose access you want to revoke.

  5. Click the **Delete** delete button next to the principal, and then click **Save**.




### Revoke all access using an IAM Deny policy

As an alternative to removing individual resource-level roles, you can use an [IAM Deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) to revoke all of a principal's permissions across all resources in a project. This approach is useful when you need to quickly revoke access from all resources without iterating over each notebook individually.

## What's next

  * To learn how to grant access to a runtime template, see [Manage access to a runtime template](https://docs.cloud.google.com/colab/docs/manage-access-runtime-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
