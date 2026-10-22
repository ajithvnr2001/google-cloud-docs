---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/configure-ntp-gdc-vm/
title: Configure NTP on a GDC VM \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:20.976257+00:00
---

# Configure NTP on a GDC VM  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/configure-ntp-gdc-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure NTP on a GDC VM Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to configure NTP servers on your Google Distributed Cloud (GDC) air-gapped virtual machine (VM).

Systems that rely on event sequencing require consistent clocks for accurate logging and debugging. To standardize time and keep connected systems synchronized, GDC VMs use the Network Time Protocol (NTP) to ensure time accuracy. Without NTP configuration, a VM's clock inevitably drifts, causing timestamp discrepancies that disrupt event sequencing and hinder troubleshooting.

When creating a VM, you can choose between two image sources, both of which include pre configured NTP details:

  * GDC-provided images
  * Bring-your-own (BYO) images



If you import an image with the value `prepareImage: false` or delete NTP URLs from your VM, you must manually configure NTP using chrony, a tool that actively synchronizes your system clock with external servers. For more information about chrony, see <https://chrony-project.org/>.

This document is for developers in platform administrator or application operator groups that create VMs using GDC-provided and bring-your-own (byo) images. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you configure NTP servers, verify or install the gdcloud CLI. All Distributed Cloud commands use the `gdcloud` or `kubectl` CLI and require an operating system (OS) environment.

  * Check for the CLI: Run `gdcloud version`

  * If the CLI isn't installed, download and install the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview)




### Required IAM roles

To get the permissions that you need to configure NTP and manage VM settings, ask your Project IAM Admin to [grant you](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/role-bindings) the following IAM roles in the namespace of the project where the VM resides:

  * Project VirtualMachine Admin (`project-vm-admin`): update VM configurations, modify instance metadata for NTP synchronization, and restart instances to apply system-level changes at the project level

  * Project Viewer (`project-viewer`): read-only access to inspect VM runtime states, list project resources, and audit configuration settings without the ability to modify project data.




Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Configure NTP for your VM

Follow the steps to configure your NTP server details for your specific OS using `chrony`.

  1. Use `ssh` to connect to your VM:

###  Console 

     1. Go to the **VM instances** page in the GDC console.

     2. Click the **SSH** button for the instance you want to configure.

###  gdcloud 

Use the gdcloud CLI to connect to your VM instance with SSH:
    
    gcloud compute instances ssh INSTANCE_NAME
    

Replace `INSTANCE_NAME` with the name of your VM instance.

  2. Use the `edit` command to navigate to your `chrony` configuration file:

###  Ubuntu 
         
         sudo edit /etc/chrony/chrony.conf
         

###  RHEL 
         
         sudo edit /etc/chrony.conf
         

  3. Add the following NTP URLs to your `chrony.conf` file:
         
         server ntp1.org.internal iburst
         server ntp2.org.internal iburst
         server ntp3.org.internal iburst
         server ntp4.org.internal iburst
         server ntp5.org.internal iburst
         server ntp6.org.internal iburst
         

  4. Restart the `chrony` service:

###  Ubuntu 
         
         sudo systemctl restart chrony
         

###  RHEL 
         
         sudo systemctl restart chronyd
         

  5. Verify your configuration using the `chrony` CLI:
         
         chronyc sources -v
         

The output looks similar to the following:
         
         210 Number of sources = 1
         MS Name/IP address         Stratum Poll Reach LastRx Last sample
         ===============================================================================
         ^* metadata.google.internal      2   7   377    98  -1343ns[-1588ns] +/-  396us
         




## What's next

  * [Monitor VM metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/monitor/monitor-metrics)
  * Check [VM resiliency](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/config-resiliency)
  * Perform [Virtual machine troubleshooting](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-troubleshooting/vm-troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
