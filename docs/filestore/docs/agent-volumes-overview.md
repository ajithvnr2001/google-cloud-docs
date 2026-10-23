---
url: https://docs.cloud.google.com/filestore/docs/agent-volumes-overview/
title: About Filestore agent volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:55.813141+00:00
---

# About Filestore agent volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/agent-volumes-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  About Filestore agent volumes Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the [Filestore agent volumes access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited GA program. To check your eligibility or to request production support, use the access form. 

Filestore agent volumes are a fully managed, high-density elastic NFS file storage capability built for stateful AI agent sandboxes, autonomous agent fleets, and multi-agent developer environments.

Filestore agent volumes provide the persistent storage layer required to maintain state, context, and history across agent executions, enabling low latency workloads, high density compute utilization, and strong sandbox isolation. Filestore agent volumes can also be used for any agent workspace or scratchpad needs, because agents natively work on file systems.

While designed primarily for AI agent workloads and developer sandboxes, volume pools and volumes also provide a general-purpose file storage architecture for applications that require multiple lightweight, independent file systems.

## Use cases

Filestore agent volumes are designed for architectures that require numerous lightweight, fast-mounting file systems. Common use cases include:

  * **Stateful AI agent sandboxes:** Provide persistent storage for interactive coding agents and autonomous workflows, supporting under 100 ms volume reattachment across suspend and resume cycles.
  * **Collaborative multi-agent swarms:** Enable teams of specialized agents to work concurrently on shared repositories with POSIX-compliant ReadWriteMany (RWX) access and byte-range locking.
  * **High-density developer environments:** Host multi-tenant cloud IDEs and developer sandboxes, scaling up to one million isolated volumes backed by a single regional capacity pool.
  * **Ephemeral CI/CD and automated testing:** Provision short-lived, isolated storage for test runners and build pipelines with sub-second API turnover.
  * **Secure execution of untrusted code:** Run model-generated code safely within gVisor container sandboxes on GKE, using root squashing (`root_squash`) to protect underlying storage.



### Stateful agent workflow on GKE

The following diagram illustrates how Filestore agent volumes, Private Service Connect (PSC), and GKE work together during an agent session:

![Workflow showing Filestore agent volumes on GKE](https://docs.cloud.google.com/static/filestore/images/filestore-agent-volumes-workflow.svg)**Figure 1.** Workflow showing how Filestore agent volumes work with GKE. 

  1. The GKE cluster communicates with the managed storage plane through PSC service connection policies. All storage and NFS traffic remains private within your Virtual Private Cloud (VPC) network without requiring external IP addresses or VPC peering.
  2. A regional volume pool reserves shared capacity and IOPS for your project. When an agent session is requested, an individual volume is provisioned from the pool using the Filestore CSI driver or API in under a second.
  3. GKE schedules a container pod isolated with gVisor. The Filestore CSI driver attaches and mounts the volume to the pod's workspace directory (such as `/workspace`) in under 100 ms.
  4. The agent initializes inside the sandbox, immediately accessing its dedicated file system to clone Git repositories, install packages, and write scratchpad artifacts. When the agent becomes idle, GKE can terminate the compute pod to save costs while the volume preserves all workspace state for instant resumption.



## Core capabilities

Filestore agent volumes deliver the following core capabilities:

  * **Ultra-high volume density:** Provision up to 1 million independent volumes within a single regional volume pool.
  * **Sub-second operations:** Create and delete volumes in under one second using REST APIs, matching the ephemeral lifecycle of autonomous agent tasks.
  * **Storage attach under 100 ms:** Mount existing volumes into pre-warmed sandboxes in under 100 ms, enabling instant interactive user sessions and high utilization of compute infrastructure.
  * **POSIX compliance and RWX sharing:** Provide NFSv3 file system semantics, directory hierarchies, and byte-range file locking across multiple containers and nodes.
  * **Private VPC connectivity:** Connect securely to your VPC network using Private Service Connect (PSC) service connection policies.



## Volume pool and volumes

Filestore agent volumes introduce a simplified two-tier resource model. The underlying storage infrastructure is managed for you, so you don't need to manage or configure file server instances:

  1. **Volume pool** : The top-level managed regional resource. A volume pool reserves a shared pool of storage capacity and IOPS for a project and VPC network, and enforces default volume quota policies.
  2. **Volume** : The individual, POSIX-compliant storage resource provisioned inside a volume pool. Each volume represents an isolated file system that can be mounted into one or more containers, pods, or VMs.



## Supported workload patterns

You can integrate Filestore agent volumes into your architectures using several orchestration models:

  * **GKE Agent Substrate:** Use GKE Agent Substrate to manage the lifecycle of stateful agent sandboxes. Agent Substrate suspends idle agents to save compute costs and resumes them in under a second, while Filestore agent volumes persist the workspace file system state across suspend and resume operations. For more information, see [Use Filestore agent volumes with GKE Agent Substrate](https://docs.cloud.google.com/filestore/docs/agent-substrate).
  * **GKE Agent Sandbox:** Use GKE Agent Sandbox to manage the lifecycle of isolated, stateful agent environments with pre-warmed sandbox pools. For more information, see [Use Filestore agent volumes with GKE Agent Sandbox](https://docs.cloud.google.com/filestore/docs/agent-sandbox).
  * **Dynamic storage late-binding:** For latency-critical interactive platforms, inject pre-provisioned NFS volumes into pre-warmed running sandbox pods in under 100 ms using host daemons and mount propagation, eliminating pod restart latency. For more information, see [Use Filestore agent volumes with Agent Sandbox dynamic storage late-binding](https://docs.cloud.google.com/filestore/docs/agent-sandbox-latebind).
  * **Self-managed GKE workloads:** Deploy standard Kubernetes `Deployment`, `StatefulSet`, or `Job` workloads with `PersistentVolumeClaim` (PVC) resources backed by the Filestore CSI driver and volume pool `StorageClass` resources. For more information, see [Use Filestore agent volumes with self-managed GKE workloads](https://docs.cloud.google.com/filestore/docs/self-managed-gke).



## What's next

  * Set up [Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-prerequisites).
  * Create and configure [volume pools](https://docs.cloud.google.com/filestore/docs/create-volume-pools).
  * Configure [GKE environment for Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/use-filestore-agent-volumes-gke).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
