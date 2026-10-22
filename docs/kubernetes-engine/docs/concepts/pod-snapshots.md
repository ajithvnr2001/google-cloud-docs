---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots/
title: About GKE Pod snapshots \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:54.695955+00:00
---

# About GKE Pod snapshots  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About GKE Pod snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) Pod snapshots help improve workload startup latency by restoring snapshots of running Pods. A Pod snapshot saves the entire Pod state, including memory and file system changes. When you create new replicas, they're restored from the snapshot, letting the workload resume instead of starting from a new state. This capability is helpful for horizontally scaling workloads, such as AI inference models that load large weights into memory or applications that load extensive dependencies.

Use this document to understand how GKE Pod snapshots work and evaluate whether your workloads can benefit from them.

Platform admins and operators and Application developers can use this document to evaluate workload compatibility, plan snapshot storage policies, and understand how GKE manages checkpointing and restoration. For more information about the common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

To prepare for and use Pod snapshots in your clusters, see the following guides:

  1. [Prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare)
  2. [Trigger a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger)
  3. [Restore a workload from a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots)



## When to use Pod snapshots

Use Pod snapshots for workloads that have long initialization times. Examples include AI inference workloads that load large models into CPU or GPU memory, or large applications that load many libraries and dependencies. Workloads that already have fast startup times generally won't benefit from Pod snapshots.

## How Pod snapshots work

GKE Pod snapshots store an exact copy of a Pod's process state at a specific time. When you create new replicas, instead of initializing the Pod from a fresh state, GKE restores the Pod from a snapshot. This restoration means that the Pod resumes execution from the point the snapshot was taken.

To configure Pod snapshots declaratively, you create Kubernetes custom resources to define snapshot behavior. An agent that runs on each GKE node manages the snapshot lifecycle. Based on the policies that you define, the agent determines when to create new snapshots and when to use existing snapshots to restore new Pods. A controller that runs on the GKE control plane cleans up obsolete snapshots and resolves issues. Cloud Storage stores your Pod snapshots.

### Snapshot contents

The following table lists what a Pod snapshot includes and excludes:

Category | Included | Excluded  
---|---|---  
Application state | 

  * Process memory
  * Execution threads
  * CPU registers
  * Open file descriptors

| Nothing (all in-memory process state is captured)  
File systems | 

  * Container root file system (`rootfs`)
  * `emptyDir` volumes
  * `tmpfs` mounts

| 

  * PersistentVolumeClaim objects
  * Any other volume or storage type not listed as included

  
Networking | 

  * Loopback connections
  * Listening sockets
  * Unix domain sockets

| 

  * Active external connections (closed on restore)
  * Custom routes
  * User-defined rules (`iptables`, `nftables`)

  
  
### Custom resources

To configure Pod snapshots declaratively, use the following custom resources:

  * **PodSnapshotStorageConfig** : specifies the storage location for snapshots. Supports only [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets).
  * **PodSnapshotPolicy** : defines which Pods to snapshot based on Kubernetes label selectors. This custom resource contains most configuration options for the feature, including how snapshots are triggered, snapshot scope, and retention policies.
  * **PodSnapshotManualTrigger** (optional): if you don't use a workload trigger, defines a manual trigger to create a snapshot for a specific Pod.



For reference specifications, see the [PodSnapshot CustomResourceDefinition reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/podsnapshot).

### Snapshot triggers

You can trigger a Pod snapshot in the following ways:

  * **Workload trigger** : the application inside the Pod signals to the GKE agent that it's ready for a snapshot. This type of trigger executes once in a workload cycle, for example at a workload ready state. This approach is best for improving startup latency of horizontally scaling workloads.
  * **Manual trigger** : you can trigger a snapshot on demand for a specific Pod by creating a PodSnapshotManualTrigger custom resource. This type of trigger can execute as many times as needed. This approach is best for situations when you can't modify your application to signal readiness.



### Snapshot matching and compatibility

To help ensure that a snapshot is compatible with a restored workload, GKE performs compatibility matching between the original checkpointed Pod and the target Pod.

GKE uses the following rules to determine compatibility:

  * **Selection order** : by default, GKE restores workloads from the most recent PodSnapshot custom resource that matches the Pod's namespace and configuration.
  * **Match criteria** : the compatibility check depends on the snapshot scope configured in your PodSnapshotPolicy custom resource (`whole-pod` or `rootfs-only`).



#### `whole-pod` scope matching (default)

