---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/storage/
title: Troubleshooting storage in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:11.950690+00:00
---

# Troubleshooting storage in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshooting storage in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Issues with storage in Google Kubernetes Engine (GKE) clusters can manifest in various ways, from performance bottlenecks and volume mounting failures to errors when using specific disk types with certain machine types. These problems can affect application statefulness, data persistence, and overall workload health.

Use this document to resolve common issues affecting storage functionality in your clusters. Find guidance on troubleshooting problems related to volume provisioning and attachment, data access and performance, and storage capacity management.

This information is important for both Platform admins and operators managing cluster infrastructure and storage and Application developers whose workloads rely on persistent storage. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Error 400: Cannot attach RePD to an optimized VM

Regional persistent disks are [restricted](https://docs.cloud.google.com/compute/docs/disks#restrictions_2) from being used with memory-optimized machines or compute-optimized machines.

Consider using a non-regional persistent disk storage class if using a regional persistent disk is not a hard requirement. If using a regional persistent disk is a hard requirement, consider scheduling strategies such as [taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to ensure that the Pods that need regional persistent disks are scheduled on a node pool that are not optimized machines.

## Troubleshooting issues with disk performance

The performance of the boot disk is important because the boot disk for GKE nodes is not only used for the operating system but also for the following:

  * Docker images.
  * The container filesystem for what is not mounted as a volume (that is, the overlay filesystem), and this often includes directories like `/tmp`.
  * Disk-backed `emptyDir` volumes, unless the node uses local SSD.



Disk performance is shared for all disks of the same [disk type](https://docs.cloud.google.com/compute/docs/disks#disk-types) on a node. For example, if you have a 100 GB `pd-standard` boot disk and a 100 GB `pd-standard` PersistentVolume with lots of activity, the performance of the boot disk is that of a 200 GB disk. Also, if there is a lot of activity on the PersistentVolume, this impacts the performance of the boot disk as well.

If you encounter messages similar to the following on your nodes, these could be symptoms of low disk performance:
    
    
    INFO: task dockerd:2314 blocked for more than 300 seconds.
    
    
    
    fs: disk usage and inodes count on following dirs took 13.572074343s
    
    
    
    PLEG is not healthy: pleg was last seen active 6m46.842473987s ago; threshold is 3m0s
    

To help resolve such issues, review the following:

  * Ensure you have consulted the [Storage disk type comparisons](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison) and chosen a persistent disk type to suit your needs.
  * This issue often occurs for nodes that use standard persistent disks with a size of less than 200 GB. Consider increasing the size of your disks or switching to SSDs, especially for clusters used in production.
  * Consider [enabling local SSD for ephemeral storage on your node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd). This is particularly effective if you have containers that frequently use `emptyDir` volumes.



## Mounting a volume stops responding due to the `fsGroup` setting

One issue that can cause `PersistentVolume` mounting to fail is a Pod that is configured with the `fsGroup` setting. Normally, mounts automatically retry and the mount failure resolves itself. However, if the `PersistentVolume` has a large number of files, kubelet will attempt to change ownership on each file on the filesystem, which can increase volume mount latency.
    
    
    Unable to attach or mount volumes for pod; skipping pod ... timed out waiting for the condition
    

To confirm if a failed mount error is due to the `fsGroup` setting, you can [check the logs for the Pod](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/using-logs). If the issue is related to the `fsGroup` setting, you see the following log entry:
    
    
    Setting volume ownership for /var/lib/kubelet/pods/POD_UUID and fsGroup set. If the volume has a lot of files then setting volume ownership could be slow, see https://github.com/kubernetes/kubernetes/issues/69699
    

If the `PersistentVolume` does not mount within a few minutes, try the following steps to resolve this issue:

  * Reduce the number of files in the [Volume](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volumes).
  * Stop using the [`[fsGroup]` setting](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod).
  * Change the application [`fsGroupChangePolicy` to `OnRootMismatch`](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#configure-volume-permission-and-ownership-change-policy-for-pods).



## Slow disk operations cause Pod creation failures

For more information, refer to [containerd issue #4604](https://github.com/containerd/containerd/issues/4604#issuecomment-1006013231).

_Affected GKE node versions:_ 1.18, 1.19, 1.20.0 to 1.20.15-gke.2100, 1.21.0 to 1.21.9-gke.2000, 1.21.10 to 1.21.10-gke.100, 1.22.0 to 1.22.6-gke.2000, 1.22.7 to 1.22.7-gke.100, 1.23.0 to 1.23.3-gke.700, 1.23.4 to 1.23.4-gke.100

The following example errors might be displayed in the `k8s_node container-runtime` logs:
    
    
    Error: failed to reserve container name "container-name-abcd-ef12345678-91011_default_12131415-1234-5678-1234-12345789012_0": name "container-name-abcd-ef12345678-91011_default_12131415-1234-5678-1234-12345789012_0" is reserved for "1234567812345678123456781234567812345678123456781234567812345678"
    

### Mitigation

  1. If Pods are failing, consider using `restartPolicy:Always` or `restartPolicy:OnFailure` in your [PodSpec](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy).
  2. Increase the [boot disk IOPS](https://docs.cloud.google.com/compute/docs/disks/performance#performance_by_disk_size) (for example, upgrade the disk type or increase the disk size).



### Fix

This issue is fixed in containerd 1.6.0+. GKE versions with this fix are 1.20.15-gke.2100+, 1.21.9-gke.2000+, 1.21.10-gke.100+, 1.22.6-gke.2000+, 1.22.7-gke.100+, 1.23.3-gke.1700+ and 1.23.4-gke.100+

## Volume expansion changes not reflecting in the container file system

When performing volume expansion, always make sure to update the PersistentVolumeClaim. Changing a PersistentVolume directly can result in volume expansion not happening. This could lead to one of the following scenarios:

  * If a PersistentVolume object is modified directly, both the PersistentVolume and PersistentVolumeClaim values are updated to a new value, but the file system size is not reflected in the container and is still using the old volume size.

  * If a PersistentVolume object is modified directly, followed by updates to the PersistentVolumeClaim where the `status.capacity` field is updated to a new size, this can result in changes to the PersistentVolume but not the PersistentVolumeClaim or the container file system.




To resolve this issue, complete the following steps:

  1. Keep the modified PersistentVolume object as it was.
  2. Edit the PersistentVolumeClaim object and set `spec.resources.requests.storage` to a value that is higher than was used in the PersistentVolume.
  3. Verify if the PersistentVolume is resized to the new value.



After these changes, PersistentVolume, PersistentVolumeClaim and container file system should be automatically resized by the kubelet.

Verify if the changes are reflected in the Pod.
    
    
    kubectl exec POD_NAME  -- /bin/bash -c "df -h"
    

Replace POD_NAME with the Pod attached to PersistentVolumeClaim.

## The selected machine type should have local SSD(s)

You might encounter the following error when creating a cluster or a node pool that uses Local SSD:
    
    
    The selected machine type (c3-standard-22-lssd) has a fixed number of local SSD(s): 4. The EphemeralStorageLocalSsdConfig's count field should be left unset or set to 4, but was set to 1.
    

In the error message, you might see `LocalNvmeSsdBlockConfig` instead of `EphemeralStorageLocalSsdConfig` depending on which you specified.

This error occurs when the number of Local SSD disks specified does not match the number of Local SSD disks included with the machine type.

To resolve this issue, specify a number of Local SSD disks that [matches the machine type that you want](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds). For third generation machine series, you must omit the Local SSD `count` flag and the correct value will be configured automatically.

## Hyperdisk Storage Pools: Cluster or node pool creation fails

You might encounter the `ZONE_RESOURCE_POOL_EXHAUSTED` error or similar [Compute Engine resource errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability#common_error_messages) when trying to provision Hyperdisk Balanced disks as your node's boot or attached disks in a [Hyperdisk Storage Pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-storage-pools).

This happens when you're trying to create a GKE cluster or node pool in a zone that's running low on resources, for example:

  * The zone might not have enough of the Hyperdisk Balanced disks available.
  * The zone might not have enough capacity to create the nodes of the machine type you specified, like `c3-standard-4`.



To resolve this issue:

  1. Select a new zone within the same region with enough capacity for your chosen machine type and where [Hyperdisk Balanced Storage Pools are available](https://docs.cloud.google.com/compute/docs/disks/storage-pools#hdbsp-regions).
  2. Delete the existing storage pool and recreate it in the new zone. This is because storage pools are zonal resources.
  3. Create your cluster or node pool in the new zone.



## Detected high node storage pressure

If you observe node events or conditions related to `StoragePressureRootFileSystem` with the reason `StoragePressureDetected`, it indicates that the node's root file system or a critical storage mount point is experiencing high disk usage, nearing its capacity.

When describing a node by using the `kubectl describe node NODE_NAME` command, you might see an event similar to this:
    
    
    Events:
      Type     Reason                      Age   From                     Message
      ----     ------                      ----  ----                     -------
      ...
      Warning  StoragePressureDetected     46m   device-capacity-monitor  Node condition StoragePressureRootFileSystem is now: True, reason: StoragePressureDetected, message: "Disk /dev/nvme0n1 usage 89% exceeds threshold 85%"
    

Cause:

The `StoragePressureDetected` reason signifies that the disk usage on the node's root file system (often `mnt/stateful_partition` or related mounts) has exceeded a predefined threshold (for example, 85%). This can be caused by the following:

  * Workloads writing excessive data to emptyDir volumes that are not backed by Local SSDs.
  * Large container images being pulled to the node.
  * Log files accumulating on the node.
  * Other processes consuming disk space.



Continued high disk usage can lead to node instability, Pod evictions, and application failures.

Debugging and resolution:

**Identify disk usage** : use SSH to connect to the affected node and use commands like `df -h` to check the disk usage on various mount points, paying close attention to `/mnt/stateful_partition` and any ephemeral storage mounts.

**Analyze workload storage patterns** : review the storage requests and usage patterns of the Pods running on the node. Identify if any specific workloads are consuming a disproportionate amount of ephemeral storage.

**Increase node storage capacity** : be aware that the primary resolution is often to ensure your nodes have adequate storage capacity for your workloads. Consider the following:

  * **Use larger boot disks** : when creating node pools, select a larger boot disk size if your workloads require more ephemeral storage on the root file system.
  * **Utilize larger local SSDs for ephemeral storage** : for workloads that require high-performance, low-latency ephemeral storage, configure your node pools to use Local SSDs. This provides a separate, larger capacity for emptyDir volumes.
  * **Adjust workload requests or limits** : ensure your Pod specifications include appropriate ephemeral storage requests and limits to help the scheduler place Pods on nodes with sufficient space and to prevent runaway disk usage.
  * **Clean up unused resources** : remove any unnecessary files, old container images, or logs from the node if they are contributing to the high disk usage.



By addressing the storage capacity and usage on the node, you can mitigate issues related to `StoragePressureDetected` and help node operation.

## Troubleshoot Cloud Storage FUSE out-of-memory (OOM) events

If your Pods experience high memory utilization or Out of Memory (OOM) events related to the Cloud Storage FUSE CSI driver, you can collect and analyze CPU and memory snapshots using Cloud Profiler. Set up these options in [Configure the Cloud Storage FUSE CSI driver sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#enable-profiler).

When a Pod experiences an OOM kill, you can correlate the event to the correct Cloud Profiler snapshot using the following workflow:

  1. **Check Cloud Logging:** Navigate to [Cloud Logging](https://console.cloud.google.com/logs) to find the Kubernetes OOM Event.
  2. **Filter by Pod name:** Run the following query to locate the event logs for your specific Pod, replacing `POD_NAME` with the workload Pod's name:
         
         jsonPayload.involvedObject.name="POD_NAME"
         jsonPayload.involvedObject.kind="Pod"
         OOMKilled
         

**Note:** If the sidecar mounter or GCSFuse process OOMs, the Pod name is the workload Pod's name. If the node driver OOMs, it will be `gcsfusecsi-node-*`.
  3. **Extract the Pod UID:** Expand the relevant OOM event log and note the timestamp and the exact Pod UID located at `jsonPayload.involvedObject.uid`.

  4. **Analyze in Cloud Profiler:** Navigate to [Cloud Profiler](https://console.cloud.google.com/profiler), filter the **Service Version** using the `POD_NAME_POD_UID` format, and adjust the time range to match the OOM timestamp. This helps ensure you are looking at the exact memory profile of the specific container instance right before it was killed.




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
