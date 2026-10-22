---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-notready/
title: Troubleshoot nodes with the NotReady status in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:56.855089+00:00
---

# Troubleshoot nodes with the NotReady status in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-notready/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot nodes with the NotReady status in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

A `NotReady` status in Google Kubernetes Engine (GKE) means that the node's kubelet isn't reporting to the control plane correctly. Because Kubernetes won't schedule new Pods on a `NotReady` node, this issue can reduce application capacity and cause downtime.

Use this document to distinguish between expected `NotReady` statuses and actual problems, diagnose the root cause, and find resolutions for common issues like resource exhaustion, network problems, and container runtime failures.

This information is for Platform admins and operators responsible for cluster stability and Application developers seeking to understand infrastructure-related application behavior. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

  * To get the permissions that you need to perform the tasks in this document, ask your administrator to grant you the following IAM roles on your Google Cloud project: 

    * To access GKE clusters: [Kubernetes Engine Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterViewer) (`roles/container.viewer`). 
    * To view logs: [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`). 
    * To view metrics: [Monitoring Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`). 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * Configure the `kubectl` command-line tool to communicate with your GKE cluster:
        
        gcloud container clusters get-credentials CLUSTER_NAME \
            --location LOCATION \
            --project PROJECT_ID
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a`) for the cluster.
    * `PROJECT_ID`: your Google Cloud project ID.



## Check the node's status and conditions

To confirm that a node has a `NotReady` status and help you diagnose the root cause, use the following steps to inspect a node's conditions, events, logs, and resource metrics:

  1. View the status of your nodes. To get additional details like IP addresses and kernel versions, which are helpful for diagnosis, use the `-o wide` flag:
         
         kubectl get nodes -o wide
         

The output is similar to the following:
         
         NAME                                STATUS     ROLES    AGE   VERSION               INTERNAL-IP  EXTERNAL-IP  OS-IMAGE                             KERNEL-VERSION   CONTAINER-RUNTIME
         gke-cluster-pool-1-node-abc1        Ready      <none>   94d   v1.32.3-gke.1785003   10.128.0.1   1.2.3.4      Container-Optimized OS from Google   6.6.72+          containerd://1.7.24
         gke-cluster-pool-1-node-def2        Ready      <none>   94d   v1.32.3-gke.1785003   10.128.0.2   5.6.7.8      Container-Optimized OS from Google   6.6.72+          containerd://1.7.24
         gke-cluster-pool-1-node-ghi3        NotReady   <none>   94d   v1.32.3-gke.1785003   10.128.0.3   9.10.11.12   Container-Optimized OS from Google   6.6.72+          containerd://1.7.24
         

In the output, look for nodes with a value of `NotReady` in the `STATUS` column and note their names.

  2. View more information about specific nodes with the `NotReady` status, including their conditions and any recent Kubernetes events:
         
         kubectl describe node NODE_NAME
         

Replace `NODE_NAME` with the name of a node with the `NotReady` status.

In the output, focus on the `Conditions` section to understand the node's health and the `Events` section for a history of recent issues. For example:
         
         Name:                   gke-cluster-pool-1-node-ghi3
         ...
         Conditions:
         Type                          Status    LastHeartbeatTime                 LastTransitionTime                Reason                   Message
         ----                          ------    -----------------                 ------------------                ------                   -------
         NetworkUnavailable            False     Wed, 01 Oct 2025 10:29:19 +0100   Wed, 01 Oct 2025 10:29:19 +0100   RouteCreated             RouteController created a route
         MemoryPressure                Unknown   Wed, 01 Oct 2025 10:31:06 +0100   Wed, 01 Oct 2025 10:31:51 +0100   NodeStatusUnknown        Kubelet stopped posting node status.
         DiskPressure                  Unknown   Wed, 01 Oct 2025 10:31:06 +0100   Wed, 01 Oct 2025 10:31:51 +0100   NodeStatusUnknown        Kubelet stopped posting node status.
         PIDPressure                   False     Wed, 01 Oct 2025 10:31:06 +0100   Wed, 01 Oct 2025 10:29:00 +0100   KubeletHasSufficientPID  kubelet has sufficient PID available
         Ready                         Unknown   Wed, 01 Oct 2025 10:31:06 +0100   Wed, 01 Oct 2025 10:31:51 +0100   NodeStatusUnknown        Kubelet stopped posting node status.
         Events:
         Type     Reason                   Age                  From                                   Message
         ----     ------                   ----                 ----                                   -------
         Normal   Starting                 32m                  kubelet, gke-cluster-pool-1-node-ghi3  Starting kubelet.
         Warning  PLEGIsNotHealthy         5m1s (x15 over 29m)  kubelet, gke-cluster-pool-1-node-ghi3  PLEG is not healthy: pleg was last seen active 5m1.123456789s ago; threshold is 3m0s
         Normal   NodeHasSufficientMemory  5m1s (x16 over 31m)  kubelet, gke-cluster-pool-1-node-ghi3  Node gke-cluster-pool-1-node-ghi3 status is now: NodeHasSufficientMemory
         

In the `Conditions` section, a status of `True` for any negative condition, or `Unknown` for the `Ready` condition, indicates a problem. Pay close attention to the `Reason` and `Message` fields for these conditions, as they explain the cause of the problem.

Here's what each condition type means:

     * **`KernelDeadlock`** : `True` if the node's operating system kernel has detected a deadlock, which is a serious error that can freeze the node.
     * **`FrequentUnregisterNetDevice`** : `True` if the node is frequently unregistering its network devices, which can be a sign of driver or hardware issues.
     * **`NetworkUnavailable`** : `True` if networking for the node isn't correctly configured.
     * **`OutOfDisk`** : `True` if the available disk space is completely exhausted. This condition is more severe than `DiskPressure`.
     * **`MemoryPressure`** : `True` if the node memory is low.
     * **`DiskPressure`** : `True` if the disk space on the node is low.
     * **`PIDPressure`** : `True` if the node is experiencing process ID (PID) exhaustion.
     * **`Ready`** : indicates if the node is healthy and ready to accept Pods. 
       * `True` if the node is healthy.
       * `False` if the node is unhealthy and not accepting Pods.
       * `Unknown` if the node controller has not heard from the node for a grace period (the default is 50 seconds) and the node status is unknown.

Next, examine the `Events` section, which provides a chronological log of actions and observations about the node. This timeline is crucial for understanding what happened immediately before the node became `NotReady`. Look for specific messages that can help find the cause, such as eviction warnings (signaling resource pressure), failed health checks, or node lifecycle events like cordoning for a repair.

  3. To learn more about why nodes have the `NotReady` status, view logs from the node and its components.

     1. Check `kubelet` logs for the `NotReady` status.

The `kubelet` is the primary agent that reports the node's status to the control plane, so its logs are the most likely place to find the literal `NotReady` message. These logs are the authoritative source for diagnosing issues with Pod lifecycle events, resource pressure conditions (like `MemoryPressure` or `DiskPressure`), and the node's connectivity to the Kubernetes control plane.

     2. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs)

     3. In the query pane, enter the following query:
            
            resource.type="k8s_node"
            resource.labels.node_name="NODE_NAME"
            resource.labels.cluster_name="CLUSTER_NAME"
            resource.labels.location="LOCATION"
            log_id("kubelet")
            textPayload=~"(?i)NotReady"
            

Replace the following:

        * `NODE_NAME`: the name of the node that you're investigating.
        * `CLUSTER_NAME`: the name of your cluster.
        * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a`) for the cluster.
     4. Click **Run query** and review the results.

     5. If the `kubelet` logs don't reveal the root cause, check the `container-runtime` and `node-problem-detector` logs. These components might not log the `NotReady` status directly, but they often log the underlying issue (like a runtime failure or kernel panic) that caused the issue.

     6. In the Logs Explorer query pane, enter the following query:
            
            resource.type="k8s_node"
            resource.labels.node_name="NODE_NAME"
            resource.labels.cluster_name="CLUSTER_NAME"
            resource.labels.location="LOCATION"
            log_id("COMPONENT_NAME")
            