For policies with the default `whole-pod` scope, GKE checks the following:

  * **Distilled spec hash** : GKE generates a unique hash based on essential runtime fields in the Pod's specification. For a restore to succeed, the target Pod must generate an identical hash from its distilled specification. This check verifies that the checkpointed and restored Pods are identical in their runtime configurations.

The following fields from the Pod object are part of the distilled specification and influence the unique hash:

    * **`metadata`** : 
      * `annotations`: only annotations that are relevant to GKE Sandbox (such as annotations that start with the `dev.gvisor.*` prefix).
      * `labels`: `batch.kubernetes.io/job-completion-index`
    * **`spec`** : 
      * `volumes`: `name`, `volumeSource`, `hostPath`, `persistentVolumeClaim`, `configMap`
      * `containers`: 
        * `name`
        * `image`
        * `command`
        * `args`
        * `workingDir`
        * `ports`: `name`, `containerPort`, `protocol`
        * `volumeMounts`: `name`, `readOnly`, `recursiveReadOnly`, `mountPath`, `subPath`, `mountPropagation`, `subPathExpr`
        * `volumeDevices`: `name`
        * `lifecycle`: `postStart`, `preStop`
        * `terminationMessagePath`
        * `terminationMessagePolicy`
        * `securityContext` (and all subfields)
        * `stdin`
        * `stdinOnce`
        * `tty`
      * `initContainers`: same subfields as `containers`.
      * `dnsPolicy`
      * `automountServiceAccountToken`
      * `hostNetwork`
      * `hostPID`
      * `hostIPC`
      * `shareProcessNamespace`
      * `securityContext`
      * `dnsConfig`
      * `runtimeClassName`
      * `os`
      * `hostUsers`
  * **Hardware compatibility** : the target Pod must run on a node with the same machine series, CPU vendor, and CPU feature set (`CPUID` flags) as the checkpointed Pod. For example, both nodes must use the same N2 or G2 series and the same Intel or AMD processor features. GKE Sandbox verifies CPU features before restoring process memory and CPU state, so a snapshot with the `whole-pod` scope can't restore onto a node with different CPU features.

  * **Version compatibility** : the GKE Sandbox kernel version and GPU driver version must match the version captured in the original snapshot.




#### `rootfs-only` scope matching

When you configure your policy with the `rootfs-only` scope (available in GKE version 1.35.3-gke.1031000 and later), the matching requirements are less strict:

  * GKE doesn't compute or compare the distilled Pod spec hash. This relaxed matching lets you restore a snapshot to a target Pod with different resources, environments, or other configuration fields. However, the underlying container image and node versions must be compatible.
  * Because process memory isn't restored, you can restore snapshots taken on one machine family to a different machine family (including E2 machine types).



#### Grouping rules matching

