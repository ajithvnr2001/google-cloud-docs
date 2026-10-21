---
url: https://docs.cloud.google.com/cluster-director/docs/slurm-settings/
title: Supported Slurm settings in Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:10:59.288812+00:00
---

# Supported Slurm settings in Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/slurm-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported Slurm settings in Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Slurm settings that you can configure when you create or modify a cluster in Cluster Director. Use these settings to customize the behavior of the Slurm scheduler and other Slurm components for the entire cluster, specific partitions, or specific nodesets to support your workloads.

To learn more about how Cluster Director uses Slurm to handle cluster management, job scheduling, and workload orchestration, see [Slurm orchestration in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/orchestration).

## Specify custom Slurm settings

When you create or modify a cluster, you can customize Slurm settings to adapt your cluster to your workload requirements. If you don't specify a value for a setting, then Cluster Director uses the default value listed in this document.

To specify custom Slurm settings, use one of the following methods:

  * **REST API** : specify settings in the `orchestrator.slurm.config`, `orchestrator.slurm.partitions[].config`, or `orchestrator.slurm.nodeSets[].config` fields in your request body.



The following sections list the supported Slurm settings for clusters, partitions, and compute nodes.

### Cluster-level settings

The following table lists the supported cluster-level settings (`orchestrator.slurm.config`) for Slurm:

