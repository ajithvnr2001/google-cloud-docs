---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/tpus/
title: Troubleshoot TPUs in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:21.453479+00:00
---

# Troubleshoot TPUs in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Troubleshoot TPUs in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When you run large-scale training or inference workloads on Google Kubernetes Engine (GKE), you might encounter issues provisioning or using Tensor Processing Units (TPUs). Your Pods might get stuck in a `Pending` state because GKE fails to provision new TPU slice nodes, or your workload might fail due to insufficient quota, incorrect topology configurations, or workload misconfigurations.

Use this document to learn how to check for quota issues, verify your workload's `nodeSelector` and resource requests are correct, and find logs to identify the root cause of scheduling or initialization failures.

This information is for Platform admins and operators who provision and manage node pools with specific TPU slice topologies, and for Application developers who are troubleshooting large-scale TPU training or inference workloads. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Insufficient quota to satisfy the TPU request

An error similar to `Insufficient quota to satisfy the request` indicates your Google Cloud project has insufficient quota available to satisfy the request.

To resolve this issue, check your project's quota limit and current usage. If needed, request an increase to your TPU quota.

### Check quota limit and current usage

The following sections help you ensure that you have enough quota when using TPUs in GKE. 

### Quota for on-demand or Spot VMs

If you are creating a [TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#terminology) with on-demand or Spot VMs, you must have sufficient TPU quota available in the region that you want to use.

Creating a TPU slice node pool that consumes a TPU reservation does _not_ require any TPU quota.1 You may safely skip this section for reserved TPUs.

Creating an on-demand or Spot TPU slice node pool in GKE requires Compute Engine API quota. Compute Engine API quota (compute.googleapis.com) is not the same as Cloud TPU API quota (tpu.googleapis.com), which is needed when creating TPUs with the Cloud TPU API. 

To check the limit and current usage of your Compute Engine API quota for TPUs, follow these steps:

  1. Go to the **Quotas** page in the Google Cloud console:

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the filter_list **Filter** box, do the following:

     1. Use the following table to select and copy the property of the quota based on the TPU version and machine type. For example, if you plan to create on-demand TPU v5e nodes whose machine type begins with `ct5lp-` , enter `Name: TPU v5 Lite PodSlice chips`.

TPU version, machine type begins with  | Property and name of the quota for on-demand instances | Property and name of the quota for Spot2 instances  
---|---|---  
TPU v3,  
`ct3-` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT3

| Not applicable  
TPU v3,  
`ct3p-` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT3P

| Not applicable  
TPU v4,  
`ct4p-` | 
            
            Name:  
            TPU v4 PodSlice chips

| 
            
            Name:  
            Preemptible TPU v4 PodSlice chips  
  
TPU v5e,  
`ct5lp-` | 
            
            Name:  
            TPU v5 Lite PodSlice chips

| 
            
            Name:  
            Preemptible TPU v5 Lite Podslice  
            chips  
  
TPU v5p,  
`ct5p-` | 
            
            Name:  
            TPU v5p chips

| 
            
            Name:  
            Preemptible TPU v5p chips  
  
TPU Trillium,  
`ct6e-` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT6E

| 
            
            Name:  
            Preemptible TPU slices v6e  
  
Ironwood (TPU7x),  
`tpu7x-standard-4t` | 
            
            Dimensions (e.g. location):  
            tpu_family:tpu7x

| 
            
            Name:  
            Preemptible TPU slices tpu7x  
  
     2. Select the **Dimensions (e.g. locations)** property and enter `region:` followed by the name of the region in which you plan to create TPUs in GKE. For example, enter `region:us-west4` if you plan to create TPU slice nodes in the zone `us-west4-a`. TPU quota is regional, so all zones within the same region consume the same TPU quota.




If no quotas match the filter you entered, then the project has not been granted any of the specified quota for the region that you need, and you must [request a TPU quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

When a TPU reservation is created, both the limit and current use values for the corresponding quota increase by the number of chips in the TPU reservation. For example, when a reservation is created for 16 TPU v5e chips whose machine type begins with `ct5lp-` , then both the **Limit** and **Current usage** for the `TPU v5 Lite PodSlice chips` quota in the relevant region increase by 16.

  1. When creating a TPU slice node pool, use the [`--reservation` and `--reservation-affinity=specific` flags](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--reservation) to create a reserved instance. TPU reservations are available when purchasing a commitment. ↩

  2. When creating a TPU slice node pool, use the [`--spot` flag](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--spot) to create a [Spot](https://cloud.google.com/spot-vms) instance. ↩




### Quotas for additional GKE resources

You may need to increase the following GKE-related quotas in the regions where GKE creates your resources.

  * **Persistent Disk SSD (GB) quota** : The boot disk of each Kubernetes node requires 100GB by default. Therefore, this quota should be set at least as high as the product of the maximum number of GKE nodes you anticipate creating and 100GB (nodes * 100GB).
  * **In-use IP addresses quota** : Each Kubernetes node consumes one IP address. Therefore, this quota should be set at least as high as the maximum number of GKE nodes you anticipate creating.
  * **Ensure that`max-pods-per-node` aligns with the subnet range**: Each Kubernetes node uses secondary IP ranges for Pods. For example, `max-pods-per-node` of 32 requires 64 IP addresses which translates to a /26 subnet [per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#cidr_ranges_for_clusters). Note that this range shouldn't be shared with any other cluster. To avoid exhausting the IP address range, use the `--max-pods-per-node` flag to limit the number of pods allowed to be scheduled on a node. The quota for `max-pods-per-node` should be set at least as high as the maximum number of GKE nodes you anticipate creating.



To request an increase in quota, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## How GKE handles capacity issues

If GKE can't create your TPU slice node pool due to insufficient TPU capacity, the request might fail with a resource availability error, or GKE might queue the provisioning request until capacity is available.

If TPU resources are temporarily unavailable, you might receive an error containing `GCE_STOCKOUT` or `ZONE_RESOURCE_POOL_EXHAUSTED` fields. For more information, see Insufficient TPU resources to satisfy the TPU request.

In other cases, GKE queues the request and you see an error message indicating that TPU slice nodes can't be created due to lack of capacity. GKE creates the nodes when capacity becomes available.

If you are creating a single-host TPU slice node pool, the error message looks similar to this:
    
    
    1 node cannot be created due to lack of capacity. The missing nodes will be
    created asynchronously once capacity is available. You can either wait for the
    nodes to be up, or delete the node pool and try re-creating it again later.
    

If you are creating a multi-host TPU slice node pool, the error message looks similar to this:
    
    
    The nodes (managed by ...) cannot be created now due to lack of capacity. They
    will be created asynchronously once capacity is available. You can either wait
    for the nodes to be up, or delete the node pool and try re-creating it again
    later.
    

Your TPU provisioning request can stay in the queue for a long time and remains in the `Provisioning` state while in the queue.

When capacity is available, GKE creates the nodes that were not created.

If you need capacity sooner, consider trying [Spot VMs](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--spot), though note that Spot VMs consume different quota than on-demand instances.

You can delete the queued TPU request by [deleting the TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deleting_a_node_pool).

## Insufficient TPU resources to satisfy the TPU request

An error that contains `GCE_STOCKOUT` indicates that TPU resources are temporarily unavailable to satisfy the request. GKE fulfills the provisioning request when TPU resources become available.

To resolve this issue, you can use any of the following consumption options:

  * **Flex-start:** to provision Flex-start VMs for up to seven days, with GKE automatically allocating the hardware on a best-effort basis based on availability. For more information, see [About GPU, TPU, and H4D provisioning with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws).
  * **Spot VMs:** to provision Spot VMs, you can get significant discounts, but Spot VMs can be preempted at any time, with a 30-second warning. For more information, see [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms).
  * **Future reservation for up to 90 days (in calendar mode):** to provision TPU resources for up to 90 days, for a specified time period. For more information, see [Request TPUs with future reservation in calendar mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-calendar-mode).
  * **TPU reservations:** to [request a future reservation for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation).
  * **On-demand:** to consume TPUs without arranging capacity in advance. Before requesting resources, you must have enough [on-demand quota](https://docs.cloud.google.com/tpu/docs/quota#on-demand-quotas) for the specific type and quantity of TPU VMs. On-demand is the most flexible consumption option; however, there is no guarantee that enough on-demand resources will be available to satisfy your request.



On-demand is the default consumption model for TPUs in GKE if you don't specify another option. To choose the consumption option that meets your workload requirements, see [About accelerator consumption options for AI/ML workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/consumption-option).

## Error when enabling node auto-provisioning in a TPU slice node pool

The following error occurs when you are enabling node auto-provisioning in a GKE cluster that doesn't support TPUs.

The error message is similar to the following:
    
    
    ERROR: (gcloud.container.clusters.create) ResponseError: code=400,
      message=Invalid resource: tpu-v4-podslice.
    

To resolve this issue, [upgrade your GKE cluster to version 1.27.6 or later](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster).

## GKE doesn't automatically provision TPU slice nodes

The following sections describe the cases where GKE doesn't automatically provision TPU slice nodes and how to fix them.

### Limit misconfiguration

If your cluster's auto-provisioning limits are missing or too low, GKE won't automatically provision TPU slice nodes. You might observe the following errors in such scenarios:

  * When GKE attempts to auto-provision a TPU slice node pool that doesn't have defined limits, the cluster autoscaler visibility logs display the following error message:
        
        messageId: "no.scale.up.nap.pod.tpu.no.limit.defined"
        

  * If a TPU slice node pool exists, but GKE can't scale up the nodes due to [violating resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-autopilot-clusters#noscaleup-resource-limits), you can see the following error message when running the `kubectl get events` command:
        
        11s Normal NotTriggerScaleUp pod/tpu-workload-65b69f6c95-ccxwz pod didn't
        trigger scale-up: 1 node(s) didn't match Pod's node affinity/selector, 1 max
        cluster cpu, memory limit reached
        

Also, in this scenario, you can see warning messages similar to the following in the Google Cloud console:
        
        "Your cluster has one or more unschedulable Pods"
        

  * When GKE attempts to auto-provision a TPU slice node pool that exceeds resource limits, the cluster autoscaler visibility logs will display the following error message:
        
        messageId: "no.scale.up.nap.pod.zonal.resources.exceeded"
        

Also, in this scenario, you can see warning messages similar to the following in the Google Cloud console:
        
        "Can't scale up because node auto-provisioning can't provision a node pool for
        the Pod if it would exceed resource limits"
        




To resolve these issues, increase the maximum number of TPU chips, CPU cores, and memory in the cluster.

To complete these steps:

  1. Calculate the resource requirements for a given TPU machine type and count. Note that you need to add resources for non-TPU slice node pools, like system workloads.
  2. Obtain a description of the available TPU, CPU, and memory for a specific machine type and zone. Use the gcloud CLI:
         
         gcloud compute machine-types describe MACHINE_TYPE \
             --zone COMPUTE_ZONE
         

Replace the following:

     * `MACHINE_TYPE`: The type of machine to search.
     * `COMPUTE_ZONE`: The name of the [compute zone](https://docs.cloud.google.com/compute/docs/regions-zones#available).

The output includes a description line similar to the following:
    
    description: 240 vCPUs, 407 GB RAM, 4 Google TPUs
      ```
    

  3. Calculate the total number of CPU and memory by multiplying these amounts by the required number of nodes. For example, the `ct4p-hightpu-4t` machine type uses 240 CPU cores and 407 GB RAM with 4 TPU chips. Assuming that you require 20 TPU chips, which corresponds to five nodes, you must define the following values:

     * `--max-accelerator=type=tpu-v4-podslice,count=20`.
     * `CPU = 1200` (240 times 5 )
     * `memory = 2035` (407 times 5)

You should define the limits with some margin to accommodate non-TPU slice nodes such as system workloads.

  4. Update the cluster limits:
         
         gcloud container clusters update CLUSTER_NAME \
             --max-accelerator type=TPU_ACCELERATOR \
             count=MAXIMUM_ACCELERATOR \
             --max-cpu=MAXIMUM_CPU \
             --max-memory=MAXIMUM_MEMORY
         

Replace the following:

     * `CLUSTER_NAME`: The name of the cluster.
     * `TPU_ACCELERATOR`: The name of the TPU accelerator.
     * `MAXIMUM_ACCELERATOR`: The maximum number of TPU chips in the cluster.
     * `MAXIMUM_CPU`: The maximum number of cores in the cluster.
     * `MAXIMUM_MEMORY`: The maximum number of gigabytes of memory in the cluster.



### Not all instances running
    
    
    ERROR: nodes cannot be created due to lack of capacity. The missing nodes
    will be created asynchronously once capacity is available. You can either
    wait for the nodes to be up, or delete the node pool and try re-creating it
    again later.
    

This error might appear when GKE operation is timed out or the request cannot be fulfilled and queued for provisioning single-host or multi-host TPU node pools. To mitigate capacity issues, you might use [reservations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#tpu_reservation), or consider Spot VMs.

### Workload misconfiguration

This error occurs due to misconfiguration of the workload. The following are some of the most common causes of the error:

  * The `cloud.google.com/gke-tpu-accelerator` and `cloud.google.com/gke-tpu-topology` labels are incorrect or missing in the Pod spec. GKE won't provision TPU slice node pools and the node auto-provision won't be able to scale up the cluster.
  * The Pod spec doesn't specify `google.com/tpu` in their resource requirements.



To resolve this issue do one of the following:

  1. Check that there are no unsupported labels in your workload node selector. For example, a node selector for `cloud.google.com/gke-nodepool` label will prevent GKE from creating additional node pools for your Pods.
  2. Ensure the Pod template specifications, where your TPU workload runs, include the following values: 
     * `cloud.google.com/gke-tpu-accelerator` and `cloud.google.com/gke-tpu-topology` labels in its `nodeSelector`.
     * `google.com/tpu` in its request.



To learn how to deploy TPU workloads in GKE, see [Run a workload that displays the number of available TPU chips in a TPU slice node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#tpu-chips-node-pool).

## Scheduling errors when deploying Pods that consume TPUs in GKE

The following issue occurs when GKE can't schedule Pods requesting TPUs on TPU slice nodes. For example, this might occur if some non-TPU Pods were already scheduled on TPU nodes.

The error message, emitted as a `FailedScheduling` event on the Pod, is similar to the following:
    
    
    Cannot schedule pods: Preemption is not helpful for scheduling.
    
    Error message: 0/2 nodes are available: 2 node(s) had untolerated taint
    {google.com/tpu: present}. preemption: 0/2 nodes are available: 2 Preemption is
    not helpful for scheduling
    

To resolve this issue, do the following:

Check that you have at least one CPU node pool in your cluster so the system critical Pods can run in the non-TPU nodes. To learn more, see [Deploy a Pod to a specific node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#deploy).

## Troubleshooting common issues with JobSets in GKE

For common issues with JobSet, and troubleshooting suggestions, see the [JobSet Troubleshooting page](https://jobset.sigs.k8s.io/docs/troubleshooting/). This page covers common issues such as "Webhook not available" error, child job, or Pods that are not created, and resuming issue of preempted workloads using JobSet and Kueue.

## TPU initialization failed

The following issue occurs when GKE can't provision new TPU workloads due to lack of permission to access TPU devices.

The error message is similar to the following:
    
    
    TPU platform initialization failed: FAILED_PRECONDITION: Couldn't mmap: Resource
    temporarily unavailable.; Unable to create Node RegisterInterface for node 0,
    config: device_path: "/dev/accel0" mode: KERNEL debug_data_directory: ""
    dump_anomalies_only: true crash_in_debug_dump: false allow_core_dump: true;
    could not create driver instance
    

To resolve this issue, make sure you either run your TPU container in privileged mode or you increase the [`ulimit` inside your container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#privileged-mode).

## Scheduling deadlock

Two or more Jobs scheduling might fail in deadlock. For example, in the scenario where all of the following occurs:

  * You have two Jobs (Job A and Job B) with Pod affinity rules. GKE schedules the TPU slices for both Jobs with a TPU topology of `v4-32`.
  * You have two `v4-32` TPU slices in the cluster.
  * Your cluster has ample capacity to schedule both Jobs and, in theory, each Job can be quickly scheduled on each TPU slice.
  * The Kubernetes scheduler schedules _one_ Pod from Job A on one slice, and then schedules _one_ Pod from Job B on the same slice.



In this case, given the Pod affinity rules for Job A, the scheduler attempts to schedule all remaining Pods for Job A and for Job B, on a single TPU slice each. As a result, GKE won't be able to fully schedule either Job A or Job B. Hence, the status of both Jobs will remain Pending.

To resolve this issue, use [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity) with `cloud.google.com/gke-nodepool` as the `topologyKey`, as shown in the following example:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
     name: pi
    spec:
     parallelism: 2
     template:
       metadata:
         labels:
           job: pi
       spec:
         affinity:
           podAffinity:
             requiredDuringSchedulingIgnoredDuringExecution:
             - labelSelector:
                 matchExpressions:
                 - key: job
                   operator: In
                   values:
                   - pi
               topologyKey: cloud.google.com/gke-nodepool
           podAntiAffinity:
             requiredDuringSchedulingIgnoredDuringExecution:
             - labelSelector:
                 matchExpressions:
                 - key: job
                   operator: NotIn
                   values:
                   - pi
               topologyKey: cloud.google.com/gke-nodepool
               namespaceSelector:
                 matchExpressions:
                 - key: kubernetes.io/metadata.name
                   operator: NotIn
                   values:
                   - kube-system
         containers:
         - name: pi
           image: perl:5.34.0
           command: ["sleep",  "60"]
         restartPolicy: Never
     backoffLimit: 4
    

## Permission denied during cluster creation in us-central2

If you are attempting to create a cluster in `us-central2` (the only region where TPU v4 is available), then you might encounter an error message similar to the following:
    
    
    ERROR: (gcloud.container.clusters.create) ResponseError: code=403,
    message=Permission denied on 'locations/us-central2' (or it may not exist).
    

This error occurs because the region `us-central2` is a private region.

To resolve this issue, [file a support case](https://cloud.google.com/support-hub) or reach out to your account team to ask for `us-central2` to be made visible within your Google Cloud project.

## Insufficient quota during TPU node pool creation in us-central2

If you are attempting to create a TPU slice node pool in `us-central2` (the only region where TPU v4 is available), then you might need to increase the following GKE-related quotas when you first create TPU v4 node pools:

  * **Persistent Disk SSD (GB) quota in us-central2** : The boot disk of each Kubernetes node requires 100 GB by default. Therefore, this quota should be set at least as high as the product of the maximum number of GKE nodes you anticipate creating in `us-central2` and 100 GB (`maximum_nodes` X `100 GB`).
  * **In-use IP addresses quota in us-central2** : Each Kubernetes node consumes one IP address. Therefore, this quota should be set at least as high as the maximum number of GKE nodes you anticipate creating in `us-central2`.



## Missing subnet during GKE cluster creation

If you are attempting to create a cluster in `us-central2` (the only region where TPU v4 is available), then you might encounter an error message similar to the following:
    
    
    ERROR: (gcloud.container.clusters.create) ResponseError: code=404,
    message=Not found: project <PROJECT> does not have an auto-mode subnetwork
    for network "default" in region <REGION>.
    

A subnet is required in your VPC network to provide connectivity to your GKE nodes. However, in certain regions such as `us-central2`, a default subnet might not be created, even when you use the default VPC network in auto-mode (for subnet creation).

To resolve this issue, ensure that you have [created a custom subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) in the region before creating your GKE cluster. This subnet must not overlap with other subnets created in other regions in the same VPC network.

## Enable the read-only kubelet port

If you use a GKE cluster version that's earlier than 1.32, make sure to check that the [`insecureKubeletReadonlyPortEnabled`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port#disable-standard-node-pools) field is set to `true`.

You can check the value of the `insecureKubeletReadonlyPortEnabled` field by describing your node pool:
    
    
    gcloud container node-pools describe NODEPOOL_NAME --cluster=CLUSTER_NAME
    

If the output includes `insecureKubeletReadonlyPortEnabled: false`, then enable the port by running the following command:
    
    
    gcloud container node-pools update NODEPOOL_NAME --cluster CLUSTER_NAME --enable-insecure-kubelet-readonly-port
    

The following sample errors mention a TCP connection error to port 10255, which indicates that you might need to enable the port.
    
    
    error sending request: Get "http://gke-tpu-d32e5ca6-f4gp:10255/pods": GET http://gke-tpu-d32e5ca6-f4gp:10255/pods giving up after 5 attempt(s): Get "http://gke-tpu-d32e5ca6-f4gp:10255/pods": dial tcp [2600:1901:8130:662:0:19c::]:10255: connect: connection refused
    
    
    
    failed to get TPU container Info: failed to call kubelet: Get "http://gke-tpu-d32e5ca6-f4gp:10255/pods": GET http://gke-tpu-d32e5ca6-f4gp:10255/pods giving up after 5 attempt(s): Get "http://gke-tpu-d32e5ca6-f4gp:10255/pods": dial tcp [2600:1901:8130:662:0:19c::]:10255: connect: connection refused
    

## Connection error when running a training workload with JAX

If you're attempting to initialize the JAX framework to run a training workload on TPU machines, then you might find an error message similar to the following:
    
    
    E0115 19:06:10.727412 340 master.cc:246] Initialization of slice failed with
    error status: INVALID_ARGUMENT: When linking node TPU_ID:pe0:0
    to TPU_ID:pe0:3</code> with link TPU_ID:pe0:0:p5:x couldn't find opposite link in destination node.; Failed to create the mesh (xW, xW, xW); Please make sure the topology is correct.;
    Failed to discover ICI network topology
    

This error occurs when GKE fails to establish the high-speed inter chip interconnects (ICI) network topology across large TPU slices.

To mitigate this issue, complete the following steps:

  1. Identify the TPU slices that experience the connectivity error. To see the event logs, use the following query:
         
         resource.type="k8s_container"
         resource.labels.project_id=PROJECT_ID
         severity>=DEFAULT
         SEARCH("`[/dev/vfio/0` `TPU_ID` Driver `opened.`")
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `TPU_ID`: the ID of the TPU experiencing errors. You can see the TPU ID in the error message.
  2. Taint the node pool or one of the nodes included in the error message. To learn more, see [Taint and label a node pool for your workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#taint-label-node-pool)

  3. Rerun the Job again on another node pool.




If the issue persists, [file a support case](https://cloud.google.com/support-hub) or reach out to your account team.

## View GKE TPU logs

To view all TPU-related logs for a specific workload, Cloud Logging offers a centralized location to query these logs when [GKE system and workload logging are enabled](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/logging#verify_logging_is_enabled_on_the_cluster). In Cloud Logging, logs are organized into log entries, and each individual log entry has a [structured format](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). The following is an example of a TPU training job log entry.
    
    
    {
      insertId: "gvqk7r5qc5hvogif"
      labels: {
      compute.googleapis.com/resource_name: "gke-tpu-9243ec28-wwf5"
      k8s-pod/batch_kubernetes_io/controller-uid: "443a3128-64f3-4f48-a4d3-69199f82b090"
      k8s-pod/batch_kubernetes_io/job-name: "mnist-training-job"
      k8s-pod/controller-uid: "443a3128-64f3-4f48-a4d3-69199f82b090"
      k8s-pod/job-name: "mnist-training-job"
    }
    logName: "projects/gke-tpu-demo-project/logs/stdout"
    receiveTimestamp: "2024-06-26T05:52:39.652122589Z"
    resource: {
      labels: {
        cluster_name: "tpu-test"
        container_name: "tensorflow"
        location: "us-central2-b"
        namespace_name: "default"
        pod_name: "mnist-training-job-l74l8"
        project_id: "gke-tpu-demo-project"
    }
      type: "k8s_container"
    }
    severity: "INFO"
    textPayload: "
      1/938 [..............................] - ETA: 13:36 - loss: 2.3238 - accuracy: 0.0469
      6/938 [..............................] - ETA: 9s - loss: 2.1227 - accuracy: 0.2995
     13/938 [..............................] - ETA: 8s - loss: 1.7952 - accuracy: 0.4760
     20/938 [..............................] - ETA: 7s - loss: 1.5536 - accuracy: 0.5539
     27/938 [..............................] - ETA: 7s - loss: 1.3590 - accuracy: 0.6071
     36/938 [>.............................] - ETA: 6s - loss: 1.1622 - accuracy: 0.6606
     44/938 [>.............................] - ETA: 6s - loss: 1.0395 - accuracy: 0.6935
     51/938 [>.............................] - ETA: 6s - loss: 0.9590 - accuracy: 0.7160
    ……
    937/938 [============================>.] - ETA: 0s - loss: 0.2184 - accuracy: 0.9349"
    timestamp: "2024-06-26T05:52:38.962950115Z"
    }
    

Each log entry from the TPU slice nodes have the label `compute.googleapis.com/resource_name` with the value set as the node name. If you want to view the logs from a particular node and you know the node name, you can filter the logs by that node in your query. For example, the following query shows the logs from the TPU node `gke-tpu-9243ec28-wwf5`:
    
    
    resource.type="k8s_container"
    labels."compute.googleapis.com/resource_name" = "gke-tpu-9243ec28-wwf5"
    

GKE attaches label `cloud.google.com/gke-tpu-accelerator` and `cloud.google.com/gke-tpu-topology` to all nodes containing TPUs. So, if you are not sure about the node name or you want to list all the TPU slice nodes, you can run the following command:
    
    
    kubectl get nodes -l cloud.google.com/gke-tpu-accelerator
    

Sample output:
    
    
    NAME                    STATUS   ROLES    AGE     VERSION
    gke-tpu-9243ec28-f2f1   Ready    <none>   25m     v1.30.1-gke.1156000
    gke-tpu-9243ec28-wwf5   Ready    <none>   7d22h   v1.30.1-gke.1156000
    

You can do additional filtering based on the node labels and their values. For example, the following command lists TPU node with a specific type and topology:
    
    
    kubectl get nodes -l cloud.google.com/gke-tpu-accelerator=tpu-v5-lite-podslice,cloud.google.com/gke-tpu-topology=1x1
    

To view all the logs across the TPU slice nodes, you can use the query that matches the label to the TPU slice node suffix. For example, use the following query:
    
    
    resource.type="k8s_container"
    labels."compute.googleapis.com/resource_name" =~ "gke-tpu-9243ec28.*"
    log_id("stdout")
    

To view the logs associated with a particular TPU workload using a [Kubernetes Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/), you can filter the logs using the `batch.kubernetes.io/job-name` label. For example, for the job `mnist-training-job`, you can run the following query for the **STDOUT** logs:
    
    
    resource.type="k8s_container"
    labels."k8s-pod/batch_kubernetes_io/job-name" = "mnist-training-job"
    log_id("stdout")
    

To view the logs for a TPU workload using a [Kubernetes JobSet](https://jobset.sigs.k8s.io/), you can filter the logs using the `k8s-pod/jobset_sigs_k8s_io/jobset-name` label. For example:
    
    
    resource.type="k8s_container"
    labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"="multislice-job"
    

To drill down further, you can filter based on the other workload labels. For example, to view the logs for a multislice workload from worker **0** and slice **1** , you can filter based on the labels: `job-complete-index` and `job-index`:
    
    
    ​​resource.type="k8s_container"
    labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"="multislice-job"
    labels."k8s-pod/batch_kubernetes_io/job-completion-index"="0"
    labels."k8s-pod/jobset_sigs_k8s_io/job-index"="1"
    

You can also filter using the Pod name pattern:

`resource.labels.pod_name:<jobSetName>-<replicateJobName>-<job-index>-<worker-index>`

For example, in the following query the `jobSetName` is multislice-job, and the `replicateJobName` is slice. Both `job-index` and `worker-index` are **0** :
    
    
    resource.type="k8s_container"
    labels."k8s-pod/jobset_sigs_k8s_io/jobset-name"="multislice-job"
    resource.labels.pod_name:"multislice-job-slice-0-0"
    

Other TPU workloads, such as a single GKE Pod workload, you can filter the logs by Pod names. For example:
    
    
    resource.type="k8s_container"
    resource.labels.pod_name="tpu-job-jax-demo"
    

If you want to check if the TPU device plugin is running correctly, you can use the following query to check its container logs:
    
    
    resource.type="k8s_container"
    labels.k8s-pod/k8s-app="tpu-device-plugin"
    resource.labels.namespace_name="kube-system"
    

Run the following query to check the related events:
    
    
    jsonPayload.involvedObject.name=~"tpu-device-plugin.*"
    log_id("events")
    

For all queries, you can add additional filters, such as cluster name, location, and project ID. You can also combine conditions to narrow down the results. For example:
    
    
    resource.type="k8s_container" AND
    resource.labels.project_id="gke-tpu-demo-project" AND
    resource.labels.location="us-west1" AND
    resource.labels.cluster_name="tpu-demo" AND
    resource.labels.namespace_name="default" AND
    labels."compute.googleapis.com/resource_name" =~ "gke-tpu-9243ec28.*" AND
    labels."k8s-pod/batch_kubernetes_io/job-name" = "mnist-training-job" AND
    log_id("stdout")
    

The `AND` operator is optional between comparisons and it can be omitted. For more information about the query language, you can read the [Logging query language specification](https://docs.cloud.google.com/logging/docs/view/logging-query-language). You can also read [Kubernetes related log queries](https://docs.cloud.google.com/logging/docs/view/query-library#kubernetes-filters) for more query examples.

If you prefer SQL using Observability Analytics, you can find query examples at [SQL query with Observability Analytics](https://github.com/GoogleCloudPlatform/observability-analytics-samples/tree/main/samples/logging/kubernetes). Alternatively, you can also run the queries using the Google Cloud CLI instead of in the Logs Explorer. For example:
    
    
    gcloud logging read 'resource.type="k8s_container" labels."compute.googleapis.com/resource_name" =~ "gke-tpu-9243ec28.*" log_id("stdout")' --limit 10 --format json
    

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