If the policy uses the `snapshotGroupingRules` field to group snapshots by specific label values (such as tenant or environment), then the restored Pod must have matching label keys and values. The Pod snapshot controller selects a snapshot only from the matching group. For more information about how to set up grouping labels, see [Configure additional Pod snapshot policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-trigger#retention-grouping).

### Restore readiness and background loading

When a Pod is restored from a snapshot, the GKE Sandbox kernel is restored first, which typically takes a few seconds. To minimize startup latency, the application resumes immediately after the kernel is restored. It doesn't wait for the application memory to be fully loaded. Application memory is restored using a background streaming mechanism.

If the application attempts to read a part of memory that hasn't been loaded yet, then a page fault occurs. GKE Sandbox intercepts this fault, pauses the application thread, and immediately fetches the required memory page from storage. This on-demand fetching is prioritized over the background stream.

Because of this background loading, memory access might experience brief latency for the first few seconds after a restore if the application requests unstreamed memory. This latency disappears when the memory state is fully synchronized.

This background loading behavior also applies to the GPU state. For example, a large language model (LLM) Pod might appear to be in the `Running` state and respond to network checks even though its GPU memory is still being populated. The model won't be fully responsive for inference until the GPU state is completely restored. Because of this delay, when measuring restoration speed, make sure that you measure when the model server is ready to serve requests. You can verify model server readiness using metrics such as time to first token (TTFT) or [Pod readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes).

## GPU state

Pod snapshots support capturing the state of GPUs. When you trigger a snapshot for a Pod that uses GPUs, the NVIDIA `cuda-checkpoint` tool saves the GPU state into process memory. This step helps ensure that data stored on the GPU, such as model weights, is included in the snapshot. GKE pauses the Pod and takes a snapshot. During restore, GKE reverses this operation.

Because GPU state is written into process memory, Pod memory usage increases during snapshot and restore operations. Account for this additional memory requirement when you set memory limits for your Pods.

## Considerations for restored Pods

From the perspective of the Kubernetes API, a new Pod object is created. When the Pod starts, if there is a corresponding snapshot for the Pod, then GKE restores the Pod from that snapshot, including the original memory and process state. However, some aspects of the Pod's state must change for it to function as a new, unique instance.

Consider the following state changes after a restore:

  * **Network interfaces** : the restored Pod receives a new IP address. All interfaces and routes are reconfigured. Active network connections that existed at the time of the snapshot are closed on restore. Listening sockets, loopback connections, and Unix domain socket connections continue to function.
  * **Hostname** : the restored Pod assumes a new identity and receives a new hostname.
  * **Wall-clock time** : the wall-clock time jumps ahead to the current time.
  * **Application state** : the application state must be unique for each Pod, such as experiment IDs or random number seeds, and must be reinitialized after a restore.
  * **Secrets** : encryption keys and certificates created before you take the snapshot must be re-created.
  * **Environment variables** : you can change environment variables between a snapshot and a restore. However, because environment variables are stored in application memory, GKE Sandbox can't reliably find and replace them. If your workload relies on new environment variables after a restore, then the Pod must manually refresh them. The new environment variables are available in the `/proc/gvisor/spec_environ` file. The file format is the same as `/proc/<pid>/environ`.



## Multi-tenancy and identity

Pod snapshots require manual Identity and Access Management (IAM) bindings for each Pod's Kubernetes ServiceAccount object to use Cloud Storage. The manual IAM bindings can take time to propagate, which might be an issue if you need to take snapshots immediately after creating a Pod.

To address delays and simplify multi-tenant management, instead of manually binding IAM to ServiceAccount objects, you can use a GKE node service account to create short-lived tokens on demand. To configure Pod snapshots with this approach, use the `tokenSource` field in the PodSnapshotStorageConfig custom resource with one of the following values:

  * `podKSA` (default): uses manual IAM bindings between the Pod's ServiceAccount object and the Cloud Storage bucket.
  * `federatedP4SA`: uses a path-specific token minted by the node service account.



## Requirements

To use GKE Pod snapshots, make sure that you meet the following requirements:

  * Pods must run in [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods) because Pod snapshots depend on the isolated environment that GKE Sandbox provides.
  * For the default `whole-pod` snapshot scope, the node where the Pod is restored must have the same machine series, CPU vendor, and CPU features as the node where the snapshot was taken. CPU-only workloads can use any non-E2 machine series supported by GKE Sandbox that meets these hardware compatibility requirements. For more information, see Limitations.
  * To use GPUs with Pod snapshots, you must also meet the following requirements: 
    * Single-GPU Pods are supported on both single-GPU and multi-GPU nodes.
    * Multi-GPU Pods are supported only on L4 GPUs (`g2-standard-*` machine types).
    * In GKE versions 1.35.0-gke.1738000 and earlier, a Pod that runs on a multi-GPU node must use all the GPUs available on that node. In versions 1.35.0-gke.1738000 and later, Pods can use a subset of the GPUs on a node.
    * For GPU workloads, you must use one of the following supported GPU machine types: 
      * `g2-standard-4` (1 x L4)
      * `g2-standard-8` (1 x L4)
      * `g2-standard-12` (1 x L4)
      * `g2-standard-16` (1 x L4)
      * `g2-standard-32` (1 x L4)
      * `g2-standard-48` (4 x L4)
      * `g2-standard-96` (8 x L4)
      * `a2-highgpu-1g` (1 x A100-40GB)
      * `a2-ultragpu-1g` (1 x A100-80GB)
      * `a3-highgpu-1g` (1 x H100-80GB)



## Limitations

GKE Pod snapshots have the following limitations:

  * When you use the default `whole-pod` snapshot scope, a snapshot can't restore onto a Compute Engine VM with different CPU features (`CPUID` flags) than the VM where the snapshot was taken: 
    * Pod snapshots with the `whole-pod` scope don't support the E2 machine series, or other machine series that dynamically mix Intel and AMD processors or CPU generations. File system snapshots (`rootfs-only` scope) support the E2 machine series.
    * Even within the same non-E2 machine series and CPU vendor, Compute Engine might provision VMs with different CPU platforms or per-VM CPU feature sets. If a Pod is scheduled onto a node with mismatched CPU features, then restoring a snapshot with the `whole-pod` scope fails.
  * GPU sharing with Multi-Instance GPU (MIG) isn't supported.
  * The Cloud Storage FUSE CSI driver sidecar container isn't supported with Pod snapshots.
  * Pod snapshots don't support TPUs.



## What's next

  * Learn how to [prepare for Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots-prepare).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
