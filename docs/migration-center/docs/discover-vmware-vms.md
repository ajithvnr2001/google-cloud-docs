---
url: https://docs.cloud.google.com/migration-center/docs/discover-vmware-vms/
title: Discover VM instances on VMware \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:20.702166+00:00
---

# Discover VM instances on VMware  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/discover-vmware-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Discover VM instances on VMware Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to run an inventory discovery on your VMware environment using the Migration Center discovery client CLI.

## Before you begin

  1. Review the [requirements for downloading and running the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements).
  2. Complete the steps to [download `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/download-collector-cli).



## Run an inventory discovery on VMware using vSphere API

Use the vSphere API to collect data about all VMs in a vCenter visible to the user running the `mcdc` CLI. You can also scope a discovery to a specific folder, cluster, or data center.

### Configure vCenter

If you plan to export the collected data to Migration Center, before you run an inventory discovery, you need to configure your vCenter environment. The data you collect with `mcdc` CLI, in fact, depend on the settings for statistics in vCenter.

vCenter supports four levels of statistics:

  * Level 1 exposes only CPU and memory performance.
  * Level 2 exposes the network performance.
  * Level 3 exposes input/output operations per second (IOPS).
  * Level 4 exposes all the available metrics.



For a detailed list of the available metrics for all statistics levels, see [Data collection levels](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vcenter-configuration/configuring-vcenter-server-using-the-vsphere-client/configuring-vcenter-server-in-the-vsphere-client/configuring-statistics-settings-in-the-vsphere-client/data-collection-levels.html).

By default, the statistics level is set to level 1. Levels 1 and 2 let you collect partial data about your infrastructure, while level 3 lets you collect everything you need to generate a complete total cost of ownership (TCO) report. After the statistics level is changed in vCenter, it might take several hours for performance data to become available.

For more information on how to change statistics levels in vCenter, see [Configure statistics collection intervals in the vSphere client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/vcenter-configuration/configuring-vcenter-server-using-the-vsphere-client/configuring-vcenter-server-in-the-vsphere-client/configuring-statistics-settings-in-the-vsphere-client/configure-statistics-intervals-for-vcenter-server-in-the-vsphere-client.html).

### Run the discovery

  1. In the command line terminal, change to the directory where you downloaded the `mcdc` CLI.
  2. Run the discovery:

### Linux
         
         ./mcdc discover vsphere -u USERNAME --url https://VSPHERE_URL

### Windows
         
         mcdc.exe discover vsphere -u USERNAME --url https://VSPHERE_URL

Replace the following:

     * USERNAME: your vCenter username
     * VSPHERE_URL: the URL for your vCenter Server instance or the vSphere Client

To avoid a certificate check for connecting to the vCenter, include the `-i` (insecure) flag in the command.

  3. When prompted, enter the vCenter password.




After the inventory discovery is complete, the collected data is stored in the local database.

### Scope a discovery

  * Run the discovery at the root:

### Linux
        
        ./mcdc discover vsphere --url https://VSPHERE_URL -u USERNAME --path /

### Windows
        
        mcdc.exe discover vsphere --url https://VSPHERE_URL -u USERNAME --path /

  * Run the discovery at a specific folder:

### Linux
        
        ./mcdc discover vsphere --url https://VSPHERE_URL -u USERNAME --path DATACENTER/vm/FOLDER

### Windows
        
        mcdc.exe discover vsphere --url https://VSPHERE_URL -u USERNAME --path DATACENTER/vm/FOLDER

Replace the following:

    * DATACENTER: the name of the data center
    * FOLDER: the path to the folder
  * Run the discovery at a specific cluster:

### Linux
        
        ./mcdc discover vsphere --url https://VSPHERE_URL -u USERNAME --path DATACENTER/host/CLUSTER

### Windows
        
        mcdc.exe discover vsphere --url https://VSPHERE_URL -u USERNAME --path DATACENTER/host/CLUSTER

Replace the following:

    * CLUSTER: the name of the cluster
  * Run the discovery at a specific data center:

### Linux
        
        ./mcdc discover vsphere --url https://VSPHERE_URL -u USERNAME --path DATACENTER

### Windows
        
        mcdc.exe discover vsphere --url https://VSPHERE_URL -u USERNAME --path DATACENTER




To avoid a certificate check for connecting to the vCenter, include the `-i` (insecure) flag in the command.

## Run an inventory discovery on VMware using RVTools

For VMs running on VMware, the `mcdc` CLI lets you analyze the XLSX report files generated with [RVTools](https://www.robware.net/rvtools/).

  * Collect data based on your existing RVTools export:

### Linux
        
        ./mcdc discover rvtools REPORT_NAME.xlsx

### Windows
        
        mcdc.exe discover rvtools REPORT_NAME.xlsx

Replace REPORT_NAME with the path to the XLSX generated with RVTools.




However, this method has following limitations:

  * The `mcdc` CLI doesn't support tables generated with the `--DBColumnNames` flag in RVTools.
  * The `mcdc` CLI doesn't support exporting the data collected using this method to Migration Center. However, you can use it to [run an offline assessment](https://docs.cloud.google.com/migration-center/docs/run-offline-assessment).



## What's next

  * Learn how to [run a guest discovery](https://docs.cloud.google.com/migration-center/docs/run-guest-discovery).
  * Learn how to [export collected data to Migration Center](https://docs.cloud.google.com/migration-center/docs/export-collected-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
