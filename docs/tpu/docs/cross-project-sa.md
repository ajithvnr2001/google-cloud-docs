---
url: https://docs.cloud.google.com/tpu/docs/cross-project-sa/
title: Use a cross-project service account \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:18.538419+00:00
---

# Use a cross-project service account  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/cross-project-sa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use a cross-project service account

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This document outlines how to use a cross-project service account when creating a TPU VM. A cross-project service account is a service account that is located in a different project than the TPU VM.

Note, the following instructions don't take Shared VPC or VPC Service Controls into consideration. Additional configurations or permissions may be required to support their use. For more information, see [Create and modify Shared VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Before you begin

  * Create two Google Cloud projects. One to contain the TPU VM (`tpu_project`) and one to contain the service account (`service_project`). For more information, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * Create a service account in the `service_project`. For more information, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  * Create a network and enable Private Google Access. For more information, see [Creating and managing networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and [Configure Private Google Access for an internal IP address](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).
  * Disable the following organization policies. For more information, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints). 
    * `constraints/iam.disableCrossProjectServiceAccountUsage` in both projects
    * `constraints/compute.vmExternalIpAccess` (for accessing the VM with SSH, optional)



## Define environment variables
    
    
    export TPU_PROJECT_ID=tpu-project-id
    export SERVICE_PROJECT_ID=service-project-id
    export SERVICE_ACCOUNT_EMAIL=your_service_account@$(SERVICE_PROJECT_ID).iam.gserviceaccount.com
    export ZONE=your-zone
    export TPU_NAME=your-tpu-name
    export NETWORK=your-network
    export SUBNET=your-subnet

## Set IAM permissions

  1. Allow your service account to use the TPU Service Agent role in the `tpu_project`.
         
         gcloud projects add-iam-policy-binding ${TPU_PROJECT_ID} \
         --member=serviceAccount:${SERVICE_ACCOUNT_EMAIL} \
         --role=roles/cloudtpu.serviceAgent

  2. Add the serviceAccountUser role to the TPU Service Agent.
         
         gcloud projects add-iam-policy-binding $SERVICE_PROJECT_ID \
         --member=serviceAccount:service-$TPU_PROJECT_ID@gcp-sa-tpu.iam.gserviceaccount.com \
         --role=roles/iam.serviceAccountUser

  3. If your workload is running in Docker containers, allow the Compute Engine Service Agent to access the metadata server.
         
         gcloud iam service-accounts add-iam-policy-binding  \
         --project $SERVICE_PROJECT_ID $SERVICE_ACCOUNT_EMAIL \
         --role roles/iam.serviceAccountTokenCreator \
         --member serviceAccount:service-$TPU_PROJECT_ID@compute-system.iam.gserviceaccount.com




## Create a TPU VM in the `tpu_project`

Create a TPU VM in the `tpu_project` using the service account in the `service_project`.
    
    
    gcloud alpha compute tpus tpu-vm create $TPU_NAME \
        --description=$TPU_NAME \
        --accelerator-type=v5litepod-8 \
        --version=tpu-vm-tf-2.17.0-pod \
        --network=projects/$PROJECT_A/global/networks/$NETWORK \
        --subnetwork=$SUBNET \
        --internal-ips \
        --service-account=$SERVICE_ACCOUNT_EMAIL \
        --project=$TPU_PROJECT_ID \
        --zone=$ZONE

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
