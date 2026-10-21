---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling/
title: ComputeScheduling \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:38.577782+00:00
---

# ComputeScheduling  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  ComputeScheduling Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * OnHostMaintenance
  * RestartType
  * SchedulingNodeAffinity
    * JSON representation
  * Operator



Scheduling information for VM on maintenance/restart behaviour and node allocation in sole tenant nodes. Options for instance behavior when the host machine undergoes maintenance that may temporarily impact instance performance.

JSON representation  
---  
      
    
    {
      "onHostMaintenance": enum ([OnHostMaintenance](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#OnHostMaintenance)),
      "restartType": enum ([RestartType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#RestartType)),
      "nodeAffinities": [
        {
          object ([SchedulingNodeAffinity](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#SchedulingNodeAffinity))
        }
      ],
      "minNodeCpus": integer
    }  
  
Fields  
---  
`onHostMaintenance` |  `enum (`[OnHostMaintenance](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#OnHostMaintenance)`)` How the instance should behave when the host machine undergoes maintenance that may temporarily impact instance performance.  
`restartType` |  `enum (`[RestartType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#RestartType)`)` Whether the Instance should be automatically restarted whenever it is terminated by Compute Engine (not terminated by user). This configuration is identical to `automaticRestart` field in Compute Engine create instance under scheduling. It was changed to an enum (instead of a boolean) to match the default value in Compute Engine which is automatic restart.  
`nodeAffinities[]` |  `object (`[SchedulingNodeAffinity](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#SchedulingNodeAffinity)`)` A set of node affinity and anti-affinity configurations for sole tenant nodes.  
`minNodeCpus` |  `integer` The minimum number of virtual CPUs this instance will consume when running on a sole-tenant node. Ignored if no node_affinites are configured.  
  
## OnHostMaintenance

Enums  
---  
`ON_HOST_MAINTENANCE_UNSPECIFIED` | An unknown, unexpected behavior.  
`TERMINATE` | Terminate the instance when the host machine undergoes maintenance.  
`MIGRATE` | Migrate the instance when the host machine undergoes maintenance.  
  
## RestartType

Defines whether the Instance should be automatically restarted whenever it is terminated by Compute Engine (not terminated by user).

Enums  
---  
`RESTART_TYPE_UNSPECIFIED` | Unspecified behavior. This will use the default.  
`AUTOMATIC_RESTART` | The Instance should be automatically restarted whenever it is terminated by Compute Engine.  
`NO_AUTOMATIC_RESTART` | The Instance isn't automatically restarted whenever it is terminated by Compute Engine.  
  
## SchedulingNodeAffinity

Node Affinity: the configuration of desired nodes onto which this Instance could be scheduled. Based on <https://cloud.google.com/compute/docs/reference/rest/v1/instances/setScheduling>

JSON representation  
---  
      
    
    {
      "key": string,
      "operator": enum ([Operator](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#Operator)),
      "values": [
        string
      ]
    }  
  
Fields  
---  
`key` |  `string` The label key of Node resource to reference.  
`operator` |  `enum (`[Operator](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeScheduling#Operator)`)` The operator to use for the node resources specified in the `values` parameter.  
`values[]` |  `string` Corresponds to the label values of Node resource.  
  
## Operator

Possible types of node selection operators. Valid operators are IN for affinity and NOT_IN for anti-affinity.

Enums  
---  
`OPERATOR_UNSPECIFIED` | An unknown, unexpected behavior.  
`IN` | The node resource group should be in these resources affinity.  
`NOT_IN` | The node resource group should not be in these resources affinity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