Replace `COMPONENT_NAME` with one of the following values:

        * `container-runtime`: the runtime (containerd), responsible for the complete container lifecycle, including pulling images and managing container execution. Reviewing `container-runtime` logs is essential for troubleshooting failures related to container instantiation, runtime service errors, or issues caused by the runtime's configuration.
        * `node-problem-detector`: a utility that proactively monitors and reports a variety of node-level issues to the control plane. Its logs are critical for identifying underlying systemic problems that can cause node instability—such as kernel deadlocks, file system corruption, or hardware failures—which might not be captured by other Kubernetes components.
     7. Click **Run query** and review the results.

  4. Use Metrics Explorer to look for resource exhaustion around the time the node became `NotReady`:

     1. In the Google Cloud console, go to the **Metrics Explorer** page:

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

     2. In Metrics Explorer, check the node's underlying Compute Engine instance for resource exhaustion. Focus on metrics related to CPU, memory, and disk I/O metrics. For example:

        * **GKE node metrics** : start with metrics prefixed with `kubernetes.io/node/`, such as `kubernetes.io/node/cpu/allocatable_utilization` or `kubernetes.io/node/memory/allocatable_utilization`. These metrics show how much of the node's available resources are being used by your Pods. The available amount doesn't include the resources Kubernetes reserves for system overhead.
        * **Guest OS metrics** : for a view from inside the node's operating system, use metrics prefixed with `compute.googleapis.com/guest/`, such as `compute.googleapis.com/guest/cpu/usage` or `compute.googleapis.com/guest/memory/bytes_used`.
        * **Hypervisor metrics** : to see the VM's performance from the hypervisor level, use metrics prefixed with `compute.googleapis.com/instance/`, such as `compute.googleapis.com/instance/cpu/utilization` or disk I/O metrics like `compute.googleapis.com/instance/disk/read_bytes_count`.

The guest OS and hypervisor metrics require you to filter by the underlying Compute Engine instance name, not the Kubernetes node name. You can find the instance name for a node by running the `kubectl describe node NODE_NAME` command and looking for the `ProviderID` field in the output. The instance name is the last part of that value. For example:
    
    ...
    Spec:
    ProviderID: gce://my-gcp-project-123/us-central1-a/gke-my-cluster-default-pool-1234abcd-5678
    ...
    

In this example, the instance name is `gke-my-cluster-default-pool-1234abcd-5678`.




## Identify the cause by symptom

If you have identified a specific symptom, such as a log message, node condition, or cluster event, use the following table to find troubleshooting advice:

