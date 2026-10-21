---
url: https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-vm/
title: Use TensorFlow Enterprise with Deep Learning VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:55.486237+00:00
---

# Use TensorFlow Enterprise with Deep Learning VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ TensorFlow Enterprise ](https://docs.cloud.google.com/tensorflow-enterprise/docs)
  * [ Guides ](https://docs.cloud.google.com/tensorflow-enterprise/docs/getting-started)



Send feedback 

#  Use TensorFlow Enterprise with Deep Learning VM Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a brief overview of [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs) and describes how to get started using TensorFlow Enterprise with a Deep Learning VM instance.

In this example, you create a TensorFlow Enterprise Deep Learning VM instance, connect to the instance using SSH, open a JupyterLab notebook, and run a classification tutorial on using neural networks with Keras.

## Overview of Deep Learning VM

Deep Learning VM Images is a set of virtual machine images optimized for data science and machine learning tasks. All images come with key ML frameworks and tools pre-installed. You can use them out of the box on instances with GPUs to accelerate your data processing tasks.

Deep Learning VM images are available to support many combinations of framework and processor. There are currently images supporting [TensorFlow Enterprise](https://docs.cloud.google.com/tensorflow-enterprise/docs), TensorFlow, PyTorch, and generic high-performance computing, with versions for both CPU-only and GPU-enabled workflows.

To see a list of frameworks available, see [Choosing an image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

## Before you begin

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




## Create a Deep Learning VM instance

To create a TensorFlow Enterprise Deep Learning VM instance, complete these steps:

  1. Go to the Deep Learning VM Cloud Marketplace page in the Google Cloud console.

[Go to the Deep Learning VM Cloud Marketplace page](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/deeplearning)

  2. Click **Launch on Compute Engine**. If you see a project selection window, choose the project in which to create the instance. If this is the first time you've launched Compute Engine, you must wait for the initial API configuration process to complete.

  3. On the **New Deep Learning VM deployment** page, enter a **Deployment name**. This will be the root of your virtual machine name. Compute Engine appends `-vm` to this name when creating your instance.

  4. Under **Number of GPUs** , select **None**. You won't need them to complete the instructions in this guide.

**Note:** If you plan to use GPUs with your TensorFlow Enterprise instance, [check the quotas page](https://console.cloud.google.com/quotas) to ensure that you have enough GPUs available in your project. If GPUs are not listed on the quotas page, or you require additional GPU quota, you can request a quota increase. See [Requesting additional quota](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota) on the Compute Engine [Resource Quotas](https://docs.cloud.google.com/compute/quotas) page.
  5. Under **Framework** , select **TensorFlow Enterprise 2.3 (CUDA 11.0)**.

  6. For this example, you can leave the remaining settings as they are.

  7. Click **Deploy**.




You've just created your first instance of a Deep Learning VM. After the instance is created, the [Deployment Manager](https://console.cloud.google.com/dm/deployments) opens. This is where you can manage your Deep Learning VM instance and other deployments.

## Connect with SSH, open a notebook, and run a classification tutorial

Complete these steps to set up an SSH connection to your Deep Learning VM instance, open a JupyterLab notebook, and run a tutorial on using neural networks with Keras:

  1. To complete these steps, you can use either [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) or any environment where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) can be installed. You can use the gcloud CLI to interface with your instance.

     * If you want to use Cloud Shell, in Google Cloud, in the upper-right corner, click the **Activate Cloud Shell** button.

![Google Cloud Platform console](https://docs.cloud.google.com/static/shell/docs/images/shell_icon.png)

     * If you want to use gcloud CLI, [download and install Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) on your local machine.

  2. In [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) or in a local terminal window, use the following command to create an SSH connection to your instance. Replace my-project-id, my-zone, and my-instance-name with the relevant information.
         
         gcloud compute ssh --project my-project-id --zone my-zone \
           my-instance-name -- -L 8080:localhost:8080
         

**Note:** To find your project ID, click the project name at the top of the Google Cloud console. To find your zone, click your instance in the [Deployment Manager](https://console.cloud.google.com/dm/deployments).
  3. In your local browser, visit http://localhost:8080 to access a JupyterLab notebook that is included in your instance by default.

  4. In the notebook, on the left, double-click **tutorials** to open the folder, and navigate to and open **tutorials/tf2_course/01_neural_nets_with_keras.ipynb**.

  5. Click the run button play_arrow to run cells of the tutorial.




## What's next

  * Learn more about [Deep Learning VM](https://docs.cloud.google.com/deep-learning-vm/docs).
  * [Learn more about the Deep Learning VM community](https://docs.cloud.google.com/deep-learning-vm/docs/getting-support#get_support_from_the_community), where you can discuss and ask questions about Deep Learning VM.
  * Get started [using TensorFlow Enterprise with Deep Learning Containers](https://docs.cloud.google.com/tensorflow-enterprise/docs/use-with-deep-learning-containers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
