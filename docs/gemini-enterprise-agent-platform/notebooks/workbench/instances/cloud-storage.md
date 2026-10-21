---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/cloud-storage/
title: Access Cloud Storage buckets and files in JupyterLab in a Agent Platform Workbench instance. \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:40:56.903136+00:00
---

# Access Cloud Storage buckets and files in JupyterLab in a Agent Platform Workbench instance.  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback 

#  Access Cloud Storage buckets and files in JupyterLab in a Agent Platform Workbench instance. Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to mount a Cloud Storage bucket to the JupyterLab interface of your Gemini Enterprise Agent Platform Workbench instance so that you can browse files that are stored in Cloud Storage. You can also open and edit files that are compatible with JupyterLab, such as text files and notebook (IPYNB) files.

## Overview

Agent Platform Workbench instances include a Cloud Storage integration that lets you mount a Cloud Storage bucket. This means you can browse the contents of the bucket and work with compatible files from within the JupyterLab interface.

You can access any of the Cloud Storage buckets and files that your instance has access to within the same project as your Agent Platform Workbench instance.

**Note:** Your Agent Platform Workbench instance's access to Cloud Storage is determined by the single user or service account that you used to grant access to your instance. For example, if you granted a specific service account access to your instance, you must also grant that service account access to the Cloud Storage buckets that you want to use in JupyterLab.

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




### Required roles

To get the permissions that you need to mount a Cloud Storage bucket to a Agent Platform Workbench instance, ask your administrator to grant you the following IAM roles: 

  * [Notebooks Runner ](https://docs.cloud.google.com/iam/docs/roles-permissions/notebooks#notebooks.runner) (`roles/notebooks.runner`) on the project
  * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the Agent Platform Workbench instance's service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required permission for enabling shared storage mounting

To enable shared storage mounting in your Agent Platform Workbench instance, ask your administrator to grant your Agent Platform Workbench instance's service account the `storage.buckets.list` permission on the project.

The `storage.buckets.list` permission is required for the **Mount shared storage** button to appear in the JupyterLab interface of your Agent Platform Workbench instance.

##  Create a bucket and a Agent Platform Workbench instance

You must have access to at least one Cloud Storage bucket in the same project as your Agent Platform Workbench instance. 

  1. If you need to create a Cloud Storage bucket, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets). 
  2. If you haven't already, [create a Agent Platform Workbench instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create) in the same project as your Cloud Storage bucket. 



## Open JupyterLab

  1. In the Google Cloud console, go to the **Instances** page.

[Go to Instances](https://console.cloud.google.com/agent-platform/workbench/instances?project=)

  2. Next to your Agent Platform Workbench instance's name, click **Open JupyterLab**. 

Your Agent Platform Workbench instance opens JupyterLab.




## Mount the Cloud Storage bucket

To mount and then access a Cloud Storage bucket, do the following:

  1. In JupyterLab, make sure the folder **File Browser** tab is selected. 

  2. In the left sidebar, click the ![Mount shared storage button](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/notebooks/workbench/images/icon-mount-shared-storage.png) **Mount shared storage** button. If you don't see the button, drag the right side of the sidebar to expand the sidebar until you see the button. 

![The Mount shared storage button in the top right corner of the left sidebar](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/notebooks/workbench/instances/images/mount-shared-storage-button.png)

  3. In the **Bucket name** field, enter the Cloud Storage bucket name that you want to mount. 

  4. Click **Mount**.

  5. Your Cloud Storage bucket appears as a folder in the **File browser** tab of the left sidebar. Double-click the folder to open it and browse the contents. 




## Troubleshoot

To find methods for diagnosing and resolving issues with mounting a Cloud Storage bucket to your instance, see [Troubleshooting Agent Platform Workbench](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/troubleshooting-workbench#instances).

## What's next

  * Learn more about [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction).

  * Learn how to [query data in BigQuery from within JupyterLab](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/bigquery).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
