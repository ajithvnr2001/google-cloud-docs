---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration/
title: Live migration \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:11.176899+00:00
---

# Live migration  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Live migration Stay organized with collections  Save and categorize content based on your preferences. 

A Confidential VM instance must have the following configuration to support [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process): 

  * An N2D machine type with AMD EPYC Milan CPU platform

  * AMD SEV Confidential Computing technology

  * An [operating system image that supports live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#operating-systems)

  * Be created after January 15, 2024




All other Confidential VM types don't support live migration, and must set their [`onHostMaintenance` policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-options#settingoptions) to `TERMINATE` when being created. This means the VM stops during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents).

## Host maintenance events for Confidential VM instances that don't support live migration

During host maintenance events, Confidential VM instances that don't support live migration and have default host maintenance policy settings are stopped. They are restarted after the maintenance is complete.

The following table shows the default values for host maintenance policy settings on Confidential VM instances that don't support live migration.

Host maintenance policy | Confidential VM default values | Description  
---|---|---  
`onHostMaintenance` | `TERMINATE` |  This property must be set to `TERMINATE` for Confidential VM instances that don't support live migration. This means your Confidential VM instance stops and its status is set to [ `TERMINATED` ](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle#comparison_table) during a maintenance event.  
`automaticRestart` | `true` | When set to `true`, your Confidential VM instance restarts after the maintenance is complete.  
`hostErrorTimeoutSeconds` | `330` | The number of seconds between `90` and `330` before the host attempts to restart an unresponsive VM.  
  
With planning, you can minimize the impact of host maintenance events on your Confidential VM instances.

## Minimize the impact of host maintenance events

To minimize the impact of host maintenance events on Confidential VM instances that don't support live migration, you can do the following things:

  * Monitor for host maintenance event notices

  * Simulate a host maintenance event

  * Change your workload

  * Provision your Confidential VM instances on sole-tenancy nodes




### Monitor for maintenance event notices

To receive advance notice of host events, monitor the `/computeMetadata/v1/instance/maintenance-event` metadata value. To do so, request an event notice by running the following command on your Confidential VM instance:
    
    
    curl http://metadata.google.internal/computeMetadata/v1/instance/maintenance-event -H "Metadata-Flavor: Google"
    

If the request to the metadata server returns `NONE`, then the VM isn't scheduled to stop. If the metadata server returns `TERMINATE_ON_HOST_MAINTENANCE`, then your VM is scheduled for stopping.

The following table shows the host maintenance event notification period for Confidential VM instances that don't support live migration, organized by Confidential Computing technology type. Use these periods to plan around host maintenance events accordingly.

Confidential Computing technology | Machine type | Notification period  
---|---|---  
AMD SEV | C2D | None  
C3D | 7 days  
AMD SEV-SNP | N2D | 1 hour  
Intel TDX | `c3-standard-*` | 7 days  
`c3-standard-*-lssd` | 7 days  
`c4-standard-*` | 7 days  
  
### Simulate a host maintenance event

To test how your workload behaves when a Confidential VM instance is restarted, you can [simulate a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance). As you work through the simulated event, think about how you can change your workload to be resilient when a real event happens.

### Change your workload

After simulating a host maintenance event, you can use the experience to modify your workload to respond to one. For example, you might make use of one of the following techniques:

  * Adjust your workload to monitor regularly for upcoming host maintenance events.

  * Before an event happens, temporarily [move your work in progress to a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects). After the Confidential VM instance restarts, have the workload retrieve the data and resume work.

  * Write all data to a [secondary Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk). After the Confidential VM instance restarts, reattach the Persistent Disk so your workload can resume work.




### Provision your Confidential VM instances on sole-tenancy nodes

If it fits your needs, you can provision your Confidential VM instances on a [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes). This lets you determine a 4-hour window in which Google can perform maintenance on your VMs. It also lets you perform a [manual live migration](https://docs.cloud.google.com/compute/docs/nodes/about-manual-live-migration), which moves your VM to a different node or node group you control.

See [Sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).

## What's next

Learn about [designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
