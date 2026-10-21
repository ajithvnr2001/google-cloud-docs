---
url: https://docs.cloud.google.com/cpp/docs/quickstart-cloud-shell/
title: Quickstart: Run C++ Examples in Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:55.555574+00:00
---

# Quickstart: Run C++ Examples in Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/quickstart-cloud-shell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Guides ](https://docs.cloud.google.com/cpp/docs/setup)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run C++ Examples in Cloud Shell

Learn how to compile and run the C++ client examples in Cloud Shell using [micromamba](https://mamba.readthedocs.io/en/latest/micromamba-installation.html) and [Conda](https://conda.io/)

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Storage API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable storage.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Cloud Storage API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable storage.googleapis.com

  14. Create a Cloud Storage bucket run the examples:

     1. Ensure that you have the Storage Admin role (`roles/storage.admin`) on the project. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create a Cloud Storage bucket: 
            
            gcloud storage buckets create gs://BUCKET_NAME

Replace `BUCKET_NAME` with a bucket name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). 
  15. Ensure that the following tools are installed: 
     * [Curl](https://curl.se/download.html)
     * [Git](https://git-scm.com/downloads)



## Install pre-compiled C++ Client Libraries in Cloud Shell

  1. In Cloud Shell, install `micromamba`:
         
         curl -fsSL https://micro.mamba.pm/api/micromamba/linux-64/latest | sudo tar -C /usr -xj bin/micromamba
         

  2. Add `micromamba` hooks to the current shell:
         
         eval "$(/usr/bin/micromamba shell hook -s posix)"
         

  3. Use `micromamba` to create a Conda environment with the necessary development tools and libraries:
         
         micromamba create -y -n base -c conda-forge cmake ninja cxx-compiler google-cloud-cpp libgoogle-cloud
         

  4. Activate the new conda environment:
         
         micromamba activate
         




## Checkout and compile the "Storage Quickstart" example

  1. Checkout the C++ Client Library source code, including the quickstart examples for all services:
         
         git clone --depth 1 https://github.com/googleapis/google-cloud-cpp
         

  2. Configure CMake to compile the "Storage Quickstart" example:
         
         cmake -S google-cloud-cpp/google/cloud/storage/quickstart -B .build
         

  3. Compile the example:
         
         cmake --build .build
         

  4. Run the example:
         
         .build/quickstart BUCKET_NAME
         

  5. After running this example, you'll see a message similar to `Successfully created object ...` followed by data specific to your object and ending with a line that shows `Hello World!`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. Delete the object created by the example:
         
         gcloud storage rm gs://BUCKET_NAME/quickstart.txt
         

  2. Delete the bucket:
         
         gcloud storage buckets delete gs://BUCKET_NAME
         




## What's next

  * Find more [C++ examples](https://docs.cloud.google.com/docs/samples/?language=cpp).
  * Deploy a [C++ application](https://github.com/GoogleCloudPlatform/cpp-samples/tree/main/getting-started) to Cloud Run and Google Kubernetes Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
