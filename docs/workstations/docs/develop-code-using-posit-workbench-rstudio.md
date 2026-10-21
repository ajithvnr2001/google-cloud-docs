---
url: https://docs.cloud.google.com/workstations/docs/develop-code-using-posit-workbench-rstudio/
title: Develop code using Posit Workbench (including RStudio Pro) \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:10.710651+00:00
---

# Develop code using Posit Workbench (including RStudio Pro)  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/develop-code-using-posit-workbench-rstudio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Develop code using Posit Workbench (including RStudio Pro) Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** A third-party provider maintains the container image listed in this section. Google Cloud does not build, maintain, or officially support this image. Carefully evaluate any solution before deploying it in your production environment.

Learn how to start developing code using Posit Workbench and RStudio Pro with Cloud Workstations. This guide takes you through configuring your environment, creating a workstation, and launching a RStudio Pro session.

## Before you begin

This guide covers steps for administrators to set up Cloud Workstations and for developers to use the workstations. 

To set up Cloud Workstations, complete the following steps: 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud Workstations API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workstations.googleapis.com)




### Required roles

To get the permissions that you need to manage and use workstations, ask your administrator to grant you the following IAM roles: 

  * Create and manage workstation clusters and configurations: [Cloud Workstations Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.admin) (`roles/workstations.admin`) on the project 
  * Create workstations using a configuration: [Cloud Workstations Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.workstationCreator) (`roles/workstations.workstationCreator`) on the project or the workstation configuration 
  * Use a workstation: [Cloud Workstations User ](https://docs.cloud.google.com/iam/docs/roles-permissions/workstations#workstations.user) (`roles/workstations.user`) on the workstation. This is automatically granted on workstations you create. 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For a detailed overview of all Cloud Workstations roles, see [Access control with IAM](https://docs.cloud.google.com/workstations/docs/access-control). 

## Create the workstation configuration

To use Posit Workbench (including RStudio Pro) the you must create a workstation configuration for the developers in your organization:

  1. Find your Posit Workbench license key and keep it nearby because you need it in a subsequent step. If you need a Posit Workbench license key, contact your Posit Customer Success representative or email [sales@posit.co](mailto:sales@posit.co).

  2. Follow the instructions to [create a workstation configuration](https://docs.cloud.google.com/workstations/docs/create-configuration).

     1. When you get to the [Environment customization](https://docs.cloud.google.com/workstations/docs/create-configuration#customize_the_environment) step, select **Code editors on base images**.

     2. From the **Code editors** menu, select '**Posit Workbench (including RStudio Pro)** Third-party provided'.

     3. Click the arrow_drop_downexpander arrow in the **Advanced container options** section.

        1. Go to the **Environment variables** section, and then click **Add variable**.

        2. Enter `RSW_LICENSE` in the **Key** field and paste your Posit Workbench license key into the **Value** field.

![](https://docs.cloud.google.com/static/workstations/images/posit-license-environment-variable.png)

        3. Click **Continue**.

     4. When you get to the [Add users](https://docs.cloud.google.com/workstations/docs/create-configuration#add_users) step, give your developers [Cloud Workstations IAM access permissions](https://docs.cloud.google.com/workstations/docs/access-control) to the workstation configuration.

     5. To create your workstation configuration and add these users to it, click **Create**.

If you also elected to create a new cluster, cluster creation can take up to 20 minutes.

Developers in your team should now be able to create workstations with Posit Workbench.




## Set up your workstation

To create a workstation, follow these steps:

  1. In the Google Cloud console, navigate to the **Cloud Workstations** > **Workstations** page. 

[Go to **Workstations**](https://console.cloud.google.com/workstations/list)

  2. Click add_box**Create**.

The **Create** link might be disabled if there aren't any configurations in the project or if you don't have permissions to view them. Ask your organization's Cloud Workstations Admin to create a workstation configuration for you.

  3. Enter your workstation **Name**.

Follow the Compute Engine resource [naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources) and choose a name that is unique within the workstation cluster. 

  4. Click the arrow_drop_downexpander arrow in the **Configuration** field and select the **Posit Workbench (Third-party)** workstation configuration.

  5. Click **Create** to create your workstation.




## Launch your workstation

Now that you have created your workstation, you can start it and then launch it to begin development:

  1. Click **Workstations**.
  2. Find the workstation that you created in the list of available workstations, select the checkbox beside it, and then click **Start**. This starts your workstation, and matches it to the parent workstation configuration.
  3. If prompted to start your workstation, click **Start** to confirm. The status changes to **Starting** and the status icon refreshspins while the start operation is in progress. It might take a few minutes to start your workstation.
  4. When your workstation is ready, the status changes to **Running** and the status icon changes to a check_circle checkmark.
  5. Click **Launch**.



## Launch a Posit Workbench RStudio Pro session

  1. The following example shows the welcome page for the Posit Workbench. Your page might look different, depending on how your organization defines your workstation configuration:

![](https://docs.cloud.google.com/static/workstations/images/posit-welcome-page.png)

  2. Click **New Session**.

  3. Select **RStudio Pro** as the IDE and leave **Cluster** set to **Local**.

![](https://docs.cloud.google.com/static/workstations/images/posit-new-session.png)

For more information about Posit Workbench and the IDEs that it supports, such as Jupyter Notebook, JupyterLab, and VS Code, see the [Posit documentation](https://docs.posit.co/ide/server-pro/user/).

  4. Click **Start Session**.

  5. Wait for the session to start up and then begin coding!

![](https://docs.cloud.google.com/static/workstations/images/posit-rstudio-pro-session.png)




## Upload files to your workstation

  1. To upload files from your local machine to your workstation, click **Upload**.

![](https://docs.cloud.google.com/static/workstations/images/posit-upload.png)

  2. Select the **Target directory** where you want to store files on your workstation.

  3. Click **Choose File** to select the file to upload.

  4. To begin the upload, click **OK**.




To upload multiple files or a directory, create a ZIP file. The ZIP file is expanded after upload.

## Import files from your workstation

  1. To import files from your workstation, click **Import dataset** and select the type of dataset.

![](https://docs.cloud.google.com/static/workstations/images/posit-import.png)

  2. Navigate to and select the dataset to import from your workstation.

The Posit Workbench IDE has dependencies on various R packages for different pieces of features. For example, if you are uploading an Excel file, certain packages need to be installed. If prompted to install required packages, click **Yes**.

  3. To begin the import, click **Import**.




## Get support for Posit Workbench issues

If you encounter issues with Posit Workbench or with the Posit Workbench container image, report them to Posit at [support@posit.co](mailto:support@posit.co).

## What's next

  * Learn how to [customize container images](https://docs.cloud.google.com/workstations/docs/customize-container-images) to your organization's needs.

  * Refer to the Posit Software [documentation hub](https://docs.posit.co/) to learn more about Posit Workbench.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
