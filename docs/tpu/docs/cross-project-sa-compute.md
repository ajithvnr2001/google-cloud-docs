---
url: https://docs.cloud.google.com/tpu/docs/cross-project-sa-compute/
title: Use a cross-project service account \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:23.339992+00:00
---

# Use a cross-project service account  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/cross-project-sa-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use a cross-project service account

This document describes how to use a cross-project service account when creating a TPU VM. A cross-project service account is a service account that resides in a different project than the TPU VM.

These instructions do not include considerations for Shared VPC or VPC Service Controls. Additional configurations or permissions might be required to support their use. For more information, see [Create and modify Shared VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

  * Create two Google Cloud projects. One to contain the TPU VM (`TPU_PROJECT`) and one to contain the service account (`SERVICE_PROJECT`). For more information, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * Create a service account in the `SERVICE_PROJECT`. For more information, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  * Create a network and enable Private Google Access. For more information, see [Creating and managing networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and [Configure Private Google Access for an internal IP address](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).
  * Disable the following organization policies. For more information, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints). 
    * `constraints/iam.disableCrossProjectServiceAccountUsage` in both projects
    * `constraints/compute.vmExternalIpAccess` (for accessing the VM with SSH, optional)



## Set IAM permissions

  1. Grant your user account the **Service Account User** role to let it attach the service account to the VM instance.
         
         gcloud iam service-accounts add-iam-policy-binding \
           SERVICE_ACCOUNT_EMAIL \
           --project=SERVICE_PROJECT_ID \
           --member=user:USER_EMAIL \
           --role=roles/iam.serviceAccountUser
         

Replace the following placeholders:

     * `SERVICE_ACCOUNT_EMAIL`: The email address of the service account.
     * `SERVICE_PROJECT_ID`: The ID of the project that contains the service account.
     * `USER_EMAIL`: The email address of the user account.
  2. If your workload runs in Docker containers, grant the Compute Engine Service Agent access to the metadata server.
         
         gcloud iam service-accounts add-iam-policy-binding \
           SERVICE_ACCOUNT_EMAIL \
           --project=SERVICE_PROJECT_ID \
           --role=roles/iam.serviceAccountTokenCreator \
           --member=serviceAccount:service-TPU_PROJECT_ID@compute-system.iam.gserviceaccount.com
         

Replace the following placeholders:

     * `SERVICE_ACCOUNT_EMAIL`: The email address of the service account.
     * `SERVICE_PROJECT_ID`: The ID of the project that contains the service account.
     * `TPU_PROJECT_ID`: The ID of the project that contains the TPU VM.



## Create a TPU VM in the TPU project

Create a TPU VM in the TPU project using the service account in the service project.
    
    
      gcloud compute instances create TPU_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --service-account=SERVICE_ACCOUNT_EMAIL \
        --project=TPU_PROJECT_ID \
        --zone=ZONE \
        --maintenance-policy=TERMINATE
    

Replace the following placeholders:

  * `TPU_NAME`: The name of the TPU VM.
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types).
  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. To install a specific OS version, use the `--image` flag.
  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * `SERVICE_ACCOUNT_EMAIL`: The email address of the service account.
  * `TPU_PROJECT_ID`: The ID of the project that contains the TPU VM.
  * `ZONE`: The zone of the TPU VM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
