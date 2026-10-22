---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench/
title: Manage notebooks \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:15.782648+00:00
---

# Manage notebooks  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage notebooks Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Workbench is a single development environment for the entire data science workflow. To set up an end-to-end notebook-based production environment, create JupyterLab instances with built-in integrations. If you are new to Vertex AI, [learn more about Vertex AI Workbench](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench-intro).

This page describes the process of managing JupyterLab notebooks in Vertex AI Workbench, including creating and sharing notebooks and using notebooks to interact with Vertex AI services. This page also shows how to delete and update the JupyterLab instances that host your notebooks.

For information about backing up and restoring data, see [Create a backup and restore notebook data](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data).

## Before you begin

Before using Vertex AI Workbench to manage notebooks, you must have a project ready to run Vertex AI services. For more information, see [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project).

To get the permissions you need to manage notebook resources within a project namespace, ask your IAM Project Admin to grant you one of the following roles:

  * **Workbench Notebooks Admin** (`workbench-notebooks-admin`): Get read and write access to all notebook resources in a project. You need this role to create JupyterLab notebooks.
  * **Workbench Notebooks Viewer** (`workbench-notebooks-viewer`): Get read-only access to all notebook resources in a project. You need this role to open JupyterLab notebooks.



For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

## Create a JupyterLab notebook

This section describes configuring a JupyterLab instance in Vertex AI Workbench and creating a JupyterLab notebook in the instance.

**Note:** All JupyterLab instances have JupyterLab 3 preinstalled.

After meeting the prerequisites, follow these steps to configure a JupyterLab instance and create a JupyterLab notebook:

  1. [Sign in to the GDC console and select your project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in).
  2. In the navigation menu, click **Vertex AI** > **Workbench**.
  3. Click add_box**New notebook**.
  4. On the **Create notebook** page, enter values for the following fields:

     * **Notebook name** : enter the name you want to give to your JupyterLab notebook. Vertex AI Workbench uses the name you choose to create a URL for accessing your notebook.
     * **Environment** : select a Docker image for your JupyterLab instance. This image provides a baseline for deployment and typical machine learning (ML) packages.
     * **Cluster** : select a Kubernetes cluster for your JupyterLab instance that meets your usage requirements. If a Kubernetes cluster isn't available, work with your administrator to add one or more clusters.
     * **CPUs / Memory** : enter the amount of CPUs and RAM you need for your workloads. For CPU-intensive workloads, you can choose more than one CPU.
     * **GPUs** : select the number of GPUs you need for your JupyterLab instance. In Distributed Cloud, a GPU is one NVIDIA Multi-Instance GPU (MIG) slice of an A100 Tensor Core GPU.
     * **Workspace volume** : enter the storage size you need in GB.
  5. Click **Create**.




Vertex AI Workbench configures the JupyterLab instance and creates your JupyterLab notebook. Save the notebook's URL for future access.

**Tip:** Bookmark the URL of the JupyterLab notebook for fast access.

After you create a JupyterLab notebook in Vertex AI Workbench, open the integrated development environment (IDE) in the JupyterLab environment. For more information, see Open a JupyterLab notebook.

## Open a JupyterLab notebook

Enter the URL of a JupyterLab notebook in a web browser to open it. If you don't know the URL, follow these steps to open the notebook:

  1. [Sign in to the GDC console and select your project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in).
  2. In the navigation menu, click **Vertex AI** > **Workbench**.
  3. Find the JupyterLab notebook you want to open and click **Open JupyterLab** to open the JupyterLab instance IDE.
  4. If prompted to authenticate, follow the authentication steps for your identity provider.
  5. In the JupyterLab instance, open the JupyterLab notebook.



Share the URL of a JupyterLab notebook with other users so that they can open it too. The intended user must have the Workbench Notebooks Viewer role.

## Use Vertex AI services from a JupyterLab notebook

Use [client libraries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries) to interact with a Vertex AI service from a JupyterLab notebook. Vertex AI client libraries let you programmatically make API calls to any Vertex AI service on Distributed Cloud.

Follow these steps to use a Vertex AI service from a JupyterLab notebook:

  1. [Enable the corresponding Vertex AI API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-enable-pre-trained-apis).
  2. [Install the corresponding Vertex AI client library](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-install-libraries).
  3. Create a JupyterLab notebook.
  4. Open the JupyterLab notebook and use it to write code with the Vertex AI client libraries. For example, you can [translate text](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation) using the Vertex AI Translation client library.



## Delete a JupyterLab instance

**Tip:** Before deleting JupyterLab instances, consider creating backups of files in a storage bucket. For more information, see [Upload and download storage objects in projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/upload-download-storage-objects).

Follow these steps to delete a JupyterLab instance:

  1. [Sign in to the GDC console and select your project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in).
  2. In the navigation menu, click **Vertex AI** > **Workbench**.
  3. Find the notebook associated with the JupyterLab instance you want to delete.
  4. Select the checkbox of the JupyterLab notebook.
  5. Click **Delete**.
  6. In the **Delete notebooks** dialog, click **Delete**.



## Update a JupyterLab instance

After your Infrastructure Operator (IO) updates Distributed Cloud, you can update your JupyterLab instances.

Follow these steps for each JupyterLab instance you want to update:

  1. Save the files from the JupyterLab instance you want to retain to a storage bucket. For more information, see [Upload and download storage objects in projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/upload-download-storage-objects).
  2. After the update, [sign in to the GDC console and select your project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in).
  3. Configure a new JupyterLab instance. Vertex AI Workbench creates a JupyterLab instance with a new version of JupyterLab. For example, the new JupyterLab instance contains client library updates from Distributed Cloud.
  4. Copy the files from the storage bucket of the outdated JupyterLab instance to the new JupyterLab instance.



You can delete the previous version of your JupyterLab instance. For more information, see Delete a JupyterLab instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
