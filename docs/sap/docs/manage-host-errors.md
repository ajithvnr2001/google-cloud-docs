---
url: https://docs.cloud.google.com/sap/docs/manage-host-errors/
title: Manage host errors for SAP workloads on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:09.960156+00:00
---

# Manage host errors for SAP workloads on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/manage-host-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Manage host errors for SAP workloads on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can detect host hardware errors on Google Cloud and protect your SAP workloads from them. 

Google Cloud is not impervious to hardware failures. While multiple layers of redundancy exist, hardware errors can occur, resulting in the termination of your Compute Engine instances.

Host hardware errors can have multiple causes because the server hardware and their associated components have many parts that can experience failure. Memory-optimized machine types in particular have a large number of memory modules, which can increase the likelihood of hardware failures being memory related. Memory related failures are of two types:

  * **Correctable memory errors** : These errors are those that can be corrected by built-in hardware and software mechanisms, such as [Error correction code (ECC) memory](https://en.wikipedia.org/wiki/ECC_memory). Such errors have no impact on the Compute Engine instance that is running on the host. They are transparently handled by hardware and software mechanisms.

  * **Uncorrectable memory errors** : These errors are those that cannot be corrected. They are rare, random and unpredictable. Any attempt to access the affected memory area results in a signal to the OS, which results either in the termination of the Compute Engine instance or a [Machine check exception (MCE)](https://en.wikipedia.org/wiki/Machine-check_exception) that is passed on to the instance. When an application on the Compute Engine instance attempts to read data from the affected uncorrectable memory area, the application consumes this signal and terminates. When the OS in a Compute Engine instance receives this signal, by default the OS prevents the affected memory pages from being re-allocated to avoid further use. When an uncorrectable memory error occurs, termination of your application is unavoidable.




Compute Engine VMs have additional safeguards, such as [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process), that can be combined with application architecture strategies to limit the impact of some of these events.

## Detect host errors

To detect host errors on M2, M3, or M4 instances that run your SAP workloads, you can [configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) that use the following predefined queries:

Query/filter name | Description  
---|---  
**Compute Engine Host Error** `(compute.instances.hostError)` | A host error indicates that a hardware error occurred that resulted in the Compute Engine instance needing to be terminated. For more information, see [Compute Engine audit logging](https://docs.cloud.google.com/compute/docs/logging/audit-logging#queries).  
**Compute Engine Host Memory Alert** `(compute.instances.hostEventNotify)` | A host memory alert indicates a type of hardware error that is associated with memory modules. Such errors can result from permanent component failures over time, or transient events caused by high energy particles or cosmic rays that prevent a memory page from being safely retrieved. For more information, see [Compute Engine audit logging](https://docs.cloud.google.com/compute/docs/logging/audit-logging#queries). For SAP workloads, you can also import the predefined [Host Memory Alert policy](https://docs.cloud.google.com/sap/docs/create-metric-based-alerting#host-memory-errors) available with Google Cloud's Agent for SAP.  
  
## Protect your SAP workloads from host errors

To protect your SAP workloads from host errors, we recommend the following:

  * Make sure that [automatic restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#autorestart) is set for your Compute Engine instances.

Compute Engine enables this option for all instances by default. We recommend that you _don't_ turn this off.

  * To protect your SAP HANA and SAP NetWeaver workloads from single-instance failures, deploy them with a high availability (HA) configuration.

For more information, see the following guides:

    * [SAP HANA high availability planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-ha-planning-guide)
    * [High availability planning guide for SAP NetWeaver on Google Cloud](https://docs.cloud.google.com/sap/docs/netweaver-ha-planning-guide)
  * To protect your SAP HANA workloads from being affected by the termination of any SAP HANA process, implement the [SAP HANA HA/DR provider hooks](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/1367c8fdefaa4808a7485b09815ae0f3.html) and enable the [SAP HANA Fast Restart option](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#sap-hana-fast-restart-on-gc).

For information about how to do these, see the deployment guide for your SAP HANA scenario in [All SAP HANA guides](https://docs.cloud.google.com/sap/docs/sap-hana-guides).

  * To protect your SAP HANA workloads from uncorrectable memory errors on X4 memory-optimized bare metal machine types, your instance is automatically restarted on a healthy host as soon as the error is detected. This provides the quickest path to enabling full operational capability for your instance.

  * To protect your SAP HANA workloads from memory errors as surfaced by **Compute Engine Host Memory Alert** (`compute.instances.host_event_notify`) events for M2, M3, or M4 machine types, do the following:

    * If the uncorrectable error cannot be handled by the VM, then the VM is automatically restarted due to the [automatic restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#autorestart) policy. In an HA cluster, the secondary node automatically takes over. No further action is required.

    * If the uncorrectable memory error can be handled by the VM and does not result in a VM crash, then do the following:

      1. If the affected instance is the current primary node in your HA cluster, then initiate a manual failover to the secondary node in your cluster.

      2. Stop the affected instance to release the virtual memory pages that were affected by the memory error.

While Compute Engine automatically migrates the affected VMs to a healthy host during these events, some memory pages can remain inaccessible. If your SAP HANA workload attempts to read the affected memory pages for the first time after the memory error occurs, then your workload fails and terminates. By stopping the instance, you release the affected virtual memory pages that might remain from the initial hardware error.

      3. Start the affected instance.

If you're unable to stop and start the affected VM, then the applications running on it might continue to operate till they can read the affected memory pages, which can take a number of hours. Restart the affected VM at your earliest convenience to release any affected memory pages.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