API field | Slurm parameter | Data type | Description | Default value  
---|---|---|---|---  
`defMemPerCpu` | [`DefMemPerCPU`](https://slurm.schedmd.com/slurm.conf.html#OPT_DefMemPerCPU) | String | The default memory in megabytes (MB) that Slurm allocates for each CPU in your cluster. Partition-level `defMemPerCpu` values, such as the values that Cluster Director calculates by default for each partition, override this cluster-level setting. | `0`  
`enforcePartLimits` | [`EnforcePartLimits`](https://slurm.schedmd.com/slurm.conf.html#OPT_EnforcePartLimits) | String | Whether Slurm enforces partition limits when you submit or run jobs. | `NO`  
`firstJobId` | [`FirstJobId`](https://slurm.schedmd.com/slurm.conf.html#OPT_FirstJobId) | String | The job ID that Slurm assigns to the first job after the cluster starts. The value of each subsequent job ID increases by `1`. | `1`  
`jobRequeue` | [`JobRequeue`](https://slurm.schedmd.com/slurm.conf.html#OPT_JobRequeue) | String | Whether batch jobs return to the queue if a compute node encounters a host error. | `1`  
`overTimeLimit` | [`OverTimeLimit`](https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit) | String | The number of minutes that a job can run past its time limit before Slurm stops the job. | `0`  
`schedulerParameters` | [`SchedulerParameters`](https://slurm.schedmd.com/slurm.conf.html#OPT_SchedulerParameters) | JSON object (Message) | The behavior of the Slurm job scheduler. | `salloc_wait_nodes,ignore_prefer_validation,bf_continue,nohold_on_prolog_fail`  
`selectTypeParameters` | [`SelectTypeParameters`](https://slurm.schedmd.com/slurm.conf.html#OPT_SelectTypeParameters) | String | How Slurm allocates compute resources to jobs. | `CR_Core_Memory`  
`accountingStorageTres` | [`AccountingStorageTRES`](https://slurm.schedmd.com/slurm.conf.html#OPT_AccountingStorageTRES) | String | The trackable resources (TRES), such as GPUs, that Slurm records in job usage logs. If you specify values for this field, then Cluster Director merges your values with the default `gres/gpu` values and doesn't replace the defaults. | `gres/gpu`  
`fairShareDampeningFactor` | [`FairShareDampeningFactor`](https://slurm.schedmd.com/slurm.conf.html#OPT_FairShareDampeningFactor) | String | A numerical factor that sets a priority on how nested accounts maintain fair access to cluster resources. | `1`  
`priorityCalcPeriod` | [`PriorityCalcPeriod`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityCalcPeriod) | String | The time interval, in seconds, at which Slurm recalculates job priority. | `300` (5 minutes)  
`priorityDecayHalfLife` | [`PriorityDecayHalfLife`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityDecayHalfLife) | String | The time it takes for past resource usage to decrease by half. | `7-0` (seven days)  
`priorityFavorSmall` | [`PriorityFavorSmall`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFavorSmall) | String | Whether Slurm gives small jobs higher priority in the queue than large jobs. | `NO`  
`priorityFlags` | [`PriorityFlags`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityFlags) | String | The configuration options that modify how Slurm calculates job priority. | None (unset)  
`priorityMaxAge` | [`PriorityMaxAge`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityMaxAge) | String | The time a job must wait in the queue to reach maximum age priority. | `7-0` (seven days)  
`priorityUsageResetPeriod` | [`PriorityUsageResetPeriod`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityUsageResetPeriod) | String | The time interval at which Slurm resets historical resource usage records to zero. | `NONE` (disabled)  
`preemptParameters` | [`PreemptParameters`](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptParameters) | JSON object (Message) | The configuration options that control how Slurm preempts jobs. | None (unset)  
  
### Partition-level settings

The following table lists the supported partition-level settings (`orchestrator.slurm.partitions[].config`) for Slurm:

API field | Slurm parameter | Data type | Description | Default value  
---|---|---|---|---  
`allowAccounts` | [`AllowAccounts`](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowAccounts) | String | A comma-separated list of user accounts that can run jobs in your cluster partition. | `ALL`  
`allowQos` | [`AllowQos`](https://slurm.schedmd.com/slurm.conf.html#OPT_AllowQoS) | String | A comma-separated list of quality of service (QoS) levels that can run jobs in your cluster partition. | `ALL`  
`defaultTime` | [`DefaultTime`](https://slurm.schedmd.com/slurm.conf.html#OPT_DefaultTime) | String | The default runtime limit for jobs that don't specify a time limit in your cluster partition. | None (unset)  
`defMemPerCpu` | [`DefMemPerCPU`](https://slurm.schedmd.com/slurm.conf.html#OPT_DefMemPerCPU_1) | String | The default memory in megabytes (MB) that Slurm allocates for each CPU in your cluster partition, which overrides the cluster-level setting. | Depends on the nodesets in the partition1  
`denyAccounts` | [`DenyAccounts`](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyAccounts) | String | A comma-separated list of user accounts that can't run jobs in your cluster partition. | None (unset)  
`denyQos` | [`DenyQos`](https://slurm.schedmd.com/slurm.conf.html#OPT_DenyQoS) | String | A comma-separated list of quality of service (QoS) levels that can't run jobs in your cluster partition. | None (unset)  
`exclusiveUser` | [`ExclusiveUser`](https://slurm.schedmd.com/slurm.conf.html#OPT_ExclusiveUser) | String | Whether Slurm reserves entire compute nodes for jobs from a single user. | `NO`  
`graceTime` | [`GraceTime`](https://slurm.schedmd.com/slurm.conf.html#OPT_GraceTime) | String | The time, in seconds, that Slurm grants to a job before Slurm stops it during preemption. | `0`  
`maxTime` | [`MaxTime`](https://slurm.schedmd.com/slurm.conf.html#OPT_MaxTime) | String | The maximum runtime limit for jobs in your cluster partition. | `UNLIMITED`  
`maxNodes` | [`MaxNodes`](https://slurm.schedmd.com/slurm.conf.html#OPT_MaxNodes) | String | The maximum number of nodes that a job can request in your cluster partition. | `UNLIMITED`  
`overSubscribe` | [`OverSubscribe`](https://slurm.schedmd.com/slurm.conf.html#OPT_OverSubscribe) | String | Whether multiple jobs can share compute resources on the same node. | `NO`  
`overTimeLimit` | [`OverTimeLimit`](https://slurm.schedmd.com/slurm.conf.html#OPT_OverTimeLimit) | String | The number of minutes that a job can run past its time limit in your cluster partition before Slurm stops the job. | `0`  
`preemptMode` | [`PreemptMode`](https://slurm.schedmd.com/slurm.conf.html#OPT_PreemptMode) | String | The preemption mechanism for jobs in your cluster partition, which overrides the cluster-level setting. | `OFF`  
`priorityJobFactor` | [`PriorityJobFactor`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityJobFactor) | String | A numerical value that Slurm adds to the priority score of jobs in your cluster partition. | `1`  
`priorityTier` | [`PriorityTier`](https://slurm.schedmd.com/slurm.conf.html#OPT_PriorityTier) | String | The priority tier that Slurm uses to schedule and preempt jobs across partitions. | `1`  
`qos` | [`QOS`](https://slurm.schedmd.com/slurm.conf.html#OPT_QOS) | String | The default quality of service (QoS) that Slurm assigns to jobs in your cluster partition. | None (unset)  
`tresBillingWeights` | [`TRESBillingWeights`](https://slurm.schedmd.com/slurm.conf.html#OPT_TRESBillingWeights) | String | The factors that Slurm uses to calculate resource usage costs from trackable resources (TRES) in your cluster partition. | `CPU=1`  
  
1 If a cluster partition has only dynamic nodesets, then Cluster Director sets the partition's default memory per CPU to 100 MB. If a cluster partition has static nodesets, then Cluster Director calculates the memory per CPU for each static nodeset and uses the lowest value for the partition. For each static nodeset, Cluster Director uses the following formula, which divides a single node's available memory by its CPU count (with a 100 MB minimum): 

\\(\max\left(100, \frac{\text{Total node memory in MB} - \text{Reserved system memory in MB} }{\text{Total CPUs on the node} }\right)\\) 

### Node-level settings

The settings in the following table correspond to Slurm [`NodeName` parameters](https://slurm.schedmd.com/slurm.conf.html#SECTION_NODE-CONFIGURATION), _not_ `NodeSet` directives. In Cluster Director, you apply these settings to all compute nodes in a nodeset by using the `orchestrator.slurm.nodeSets[].config` field. You can't configure individual compute nodes in a nodeset separately, but different nodesets can have different node settings.

The following table lists the supported node settings for Slurm:

API field | Slurm parameter | Data type | Description | Default value  
---|---|---|---|---  
`cpuSpecList` | [`CpuSpecList`](https://slurm.schedmd.com/slurm.conf.html#OPT_CpuSpecList) | String | A comma-separated list of CPU IDs that Slurm reserves for system processes on each node in your nodeset. | None (unset)  
`features` | [`Features`](https://slurm.schedmd.com/slurm.conf.html#OPT_Features) | String | A comma-separated list of labels that you assign to nodes in your nodeset. | None (unset)  
`memSpecLimit` | [`MemSpecLimit`](https://slurm.schedmd.com/slurm.conf.html#OPT_MemSpecLimit) | String | The amount of memory in megabytes (MB) that Slurm reserves for system processes on each node in your nodeset. | `0` (unset)  
`weight` | [`Weight`](https://slurm.schedmd.com/slurm.conf.html#OPT_Weight) | String | A priority weight that Slurm uses to select nodes for jobs. Slurm allocates nodes with lower weights before nodes with higher weights. | `1`  
`coreSpecCount` | [`CoreSpecCount`](https://slurm.schedmd.com/slurm.conf.html#OPT_CoreSpecCount) | String | The number of CPU cores that Slurm reserves for system processes on each node in your nodeset. | `0` (unset)  
  
## What's next

  * [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster)

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
