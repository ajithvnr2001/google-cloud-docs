---
url: https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-notebooks/
title: Use TensorFlow Enterprise with a user-managed notebooks instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:40.525782+00:00
---

# Use TensorFlow Enterprise with a user-managed notebooks instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-notebooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ TensorFlow Enterprise ](https://docs.cloud.google.com/tensorflow-enterprise/docs)
  * [ Guides ](https://docs.cloud.google.com/tensorflow-enterprise/docs/getting-started)



Send feedback 

#  Use TensorFlow Enterprise with a user-managed notebooks instance Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Workbench user-managed notebooks is deprecated. Support for user-managed notebooks will end soon and the ability to create user-managed notebooks instances will be removed. For the end of availability date, see [Vertex AI deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations). 

This page provides a brief overview of [Vertex AI Workbench user-managed notebooks instances](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/introduction) and describes how to get started using TensorFlow Enterprise in a user-managed notebooks instance.

In this example, you create a TensorFlow Enterprise user-managed notebooks instance, open a JupyterLab notebook, and run a classification tutorial on using neural networks with Keras.

## Overview of Vertex AI Workbench user-managed notebooks instances

Vertex AI Workbench user-managed notebooks instances let you create and manage deep learning virtual machine (VM) instances that are prepackaged with [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html).

User-managed notebooks instances have a preinstalled suite of deep learning packages, including support for the TensorFlow and PyTorch frameworks. You can configure either CPU-only or GPU-enabled instances.

Your user-managed notebooks instances are protected by Google Cloud authentication and authorization and are available by using a user-managed notebooks instance URL. User-managed notebooks instances also integrate with [GitHub](https://github.com/) and can sync with a GitHub repository.

## Before you begin

Before you can create a user-managed notebooks instance, you must have a Google Cloud project and enable the Notebooks API for that project. 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Notebooks API. 

**Roles required to enable APIs**

To enable APIs, you need the Service Usage Admin IAM role (`roles/serviceusage.serviceUsageAdmin`), which contains the `serviceusage.services.enable` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=notebooks.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Notebooks API. 

**Roles required to enable APIs**

To enable APIs, you need the Service Usage Admin IAM role (`roles/serviceusage.serviceUsageAdmin`), which contains the `serviceusage.services.enable` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=notebooks.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

If you created the project, you have the Owner (`roles/owner`) IAM role on the project, which includes all required permissions. Skip this section and start creating your user-managed notebooks instance. If you didn't create the project yourself, continue in this section. 

To get the permissions that you need to create a Vertex AI Workbench user-managed notebooks instance, ask your administrator to grant you the following IAM roles on the project: 

  * Notebooks Admin ([`roles/notebooks.admin`](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/iam#notebooks.admin)) 
  * Service Account User ([`roles/iam.serviceAccountUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser)) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a user-managed notebooks instance

To create a default TensorFlow Enterprise 2.13 user-managed notebooks instance, complete the following steps.

  1. In the Google Cloud console, go to the **User-managed notebooks** page.

[Go to User-managed notebooks](https://console.cloud.google.com/vertex-ai/workbench/user-managed)

  2. Click add_box **Create new**.

  3. In **Environment** , select **TensorFlow Enterprise 2.13**.

  4. If you want to include a GPU, you must select the option to **Attach 1 NVIDIA T4 GPU**. You can adjust the number of GPUs later if you need to. For information about adjusting the number of GPUs, see [Change machine type and configure GPUs of a user-managed notebooks instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/manage-hardware-accelerators).

  5. Click **Create**.

  6. Vertex AI Workbench automatically starts the instance. When the instance is ready to use, Vertex AI Workbench activates an **Open JupyterLab** link. 




## Open the notebook

To open a user-managed notebooks instance, complete the following steps: 

  1. In the Google Cloud console, next to your user-managed notebooks instance's name, click **Open JupyterLab**.

  2. Your user-managed notebooks instance opens JupyterLab. 




## Run a classification tutorial in your notebook instance

Complete these steps to try out your new notebook by running a classification tutorial:

  1. In the JupyterLab folder **File Browser** , double-click the **tutorials** folder to open it, and navigate to and open **tutorials/keras/basic_classification.ipynb**.

![](https://docs.cloud.google.com/static/vertex-ai/docs/workbench/images/jupyterlab-tutorials-folder.png)

  2. To run cells of the tutorial, click the play_arrow run button.




## What's next

  * Learn more about [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction).
  * Get started [using TensorFlow Enterprise with Deep Learning VM](https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-vm).
  * Get started [using TensorFlow Enterprise with Deep Learning Containers](https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-containers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-14 UTC."],[],[]] 