Category | **Symptom or log message** | **Potential cause** | **Troubleshooting steps**  
---|---|---|---  
**Node conditions** | `NetworkUnavailable: True` | Node-to-control-plane connectivity issue or Container Network Interface (CNI) plugin failure. | Troubleshoot network connectivity  
`MemoryPressure: True` | Node has insufficient memory. | Troubleshoot node resource shortages  
`DiskPressure: True` | Node has insufficient disk space. | Troubleshoot node resource shortages  
`PIDPressure: True` | Node has insufficient Process IDs available. | Troubleshoot node resource shortages  
**Events and log messages** | `PLEG is not healthy` | Kubelet is overloaded due to high CPU/IO or too many Pods. | Resolve PLEG issues  
`Out of memory: Kill process`  
`sys oom event` | Node memory is completely exhausted. | Resolve system-level OOM events  
`leases.coordination.k8s.io...is forbidden` | `kube-node-lease` namespace is stuck terminating. | Resolve issues with the `kube-node-lease` namespace  
`Container runtime not ready`  
`runtime is down`  
Errors referencing `/run/containerd/containerd.sock` or `docker.sock` | Containerd or Docker service has failed or is misconfigured. | Resolve container runtime issues  
Pods stuck in `Terminating`  
Kubelet logs show `DeadlineExceeded` for kill container  
containerd logs show repeated `Kill container` messages | Processes stuck in uninterruptible disk sleep (D-state), often related to I/O. | Resolve processes stuck in D-state  
**Cluster-level symptoms** | Multiple nodes fail after a DaemonSet rollout. | DaemonSet is interfering with node operations. | Resolve issues caused by third-party DaemonSets  
`compute.instances.preempted` in audit logs. | Spot VM was preempted, which is expected behavior. | Confirm node preemption  
`kube-system` Pods stuck in `Pending`. | Admission webhook is blocking critical components. | Resolve issues caused by admission webhooks  
`exceeded quota: gcp-critical-pods` | Misconfigured quota is blocking system Pods. | Resolve issues caused by resource quotas  
  
## Check for expected `NotReady` events

A `NotReady` status doesn't always signal a problem. It can be expected behavior during planned operations like a node pool upgrade, or if you use certain types of virtual machines.

### Confirm node lifecycle operations

**Symptoms** :

A node temporarily shows a `NotReady` status during certain lifecycle events.

**Cause** :

A node's status temporarily becomes `NotReady` during several common lifecycle events. This behavior is expected whenever a node is being created or re-created, such as in the following scenarios:

  * **Node pool upgrades** : during an upgrade, each node is drained and replaced. The new, upgraded node has a status of `NotReady` until it finishes initializing and joins the cluster.
  * **Node auto-repair** : when GKE replaces a malfunctioning node, the replacement node remains `NotReady` while it is being provisioned.
  * **Cluster autoscaler scale-up** : when new nodes are added, they start in a `NotReady` status and become `Ready` only after they are fully provisioned and have joined the cluster.
  * **Manual instance template changes** : GKE re-creates the nodes when you apply template changes. The new node has a `NotReady` status during its startup phase.



**Resolution** :

Nodes should have the `NotReady` status only briefly. If the status persists for more than 10 minutes, investigate other causes.

### Confirm node preemption

If your node is running on a [Spot VM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/spot-vms) or a [Preemptible VM](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms), Compute Engine might abruptly terminate it to reclaim resources. This is expected behavior for these types of short-lived virtual machines and isn't an error.

**Symptoms** :

If you observe the following symptoms, the node's `NotReady` status is likely caused by an expected Spot VM preemption:

  * A node unexpectedly enters a `NotReady` status before being deleted and re-created by the cluster autoscaler.
  * Cloud Audit Logs show a `compute.instances.preempted` event for the underlying VM instance.



**Cause** :

The node was running on a Spot VM or Preemptible VM instance and Compute Engine reclaimed those compute resources for another task. Spot VMs can be interrupted at any time, though they typically provide a 30-second termination notice.

**Resolution** :

Use Spot VMs or Preemptible VMs only for fault-tolerant, stateless, or batch workloads that are designed to handle frequent terminations gracefully. For production or stateful workloads that can't tolerate sudden interruptions, provision your node pools using standard, on-demand VMs.

## Troubleshoot node resource shortages

A node often becomes `NotReady` because it lacks essential resources like CPU, memory, or disk space. When a node doesn't have enough of these resources, critical components can't function correctly, leading to application instability and node unresponsiveness. The following sections cover the different ways these shortages can appear, from general pressure conditions to more severe system-wide events.

### Resolve node resource pressure

Resource exhaustion occurs when a node lacks sufficient CPU, memory, disk space, or process IDs (PIDs) to run its workloads. This issue can lead to the `NotReady` status.

**Symptoms** :

If you observe the following node conditions and logs, resource exhaustion is the probable cause of the node's `NotReady` status:

  * In the output of the `kubectl describe node` command, you see a status of `True` for conditions such as `OutOfDisk`, `MemoryPressure`, `DiskPressure`, or `PIDPressure`.
  * The kubelet logs might contain Out of Memory (OOM) events, indicating that the system's OOM Killer was invoked.



**Cause** :

Workloads on the node are collectively demanding more resources than the node can provide.

**Resolution** :

