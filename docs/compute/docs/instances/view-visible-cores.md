---
url: https://docs.cloud.google.com/compute/docs/instances/view-visible-cores/
title: View the number of visible CPU cores \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:32:00.899475+00:00
---

# View the number of visible CPU cores  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-visible-cores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View the number of visible CPU cores Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to view the number of visible CPU cores for a virtual machine (VM) instance.

When you [view the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details), you can verify if the VM has the default number of visible CPU cores, or if this number has been customized. Reducing the number of visible CPU cores for a VM can help reduce licensing costs without reducing Persistent Disk performance limits. However, reducing the number of visible CPU cores might affect network performance.

**Note:** Reducing the number of visible CPU cores for a VM might impact the performance of the VM. For more information, see [Performance considerations](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores#performance_considerations).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permission that you need to view the details of a VM, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the VM or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.instances.get` permission, which is required to view the details of a VM. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View the number of visible CPU cores for a VM

To determine if the number of visible CPU cores was customized for a VM, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM.

The details page of the VM opens and the **Details** tab is selected.

  3. In the **Machine configuration** section, check the value for **Custom visible cores**. If there is no value displayed, then the VM has the [default number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores).




###  gcloud 

To view the details of the VM, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe).
    
    
    gcloud compute instances describe VM_NAME \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM.

  * `ZONE`: the zone where the VM is located.




If the number of visible CPU cores for the VM was customized, then the output contains the `visibleCoreCount` field as follows:
    
    
    advancedMachineFeatures:
      visibleCoreCount: VISIBLE_CORE_COUNT
    ...
    

If the output doesn't contain the `visibleCoreCount` field, then the VM has the [default number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores).

###  REST 

To view the details of the VM, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VM is located.

  * `ZONE`: the zone where the VM is located.

  * `VM_NAME`: the name of the VM.




If the number of visible CPU cores for the VM was customized, then the output contains the `visibleCoreCount` field as follows:
    
    
    {
      ...
      "advancedMachineFeatures": {
        visibleCoreCount: VISIBLE_CORE_COUNT
      },
      ...
    }
    

If the output doesn't contain the `visibleCoreCount` field, then the VM has the [default number of visible CPU cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores).

## What's next

  * [Customize the number of visible cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores)
  * [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
