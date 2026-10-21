---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails/
title: ComputeEngineDisksTargetDetails \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:38.347665+00:00
---

# ComputeEngineDisksTargetDetails  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  ComputeEngineDisksTargetDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DisksMigrationDisksTargetDetails
  * DisksMigrationVmTargetDetails
    * JSON representation
  * PersistentDisk
    * JSON representation



ComputeEngineDisksTargetDetails is a collection of created Persistent Disks details.

JSON representation  
---  
      
    
    {
      "disks": [
        {
          object ([PersistentDisk](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails#PersistentDisk))
        }
      ],
    
      // Union field vm_target can be only one of the following:
      "disksTargetDetails": {
        object ([DisksMigrationDisksTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails#DisksMigrationDisksTargetDetails))
      },
      "vmTargetDetails": {
        object ([DisksMigrationVmTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails#DisksMigrationVmTargetDetails))
      }
      // End of list of possible types for union field vm_target.
    }  
  
Fields  
---  
`disks[]` |  `object (`[PersistentDisk](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails#PersistentDisk)`)` The details of each created Persistent Disk.  
Union field `vm_target`. Details of the VM the disks are attached to. `vm_target` can be only one of the following:  
`disksTargetDetails` |  `object (`[DisksMigrationDisksTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails#DisksMigrationDisksTargetDetails)`)` Details of the disks-only migration target.  
`vmTargetDetails` |  `object (`[DisksMigrationVmTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails#DisksMigrationVmTargetDetails)`)` Details for the VM the migrated data disks are attached to.  
  
## DisksMigrationDisksTargetDetails

This type has no fields.

Details for a disks-only migration.

## DisksMigrationVmTargetDetails

Details for the VM created VM as part of disks migration.

JSON representation  
---  
      
    
    {
      "vmUri": string
    }  
  
Fields  
---  
`vmUri` |  `string` Output only. The URI of the Compute Engine VM.  
  
## PersistentDisk

Details of a created Persistent Disk.

JSON representation  
---  
      
    
    {
      "sourceDiskNumber": integer,
      "diskUri": string
    }  
  
Fields  
---  
`sourceDiskNumber` |  `integer` The ordinal number of the source VM disk.  
`diskUri` |  `string` The URI of the Persistent Disk.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
