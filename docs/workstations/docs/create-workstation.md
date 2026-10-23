---
url: https://docs.cloud.google.com/workstations/docs/create-workstation/
title: Create and launch a workstation \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:06.878514+00:00
---

# Create and launch a workstation  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/create-workstation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Create and launch a workstation Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to get started creating a workstation with Cloud Workstations.

A _workstation_ is a preconfigured development environment that administrators or platform teams define in a _workstation configuration_. The workstation configuration includes the container image used by the workstation. Your administrators choose whether to use one of the Cloud Workstations [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) or whether to provide a reference to a [customized container image](https://docs.cloud.google.com/workstations/docs/customize-container-images).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?journey_id=workstations--set-up--intro&walkthrough_id=workstations--set-up--launch)

* * *

### Before you begin

Before you begin using Cloud Workstations, be sure that you have the [required permissions](https://docs.cloud.google.com/workstations/docs/access-control#enable_required_roles) and that you complete these required setup steps. You can skip this section if you've already completed this setup.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Workstations API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workstations.googleapis.com)

  7. Optional: If you don't have workstation configurations available in the [Google Cloud console](https://console.cloud.google.com/workstations/), ask your administrator to create a workstation configuration for you, or make sure that you have a Cloud Workstations Admin IAM role on the project so that you can create these resources yourself. To check your IAM roles, go to the IAM page in the Google Cloud console:

[ Go to IAM](https://console.cloud.google.com/iam-admin/iam)




## Create a workstation

To create a workstation, follow these steps: 

  1. In the Google Cloud console, navigate to the **Cloud Workstations** > **Workstations** page. 

[Go to Workstations](https://console.cloud.google.com/workstations/list)

  2. Click add_box**Create**.

The **Create** link might be disabled if there aren't any workstation configurations in the project or if you don't have permissions to view them. Ask your organization's Cloud Workstations Admin to create a workstation configuration for you. 

  3. Accept the default workstation **Name**.

If you prefer, you can enter your own resource name for your workstation—for example, `test-workstation`. Follow the Compute Engine resource [naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources) and choose a name that is unique within the workstation cluster. 

  4. Click the arrow_drop_downexpander arrow in the **Configuration** field and select the workstation configuration to define your workstation. 

  5. Click **Create** to create your workstation.




## Launch a workstation

Now that you have created a workstation, launch it to begin development: 

  1. Click **Workstations**.
  2. In the list of workstations, find your workstation name and click **Launch**.
  3. The workstation connects to port `80` by default. If the workstation is stopped, clicking **Launch** also starts it.

**Tip:** You can bookmark the launch page to restart and access your workstation.

Optional: You can also click the arrow_drop_downexpander arrow next to **Launch** and select from the list of launch options:

     * **Start**
     * **Connect to port 80** (default)
     * **Connect to web app on port**
     * **Port forwarding**
     * **Connect using SSH**
     * **Launch with JetBrains Gateway** (if you are using a JetBrains IDE)

The **Start** option starts the workstation without launching it. 

  4. The following example shows the welcome page for the Cloud Workstations [base editor](https://docs.cloud.google.com/workstations/docs/base-editor-overview). Your page might look different, depending on how you define your workstation configuration:

![Cloud Workstations base editor](https://docs.cloud.google.com/static/workstations/images/workstations-code-oss-sample-welcome-page.png)

For more information about connecting through SSH, see [SSH support](https://docs.cloud.google.com/workstations/docs/ssh-support).

For more information about connecting to web apps running on your workstation, see [Access HTTP servers running on a workstation](https://docs.cloud.google.com/workstations/docs/access-http-servers-running-on-workstations).




## Clean up

To delete a workstation from the Google Cloud console:

  1. In the Google Cloud console, go to **Cloud Workstations** > **Workstations**.
  2. Select the checkbox beside the workstation that you want to delete.
  3. Click themore_vert**More** options menu and select **Delete** to delete the selected workstation.



If your workstation configuration uses persistent disks and the [reclaim policy](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs#reclaimpolicy) is set to retain persistent disks after you delete the workstation, be sure to remind your Cloud Workstations Admin to manually delete the persistent disk for you. For more about deleting workstation configurations, workstation clusters, and Google Cloud projects, see [Delete resources](https://docs.cloud.google.com/workstations/docs/delete-resources).

## What's next

  * Use the [Cloud Workstations base editor](https://docs.cloud.google.com/workstations/docs/base-editor-overview).

  * Learn more about configuring additional options in your [workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration).

  * Customize your [workstation configuration](https://docs.cloud.google.com/workstations/docs/customize-development-environment) through the API.

  * Create [customized container images](https://docs.cloud.google.com/workstations/docs/customize-container-images) that extend the [preconfigured base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) provided by Cloud Workstations.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