For Standard clusters, try the following solutions:

  * **Reduce workload demand** : 
    * Reduce the number of Pods running on the affected node by scaling down the replica count of your deployments. For more information, see [Scaling an application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps#scaling_an_application).
    * Review and optimize your applications to consume fewer resources.
  * **Increase node capacity** : 
    * Increase the node's allocated CPU and memory. For more information, see [Vertically scale by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes).
    * If the issue is disk-related, [increase the size of the node's boot disk](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-boot-disks). Consider using an SSD boot disk for better performance.



For Autopilot clusters, you don't directly control node machine types or boot disk sizes. Node capacity is automatically managed based on your Pod requests. Ensure that your workload resource requests are within Autopilot limits and accurately reflect your application's needs. Persistent resource issues might indicate a need to optimize Pod requests or, in rare cases, a platform issue requiring assistance from Cloud Customer Care.

### Resolve system-level OOM events

A system-level Out of Memory (OOM) event occurs when a node's total memory is exhausted, forcing the Linux kernel to terminate processes to free up resources. This event is different from a container-level OOM event, where a single Pod exceeds its memory limits.

**Symptoms** :

If you notice the following symptoms, a system-level OOM event is the likely reason for the node's instability:

  * You notice the message `Out of memory: Kill process` in the node's serial console logs.
  * The kubelet logs contain `oom_watcher` events, which indicate that the kubelet has detected a system-level OOM event.
  * Unexpected termination of various processes, including potentially critical system daemons or workload Pods, not necessarily the highest memory consumers.



**Cause** :

The node's overall memory is exhausted. This issue can be due to a bug in a system service, a misconfigured workload that's consuming an excessive amount of memory, or a node that's too small for the collective memory demands of all its running Pods.

**Resolution** :

To resolve system-level OOM events, diagnose the cause and then either reduce memory demand or increase node capacity. For more information, see [Troubleshoot OOM events](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/oom-events).

### Resolve PLEG issues

The Pod lifecycle event generator (PLEG) is a component within the kubelet. It periodically checks the state of all containers on the node and reports any changes back to the kubelet.

When the PLEG experiences performance issues, it can't provide timely updates to the kubelet, which can cause the node to become unstable.

**Symptoms** :

If you observe the following symptoms, the PLEG might not be functioning correctly:

  * The kubelet logs for the node contain a message similar to `PLEG is not healthy`.
  * The node's status frequently changes between `Ready` and `NotReady`.



**Cause** :

PLEG issues are typically caused by performance problems that prevent the kubelet from receiving timely updates from the container runtime. Common causes include the following:

  * **High CPU load** : the node's CPU is saturated, which prevents the kubelet and container runtime from having the processing power that they need.
  * **I/O throttling** : the node's boot disk is experiencing heavy I/O operations, which can slow down all disk-related tasks.
  * **Excessive Pods** : too many Pods on a single node can overwhelm the kubelet and container runtime, leading to resource contention.



**Resolution** :

For Standard clusters, reduce the strain on the node's resources:

  * **Reduce node load** : decrease the overall workload on the node by [scaling down deployments](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps#scaling_an_application). You can also distribute Pods more evenly across other nodes in the cluster by using [taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/), [node affinities](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity), or [Pod topology spread constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/) to influence scheduling.
  * **Set CPU limits** : to prevent any single workload from consuming all available CPU resources, enforce CPU limits on your Pods. For more information, see [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) in the Kubernetes documentation.
  * **Increase node capacity** : consider using larger nodes with more CPU and memory to handle the workload. For more information, see [Vertically scale by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes).
  * **Improve disk performance** : if the issue is related to I/O throttling, use a larger boot disk or upgrade to an SSD boot disk. This change can significantly improve disk performance. For more information, see [Troubleshooting issues with disk performance](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/storage#disk_performance_issues).



For Autopilot clusters, although you can't directly change an existing node's size or disk type, you can influence the hardware that your workloads run on by using [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). This feature lets you specify requirements in your workload manifest, such as a minimum amount of CPU and memory or a specific machine series, to guide where your Pods are scheduled.

If you don't use ComputeClasses, adjust workload deployments (like replica counts and resource requests or limits) and ensure that they are within Autopilot constraints. If PLEG issues persist after optimizing your workloads, contact Cloud Customer Care.

### Resolve processes stuck in D-state

Processes stuck in an uninterruptible disk sleep (D-state) can make a node unresponsive. This issue prevents Pods from terminating and can cause critical components like containerd to fail, leading to a `NotReady` status.

**Symptoms** :

  * Pods, especially those using network storage like NFS, are stuck in the `Terminating` status for a long time.
  * Kubelet logs show `DeadlineExceeded` errors when trying to stop a container.
  * The node's serial console logs might show kernel messages about `hung tasks` or tasks being blocked for more than 120 seconds.



**Cause** :

Processes enter a D-state when they are waiting for an I/O operation to complete and can't be interrupted. Common causes include the following:

  * Slow or unresponsive remote file systems, such as a misconfigured or overloaded NFS share.
  * Severe disk performance degradation or hardware I/O errors on the node's local disks.



**Resolution** :

To resolve issues with D-state processes, identify the I/O source and then clear the state by selecting one of the following options:

###  Standard clusters 

  1. **Find the stuck process and determine what it's waiting for** :

     1. Connect to the affected node by using SSH:
            
            gcloud compute ssh NODE_NAME \
                --zone ZONE \
                --project PROJECT_ID
            

Replace the following:

        * `NODE_NAME`: the name of the node to connect to.
        * `ZONE`: the Compute Engine zone of the node.
        * `PROJECT_ID`: your project ID.
     2. Find any processes in a D-state:
            
            ps -eo state,pid,comm,wchan | grep '^D'
            

The output is similar to the following:
            
            D  12345  my-app      nfs_wait
            D  54321  data-writer io_schedule
            

The output won't have a header. The columns, in order, represent:

        * State
        * Process ID (PID)
        * Command
        * Wait channel (wchan)
     3. Examine the `wchan` column to identify the I/O source:

        * If the `wchan` column includes terms like `nfs` or `rpc`, the process is waiting on an NFS share.
        * If the `wchan` column includes terms like `io_schedule`, `jbd2`, or `ext4`, the process is waiting on the node's local boot disk.
     4. For more detail about which kernel functions the process is waiting on, check the process's kernel call stack:
            
            cat /proc/PID/stack
            

Replace `PID` with the process ID that you found in the previous step.

  2. **Reboot the node.** Rebooting is often the most effective way to clear a process stuck in a D-state.

     1. [Drain the node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/).
     2. [Delete the underlying VM instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance). GKE typically creates a new VM to replace it.
  3. **After clearing the immediate issue, investigate the underlying storage system to prevent recurrence.**

     * **For network storage (NFS) issues** : use your storage provider's monitoring tools to check for high latency, server-side errors, or network issues between the GKE node and the NFS server.

     * **For local disk issues** : check for I/O throttling in Cloud Monitoring by viewing the `compute.googleapis.com/instance/disk/throttled_read_ops_count` and `compute.googleapis.com/instance/disk/throttled_write_ops_count` metrics for the Compute Engine instance.




###  Autopilot clusters 

  1. **Attempt to identify the source of the blockage** :

Direct SSH access to nodes and running commands like `ps` or `cat /proc` aren't available in Autopilot clusters. You must rely on logs and metrics.

     1. **Check node logs** : in Cloud Logging, analyze logs from the affected node. Filter by the node name and the timeframe of the issue. Look for kernel messages indicating I/O errors, storage timeouts (for example, to disk or NFS), or messages from CSI drivers.
     2. **Check workload logs** : examine the logs of the Pods running on the affected node. Application logs might reveal errors related to file operations, database calls, or network storage access.
     3. **Use Cloud Monitoring** : although you can't get process-level details, check for node-level I/O issues.
  2. **Trigger a node replacement to clear the state.**

You can't manually delete the underlying VM. To trigger a replacement, [drain the node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/). This action cordons the node and evicts the Pods.

GKE automatically detects unhealthy nodes and initiates repairs, typically by replacing the underlying VM.

If the node remains stuck after draining and isn't automatically replaced, contact Cloud Customer Care.

  3. **After clearing the immediate issue, investigate the underlying storage system to prevent recurrence.**

     * **For local disk issues** : check for I/O throttling in Cloud Monitoring by viewing the `compute.googleapis.com/instance/disk/throttled_read_ops_count` and `compute.googleapis.com/instance/disk/throttled_write_ops_count` metrics. You can filter these metrics for the node pool's underlying instance group, though individual instances are managed by Google.
     * **For network storage (NFS) issues** : use your storage provider's monitoring tools to check for high latency, server-side errors, or network issues between the GKE node and the NFS server. Check logs from any CSI driver Pods in Cloud Logging.



## Troubleshoot core component failures

After you rule out expected causes and resource shortages, the node's software or a core Kubernetes mechanism might be the cause of the issue. A `NotReady` status can occur when a critical component, like the container runtime, fails. It can also happen when a core Kubernetes health-check mechanism, such as the node lease system, breaks down.

### Resolve container runtime issues

Issues with the container runtime, such as containerd, can prevent the kubelet from launching Pods on a node.

**Symptoms** :

If you observe the following messages in the kubelet logs, a container runtime issue is the probable cause of the node's `NotReady` status:

  * `Container runtime not ready`
  * `Container runtime docker failed!`
  * `docker daemon exited`
  * Errors connecting to the runtime socket (for example, `unix:///var/run/docker.sock` or `unix:///run/containerd/containerd.sock`).



**Cause** :

The container runtime isn't functioning correctly, is misconfigured, or is stuck in a restart loop.

**Resolution** :

To resolve container runtime issues, do the following:

  1. **Analyze container runtime logs** :

     1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

     2. To view all of the container runtime's warning and error logs on the affected node, in the query pane, enter the following:
            
            resource.type="k8s_node"
            resource.labels.node_name="NODE_NAME"
            resource.labels.cluster_name="CLUSTER_NAME"
            resource.labels.location="LOCATION"
            log_id("container-runtime")
            severity>=WARNING
            

Replace the following:

        * `NODE_NAME`: the name of the node that you're investigating.
        * `CLUSTER_NAME`: the name of your cluster.
        * `LOCATION`: the Compute Engine region or zone (for example, `us-central1` or `us-central1-a`) for the cluster.
     3. Click **Run query** and review the output for specific error messages that indicate why the runtime failed. A message such as `failed to load TOML` in the `containerd` logs in Cloud Logging often indicates a malformed file.

     4. To check if the runtime is stuck in a restart loop, run a query that searches for startup messages. A high number of these messages in a short period confirms frequent restarts.
            
            resource.type="k8s_node"
            resource.labels.node_name="NODE_NAME"
            resource.labels.cluster_name="CLUSTER_NAME"
            resource.labels.location="LOCATION"
            log_id("container-runtime")
            ("starting containerd" OR "Containerd cri plugin version" OR "serving..."
            OR "loading plugin" OR "containerd successfully booted")
            

Frequent restarts often point to an underlying issue, like a corrupted configuration file or resource pressure, that's causing the service to crash repeatedly.

  2. **Review the`containerd` configuration for modifications**: incorrect settings can cause the container runtime to fail. You can make configuration changes through a [node system configuration file](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration) or through direct modifications that are made by workloads with elevated privileges.

     1. Determine if the node pool uses a node system configuration file:
            
            gcloud container node-pools describe NODE_POOL_NAME \
                --cluster CLUSTER_NAME \
                --location LOCATION \
                --format="yaml(config.containerdConfig)"
            

Replace the following:

        * `NODE_POOL_NAME`: the name of your node pool.
        * `CLUSTER_NAME`: the name of your cluster.
        * `LOCATION`: the Compute Engine region or zone of your cluster.

If the output shows a `containerdConfig` section, then GKE is managing these custom settings. To modify or revert the settings, follow the instructions in [Customize containerd configuration in GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).

     2. If GKE-managed customizations aren't active, or if you suspect other changes, look for workloads that might be modifying the node's file system directly. Look for DaemonSets with elevated permissions (`securityContext.privileged: true`) or `hostPath` volumes mounting sensitive directories like `/etc`.

To inspect their configuration, list all DaemonSets in YAML format:
            
            kubectl get daemonsets --all-namespaces -o yaml
            

Review the output and inspect the logs of any suspicious DaemonSets.

     3. For Standard clusters, inspect the configuration file directly. SSH access and manual file inspection aren't possible in Autopilot clusters, because Google manages the runtime configuration. Report persistent runtime issues to Google Cloud Customer Care.

**Important:** The following steps are for inspection only. Avoid editing the `/etc/containerd/config.toml` file directly on the node, because your changes can be overwritten by GKE. To apply persistent changes, use a [node configuration file](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).

If you use a Standard cluster, inspect the file:

        1. Connect to the node by using SSH:
               
               gcloud compute ssh NODE_NAME \
                   --zone ZONE \
                   --project PROJECT_ID
               

Replace the following:

           * `NODE_NAME`: the name of the node to connect to.
           * `ZONE`: the Compute Engine zone of the node.
           * `PROJECT_ID`: your project ID.
        2. Display the contents of the containerd configuration file:
               
               sudo cat /etc/containerd/config.toml
               

        3. To check for recent modifications, list file details:
               
               ls -l /etc/containerd/config.toml
               

     4. Compare the contents of this file to the containerdConfig output from the `gcloud node-pools describe` command that you ran in the previous step. Any setting in `/etc/containerd/config.toml` that isn't in the `gcloud` output is an unmanaged change.

     5. To correct any misconfiguration, remove any changes that were not applied through a node system configuration.

  3. **Troubleshoot common runtime issues** : for more troubleshooting steps, see [Troubleshooting the container runtime](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/container-runtime).




### Resolve issues with the `kube-node-lease` namespace

Resources in the `kube-node-lease` namespace are responsible for maintaining node health. This namespace shouldn't be deleted. Attempts to delete this namespace result in the namespace being stuck in the `Terminating` status. When the `kube-node-lease` namespace gets stuck in a `Terminating` status, kubelets can't renew their health-check leases. This issue causes the control plane to consider the nodes to be unhealthy, leading to a cluster-wide issue where nodes alternate between the `Ready` and `NotReady` statuses.

**Symptoms** :

If you observe the following symptoms, then a problem with the `kube-node-lease` namespace is the likely cause of the cluster-wide instability:

  * The kubelet logs on every node show persistent errors similar to the following:
        
        leases.coordination.k8s.io NODE_NAME is forbidden: unable to create new content in namespace kube-node-lease because it is being terminated
        

  * Nodes across the cluster repeatedly alternate between `Ready` and `NotReady` statuses.




**Cause** :

The `kube-node-lease` namespace, which manages [node heartbeats](https://kubernetes.io/docs/concepts/architecture/leases/#node-heart-beats), is abnormally stuck in the `Terminating` status. This error prevents the Kubernetes API server from allowing object creation or modification within the namespace. As a result, kubelets can't renew their `Lease` objects, which are essential for signalling their liveness to the control plane. Without these status updates, the control plane can't confirm that the nodes are healthy, leading to the nodes' statuses alternating between `Ready` and `NotReady`.

The underlying reasons why the `kube-node-lease` namespace itself might become stuck in the `Terminating` status include the following:

  * **Resources with finalizers** : although less common for the system `kube-node-lease` namespace (which primarily contains `Lease` objects), a resource within it could have a finalizer. Kubernetes finalizers are keys that signal a controller must perform cleanup tasks before a resource can be deleted. If the controller responsible for removing the finalizer isn't functioning correctly, the resource isn't deleted, and the namespace deletion process is halted.
  * **Unhealthy or unresponsive aggregated API services** : the namespace termination can be blocked if an APIService object, which is used to register an aggregated API server, is linked to the namespace and becomes unhealthy. The control plane might wait for the aggregated API server to be properly shut down or cleaned up, which won't occur if the service is unresponsive.
  * **Control plane or controller issues** : in rare cases, bugs or issues within the Kubernetes control plane, specifically the namespace controller, could prevent the successful garbage collection and deletion of the namespace.



**Resolution** :

Follow the guidance in [Troubleshoot namespaces stuck in the Terminating state](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/terminating-namespaces).

## Troubleshoot network connectivity

Network problems can prevent a node from communicating with the control plane or prevent critical components like the CNI plugin from functioning, leading to a `NotReady` status.

**Symptoms** :

If you observe the following symptoms, then network issues might be the cause of your nodes' `NotReady` status:

  * The `NetworkNotReady` condition is `True`.
  * Kubelet logs on the node show errors similar to the following: 
    * `connection timeout to the control plane IP address`
    * `network plugin not ready`
    * `CNI plugin not initialized`
    * `connection refused` or `timeout` messages when trying to reach the control plane IP address.
  * Pods, especially in the `kube-system` namespace, are stuck in `ContainerCreating` with events like `NetworkPluginNotReady`.



**Cause** :

Network-related symptoms typically indicate a failure in one of the following areas:

  * **Connectivity problems** : the node can't establish a stable network connection to the Kubernetes control plane.
  * **CNI plugin failure** : the CNI plugin, which is responsible for configuring Pod networking, isn't running correctly or has failed to initialize.
  * **Webhook issues** : misconfigured admission webhooks can interfere with CNI plugin-related resources, preventing the network from being configured correctly.



**Resolution** :

To resolve network issues, do the following:

  1. **Address transient`NetworkNotReady` status**: on newly created nodes, it's normal to see a brief `NetworkNotReady` event. This status should resolve within a minute or two while the CNI plugin and other components initialize. If the status persists, proceed with the following steps.

  2. **Verify node-to-control plane connectivity and firewall rules** : ensure that the network path between your node and the control plane is open and functioning correctly:

     1. **Check firewall rules** : ensure that your VPC firewall rules allow the necessary traffic between your GKE nodes and the control plane. For information about the rules GKE requires for node-to-control plane communication, see [Automatically created firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules).
     2. **Test connectivity** : use the [Connectivity Test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) in the Network Intelligence Center to verify the network path between the node's internal IP address and the control plane's endpoint IP address on port `443`. A result of `Not Reachable` often helps you identify the firewall rule or routing issue that's blocking communication.
  3. **Investigate CNI plugin status and logs** : if the node's network isn't ready, the CNI plugin might be at fault.

     1. **Check CNI Pod status** : identify the CNI plugin in use (for example, `netd` or `calico-node`) and check the status of its Pods in the `kube-system` namespace. You can filter for the specific node with the following command:
            
            kubectl get pods \
                -n kube-system \
                -o wide \
                --field-selector spec.nodeName=NODE_NAME \
                | grep -E "netd|calico|anetd"
            

     2. **Examine CNI Pod logs** : if the Pods aren't functioning correctly, examine their logs in Cloud Logging for detailed error messages. Use a query similar to the following for `netd` Pods on a specific node:
            
            resource.type="k8s_container"
            resource.labels.cluster_name="CLUSTER_NAME"
            resource.labels.location="LOCATION"
            resource.labels.namespace_name="kube-system"
            labels."k8s-pod/app"="netd"
            resource.labels.node_name="NODE_NAME"
            severity>=WARNING
            

     3. **Address specific CNI errors** :

        * If the logs show `Failed to allocate IP address`, your Pod IP address ranges might be exhausted. Verify your Pod IP address utilization and review your cluster's CIDR ranges.
        * If the logs show `NetworkPluginNotReady` or `cni plugin not initialized`, confirm that the node has sufficient CPU and memory resources. You can also try restarting the CNI Pod by deleting it, which lets the DaemonSet re-create it.
        * If you use GKE Dataplane V2 and logs show `Cilium API client timeout exceeded`, restart the `anetd` Pod on the node.
     4. **Check for admission webhook interference** : malfunctioning webhooks can prevent CNI Pods from starting, leaving the node in a `NetworkNotReady` status.

     5. **Check API server logs** : review the API server logs in Cloud Logging for errors related to webhook calls. To identify if a webhook is blocking CNI resource creation, search for messages like `failed calling webhook`.

If a webhook is causing problems, you might need to identify the problematic `ValidatingWebhookConfiguration` or `MutatingWebhookConfiguration` and temporarily disable it to let the node become ready. For more information, see Resolve issues caused by admission webhooks.




## Troubleshoot cluster misconfigurations

The following sections help you audit some cluster-wide configurations that might be interfering with normal node operations.

### Resolve issues caused by admission webhooks

An admission webhook that is misconfigured, unavailable, or too slow can block critical API requests, preventing essential components from starting or nodes from joining the cluster.

**Symptoms** :

If you observe the following symptoms, a misconfigured or unavailable admission webhook is likely blocking essential cluster operations:

  * Pods, especially in the `kube-system` namespace (like CNI or storage Pods), are stuck in a `Pending` or `Terminating` status.
  * New nodes fail to join the cluster, often timing out with a `NotReady` status.



**Cause** :

Misconfigured or unresponsive admission webhooks might be blocking essential cluster operations.

**Resolution** :

Review your webhook configurations to ensure that they are resilient and properly scoped. To prevent outages, set the `failurePolicy` field to `Ignore` for non-critical webhooks. For critical webhooks, ensure their backing service is highly available and exclude the `kube-system` namespace from webhook oversight by using a `namespaceSelector` to avoid control plane deadlocks. For more information, see [Ensure control plane stability when using webhooks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-webhooks).

### Resolve issues caused by resource quotas

A miscalculated [resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) in the `kube-system` namespace can prevent GKE from creating critical system Pods. Because components like networking (CNI) and DNS are blocked, this issue can stop new nodes from successfully joining the cluster.

**Symptoms** :

  * Critical Pods in the `kube-system` namespace (for example, `netd`, `konnectivity-agent`, or `kube-dns`) are stuck in a `Pending` status.
  * Error messages in the cluster logs or `kubectl describe pod` output show failures like `exceeded quota: gcp-critical-pods`.



**Cause** :

This issue occurs when the Kubernetes resource quota controller stops accurately updating the used count in `ResourceQuota` objects. A common cause is a malfunctioning third-party admission webhook that blocks the controller's updates, making the quota usage appear much higher than it actually is.

**Resolution** :

  1. Because a problematic webhook is the most likely root cause, follow the guidance in the Resolve issues caused by admission webhooks section to identify and fix any webhooks that might be blocking system components. Fixing the webhook often resolves the quota issue automatically.
  2. Verify that the quota's recorded usage is out of sync with the actual number of running Pods. This step confirms if the ResourceQuota object's count is incorrect:

     1. Check the quota's reported usage:
            
            kubectl get resourcequota gcp-critical-pods -n kube-system -o yaml
            

     2. Check the actual number of Pods:
            
            kubectl get pods -n kube-system --no-headers | wc -l
            

  3. If the used count in the `ResourceQuota` seems incorrect (for example, much higher than the actual number of Pods), delete the `gcp-critical-pods` object. The GKE control plane is designed to automatically re-create this object with the correct, reconciled usage counts:
         
         kubectl delete resourcequota gcp-critical-pods -n kube-system
         

  4. Monitor the `kube-system` namespace for a few minutes to ensure the object is re-created and that the pending Pods start scheduling.




### Resolve issues caused by third-party DaemonSets

A newly deployed or updated third-party DaemonSet, which is often used for security, monitoring, or logging, can sometimes cause node instability. This issue can happen if the DaemonSet interferes with the node's container runtime or networking, consumes excessive system resources, or makes unexpected system modifications.

**Symptoms** :

If you observe the following symptoms, a recently deployed or modified third-party DaemonSet is a possible cause of node failures:

  * Multiple nodes, potentially across the cluster, enter a `NotReady` status shortly after the DaemonSet is deployed or updated.
  * Kubelet logs for affected nodes report errors such as the following: 
    * `container runtime is down`
    * `Failed to create pod sandbox`
    * Errors connecting to the container runtime socket (for example, `/run/containerd/containerd.sock`).
  * Pods, including system Pods or the DaemonSet's own Pods, are stuck in `PodInitializing` or `ContainerCreating` states.
  * Container logs for applications show unusual errors, like `exec format error`.
  * Node Problem Detector might report conditions related to runtime health or resource pressure.



**Cause** :

The third-party DaemonSet could be affecting node stability for the following reasons:

  * Consuming excessive CPU, memory, or disk I/O, which affects the performance of critical node components.
  * Interfering with the container runtime's operation.
  * Causing conflicts with the node's network configuration or Container Network Interface (CNI) plugin.
  * Altering system configurations or security policies in an unintended way.



**Resolution** :

To determine if a DaemonSet is the cause, isolate and test it:

  1. **Identify DaemonSets** : list all DaemonSets running in your cluster:
         
         kubectl get daemonsets --all-namespaces
         

Pay close attention to DaemonSets that aren't part of the default GKE installation.

You can often identify these DaemonSets by reviewing the following:

     * **Namespace** : default GKE components usually run in the `kube-system` namespace. DaemonSets in other namespaces are likely third-party or custom.
     * **Naming** : default DaemonSets often have names like `gke-metrics-agent`, `netd`, or `calico-node`. Third-party agents often have names reflecting the product.
  2. **Correlate deployment time** : check if the appearance of `NotReady` nodes coincides with the deployment or update of a specific third-party DaemonSet.

  3. **Test on a single node** :

     1. Choose one affected node.
     2. [Cordon and drain](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) the node.
     3. Temporarily prevent the DaemonSet from scheduling on this node: 
        * Apply a temporary node label and configure node affinity or anti-affinity in the DaemonSet's manifest.
        * Delete the DaemonSet's Pod on that specific node.
     4. Reboot the node's virtual machine instance.
     5. Observe if the node becomes `Ready` and remains stable while the DaemonSet isn't running on it. If the issues reappear after the DaemonSet is reintroduced, it is likely a contributing factor.
  4. **Consult the vendor** : if you suspect a third-party agent is the cause, review the vendor's documentation for known compatibility issues or best practices for running the agent on GKE. If you need further support, contact the software vendor.




## Verify that the node has recovered

After applying a potential solution, follow these steps to verify that the node has successfully recovered and is stable:

  1. Check the node's status:
         
         kubectl get nodes -o wide
         

Look for the affected node in the output. The `Status` column should now show a value of `Ready`. The status might take a few minutes to update after the fix is applied. If the status still shows `NotReady` or is cycling between statuses, then the issue isn't fully resolved.

  2. Inspect the node's `Conditions` section:
         
         kubectl describe node NODE_NAME
         

In the `Conditions` section, verify the following values:

     * The `Ready` condition has a status of `True`.
     * The negative conditions that previously had a status of `True` (for example, `MemoryPressure` or `NetworkUnavailable`) now have a status of `False`. The `Reason` and `Message` fields for these conditions should indicate that the issue is resolved.
  3. Test Pod scheduling. If the node was previously unable to run workloads, check if new Pods are being scheduled on it and if existing pods are running without issues:
         
         kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=NODE_NAME
         

Pods on the node should have a `Running` or `Completed` status. You shouldn't see Pods stuck in `Pending` or other error statuses.




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
