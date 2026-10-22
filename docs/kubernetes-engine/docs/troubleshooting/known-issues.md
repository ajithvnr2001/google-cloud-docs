---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues/
title: GKE known issues \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:39.613720+00:00
---

# GKE known issues  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  GKE known issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page lists known issues for GKE. This page is for Admins and architects who manage the lifecycle of the underlying technology infrastructure, and respond to alerts and pages when service level objectives (SLOs) aren't met or applications fail.

This page lists known issues for all supported versions and for the two minor versions that immediately precede the earliest version in [extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#periods_of_availability_in_the_minor_version_lifecycle). After a version reaches the end of extended support, all N-2 issues are removed. For example, when version 1.30 reaches the end of extended support, known issues specific to versions 1.28 and earlier are removed.

If you're part of the Google Developer Program, save this page to receive notifications when a release note related to this page is published. To learn more, see [Saved Pages](https://developers.google.com/profile/help/saved-pages).

To filter the known issues by a product version or category, select your filters from the following drop-down menus.

Select your GKE version:

1.351.341.331.321.311.301.291.281.27

Select your problem category:

ConfigurationInstallationUpgrades and updatesOperationLogging and monitoringSecurityReset/DeletionPerformance

Or, search for your issue:

Category | Identified version(s) | Fixed version(s) | Issue and workaround  
---|---|---|---  
Operation | 

  * 1.35
  * 1.36
  * 1.37

| 

  * 1.35.6-gke.1250001 and later
  * 1.36.4-gke.1391002 and later
  * 1.37.1-gke.1187000 and later

| 

###  HTTP POST requests for tokens from the metadata server fail with a 400 Bad Request error 

Workloads that use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate to Google Cloud APIs by requesting service account access tokens or identity tokens from the GKE metadata server (such as `/computeMetadata/v1/instance/service-accounts/default/token` or `/computeMetadata/v1/instance/service-accounts/default/identity`) might fail with an `HTTP 400 Bad Request` (`INVALID_ARGUMENT`) error.  This issue occurs when an application, client library, or API gateway sends an HTTP `POST` request without a valid certificate chain in the request body. In affected GKE versions, `POST` requests to these token endpoints are strictly reserved for bound access and ID tokens. As a result, requests that have empty, form-encoded, or invalid JSON in the payloads are rejected.  To fix the issue, upgrade to the latest patch version within the minor version of any release channel.  **Workaround:** To resolve this issue, configure your application, client library, or API gateway to use the `GET` method instead of `POST` when you request access or ID tokens from the metadata server, like in the following example: 
    
    
    curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"
        

If your workload uses a third-party SDK or gateway (such as MuleSoft Flex Gateway, IBM App Connect, or custom HTTP scripts) that defaults to sending `POST` requests to metadata server endpoints, update the configuration or client library to send `GET` requests.   
Upgrades and updates | 

  * 1.33 and later

| TBD | 

###  Unscheduled Pods and exhausted quota during two-step minor upgrades for the control plane. 

During two-step minor version upgrades for control planes in Autopilot clusters that use [extended duration Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods), new node pools might be provisioned using the earlier node version. Cluster Autoscaler evaluates the newly provisioned nodes against the upgraded control plane version, detects a version mismatch, and applies the `cloud.google.com/not-target-gke-version:true` taint. Cluster Autoscaler also blocks scaling up existing or newly created extended duration Pod node pools that use the earlier node version.  This behavior prevents Pods from scheduling and triggers an infinite scaling loop. Instead of scaling up an existing node pool, node auto-provisioning creates a new single-node pool on every scale-up iteration to accommodate the pending workloads. This loop generates hundreds of separate empty node pools that can eventually exhaust regional Managed instance group quotas.    
**Workaround:** To resolve the scaling loop, manually complete the control plane upgrade by running the following command: 
    
    
    gcloud container clusters complete-control-plane-upgrade [CLUSTER_NAME] --location=[LOCATION]

Alternatively, apply the following toleration to the affected workloads so they can be scheduled on the earlier-version nodes: 
    
    
    tolerations:
    - key: "cloud.google.com/not-target-gke-version"
      operator: "Equal"
      value: "true"
      effect: "NoSchedule"  
  
Operation | 1.37.0-gke.2941000 and later | 1.37.1-gke.1131000 | 

### Nodes that mount NFS volumes accumulate mount entries and stop creating containers

On nodes running affected versions, mounting an NFS volume leaves extra entries in the node's mount table. Additionally, when a Pod using an NFS volume terminates, unmount attempts fail, causing the `kubelet` to repeatedly retry the unmount. Each retry adds more entries to the mount table, which causes the mount table to grow continuously even when no new workloads are scheduled. When the mount table reaches the kernel limit, the container runtime can no longer create containers on that node. The node stops running new Pods, might report a `NotReady` status, and might restart repeatedly. Pods that use NFS volumes might remain in the `Terminating` state because their volumes can't be unmounted. In Pod events and `kubelet` logs, nodes in this state report errors similar to the following:
    
    
    MountVolume.SetUp failed for volume "VOLUME_NAME" : mount failed: exit status 1
    
    
    mount: /etc: mount(2) system call failed: No space left on device

This issue affects node pools that mount NFS volumes with the Kubernetes in-tree NFS driver. Nodes that don't use the in-tree NFS driver to mount NFS volumes aren't affected. **Workaround:** To recover an affected node, restart or re-create it. The extra mount entries exist only in the running state of the node, so they're cleared when the node restarts. Pods that are stuck in the `Terminating` state after the restart can be removed with the following command:
    
    
    kubectl delete pod POD_NAME --namespace NAMESPACE --force --grace-period=0
        

To stop the issue from recurring in Standard clusters, [downgrade the node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#downgrading_nodes) that mount NFS volumes to a 1.36 version. Set a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) so that GKE doesn't automatically upgrade the node pools back to an affected version. If an Autopilot cluster runs an affected version, use one of the following options instead:

  * If your NFS volumes are backed by Filestore, mount them with the [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver) instead of the in-tree NFS driver. The CSI driver mounts volumes from its own container and doesn't use the affected node component.
  * If you must keep using the in-tree NFS driver, let [node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) recover affected nodes. Autopilot clusters repair nodes automatically, and a node that reports a `NotReady` status for about 10 minutes is drained and re-created, which clears its mount table.

  
Upgrades | 1.34.9-gke.1065000 and later, 1.35.6-gke.1049000 and later, and all 1.36 patch versions | 1.34.10-gke.1328000 and later, 1.35.8-gke.1026000 and later, 1.36.4-gke.1058000 and later (no fix is available yet for 1.37) | 

### A4X Max (GB300) GPU workload failures

Creating or upgrading GKE [A4X Max node pools](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-max-metal-machine-type) (`a4x-maxgpu-4g-metal`) on or to specific patch versions (see the **Identified version(s)** column) causes GPU workload failures with the attached NVIDIA GB300 Grace Blackwell Ultra Superchips. Due to extended High Bandwidth Memory (HBM) boot times on GB300 hardware with this bare metal machine type, the `nvidia-persistenced` startup service times out. This timeout leaves the GPUs uninitialized, and results in the `cudaErrorDeviceUnavailable(46)` error message when Pods attempt to claim CUDA resources. **Solution:** Upgrade each impacted cluster and node pool to a fixed version. GKE prevents creating A4X Max node pools with affected versions, and won't automatically upgrade the node pools to affected versions. GKE doesn't prevent manual upgrades to the affected versions. However, to avoid the failures, we recommend not upgrading to the affected versions. **Workaround:** If you cannot upgrade, delete all A4X Max node pools that are running affected versions, and re-create the node pools using an earlier, unaffected version. Note that because A4X Max capacity must be obtained through a reservation, you won't forfeit any capacity by deleting the node pools.   
Operation | 1.33 versions earlier than 1.33.5-gke.2469000, 1.34 versions earlier than 1.34.1-gke.2037001 | 1.33.5-gke.2469000 and later, 1.34.1-gke.2037001 and later, 1.35 and later | 

### GPU or TPU nodes stuck with impending-node-termination taints after host maintenance

On GKE clusters with accelerator nodes (GPU or TPU) that run affected versions, nodes might become stuck with the `cloud.google.com/impending-node-termination` or `cloud.google.com/maintenance-window-started` taints after Compute Engine host maintenance or repairs are completed. When the VM instance is started again, the GKE maintenance controller might prematurely re-apply these taints if there is another future maintenance event scheduled for the node, preventing new workloads from scheduling on healthy nodes. **Workaround:** To resolve the stuck state, you must manually remove both the GKE managed active maintenance labels and the taints from the affected nodes. If you only remove the taints, the GKE maintenance controller will automatically re-apply them. To clear the labels and taints, run the following commands:
    
    
    kubectl label nodes NODE_NAME cloud.google.com/active-node-maintenance-
    kubectl label nodes NODE_NAME cloud.google.com/scheduled-maintenance-time-
    kubectl label nodes NODE_NAME cloud.google.com/scheduled-maintenance-time-latest-
    kubectl taint nodes NODE_NAME cloud.google.com/impending-node-termination-
    kubectl taint nodes NODE_NAME cloud.google.com/maintenance-window-started-
        

Replace `NODE_NAME` with the name of the affected node.  
Operation | 

  * 1.33
  * 1.34

| 1.34.1-gke.1829001 and later | 

###  Pod admission failures for TPU v7 workloads due to reporting an incorrect chip count. 

GKE incorrectly advertises eight allocatable TPU chips for TPU v7 (tpu7x) accelerators with a 2x2x1 topology, which physically contains only four chips. This reporting mismatch prevents Pod scheduling for TPU v7 workloads.  The dual-chiplet architecture of TPU v7 is not correctly handled in earlier versions, resulting in Pod admission failures. Depending on the requested TPU resources, the following errors occur: 

  * When requesting four TPUs (`google.com/tpu: 4`), the `kubelet` returns an `UnexpectedAdmissionError`: _"invalid TPU chip count request, you must request all 4 chips on this node together"_. 
  * When requesting eight TPUs (`google.com/tpu: 8`), the `tpu-accelerator-topology-constraints` admission webhook denies the request with the following error: _"Invalid resource requests for google.com/tpu. It should be equal to one of [4] for accelerator tpu7x and topology 2x2x1"_. 

  
**Workaround:** To resolve this issue, upgrade the GKE cluster to version 1.34.1-gke.1829001 or later.   
Operation | 1.35.3-gke.1234000 and later | TBD | 

### Lustre client does not utilize secondary NICs on multi-NIC nodes

On GKE nodes with multiple Network Interface Cards (NICs), the Managed Lustre CSI driver is enabled by default to use all available NICs to aggregate bandwidth by spreading TCP storage traffic across network interfaces. However, because of a known issue, Lustre clients starting from version `2.14.0_p249` might not utilize secondary NICs. Instead, all TCP storage traffic to the Managed Lustre instance is routed exclusively through the primary NIC, preventing bandwidth aggregation and limiting storage throughput. **Workaround:** If your workloads require multi-NIC bandwidth aggregation for Managed Lustre, [downgrade your node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#downgrading_nodes) to a GKE version earlier than 1.35.3-gke.1234000, such as 1.35.2-gke.1842000.  
Operation | 1.35 and later | TBD | 

### Connection timeout or connection refused for flows redirected to GKE metadata server

In GKE version 1.35 and later, workloads that use [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to authenticate to Google Cloud APIs might experience transient connectivity timeouts or refused connections to the GKE metadata server immediately following node startup. **Workaround:** For recommendations and workarounds, see [troubleshoot timeout errors at Pod startup](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/authentication#troubleshoot-timeout).  
Operation | 1.33.8-gke.1026000 and later | 1.35.1 and later | 

### gVisor shim fails to clean up, logs `"runsc: executable file not found in $PATH"` error

Upon every gVisor Pod exit or OOM kill, containerd attempts to tear down the sandbox. However, the cleanup process sometimes fails, logging the error `exec: "runsc": executable file not found in $PATH`. This error can cause issues such as resource exhaustion, network degradation, NodeLocalDNS panic, DNS timeouts, or high latency when creating Pods. **Solution:** Upgrade the GKE nodes to version 1.35.1 or later. For Standard clusters, upgrade the node pool with the affected nodes. For Autopilot clusters, manually upgrade the Autopilot cluster to 1.35.1 or later, and GKE automatically upgrades your nodes to match the control plane version as soon as possible. **Workaround:** If you can't upgrade your cluster, do one of the following:

  * Review and increase the memory requests and limits for the gVisor pods.
  * Deploy the following privileged DaemonSet to copy the `runsc` binary from `/home/containerd/usr/local/sbin` to `/home/kubernetes/bin`:


    
    
    apiVersion: apps/v1
    kind: DaemonSet
    metadata:
      name: runsc-path
      namespace: kube-system
    spec:
      selector:
        matchLabels:
          app: runsc-path
      updateStrategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app: runsc-path
        spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: sandbox.gke.io/runtime
                    operator: In
                    values:
                    - gvisor
          tolerations:
            - effect: NoSchedule
              key: sandbox.gke.io/runtime
              operator: Equal
              value: gvisor
          volumes:
          - name: host
            hostPath:
              path: /
          initContainers:
          - name: copy-runsc
            image: bash
            command:
            - /usr/local/bin/bash
            - -c
            - |
              set -euo pipefail
              cp /host/home/containerd/usr/local/sbin/runsc /host/home/kubernetes/bin
              chmod a+rx /host/home/kubernetes/bin/runsc
            volumeMounts:
            - name: host
              mountPath: /host
            resources:
              requests:
                memory: 5Mi
                cpu: 5m
            securityContext:
              privileged: true
          containers:
          - image: gcr.io/google-containers/pause:3.2
            name: pause
          
  
Operation | 1.35.0-gke.2232000 and later | 1.35.3-gke.1.35.3-gke.1290000 and later | 

### Dynamic volumes fallback to default disk type

Workloads using [dynamic volumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#automated_disk_type_selection) in GKE version 1.35.0-gke.2232000 or later might fail to schedule or attach. This issue can also cause volumes to be provisioned using the fallback `hd-type` (such as `hyperdisk-balanced`) instead of the `pd-type`, even on nodes that don't support Hyperdisk. This occurs because the PDCSI Node server fails to populate the `CSINode` object with the supported disk type topologies. As a result, the controller lacks the necessary topology information to match volumes with compatible nodes. **Workaround:** Upgrade to 1.35.3-gke.1290000 or later.  
Upgrades and updates | 

  * All patch versions earlier than 1.34.3-gke.1208000 for GKE 1.34
  * All patch versions earlier than 1.35.0-gke.2232000 for GKE 1.35

| 

  * 1.34.3-gke.1208000 for GKE 1.34
  * 1.35.0-gke.2232000 for GKE 1.35

| 

### Pod startup issues during upgrades to GKE 1.35 for GKE Dataplane V2 clusters

Clusters upgrading control plane to GKE version 1.35.0-gke.2232000 and later from versions 

  * earlier than 1.34.3-gke.1208000 for GKE 1.34
  * earlier than 1.35.0-gke.2232000 for GKE 1.35

might experience Pod startup issues for new workloads created during `anetd` DaemonSet rollout. New workloads will fail to startup during `anetd` rollout if they are scheduled on a node with outdated `anetd`. During rollout, you might see the following error message:  ` Failed to create pod sandbox: rpc error [...] plugin type="cilium-cni" failed (add): unable to create endpoint: Cilium API client timeout exceeded ` This occurs because GKE uses Operator [identity-management-mode](https://docs.cilium.io/en/stable/network/kubernetes/identity-management-mode/#enable-identity-management-by-the-cilium-operator-beta) which requires all agents and the operator to have a synchronized view of [identity-relevant labels](https://docs.cilium.io/en/stable/operations/performance/scalability/identity-relevant-labels/). Starting in GKE 1.35.0-gke.2232000 `topology.kubernetes.io` labels are excluded from identity-relevant set to prevent identity duplication. This change causes a temporary configuration mismatch between the upgraded control plane and outdated `anetd` agents during the rollout. For more information, see the [Cilium PR](https://github.com/cilium/cilium/pull/43725). **Workaround:**

  * **For GKE 1.34 earlier than 1.34.3-gke.1208000** : upgrade first to 1.34.3-gke.1208000 or later and then upgrade to 1.35.0-gke.2232000 or later
  * **For GKE 1.35 earlier than 1.35.0-gke.2232000** : after upgrading, wait for the `anetd` rollout to finish. To speed up the rollout manually, delete outdated `anetd` Pods. This will ensure that the operator and the `anetd` node agents have a synchronized views of the identity-relevant labels.

  
Upgrades and updates | 

  * 1.32
  * 1.33
  * 1.34
  * 1.35

| 

  * 1.32.11-gke.1153001 and later
  * 1.33.5-gke.2326000 and later
  * 1.34.3-gke.1214000 and later
  * 1.35.0-gke.2180000 and later

| 

###  Pod scheduling delays on new nodes with Calico network policy enabled 

On GKE clusters with Calico network policy enabled, a regression in affected versions can cause significant delays in Pod scheduling on new or re-created nodes. These delays can result in nodes remaining in a `NotReady` state for extended periods.  The issue is caused by the Calico CNI startup script incorrectly formatting the Kubernetes API server URL for IPv4 addresses by enclosing them in square brackets ([]). This approach leads to a URL parsing error when creating new Pod sandboxes, visible in `kubelet` logs:  ` Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox ""sandbox-id"": plugin type="calico" failed (add): error creating calico client: host must be a URL or a host:port pair: "https://[IPv4-address]:443" `   
**Workaround:** The Calico component version is determined by the cluster's control plane version. To mitigate this issue, upgrade your cluster's control plane to one of the fixed versions. After upgrading the control plane, you must re-create the nodes in your node pools to ensure they use the correct Kubernetes API server URL format. You can achieve this by performing an in-place [upgrade of your node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading-nodes) to the same or a newer version or by manually re-creating your node pools.   
Performance | 

  * 1.32.8-gke.1134000 and later for GKE 1.32
  * 1.33.3-gke.1392000 and later for GKE 1.33
  * All patch versions for GKE 1.34 and 1.35

| 

  * 1.32.11-gke.1075000 and later for GKE 1.32
  * 1.33.5-gke.2392000 and later for GKE 1.33
  * 1.34.3-gke.1318000 and later for GKE 1.34
  * 1.35.0-gke.2398000 and later for GKE 1.35

| 

### General purpose networking's performance drops on A series and G4 GPU machine types

GKE clusters with A series and G4 GPU nodes shows degraded performance for general purpose networking on GKE 1.32.8-gke.1134000 and later for GKE 1.32, and on GKE 1.33.3-gke.1392000 and later. The performance degradation on general purpose networking impacts GPU machine types including A3 machine series, A4 machine series, A4X machine series, and G4 machine series. Note that GPUDirect-TCPXO on A3 Mega and GPUDirect-RDMA on A3 Ultra, A4, and A4X are not affected.  This occurs because the node level script (`/usr/bin/google_set_multiqueue`) that sets interrupt affinity is configured incorrectly. **Workaround:** Upgrade each impacted node pool to a fixed version.  
Performance | 

  * 1.32.8-gke.1134000 and later for GKE 1.32
  * 1.33.3-gke.1392000 and later for GKE 1.33 and later

| 

  * 1.32.11-gke.1075000 and later for GKE 1.32
  * 1.33.5-gke.2392000 and later for GKE 1.33

| 

### GPUDirect-TCPX's performance drops on A3 High

GKE clusters with A3 High (`a3-highgpu-8g`) nodes shows degraded performance when using [GPUDirect-TCPX](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx) on GKE 1.32.8-gke.1134000 and later for GKE 1.32, and on GKE 1.33.3-gke.1392000 and later.  This occurs because the node level script (`/usr/bin/google_set_multiqueue`) that sets interrupt affinity is configured incorrectly. **Workaround:** For GKE 1.32 node pools, upgrade the GKE nodepool versions to 1.32.11-gke.1075000 or later. For GKE 1.33 and later nodepools, upgrade the GKE nodepool versions to 1.33.5-gke.2392000 or later.1392000. For GKE 1.34 node pools, please see [GPUDirect-TCPX is unavailable with A3 High for GKE version 1.34 and later](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues#tcpx-cos125).  
Upgrades | 1.35 |  1.35.0-gke.2232000 and later. | 

### Cilium identity duplication in GKE Dataplane V2 clusters

GKE clusters running version 1.35 with GKE Dataplane V2 enabled might experience an increase in the number of `ciliumidentities.cilium.io` custom resources. This issue is caused by [topology.kubernetes.io labels being added to Pods](https://github.com/cilium/cilium/issues/43723) in Kubernetes 1.35, which produces additional Cilium identities for each zone that a Pod from a workload is scheduled to. In both Regional and Zonal clusters, scheduling a new workload can cause temporary Cilium identity duplication. This duplication occurs because Pods get one identity at creation time based on initial labels, and another identity after topology labels are added when the Pod is scheduled to a node. In Regional clusters, the number of identities might additionally increase by a factor proportional to the number of zones the cluster spans. **Impact:** If the total number of identities exceeds 65,535, new workloads might fail to schedule. **Workaround:** To limit the total number of identities, avoid adding labels with a large number of unique values to your Pods. For more information, see the following Cilium documentation: 

  * [Identity-based security](https://docs.cilium.io/en/stable/security/network/identity/)
  * [Security identities](https://docs.cilium.io/en/stable/internals/security-identities/)

Manual upgrades should be performed from versions 1.34.3-gke.1208000 and later. If you start the upgrade from a version earlier than 1.34.3-gke.1208000, you might experience temporary issues with Pod scheduling during the upgrade process.  
Upgrades | 

  * 1.34 patch versions before 1.34.5-gke.1153000
  * 1.35 patch versions before 1.35.2-gke.1485000

| 

  * 1.34.5-gke.1153000 and later
  * 1.35.2-gke.1485000 and later
  * 1.36 and later

You must also use GPUDirect-TCPX installer version 3.1.9 or later and sidecar version 2.0.12 or later. The installer and sidecar versions have a one-to-one mapping and must correspond. For example, the GPUDirect-TCPX installer version 3.1.12 corresponds to sidecar version 2.0.15. For more information about installer and sidecar versions, see the [GPUDirect-TCPX Release Notes](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/gpudirect-tcpx). | 

### GPUDirect-TCPX is unavailable with A3 High for specific GKE versions

GKE clusters with A3 High (`a3-highgpu-8g`) nodes use [GPUDirect-TCPX](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx) to maximize GPU network bandwidth. For nodes that use TCPX and A3 High, upgrading to affected GKE versions can result in functional or performance issues with TCPX. This is because TCPX is incompatible with the updated Linux kernel 6.12 used by Container-Optimized OS milestone 125 or later. Milestone 125 is used by GKE version 1.34. Other A3 High (`a3-highgpu-1g`, `a3-highgpu-2g`, `a3-highgpu-4g`) GPU machine types and other GPU machine series are not affected because they don't support GPUDirect-TCPX. **Solution:** Upgrade to fixed GKE version patches to resolve this issue. For details on configuring and upgrading node pools with GPUDirect-TCPX, see [Maximize GPU network bandwidth in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx) or [Maximize GPU network bandwidth in Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx-autopilot). When running NCCL tests on fixed versions, you might see the following warnings that have no impact on performance or functionality:

  * NCCL WARN logs for `Rx Ctrl Timeouts`: this message can appear if the workload posts a `Recv` communication operation on the target much earlier than it posts a `Send` communication operation on the initiator. There is no expected impact on performance.
  * NCCL WARN logs for `No free space for recv task`: this message warns of a low total number of network tasks to process operations, which results in all tasks being occupied temporarily. There is no expected impact on performance.

  
Operation | All versions before 1.34.0-gke.2285000 | 1.34.0-gke.2285000 and later | 

### Updated minimum instance capacity

The minimum capacity for Managed Lustre instances has been updated to 9000 GiB. Clusters running versions earlier than 1.34.0-gke.2285000 cannot create instances with this minimum capacity through the Managed Lustre CSI driver. **Workaround:** Upgrade your cluster version to 1.34.0-gke.2285000 or later to enable the creation of Managed Lustre instances with the minimum capacity of 9000 GiB.  
Operation | All versions | TBD | 

### Google Cloud console UI becomes uneditable during node auto-repair

When a GKE node is undergoing auto-repair, the node pool becomes uneditable through the Google Cloud console because of an ongoing operation. **Workaround:** You can still edit the node pool configuration by using gcloud CLI commands.  
Operation | 1.33 versions before 1.33.4-gke.1036000 | 1.33.4-gke.1036000 and later | 

### Incorrect performance tier for dynamically provisioned Lustre instances

When dynamically provisioning a Lustre instance, the instance creation fails with an `InvalidArgument` error for PerUnitStorageThroughput, regardless of the perUnitStorageThroughput value specified in the API request. **Workaround:** Upgrade the GKE cluster to version 1.33.4-gke.1036000 or later. If using the Stable channel, a newer version might not be available yet. In this case, you can manually select a version from the Regular or Rapid channels that includes the fix.  
Operation | 

  * 1.32.3-gke.1099000 and later
  * 1.33

| 1.33.3-gke.1266000 and later | 

### Input/output error when renaming or moving files using Cloud Storage FUSE CSI driver

When using an affected version of the Cloud Storage FUSE CSI driver, renaming or moving files in Cloud Storage buckets might fail with an I/O error. **Workaround:** Temporarily add a specific sidecar image definition to your Pod manifest. In the `spec.containers` section of your Pod manifest, add the following container definition with the image: `gcr.io/gke-release/gcs-fuse-csi-driver-sidecar-mounter:v1.8.9-gke.2`.
    
    
        # Add the following block to use the fixed sidecar image
        - name: gke-gcsfuse-sidecar
          image: gcr.io/gke-release/gcs-fuse-csi-driver-sidecar-mounter:v1.8.9-gke.2
        

For more information, see the Pod manifest in [Configure a private image for the sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-a-private-image). After you upgrade your cluster to a fixed GKE version or later, you must remove the entire `gke-gcsfuse-sidecar` block from your manifest. After removing this block GKE will resume to automatically inject and manage the correct sidecar image for your upgraded cluster version.  
Logging and monitoring | All versions | TBD | 

### Race condition in `gke-metrics-agent` DaemonSets

When you add the `cloud.google.com/gke-metrics-agent-scaling-level` label to a node pool to [manually increase the memory allocation of the `gke-metrics-agent` DaemonSet](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/system-metrics#confirm_metrics_agent_has_sufficient_memory), a race condition occurs in the DaemonSet during new node creation. This race condition results in intermittent restarts and might result in lost metrics. This issue occurs because there's a delay before the label is added to a new node in the node pool. During this delay, the DaemonSet creates a Pod with the original memory allocation on that node. After the label is applied, the DaemonSet creates a Pod that has the new memory allocation. The existing Pod isn't completely deleted when the updated Pod starts. Both of these Pods try to bind to the same port number. **Workaround:** After you add the `cloud.google.com/gke-metrics-agent-scaling-level` label to a node pool, restart the `gke-metrics-agent` DaemonSet:
    
    
    kubectl -n kube-system rollout restart daemonset gke-metrics-agent  
  
Upgrades | 1.33 | 1.33.2-gke.1043000 | 

### Lowered open files limit with containerd 2.0

For node pools running GKE version 1.33, which uses containerd 2.0, the default soft limit for open files (`ulimit -n`) for containers is lowered to 1024. This is a change in containerd itself (see [containerd PR #8924](https://github.com/containerd/containerd/pull/8924)) where `LimitNOFILE` was removed from `containerd.service` as a best practice, making the default system soft limit apply. Workloads expecting a higher default soft limit (for example, those implicitly relying on the previous higher default) might experience failures, such as `Too many open files` errors. **Solution:** Upgrade from an earlier 1.33 patch version to 1.33.2-gke.1043000 or later.  **Workaround:** Increase the open files limit for your workloads using one of the following methods:

  * **Application-Level adjustment:** Modify the application code or configuration to explicitly set the ` ulimit -n` or `prlimit --nofile=524288`.
  * **Containerd NRI Ulimit Adjuster Plugin** Use the [`containerd/nri ulimit-adjuster` plugin](https://github.com/containerd/nri/tree/main/plugins/ulimit-adjuster) to adjust the ulimit.
  * **Downgrade node pool (Standard only):** For Standard GKE clusters, you can temporarily [downgrade your node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_nodes) to version 1.32 to avoid this issue until a permanent resolution is available.

For more information about the migration to containerd 2, see [Migrate nodes to containerd 2](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2).   
Upgrades | 1.31.5-gke.1169000, 1.32.1-gke.1376000 | 1.31.7-gke.1164000, 1.32.3-gke.1512000 | 

### Invalid CRD status.storedVersions for managed CRDs

Some GKE-managed CRDs might have an invalid `status.storedVersions` field, which creates a risk for breaking access to CRD objects after an upgrade. This issue impacts clusters that are both of the following:

  * Clusters that used an affected GKE version at some point in time.
  * Clusters that had unsupported (`served=false`) versions of CRD objects stored in etcd.

**Workaround:** The recommended workaround is to delay cluster upgrades until the issue is resolved. Alternatively, if you know your cluster contains unsupported versions of CRD objects, you can add these versions to the `status.storedVersions` field by using the `kubectl patch` command.  
Operation, logging and monitoring | 1.32.2-gke.1652000, 1.31.6-gke.1221000, 1.30.10-gke.1227000 | 

  * 1.32.2-gke.1652003 or later
  * 1.31.6-gke.1221001 or later
  * 1.30.10-gke.1227001 or later

| 

### Missing metrics or workload autoscaler not scaling

You might observe gaps in metrics data on the affected versions after the cluster size increases by more than five nodes. This issue might also impact autoscaling operations. This issue impacts only clusters upgraded to the impacted versions. Newly created clusters should work as expected. **Workaround:** If you are impacted, you can downgrade one patch version or upgrade to the newer fixed versions.  
Operation |  |  | 

### Google Cloud Hyperdisk size and attachment limits

Typically, a pod that cannot be successfully scheduled due to a node's volume attachment limits triggers the auto-provisioning of a new node. When running workloads that use a Hyperdisk product are scheduled to a node that runs a C3 VM, node auto-provisioning does not occur and the pod is scheduled onto the already full node. The workload is scheduled onto the node despite the lack of an available disk attachment. The workload also fails to start, due to an error like the following:
    
    
     AttachVolume.Attach failed for volume "[VOLUME NAME]" : rpc error: code = InvalidArgument desc = Failed to Attach: failed when waiting for zonal op: rpc error: code = InvalidArgument desc = operation operation-[OPERATION NUMBERS] failed (UNSUPPORTED_OPERATION): Maximum hyperdisk-balanced disks count should be less than or equal to [16], Requested : [17]

The problem is present for all Hyperdisk products on C3 machines. Hyperdisk attachment limits vary by VM vCPU number and Hyperdisk product. For more information, see [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance). **Workaround:** Google Cloud Hyperdisk products trigger auto-provisioning on other VM shapes. We recommend a shape that supports only Google Cloud Hyperdisk.  
Operation | 1.32.3-gke.1927000, 1.32.3-gke.1785000, 1.32.3-gke.1717000, 1.32.3-gke.1440000, 1.32.3-gke.1170000, 1.32.3-gke.1250000, 1.32.3-gke.1671000, 1.32.3-gke.1596000, 1.32.3-gke.1298000 |  | 

### gke-metadata-server is OOMKilled on TPU/GPU nodes

On GKE TPU nodes (for example `ct4p-hightpu-4t`) and GPU nodes (for example `a3-highgpu-8g`), the kernel might terminate the `gke-metadata-server` with an `OOMKilled` when the server's memory usage exceeds 100 MB. **Workaround:** If you observe `OOMKilled` events for `gke-metadata-server` on TPU or GPU nodes, contact the GKE Identity on-call team (Component ID: 395450) for mitigation options.   
Operation | 

  * 1.32.0-gke.1358000 to 1.32.4-gke.1106006, 1.32.4-gke.1236007, 1.32.4-gke.1353001, 1.32.4-gke.1415001, 1.32.4-gke.1533000
  * 1.33.0-gke.0 to 1.33.0-gke.1552000

| 

  * 1.32.4-gke.1353003 and later
  * 1.33.0-gke.1552000 and later

| 

### Volume resizes might be stuck due to dangling NodePendingResize status on PVCs.

Clusters on version 1.32 that have nodes on versions 1.31 or earlier will fail to update PersistentVolumeClaim status during resizing. This incorrect status prevents subsequent resize operations from beginning, effectively preventing further resizes. A PVC in this state has a `status.allocatedResourceStatuses` field that contains `NodePendingResize` or both `status.allocatedResources` field and `status.conditions.type: FileSystemResizePending`. If a PVC was created while your cluster was on an affected version, you might see this issue persist after your cluster upgrades to a known fixed version. In this scenario, your PVC needs to be patched to remove the `status.allocatedResources` field with a one-time workaround.  **Workaround:** PVCs stuck due to dangling status can be patched to remove that status. You can use a patch command like the following to remove the dangling status:
    
    
    kubectl patch pvc $PVC_NAME --subresource='status' --type='merge' -p '{"status":{"allocatedResourceStatuses":null}}'
    
    
    kubectl patch pvc $PVC_NAME --subresource='status' --type='merge' -p '{"status":{"allocatedResources":null}}'  
  
Operation | 

  * 1.32.4-gke.1236007, 1.32.4-gke.1353001

| 

  * 1.32.4-gke.1353003 and later

| 

### The PDCSI driver might log excessively

GKE clusters on specific versions of 1.32 might emit excessive log messages from the PDCSI driver. This excess logging would consume Cloud Logging Write API quota. **Workaround:** You can reduce this excessive logging by adding an [exclusion filter](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exclude-logs#add-filter). To exclude the log messages from being ingested into Cloud Logging, use the following query: 
    
    
          resource.type="k8s_container"
          resource.labels.container_name="gce-pd-driver"
          (sourceLocation.file="cache.go" OR "Cannot process volume group")
          
  
Operations | 

  * 1.27.16-gke.2440000 and later
  * 1.28.15-gke.1673000 and later
  * 1.29.13-gke.1038000 and later
  * 1.30.9 and later
  * 1.31.7 and later
  * 1.32.1-gke.1357001 and later

| 

  * 1.27.16-gke.2691000 and later
  * 1.28.15-gke.2152000 and later
  * 1.29.15-gke.1218000 and later
  * 1.30.11-gke.1190000 and later
  * 1.31.7-gke.1363000 and later
  * 1.32.4-gke.1106000 and later
  * 1.33.0-gke.1552000 and later

| 

### Pods that attempt to mount NFS persistent volumes on COS nodes which previously had a Read-Only (RO) mount will only be mounted in RO mode

For GKE version 1.27 and later, NFS volumes using the Kubernetes in-tree CSI driver are only able to mount persistent volumes in RO mode after a previous RO mount on the same node.  **Workaround:** [Downgrade node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#downgrading_nodes) to a version that's earlier than the impacted versions  
Operations | 

  * 1.32 versions from 1.32.1-gke.1357001 up to, but not including, 1.32.4-gke.1106000
  * All 1.33 versions earlier than 1.33.0-gke.1552000


  * 1.32 release: 1.32.4-gke.1106000 and later
  * 1.33 release: 1.33.0-gke.1552000 and later

| 

### Pods attempting to mount NFS persistent volumes on Ubuntu nodes will be unable to run.

For GKE version 1.32 and later NFS volumes using the Kubernetes in-tree CSI driver won't be able to mount persistent volumes on Ubuntu nodes. When this happens, you might see the following error messages:
    
    
    "MountVolume.SetUp failed for volume 'nfs-storage' : mount failed: exit status 1"
    
    
    Output: Mount failed: mount failed: exit status 127
    
    
    "Output: chroot: failed to run command 'mount': No such file or directory failed to run command mount on Ubuntu nodes"

In addition to seeing these error messages, Pods using these volumes won't be able to come up. **Workaround:** [Downgrade node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#downgrading_nodes) to version 1.31.  
Operation | >= 1.28.15-gke.1436000, < 1.28.15-gke.1668000, >= 1.29.12-gke.1040000, < 1.29.13-gke.1028000, >= 1.30.8-gke.1053000, < 1.30.8-gke.1287000, >= 1.31.4-gke.1057000, < 1.31.6-gke.1020000, >= 1.32.0-gke.1281000, < 1.32.1-gke.1369000 | 

  * 1.28.15-gke.1668000 or later
  * 1.29.13-gke.1028000 or later
  * 1.30.8-gke.1287000 or later
  * 1.31.6-gke.1020000 or later
  * 1.32.1-gke.1369000 or later

| 

### Pods using io_uring-related syscalls might be stuck in Terminating

Pods that use io_uring-related syscalls might enter the D (disk sleep) state, which is also called TASK_UNINTERRUPTIBLE, due to a bug in the Linux kernel. Processes in D state cannot be woken by signals, including `SIGKILL`.  
When a Pod is affected by this known issue, its containers might fail to terminate normally. In the containerd logs, you might observe repeated messages similar to the following: `Kill container [container-id]` indicating that the system is repeatedly attempting to stop a container.  
Concurrently, the kubelet logs display error messages, such as the following:  ` "Kill container failed" err="rpc error: code = DeadlineExceeded desc = context deadline exceeded" ` or  ` "Error syncing pod, skipping" err="[failed to \"KillContainer\" for \"container-name\" with KillContainerError: \"rpc error: code = DeadlineExceeded desc = an error occurs during waiting for container \\\"container-id\\\" to be killed: wait container \\\"container-id\\\": context deadline exceeded\", failed to \"KillPodSandbox\" for \"pod-uuid\" with KillPodSandboxError: \"rpc error: code = DeadlineExceeded desc = context deadline exceeded\"]" pod="pod-name" podUID="pod-uuid" ` These symptoms point to processes within the container that are stuck in an uninterruptible sleep (D-state), which prevents proper termination of the Pod.  Workloads that use io_uring directly, or that use io_uring indirectly through a language runtime like NodeJS, might be affected by this known issue. Affected workloads have a process in the D (disk sleep) state in the `/proc/<pid>/state` file, and show the `io_uring` string as part of the contents of `/proc/<pid>/stack`. NodeJS workloads might be able to disable the use of io_uring through `UV_USE_IO_URING=0`.  **Workaround:** Upgrade the cluster nodes to a fixed version or later.  
Operation | 1.28, 1.29, 1.30, 1.31 | 

  * 1.30.8-gke.1261000 and later
  * 1.31.4-gke.1183000 and later
  * 1.32.0-gke.1448000 and later

| 

### Workloads using Image streaming fail with authentication errors

A bug in the Image streaming feature might cause workloads to fail when a set of specific conditions is met while the container reads files. Error messages related to authentication failures might be visible in the gcfsd log.  To check if you are impacted, search the logs with this search query: ` resource.type="k8s_node" resource.labels.project_id="[project_id]" resource.labels.cluster_name="[cluster_name]" logName="projects/[project_id]/logs/gcfsd" "backend.FileContent failed" "Request is missing required authentication credential." ` The presence of these errors indicate that the nodes are impacted.  If you are impacted by this issue, you can [ upgrade your node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading-nodes) to a patched GKE version.   
Operation | 

  * 1.30.0 to 1.30.5-gke.1443001
  * 1.31.0 to 1.31.1-gke.1678000

| 

  * 1.30.5-gke.1628000 and later
  * 1.31.1-gke.1846000 and later

| 

### Increased Pod eviction rates on GKE versions 1.30 and 1.31

Some versions of GKE 1.30 and GKE 1.31 that use COS 113 and COS 117, respectively, have kernels that were built with the option `CONFIG_LRU_GEN_ENABLED=y`. This option enables the kernel feature [Multi-Gen LRU](https://docs.kernel.org/admin-guide/mm/multigen_lru.html), which causes the kubelet to miscalculate memory usage and might lead to the kubelet evicting Pods.  The config option `CONFIG_LRU_GEN_ENABLED` is disabled in [cos-113-18244-151-96](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m113#cos-113-18244-151-96_) and [cos-117-18613-0-76](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m117#cos-117-18613-0-76_).  You might not always see an unusual Pod eviction rate because this issue depends on the workload's memory usage pattern. There is a higher risk of the kubelet evicting Pods for workloads that haven't set a memory limit in the resources field. This is because the workloads might request more memory than what the kubelet reports as available.  If you see higher memory usage of an application after upgrading to the mentioned GKE versions without any other changes, then you might be affected by the kernel option.  To check if there are unusual Pod eviction rates, analyze the following metrics with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer): `kubernetes.io/container_memory_used_bytes` and `kubernetes.io/container_memory_request_bytes` You can use the following PromQL queries. Replace the values for `cluster_name`, `namespace_name`, `metadata_system_top_level_controller_type` and `metadata_system_top_level_controller_name` with the workload name and type that you want to analyze:  ` max by (pod_name)(max_over_time(kubernetes_io:container_memory_used_bytes{monitored_resource="k8s_container",memory_type="non-evictable",cluster_name="REPLACE_cluster_name",namespace_name="REPLACE_namespace",metadata_system_top_level_controller_type="REPLACE_controller_type",metadata_system_top_level_controller_name="REPLACE_controller_name"}[${__interval}])) `   
  
` sum by (pod_name)(avg_over_time(kubernetes_io:container_memory_request_bytes{monitored_resource="k8s_container",cluster_name="REPLACE_cluster_name",namespace_name="REPLACE_namespace",metadata_system_top_level_controller_type="REPLACE_controller_type",metadata_system_top_level_controller_name="REPLACE_controller_name"}[${__interval}])) ` If you see unusual spikes in the memory usage that go above the requested memory, the workload might be getting evicted more often. 

#### Workaround

If you can't upgrade to the fixed versions and if you're running in a GKE environment where you can deploy privileged Pods, you can disable the Multi-Gen LRU option by using a DaemonSet. 

  1. Update the GKE node pools from where you want to run the DaemonSet with an annotation to disable the Multi-Gen LRU option. For example, `disable-mglru: "true"`. 
  2. Update the `nodeSelector` parameter in the DaemonSet manifest with the same annotation you used in the preceding step. For example, see the [`disable-mglru.yaml` file in the GoogleCloudPlatform/k8s-node-tools](https://github.com/GoogleCloudPlatform/k8s-node-tools/blob/master/disable-mglru/disable-mglru.yaml) repository. 
  3. Deploy the DaemonSet to your cluster. 

After the DaemonSet is running in all the selected node pools, the change is effective immediately and the kubelet memory usage calculation is back to normal.   
Operation | 1.28, 1.29, 1.30, 1.31 | 

  * 1.28.14-gke.1175000 and later
  * 1.29.9-gke.1341000 and later
  * 1.30.5-gke.1355000 and later
  * 1.31.1-gke.1621000 and later

| 

### Pods stuck in Terminating status

A bug in the container runtime (containerd) might cause Pods and containers to be stuck in Terminating status with errors similar to the following:  `OCI runtime exec failed: exec failed: cannot exec in a stopped container: unknown` If you are impacted by this issue, you can [ upgrade your nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading-nodes) to a GKE version with a fixed version of containerd.   
Operation | 

  * 1.34 and earlier
  * 1.35 versions earlier than 1.35.6-gke.1005000
  * 1.36 versions earlier than 1.36.0-gke.2459000

| 

  * 1.35.6-gke.1005000 and later
  * 1.36.0-gke.2459000 and later

| 

### Image streaming fails because of symbolic links

A bug in the Image streaming feature might cause containers to fail to start.  Containers running on a node with image streaming enabled on specific GKE versions might fail to be created with the following error:  `"CreateContainer in sandbox from runtime service failed" err="rpc error: code = Unknown desc = failed to create containerd container: failed to mount [PATH]: too many levels of symbolic links"` **Workaround:** To resolve this issue, upgrade your node pools to a fixed version (1.35.6-gke.1005000 or later, or 1.36.0-gke.2459000 or later).  If you cannot upgrade, you can [ check for empty layers or duplicate layers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming#check-for-empty-or-duplicate-layers). If you can't remove empty empty layers or duplicate layers, then [disable Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming#disable).   
Operation | 1.27,1.28,1.29 | 

  * 1.28.9-gke.1103000 and later
  * 1.29.4-gke.1202000 and later
  * 1.30: All versions

| 

### Image streaming fails because of missing files

A bug in the Image streaming feature might cause containers to fail because of a missing file or files.  Containers running on a node with Image streaming enabled on the following versions might fail to start or run with errors informing that certain files don't exist. The following are examples of such errors: 

  * `No such file or directory`
  * `Executable file not found in $PATH`

If you are impacted by this issue, you can [disable Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming#disable).   
Networking,Upgrades and updates | 1.28 |  | 

### Gateway TLS configuration error

We've identified an issue with configuring TLS for Gateways in clusters running GKE version 1.28.4-gke.1083000. This affects TLS configurations using either an [SSLCertificate](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-ssl-certificate) or a [CertificateMap](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager). If you're upgrading a cluster with existing Gateways, updates made to the Gateway will fail. For new Gateways, the load balancers won't be provisioned. This issue will be fixed in an upcoming GKE 1.28 patch version.   
Upgrades and updates | 1.27 | 1.27.8 or later | 

### GPU device plugin issue

Clusters that are running GPUs and are upgraded from 1.26 to a 1.27 patch version earlier than 1.27.8 might experience issues with their nodes' GPU device plugins (`nvidia-gpu-device-plugin`). Do the following steps depending on the state of your cluster: 

  * If your cluster is running version 1.26 and has GPUs, don't manually upgrade your cluster until version 1.27.8 is available in your cluster's release channel. 
  * If your cluster is running an earlier 1.27 patch version and the nodes are affected, restart the nodes or manually delete the `nvidia-gpu-device-plugin` Pod on the nodes (the add-on manager will create a new working plugin). 
  * If your cluster is using auto-upgrades, this doesn't affect you as automatic upgrades will only move clusters to patch versions with the fix. 

  
Operation | 1.27,1.28 | 

  * 1.27.5-gke.1300 and later
  * 1.28.1-gke.1400 and later

| 

### Autoscaling for all workloads stops

HorizontalPodAutoscaler (HPA) and VerticalPodAutoscaler (VPA) might stop autoscaling all workloads in a cluster if it contains misconfigured `autoscaling/v2` HPA objects. The issue impacts clusters running earlier patch versions of GKE version 1.27 and 1.28 (for example, 1.27.3-gke.100).  **Workaround:** Correct misconfigured `autoscaling/v2` HPA objects by making sure the fields in `spec.metrics.resource.target` match, for example: 

  * When `spec.metrics.resource.target.type` is `Utilization` then target should be `averageUtilization`
  * When `spec.metrics.resource.target.type` is `AverageValue` then target should be `averageValue`

For more details on how to configure `autoscaling/v2` HPA objects, see the [HorizontalPodAutoscaler Kubernetes documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics).   
Operation | 1.28,1.29 | 

  * 1.28.7-gke.1026000
  * 1.29.2-gke.1060000

| 

### Container Threat Detection fails to deploy

Container Threat Detection might fail to deploy on Autopilot clusters running the following GKE versions: 

  * 1.28.6-gke.1095000 to 1.28.7-gke.1025000 
  * 1.29.1-gke.1016000 to 1.29.1-gke.1781000

  
Networking, Upgrades | 1.27, 1.28, 1.29, 1.30 | 

  * 1.30.4-gke.1282000 or later
  * 1.29.8-gke.1157000 or later
  * 1.28.13-gke.1078000 or later
  * 1.27.16-gke.1342000 or later

| 

### Connectivity issues for `hostPort` Pods after control plane upgrade

Clusters with [network policy enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) might experience connectivity issues with [hostPort](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#container-v1-core) Pods. Additionally, newly created Pods might take an additional 30 to 60 seconds to be ready.  The issue is triggered when the GKE control plane of a cluster is upgraded to one of the following GKE versions 

  * 1.30 to 1.30.4-gke.1281999
  * 1.29.1-gke.1545000 to 1.29.8-gke.1156999
  * 1.28.7-gke.1042000 to 1.28.13-gke.1077999
  * 1.27.12-gke.1107000 to 1.27.16-gke.1341999

**Workaround:** Upgrade or recreate nodes immediately after the GKE control plane upgrade.  
Networking | 1.31, 1.32 | 

  * 1.32.1-gke.1729000 or later
  * 1.31.6-gke.1020000 or later

| 

### Broken UDP traffic between Pods that run on the same node

Clusters with [intra-node visibility enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) might experience broken UDP traffic between Pods that run on the same node.  The issue is triggered when the GKE cluster node is upgraded to or created with one of the following GKE versions: 

  * 1.32.1-gke.1729000 or later
  * 1.31.6-gke.1020000 or later

The impacted path is Pod-to-Pod UDP traffic on the same node through Hostport or Service. **Resolution** Upgrade the cluster to one of the following fixed versions:

  * 1.32.3-gke.1927000 or later
  * 1.31.7-gke.1390000 or later

  
Operation | 1.29,1.30,1.31 | 

  * 1.29.10-gke.1071000 or later
  * 1.30.5-gke.1723000 or later
  * 1.31.2-gke.1115000 or later

| 

### Incompatible Ray Operator and Cloud KMS database encryption

Some Ray Operator versions are incompatible with Cloud KMS database encryption.  **Workarounds:** Upgrade the cluster control plane to a fixed version or later.  
Upgrades and updates | 1.30, 1.31 | 

  * 1.30.8-gke.1051000 or later
  * 1.31.1-gke.2008000 and later

| 

### GPU Maintenance Handler Pod Stuck in CrashLoopBackOff State

With this issue, gpu-maintenance-handler Pods are stuck in a `CrashLoopBackOff` state on their respective nodes. This state prevents the `upcoming maintenance` label from being applied to GKE nodes, which can impact both node-drain and pod-eviction processes for workloads.  ` "Node upcoming maintenance label not applied due to error: Node "gke-yyy-yyy" is invalid: metadata.labels: Invalid value: "-62135596800": a valid label must be an empty string or consist of alphanumeric characters, '-','' or '.', and must start and end with an alphanumeric character (e.g.'MyValue', or 'my_value', or '12345', regex used for validation is '(([A-Za-z0-9][-A-Za-z0-9.]*)?[A-Za-z0-9])?')" ` If you are impacted by this issue, you can resolve it by upgrading your control plane to a GKE version that includes the fix.   
Operation | 1.33.1-gke.1522000 and later | 1.33.4-gke.1142000 and later | 

### Pods fail to start on nodes with Image streaming enabled

On nodes with Image streaming enabled, workloads might fail to start with the following error signature: `Failed to create pod sandbox ... context deadline exceeded` An affected node's serial-port logs also contain the following error signature: `task gcfsd ... blocked for more than X seconds` The presence of these two error signatures indicates a deadlock in one of the Image streaming components. This deadlock inhibits Pods from successfully starting.  **Mitigation:** Restart the node for a quick mitigation. Note that the restarted node might still encounter the deadlock again. For a more robust mitigation, disable Image streaming on the node pool by running the following: 
    
    
    gcloud container node-pools update NODE_POOL_NAME --cluster CLUSTER_NAME --no-enable-image-streaming

Note: disabling Image streaming re-creates all of the nodes within a node pool.   
Operation | 

  * 1.32.4-gke.1198000 and later
  * 1.33 versions before 1.33.5-gke.1862000
  * 1.34 versions before 1.34.1-gke.2541000

| 

  * 1.33.5-gke.1862000 and later
  * 1.34.1-gke.2541000 and later

| 

### Custom ComputeClasses with `ImageType` not using existing GKE node pools.

When using a custom ComputeClass that defines an `ImageType` field, Cluster Autoscaler repeatedly creates and scales up new node pools instead of scaling up existing node pools. ComputeClass status is not healthy.  **Workaround:** Upgrade the cluster to one of the following fixed versions:

  * 1.33.5-gke.1862000 or later
  * 1.34.1-gke.2541000 or later

Alternatively, you can mitigate this issue by not defining certain fields in the custom ComputeClass. 

  * If you don't use an Autopilot custom ComputeClass, don't define the `ImageType` field. In this case, the value that's used is the default cluster-level setting, which by default is `cos_containerd`.
  * If you use an Autopilot custom ComputeClass, don't define the `nodePoolConfig` field, which is one level `ImageType`.

  
  
## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
