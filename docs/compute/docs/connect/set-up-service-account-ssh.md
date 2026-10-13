---
url: https://docs.cloud.google.com/compute/docs/connect/set-up-service-account-ssh/
title: Connect using service accounts \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:36.081548+00:00
---

# Connect using service accounts  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/set-up-service-account-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect using service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use a [service account](https://docs.cloud.google.com/compute/docs/access/service-accounts) to connect to Compute Engine virtual machine (VM) instances using SSH. Setting up SSH for a service account lets you to [configure apps to use SSH](https://docs.cloud.google.com/compute/docs/tutorials/service-account-ssh), which can help you to automate your workloads.

## Before you begin

  * [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Manually connect to VMs as a service account

To connect to VMs as a service account, use one of the following methods:

**Note:** If you are connecting from a machine that is hosted outside of Google Cloud you must directly impersonate the service account.

###  Directly impersonate service account 

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All the permissions included in the [Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`)](https://docs.cloud.google.com/compute/docs/access/iam#the_serviceaccountuser_role), on the service account. For details about how to grant this role on a singular service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).
  * If you use OS Login, you require all the permissions included one of the [OS Login IAM roles](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#grant-iam-roles) on the service account.
  * If you don't use OS Login, the service account also requires the `compute.projects.setCommonInstanceMetadata` permission.



Use the gcloud CLI [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) to connect directly to a VM using a service account's identity. Run the following command to connect to a VM as a service account:
    
    
    gcloud compute ssh VM_NAME \
        --impersonate-service-account=SERVICE_ACCOUNT_EMAIL
    

Replace the following:

  * `VM_NAME`: the name of the VM you want to connect to the service account as.
  * `SERVICE_ACCOUNT_EMAIL`: the email address associated with the service account.



###  Impersonate service account from a VM 

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions included in the [Service Account User role (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/compute/docs/access/iam#the_serviceaccountuser_role) on the service account and your user account. For details about how to grant this role on a singular service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).
  * If you use OS Login, you require all the permissions included one of the [OS Login IAM roles](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin#grant-iam-roles) on the service account and your user account.
  * If you don't use OS Login, you also require the `compute.projects.setCommonInstanceMetadata` permission on the service account and your user account.



You must additionally [assign your service account to a VM and set the `cloud-platform` access scope](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) on the VM.

Impersonate a service account from another VM by doing the following:

  1. [Connect to the VM that runs as a service account](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#connect_to_vms).
  2. From the VM that runs as a service account, connect to other VMs using the same methods.

**Note:** Connection attempts made from within the VM that runs as the service account use the service account's identity.



## What's next

  * Learn how to [configure apps to use SSH](https://docs.cloud.google.com/compute/docs/tutorials/service-account-ssh).
  * Learn more about [how SSH connections work in Compute Engine](https://docs.cloud.google.com/compute/docs/instances/ssh), including SSH key configuration and storage.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
