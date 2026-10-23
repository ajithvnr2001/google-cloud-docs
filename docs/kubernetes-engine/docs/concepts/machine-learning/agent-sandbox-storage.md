---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox-storage/
title: Choose storage for AI agentic workloads \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:21.072799+00:00
---

# Choose storage for AI agentic workloads  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Choose storage for AI agentic workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document helps you select an appropriate storage option for your AI agents based on their specific data lifecycle needs and latency requirements.

For implementation details, see [Manage Agent Sandbox on GKE storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-storage).

## Considerations for choosing a storage solution

When choosing a storage solution for your AI agents, you should consider your agentic platform requirements, such as performance and scale, and your agents' data management requirements.

### Platform requirements

Evaluate the following operational and architectural requirements of your platform:

  * **Platform scale and agents churn frequency (control plane)** : the number of concurrent agents, and the number of agents created, paused, reactivated, and deleted per minute. Platforms creating thousands of agents per minute or pausing idle agents require storage with low-latency attach and mount operations at significant scale (for example, Filestore mounts faster than Hyperdisk can attach).
  * **Dataset size and load latency (data plane)** : agents loading multi-gigabyte datasets or heavy libraries (such as Node.js or Python packages) during startup require high storage I/O performance for reading the data in seconds (for example, Hyperdisk offers high per-disk read throughput).
  * **Agent cold-start and reactivation latency** : the expected latency, such as sub-second or multi-second. Achieving sub-second startup latency requires using [Agent Sandbox on GKE Warm Pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox#warm-pools). Using [direct sandbox creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#alternative_create_a_sandbox_directly) generally incurs a multi-second delay for Pod startup and dynamic disk attachment.
  * **Storage size per agent** : depending on the service chosen, you must accommodate provisioning limits, such as a minimum size of 4 GiB for Google Cloud Hyperdisk or a minimum of 10 GiB for a single Filestore share.
  * **Data access modes and isolation** : how the platform should support workspace isolation and collaborative workspaces. This determines whether your agents will need private isolated workspaces (ReadWriteOnce), collaborative workspaces (ReadWriteMany), or exploration branching workspaces (Read-Only template with a writable scratchpad).
  * **Resilience** : if your agents specifically require regional resilience, [Filestore Multishares for GKE (Enterprise)](https://docs.cloud.google.com/filestore/docs/service-tiers-enterprise) is the appropriate choice.
  * **Storage cost** : storage services vary significantly in price, with Hyperdisk Balanced offering a cost-efficient option compared to Filestore Multishares.



### Agent data lifecycle patterns

When you decide how your solution handles persistent and ephemeral data, consider the following agent data lifecycle patterns:

  * **Stateful workspace (continuous state)** : the workspace maintains a continuous state across sessions. The agent preserves its data when it is paused (the Agent Sandbox is deleted) and restores that data from the latest saved state when reactivated (the Sandbox is re-created).
  * **Point-in-time restore and ownership transfer (snapshot state)** : the workspace acts as a snapshot state, meaning it branches off from a frozen point in time. The workspace is initialized from a historical dataset or another user's shared state, to execute an ownership transfer. Subsequent modifications are saved to a separate, private writable layer, leaving the master copy untouched. This pattern is useful for scenarios like cloning a dataset to run parallel experiments, debugging, or performing independent work based on shared data.
  * **Ephemeral workspace (scratch state)** : the workspace provides a temporary scratch state where no data is preserved. The agent uses a storage volume strictly for holding temporary files while it is active. When the agent is paused or deleted (Agent Sandbox deletion), the temporary data is permanently discarded.



### Agent data access modes

Choose a storage service that supports your agents' needs if they need to access storage in one of these data access modes:

  * **Private isolated workspace** : an agent starts up with a private isolated storage directory it has sole read and write access to.
  * **Collaborative workspace** : multiple coordinating agents mount the exact same shared directory in Read-Write (RW) mode to collaboratively update files in real time.
  * **Exploration branching workspace** : the agent accesses base template files in Read-Only (RO) mode to avoid altering the template, and makes new writes either by routing them to a separate local `emptyDir` scratchpad or private persistent path or by copying the template files directly into a private writable workspace on startup.



## Compare storage options for Agent Sandbox on GKE

Consider the following scenarios to help you compare your storage options:

  * Use Hyperdisk Balanced for cost-efficient storage for agents that tolerate a few seconds startup latency and use a private isolated workspace with ReadWriteOnce (RWO) access mode.
  * Use Filestore Multishares for GKE (Enterprise) for agents that require a collaborative workspace or regional resilience.

**Note:** Filestore Multishares for Agent Storage is available in Preview. This service improves performance and lowers costs per agent compared to Filestore Multishares for GKE (Enterprise). It offers faster provisioning latency, more shares per instance, and smaller share sizes. To try this Preview release, contact your account team.

The following table compares storage services to help you meet the performance, scale, data access, and cost requirements of your AI agents.

Feature | [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced) | [Filestore Multishares for GKE (Enterprise)](https://docs.cloud.google.com/filestore/docs/service-tiers-enterprise)  
---|---|---  
**Best for** | 

  * Individual workspaces with ReadWriteOnce (RWO) access mode
  * Workloads that tolerate multi-second storage attach latency
  * Cost efficiency
  * [Direct Sandbox creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox#alternative_create_a_sandbox_directly)

| 

  * Collaborative workspaces with ReadWriteMany (RWX) access mode
  * Workloads that require sub-second storage attach latency
  * Regional resilience

  
**Access modes** |  ReadWriteOnce (RWO)  
  
_Note:_ Use [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml) for ReadOnlyMany (ROX) mode.  | ReadWriteMany (RWX)  
**Sub-second Agent Sandbox on GKE startup ([Warm Pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox#warm-pools))** | 

  * **Ephemeral workspace:** an empty volume can be pre-attached on creation and destroyed after the active session ends.
  * **Stateful workspace or point-in-time restore:** requires custom scripting and a DaemonSet for dynamic volume binding ([example in GitHub](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/latebind-storage-gke-sandbox)).

| 

  * **Ephemeral workspace:** an empty volume can be pre-attached on creation and destroyed after the active session ends.
  * **Stateful workspace or point-in-time restore:** requires custom scripting and a DaemonSet for dynamic volume binding ([example in GitHub](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/latebind-storage-gke-sandbox)).

  
**Storage provisioning latency** | Several seconds per volume | 

  * Six minutes to create an instance with up to 80 shares
  * Multiple instances can be created in parallel

  
**Hot path attachment and mount latency** | Several seconds for disk attachment | Sub-second for Network NFS mount  
**Maximum read throughput** | 

  * 2,400 MiB/s per disk
  * Throughput is limited by the attached device's physical hardware limit

| 

  * 120 MiB/s per 1 TiB of provisioned capacity
  * Throughput is capped at 1,200 MiB/s for a maximum-capacity 10 TiB multishares instance

  
**IOPS** |  From 3,000 to 160,000, [depending on volume size and configuration](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#provisioned-iops-limits) | 

  * **Read IOPS:** 12,000 Read IOPS per 1 TiB of instance capacity (maximum of 120,000 Read IOPS)
  * **Write IOPS:** 4,000 Write IOPS per 1 TiB of instance capacity (maximum of 40,000 Write IOPS)

  
**Size limits** | 

  * **[Per disk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits):** 4 GiB minimum, 64 TiB maximum (128 TiB on C4)
  * **[Per node](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#hyperdisk-capacity):** maximum 247 TiB for fewer than 32 vCPUs, or 512 TiB for 32 or more vCPUs

| 

  * **[Multishare instance](https://docs.cloud.google.com/filestore/docs/service-tiers-enterprise):** 1 TiB minimum, 10 TiB maximum
  * **[Share size (PVC)](https://docs.cloud.google.com/filestore/docs/limits#fileshare-limits):** 10 GiB minimum, 1 TiB maximum

  
**Scale limits** | 

  * **Per node:** up to 128 attached volumes ([varies by machine type](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#max-total-disks-per-vm))
  * **[Per volume](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#hdml-ro-limitations):** up to 2,500 instances in ROX mode for Google Cloud Hyperdisk ML

| 

  * **Per node:** no attachment limits
  * **Per multishare instance:** maximum 80 shares, and up to 20,000 connections (2,000 per 1 TiB, scaling in increments of 500)

  
**Capacity scaling direction** | Only scales up | Scales up or down  
**CSI VolumeSnapshot support** | Supported | Not supported (per-share snapshots are not supported)  
**Price** |  [Persistent Disk and Google Cloud Hyperdisk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#persistent-disk-and-hyperdisk-pricing) |  [Filestore pricing](https://docs.cloud.google.com/filestore/pricing#filestore-pricing)  
  
## What's next

  * [Learn more about Agent Sandbox on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox).
  * [Learn how to manage Agent Sandbox on GKE file storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
