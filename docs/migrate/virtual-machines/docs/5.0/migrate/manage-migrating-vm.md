---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/manage-migrating-vm/
title: Lifecycle of a migrating VM \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:41.968256+00:00
---

# Lifecycle of a migrating VM  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/manage-migrating-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Lifecycle of a migrating VM Stay organized with collections  Save and categorize content based on your preferences. 

When you create a migrating VM using Migrate to Virtual Machines, the VM stays active for 100 days from the time that the VM appears in the **VM Migrations** tab. A migrating VM is considered active if the VM is in the `FIRST_SYNC`, `ACTIVE`, `PAUSED`, `CUTTING_OVER`, `FINAL_SYNC`, `CUTOVER`, or `FINALIZING` states. For more information about these states, see States of a migrating VM. You can use the migrating VM during this time to perform your migrations.

A 100 days after a migrating VM is created, the VM moves to the `EXPIRED` state. The VM stays in the `EXPIRED` state for 30 days. The `EXPIRED` state is similar to the `PAUSED` state. In this state, the VM stops cycling, but its resources aren't deleted. If you need more time to complete your migration, you can extend the lifespan of the migrating VM by an additional 100 days. You can only extend the lifespan of a migrating VM two weeks before the VM expires and throughout the expiration period (between 86 to 130 days from the creation of the VM). If you don't extend the lifespan of the VM during this period, the VM expires as shown in the following figure.

**Note:** You can only extend the lifespan of a migrating VM once. Any VM that you create for a migration using Migrate to Virtual Machines will have a total lifespan of 200 days at the maximum (including the extension).![Lifecycle of a migrating VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/time-limit.png)Lifecycle of a migrating VM 

If you don't extend the lifespan of the migrating VM between 86 to 130 days, the VM moves to the `FINALIZED_EXPIRED` state. You cannot recover a VM from the `FINALIZED_EXPIRED` state. Similar to the `FINALIZED` state, a `FINALIZED_EXPIRED` VM will have its allocated resources deleted.

**Note:** If the VM is in the `PENDING`, `READY`, `ERROR`, or `FINALIZED` states for 100 days, the VM is directly moved to the `FINALIZED_EXPIRED` state.

## Extend the lifespan of a migrating VM

To extend the lifespan of a migrating VM, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console: [Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)
  2. Select the **VM Migrations** tab. A table of available source VMs appears.
  3. Select one or more VMs.
  4. Click **Migrations** to open the menu, and then click **Extend migration**.



The state of the selected VMs will now be set to `ACTIVE` and the lifespan is extended by a 100 days.

## States of a migrating VM

The following table describes the various states that a migrating VM exists in during and after a migration.

VM Status | Description  
---|---  
`ACTIVE` | The replication is active, and the replication is running or scheduled to run.  
`CUTOVER` | The replication was paused by you and no cycles are scheduled to run.  
`CUTTING_OVER` | The source VM was stopped and replicated. The replication is paused.  
`ERROR` | The replication process encountered an unrecoverable error and was aborted.  
`EXPIRED` | The migrating VM is moved to the `EXPIRED` state a 100 days after creation. The VM stays in this state for 30 days. In this state, the VM stop cycling, but its resources won't be deleted.  
`FIRST_SYNC` | Migration is going through the first sync cycle.  
`FINAL_SYNC` | A cutover job is active and replication cycle is running the final sync.   
`FINALIZING` | The migrating VM is being finalized and migration resources are being removed.  
`FINALIZED` | The replication process is complete and the migrating VM is finalized.  
`FINALIZED_EXPIRED` | The migrating VM is expired and finalized.  
`PENDING` | The VM in the source is being verified.  
`PAUSED` | The source VM was stopped and replicated. The replication is paused.  
`READY` | The source VM was verified and the VM is ready to start replication.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
