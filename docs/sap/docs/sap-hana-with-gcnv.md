---
url: https://docs.cloud.google.com/sap/docs/sap-hana-with-gcnv/
title: Deploy Google Cloud NetApp Volumes for SAP HANA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:12:39.923687+00:00
---

# Deploy Google Cloud NetApp Volumes for SAP HANA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-hana-with-gcnv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Deploy Google Cloud NetApp Volumes for SAP HANA Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to deploy and configure Google Cloud NetApp Volumes to provide storage for an SAP HANA workload that runs on Google Cloud. 

The procedure described in this guide deploys NetApp Volumes to replace the block storage that is provisioned for the `/hana/data` and `/hana/log` directories of an SAP HANA scale-up workload. If you're running a scale-out workload, then repeat this procedure for all the nodes in your scale-out workload.

## Before you begin

Before you deploy NetApp Volumes for SAP HANA, ensure that you complete the following prerequisites:

  * Review the list of Compute Engine machine types and the type of SAP HANA workloads with which SAP has certified the use of NetApp Volumes.

To view this information, see the table in [Certified Compute Engine machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#certified-vms).

  * Deploy an SAP HANA workload on Linux on Google Cloud on SAP-certified Compute Engine machine types, with Hyperdisk or Persistent Disk volumes providing block storage for the `/hana/data` and `/hana/log` directories.

To deploy this workload, you can use the Terraform configurations provided by Google Cloud. For more information, see the deployment guide for your scenario in [Supported SAP solutions](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions).

  * Review the guidance provided by Google Cloud for using NetApp Volumes with SAP HANA, which is described in the [Google Cloud NetApp Volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#netapp_cvs) section of the SAP HANA planning guide.




## Deploy NetApp Volumes

To deploy volumes of NetApp Volumes and use them to provide storage for your SAP HANA workload, complete the following steps:

  1. Create volumes of NetApp Volumes to host the `/hana/data` and `/hana/log` directories.

For information about how to create a NetApp Volumes volume, see [Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

  2. Mount the volumes of NetApp Volumes to a temporary mount point by using the `mount` command with the following settings:
         
         mount -t nfs -o rw,bg,hard,timeo=600,vers=NFS_VERSION,rsize=262144,wsize=262144,tcp,nconnect=16,noatime,nodiratime,sec=sys server:path mountpoint

     * Replace `NFS_VERSION` with the NFS version that you want to use. We recommend that you use NFSv4.1 by setting the value `4.1`. You can also use NFSv3 by setting the value `3`.
     * For database persistence, we recommend that you set `rsize=262144` and `wsize=262144`. These settings help optimize random I/O latency and prevent head-of-line blocking. For directories such as `/hana/shared` and `/sapmnt`, the standard mount value defaults are sufficient.
  3. On the compute instance that runs your SAP HANA workload, stop the SAP HANA database and any related services that are using the Hyperdisk or Persistent Disk volumes that host the `/hana/data` and `/hana/log` directories.

  4. Copy the contents of the Hyperdisk or Persistent Disk volumes to the volumes of NetApp Volumes that you created.

  5. Detach the Hyperdisk or Persistent Disk volumes from the compute instance.

For information about how to detach these disks, follow the instructions described in [Detach a non-boot disk from an instance](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_non_boot_disk).

  6. Remount the volumes of NetApp Volumes to the permanent mount points by updating the `/etc/fstab` with the following settings:
         
         server:path   /mountpoint   nfs   vers=NFS_VERSION,hard,tcp,timeo=600,rsize=262144,wsize=262144,nconnect=16,noatime,nodiratime,sec=sys,_netdev   0 0

Replace `NFS_VERSION` with the NFS version that you want to use. We recommend that you use `4.1`. You can also use `3`.

For information about how to update the `/etc/fstab` file, see the `nfs` page in the Linux file formats manual.

  7. To optimize the performance of your SAP HANA workload, we recommend that you update the `fileio` category in the SAP HANA `global.ini` file with the following parameters and values:

Parameter | Value  
---|---  
`async_read_submit` | `on`  
`async_write_submit_active` | `on`  
`async_write_submit_blocks` | `all`  
`max_parallel_io_requests` | `128`  
`max_parallel_io_requests[data]` | `128`  
`max_parallel_io_requests[log]` | `128`  
`num_completion_queues` | `4`  
`num_completion_queues[data]` | `4`  
`num_completion_queues[log]` | `4`  
`num_submit_queues` | `8`  
`num_submit_queues[data]` | `8`  
`num_submit_queues[log]` | `8`  
  8. Save your changes.

  9. Restart the SAP HANA database.

  10. After confirming that everything works as expected, delete the detached Hyperdisk or Persistent Disk volumes. This helps you avoid incurring charges for them.




## What's next

  * For information about how to administer and monitor the compute instances that run your SAP HANA workload, see the [SAP HANA operations guide](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
