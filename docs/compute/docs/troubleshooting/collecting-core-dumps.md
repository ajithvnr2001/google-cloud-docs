---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/collecting-core-dumps/
title: Collecting core dumps \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:58:53.489109+00:00
---

# Collecting core dumps  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/collecting-core-dumps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Collecting core dumps Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Use core dumps to analyze the causes of an unresponsive virtual machine (VM) instance.

To collect core dumps on Compute Engine, you must configure your VMs to receive a [Non-Maskable Interrupt (NMI)](https://en.wikipedia.org/wiki/Non-maskable_interrupt) signal, and then run a `SendDiagnosticInterrupt` command to prompt a kernel panic or blue screen in your operating system. A kernel panic or blue screen starts a core dump collection by the guest operating system. These core dumps can then be used for debugging purposes especially in scenarios that are hard to reproduce, such as a kernel freeze.

## Before you begin

  * Sending NMI signals are counted in the default **Queries** API quota. For more information, see [API rate limits](https://docs.cloud.google.com/compute/docs/api-rate-limits).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

To ensure that your user or service account has the necessary permission to send NMI signals to a VM, ask your administrator to grant the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role to your user or service account on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.instances.sendDiagnosticInterrupt` permission, which is required to send NMI signals to a VM. 

Your administrator might also be able to give your user or service account this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

To use core dumps to help debug an unresponsive VM or a security issue, you need to complete the following steps:

  1. Configure your VM to generate core dumps
  2. Send an NMI signal to generate core dumps
  3. Review the core dumps



## Limitations

For VMs that have Secure Boot enabled, you must disable Secure boot before you send an NMI interrupt signal. For instructions, see [Modifying Shielded VM options on a VM instance](https://docs.cloud.google.com/compute/docs/instances/modifying-shielded-vm#modify-shielded-vm-instance).

## Configure VM

A VM's response to receiving an NMI interrupt signal depends on the VM's operating system configuration.

Each operating system writes its core dump logs in a different location. For example in Ubuntu operating systems the crash dump file is saved to `/var/crash/` by default.

To configure your guest OS to generate a crash dump when an NMI signal is received, review the documentation for the supported operating system.

**Operating system** | **Links to instructions** | **Additional notes**  
---|---|---  
Ubuntu | [Ubuntu: Kernel crash dump](https://documentation.ubuntu.com/server/how-to/software/kernel-crash-dump/) | For Linux VMs, you must configure the kernel to crash when it receives the NMI interrupt signal.  
  
To configure the kernel to crash, add the following to your configuration file:  

    
    
    kernel.unknown_nmi_panic=1
      
  
SUSE Linux Enterprise Server (SLES) | [Configure crashkernel memory for kernel core dump analysis](https://support.scc.suse.com/s/kb/Configure-crashkernel-memory-for-kernel-core-dump-analysis-1583239303159)  
Red Hat Enterprise Linux (RHEL) | Use both of the following documents:  


  * [Handling a Non-Responsive Virtual Machine by Sending a Non-Maskable Interrupt](https://access.redhat.com/articles/3587631)
  * [Configuring kdump](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/kernel_administration_guide/index#sect-kdump-config-cli)

  
Container-Optimized OS (COS) | [Enabling Kernel Crash Dump on GCE COS Instances](https://cos.googlesource.com/cos/overlays/board-overlays/+/refs/heads/master/project-lakitu/docs/kdump.md#for-cos-instances-created-from-google-compute-engine-gce_directly) | Only COS 93 and later support kdump generation using NMI signal.   
Windows | [Generate a kernel or complete crash dump](https://docs.microsoft.com/en-US/windows/client-management/generate-kernel-or-complete-crash-dump) | Windows client VMs don't keep memory dump files unless they are members of an AD domain or the following is true:

  * The registry sets `AlwaysKeepMemoryDump` to `1`
  * The disk has more than 25 GB of free space

For more information, see [ Kernel dump storage and clean up behavior in Windows 7](https://learn.microsoft.com/en-us/archive/blogs/wer/kernel-dump-storage-and-clean-up-behavior-in-windows-7)  
  
## Send NMI to generate core dumps

After you configure the VM, you can then send the NMI signal to the VM by using either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

**Note:** When you configure your VM to trigger kernel panic and generate crash dumps, the VM becomes unreachable after the NMI signal is sent. If you want to connect to the VM after the signal is sent, you need to restart the VM.

###  gcloud 

To send the NMI signal, use the [`instances send-diagnostic-interrupt` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/send-diagnostic-interrupt).
    
    
    gcloud compute instances send-diagnostic-interrupt VM_NAME \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: instance ID or name of the VM that you want to collect core dumps from
  * `ZONE`: the zone where your VM is located



The output is similar to the following:
    
    
    <Empty Response>

For a complete list of outputs, see the next section in this document about "NMI command responses".

###  REST 

  1. Optional. If not already available, create an API key. For more information about creating API keys, see [Creating an API key](https://docs.cloud.google.com/docs/authentication/api-keys#creating_an_api_key).

  2. To send the NMI signal, make a `POST` request to the [`sendDiagnosticInterrupt` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/sendDiagnosticInterrupt).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/sendDiagnosticInterrupt?key=API_KEY
         

For, example, you can use the `curl` command to make the request as follows:
         
         curl --request POST 'https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/sendDiagnosticInterrupt?key=API_KEY' \
           --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
           --header 'Accept: application/json' \
           --compressed
         

Replace the following:

     * `PROJECT_ID`: ID of the project to create the VM in
     * `ZONE`: the zone where your VM is located
     * `VM_NAME`: instance ID or name of the VM that you want to collect core dumps from
     * `API_KEY`: your API key

The output is similar to the following:
    
    <Empty Response>

For a complete list of outputs, see the next section in this document about "NMI command responses".




### NMI command responses

One of the following responses are returned when you attempt to send an NMI signal.

State | Body | Notes  
---|---|---  
SUCCESS | `<Empty Response>` | `SUCCESS` shows that the NMI signal is delivered to the operating system. It does not guarantee that the core dump is collected, or that the VM shuts down or reboots. These behaviors are determined by the operating system configuration.  
FAIL | `UNSUPPORTED_OPERATION` | This occurs when the operating system fails to receive the NMI signal. There are multiple reasons for this. Common scenarios are that the VM is being [live migrated](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) or the VM is not properly configured to receive NMI signals.   
To resolve this, you can try the following: 

  * Verify that the VM is properly configured. See Configure VM.
  * Wait and retry the `SendDiagnosticInterrupt` request.

  
FAIL | `Required 'compute.instances.sendDiagnosticInterrupt' permission for [..]` | The command failed because the user making the request does not have sufficient permissions.  
  
To resolve this, you can assign a role to the user that contains the `compute.instances.sendDiagnosticInterrupt` permission.  
  
## Review core dumps

Review the crash dump file in the configured or default location for your operating system.

For example in Ubuntu operating systems, by default, the crash dump file is saved to `/var/crash/`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
