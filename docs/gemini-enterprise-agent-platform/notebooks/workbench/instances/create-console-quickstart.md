---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-console-quickstart/
title: Quickstart: Create a Agent Platform Workbench instance by using the Google Cloud console \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:22.173015+00:00
---

# Quickstart: Create a Agent Platform Workbench instance by using the Google Cloud console  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-console-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an instance by using the Google Cloud console

Learn how to create a Gemini Enterprise Agent Platform Workbench instance and open JupyterLab by using the Google Cloud console. This page also describes how to stop, start, reset, or delete an instance.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Notebooks API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=notebooks.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Notebooks API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=notebooks.googleapis.com&redirect=https%3A//console.cloud.google.com)


**Note:** The [Notebooks API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest) lets you manage Agent Platform Workbench resources. For managing Agent Platform resources, see the [Agent Platform API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest).

### Required roles

To get the permissions that you need to create and manage a Agent Platform Workbench instance, ask your administrator to grant you the [Notebooks Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.admin) (`roles/notebooks.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an instance

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)

  2. Click add_box **Create new**.

  3. For **Name** , enter `my-instance`.

  4. Click **Create**.




When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Open JupyterLab

After you create your instance, Agent Platform Workbench automatically starts the instance. The **Open JupyterLab** link is initially disabled while the instance is provisioning. Wait for the instance status to become active.

When the instance is ready to use, next to your instance's name, click **Open JupyterLab**.

Your Agent Platform Workbench instance opens JupyterLab.

## Open a new notebook file

  1. In JupyterLab, select **File > New > Notebook**.

  2. In the **Select kernel** dialog, select **Python 3** , and then click **Select**.

Your new notebook file opens.




## Stop your instance

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)

  2. Select the instance that you want to stop.

  3. Click square **Stop**.




## Start your instance

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)

  2. Select the instance that you want to start.

  3. Click arrow_right **Start**.




## Reset your instance

Resetting an instance forcibly wipes the memory contents of your instance and resets the instance to its initial state. To learn more about how resetting an instance works, see [Reset operation](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#resetting-instance).

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)

  2. Select the instance that you want to reset.

  3. Click ![Reset icon](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/notebooks/workbench/images/reset.png)**Reset** , and then click **Reset** to confirm.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

If you created a new project to learn about Agent Platform Workbench instances and you no longer need the project, then [delete the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

If you used an existing Google Cloud project, then delete the resources you created to avoid incurring charges to your account:

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances)

  2. Select the row containing the instance that you want to delete.

  3. Click delete **Delete**. (Depending on the size of your window, the **Delete** button might be in the more_vert options menu.)

  4. To confirm, click **Confirm**.




## What's next

  1. Read the [Introduction to Agent Platform Workbench instances](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/introduction). 
  2. To use a notebook to help you get started using Gemini Enterprise Agent Platform and other Google Cloud services, see [Agent Platform notebook tutorials](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/jupyter-notebooks). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
