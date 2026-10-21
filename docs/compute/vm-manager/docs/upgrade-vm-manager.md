---
url: https://docs.cloud.google.com/compute/vm-manager/docs/upgrade-vm-manager/
title: Update VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:18.134103+00:00
---

# Update VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/upgrade-vm-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Update VM Manager Stay organized with collections  Save and categorize content based on your preferences. 

On Compute Engine you can manage the operating systems that are running on your virtual machines (VMs) by using [VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs).

This page describes how to upgrade [an existing setup of VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup). Google recommends that you use the latest version of the agent.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Overview

To update your VM Manager setup, complete the following steps:

  1. Check the current version of the OS Config agent that is installed on your VMs. For more information about the OS Config agent versions, see the [GoogleCloudPlatform/osconfig](https://github.com/GoogleCloudPlatform/osconfig/tags) GitHub repository. 
     * To use OS inventory management, your VM must be running an OS Config agent version dated `20201110` or later
     * To use OS policies, your VM must be running an OS Config agent version dated `20210427` or later.
  2. If the version of your OS config agent does not support the new features, update the OS Config agent.



## View OS Config agent version

If you have [OS inventory management (earlier version)](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/view-os-details#version-one) running on your VMs, you can check the OS Config agent version by running the following command:
    
    
    gcloud compute instances os-inventory describe VM-NAME \
        --zone=ZONE
    

Replace the following:

  * `VM-NAME`: the name of your VM
  * `ZONE`: the zone where the VM is located



In the output, search for `OSConfigAgentVersion`.
    
    
    OSConfigAgentVersion: 20210316.00-g1
    

In the preceding output snippet, the OS Config agent version is dated `20210316` (2021-03-16).

## Update the OS Config agent

To update the OS Config agent, do one of the following:

  * Update the package for your operating system
  * Run a patch job



### Update OS packages

One method of updating the OS Config agent is to update the package for your operating system.

###  CentOS/RHEL/Rocky 

To update the agent on CentOS, Rocky Linux, and RHEL operating systems, run the following command:
    
    
    sudo yum update google-osconfig-agent
    

###  Debian 

To update the agent on Debian operating systems, run the following commands:
    
    
    sudo apt update
    sudo apt install google-osconfig-agent
    

###  SLES 

To update the agent on SLES, run the following command:
    
    
    sudo zypper -n update google-osconfig-agent
    

**Note:** The package repository available from SUSE Linux Enterprise Server (SLES) might not have the latest OS Config agent available.

To update the agent on SLES VMs, you can also do a reinstall of the agent using the Google-provided packages. To do an install using Google-provided packages, see [Install the OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#agent-install). 

###  Ubuntu 

To update the agent on Ubuntu operating systems, run the following commands:
    
    
    sudo apt update
    sudo apt install google-osconfig-agent
    

**Note:** The package repository available from Ubuntu might not have the latest OS Config agent available.

To update the agent on Ubuntu VMs, we recommend that you do a reinstall of the agent using the Google-provided packages. To do an install using Google-provided packages, see [Install the OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#agent-install). 

###  Windows 

To update the agent on Windows operating systems, run the following command:
    
    
    googet install google-osconfig-agent
    

### Run a patch job

Another method for updating the OS Config agent is by running a patch job and specifying the `exclusive-packages` or the `exclusive-patches` flag in the [`gcloud compute os-config patch-jobs execute` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/patch-jobs/execute). This patch job only updates the OS Config agent on the target VMs.

To set the target VMs, you need to specify an `INSTANCE_FILTER`. For more information about instance filters, see [instance filters](https://docs.cloud.google.com/compute/docs/os-patch-management/create-patch-job#instance-filters).

###  CentOS/RHEL/Rocky 

To update the agent for CentOS, Rocky Linux and RHEL VMs, run the following command:
    
    
    gcloud compute os-config patch-jobs execute --instance-filter-names=INSTANCE_FILTER \
        --yum-exclusive-packages=google-osconfig-agent
    

###  Debian 

To update the agent for Debian VMs, run the following commands:
    
    
    gcloud compute os-config patch-jobs execute --instance-filter-names=INSTANCE_FILTER \
        --apt-exclusive-packages=google-osconfig-agent
    

###  SLES 

To update the agent for SLES VMs, run the following command:
    
    
    gcloud compute os-config patch-jobs execute --instance-filter-names=INSTANCE_FILTER \
        --zypper-exclusive-patches=google-osconfig-agent
    

**Note:** The package repository available from SUSE Linux Enterprise Server (SLES) might not have the latest OS Config agent available.

To update the agent on SLES VMs, you can also do a reinstall of the agent using the Google-provided packages. To do an install using Google-provided packages, see [Install the OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#agent-install). 

###  Ubuntu 

To update the agent for Ubuntu VMs, run the following commands:
    
    
    gcloud compute os-config patch-jobs execute --instance-filter-names=INSTANCE_FILTER \
        --apt-exclusive-packages=google-osconfig-agent
    

**Note:** The package repository available from Ubuntu might not have the latest OS Config agent available.

To update the agent on Ubuntu VMs, we recommend that you do a reinstall of the agent using the Google-provided packages. To do an install using Google-provided packages, see [Install the OS Config agent](https://docs.cloud.google.com/compute/docs/manage-os#agent-install). 

###  Windows 

To update the agent for Windows VMs, run the following command:

**Note:** This command also updates all the Google-provided software on the VM.
    
    
    gcloud compute os-config patch-jobs execute --instance-filter-names=INSTANCE_FILTER \
        --windows-exclusive-patches=google-packages
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
