---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-aws-linux2/
title: Migrate an Amazon Linux 2 VM to Google Cloud \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:08.017060+00:00
---

# Migrate an Amazon Linux 2 VM to Google Cloud  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-aws-linux2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migrate an Amazon Linux 2 VM to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

**Experimental**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To inquire about this feature, send an email to the email address: [m2vm-amazon-linux-migration@google.com](mailto:m2vm-amazon-linux-migration@google.com). 

Amazon Linux 2 is a Linux distribution developed and maintained by Amazon. While it can be run on other cloud platforms, it is not supported by Amazon.

Migrate to Virtual Machines can automatically convert Amazon Linux 2 running on a VM to an operating system supported by Google Cloud. The VM is then migrated to Google Cloud. If your VM cannot be converted, you can rebuild the VM using a Google Cloud OS image, and then transfer data from the source VM to the rebuilt VM.

To migrate your Amazon Linux 2 workloads to Google Cloud, choose one of the available migration flows:

**Note:** Some VMs running Amazon Linux 2 cannot be automatically converted to Rocky Linux 8. For these VMs, we recommend that you use the VM disk migration flow to migrate your VM to Google Cloud.

  * **OS conversion** : In this approach, Migrate to Virtual Machines first attempts to convert the Amazon Linux 2 running on your VM instance to Rocky Linux 8. If the conversion is successful, Migrate to Virtual Machines completes the migration. This process includes the following steps:

    1. Run the following command on your source VM. 
           
           mkdir -p /etc/google/migrate/elevate_amazonlinux2_to_rocky

    2. Start the [replication of the source VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#replication). The replication process converts and upgrades the Amazon Linux 2 OS to Rocky Linux 8 (including all installed packages), and adapts the VM to Compute Engine.

The VM boots with Rocky Linux 8. You can now set the target details, create a test-clone and test the VM. If the VM works as expected, you can cut-over to the VM on Google Cloud.

  * **VM Disk migration** : If you don't want to perform an automated OS conversion, or if your VM is not suitable for this process, you can choose to [migrate your VM's disks to Persistent Disk volumes](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disks) on Google Cloud. This feature helps you migrate the workload state (VM disks) from a source VM and attach it as a Persistent Disk volume to an existing or new VM on Google Cloud, using an officially supported or any other base image, with minimal interruptions to the workload.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
