---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/scalability/
title: Scalability \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:35.427327+00:00
---

# Scalability  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/scalability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Scalability Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices for creating, configuring, and operating clusters created using Google Distributed Cloud (software only) for VMware to accommodate workloads that approach Kubernetes scalability limits.

## Cluster name rules

For each Google Cloud project:

  * Each user cluster must have a unique name across all admin clusters that are within a single Google Cloud project.



## Scalability limits

Take the following limits into account when designing your applications:

  * If [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) isn't enabled:

    * Each admin cluster supports up to 100 user clusters, including both high availability (HA) and non-HA user clusters, using bundled load balancing mode ([MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb)), or ([manual load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance)).

    * Each user cluster supports up to:

      * 500 nodes using bundled load balancing mode ([MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb))

      * 15,000 Pods

      * 500 [LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) Services using bundled load balancing mode ([MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb)).

    * For each node, you can create a maximum of 110 Pods (each Pod can consist of 1-2 containers). This includes Pods running add-on system services.

  * If [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) is enabled

    * Each admin cluster supports up to 100 user clusters, user cluster must be high availability (HA) clusters, using bundled load balancing mode ([MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb)), or ([manual load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance)).

    * Each user cluster supports up to:

      * 500 nodes using bundled load balancing mode ([MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb)).

      * 15,000 Pods

      * 500 [LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) Services using bundled load balancing mode ([MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb)).

    * For each node, you can create a maximum of 110 Pods (each Pod can consist of 1-2 containers). This includes Pods running add-on system services.

    * The total number of nodes which includes admin cluster control plane nodes + all user cluster control plane nodes + worker nodes should not exceed 500 nodes.




## Understanding limits

Since Google Distributed Cloud is a complex system with a large integration surface, cluster scalability involves many interrelated dimensions. For example, Google Distributed Cloud can scale through the number of nodes, Pods, or Services. Stretching more than one dimension at the time can cause problems even in smaller clusters. For example, scheduling 110 Pods per node in a 500 node cluster can overstretch the number of Pods, Pods per node, and nodes.

See [Kubernetes Scalability thresholds](https://github.com/kubernetes/community/blob/master/sig-scalability/configs-and-limits/thresholds.md) for more details.

Scalability limits are also sensitive to the vSphere configuration and hardware your cluster is running on. These limits are verified in an environment that is likely different than yours. Therefore, you might not reproduce the exact numbers when the underlying environment is the limiting factor.

## Preparing to scale

As you prepare to scale your admin clusters or user clusters, consider the following requirements and limitations.

### CPU, memory, and storage requirements

See the [CPU, RAM, and storage requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage) for each individual VM.

### Disk and network I/O requirements

Data-intensive workloads and certain control plane components are sensitive to disk and network I/O latency. For example, 500 sequential IOPS (for example, a typical local SSD or a high performance virtualized block device) is typically needed for etcd's performance and stability in a cluster with dozens of nodes and thousands of Pods.

### Node IP address

Each node requires one DHCP or statically-assigned IP address.

For example, 307 IP addresses are needed in a setup with one non-HA user cluster with 50 nodes and one HA user cluster with 250 nodes.

The following table shows the breakdown of the IP addresses:

Node type | Number of IP addresses  
---|---  
Admin cluster control-plane VMs | 3  
User cluster 1 (non-HA) control-plane VM | 1  
User cluster 1 worker node VMs | 50  
User cluster 2 (HA) control-plane VMs | 3  
User cluster 2 worker node VMs | 250  
**Total** | **307**  
  
## Running many user clusters in an admin cluster

As you prepare to run many user clusters in an admin cluster, perform the following steps when creating the admin cluster.

### Pod CIDR block in the admin cluster

The Pod CIDR block is the CIDR block for all Pods in an admin cluster. It is configured via the `network.podCIDR` field in the `admin-cluster.yaml`.

From this range, smaller /24 blocks are assigned to each node. If all of your your user clusters have [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/scalability/) enabled, then your admin cluster has only three nodes, and there are plenty of Pod IP addresses available. However, each time you create a user cluster that uses [kubeception](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/scalability/) instead of Controlplane V2, one or three nodes are added to the admin cluster:

  * Each high availability (HA) kubeception user cluster adds three nodes to the admin cluster.

  * Each non-HA kubeception user cluster adds one node to the admin cluster.




If you need an N node admin cluster, you must ensure the Pod CIDR block is large enough to support N /24 blocks.

The following table describes the maximum number of nodes supported by different Pod CIDR block sizes:

Pod CIDR block size | Max number of nodes supported  
---|---  
/18 | 64  
/17 | 128  
/16 | 256  
/15 | 512  
  
The default Pod CIDR block of an admin cluster is 192.168.0.0/16, which supports 256 nodes.

In an admin cluster with 100 HA kubeception user clusters, there are 3 admin cluster control-plane nodes and 300 user cluster control-plane nodes. The total number of nodes is 303 (more than 256). Therefore, you must update the Pod CIDR block to /15 to support up to 100 HA kubeception user clusters.

To configure the Pod CIDR block, set the `network.podCIDR` field in the admin cluster configuration file.

### Service CIDR block in the admin cluster

The Service CIDR block is the CIDR block for all Services in an admin cluster. It is configured via the `network.serviceCIDR` field in the `admin-cluster.yaml`.

The following table describes the maximum number of Services supported by different Service CIDR block sizes:

Service CIDR block size | Max number of Services supported  
---|---  
/24 | 256  
/23 | 512  
/22 | 1,024  
  
The default value is 10.96.232.0/24, which supports 256 services.

Each kubeception user cluster uses 6 Services, and the admin cluster control plane uses 14 Services. Therefore, in order to run 100 kubeception user clusters, you must change the Service CIDR block in the admin cluster to use a /22 range.

### Cloud Logging and Cloud Monitoring for kubeception user clusters

[Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) help you track your resources.

The CPU and memory usage of the logging and monitoring components deployed in an admin cluster scale according to the number of kubeception user clusters.

The following table describes the amount of admin cluster node CPU and memory required to run a large number of kubeception user clusters:

Number of kubeception user clusters | Admin cluster node CPU | Admin cluster node memory  
---|---|---  
0 to 10 | 4 CPUs | 16GB  
11 to 20 | 4 CPUs | 32GB  
20 to 100 | 4 CPUs | 90GB  
  
For example, if there are 2 admin cluster nodes and each has 4 CPUs and 16GB memory, you can run 0 to 10 kubeception user clusters. To create more than 20 kubeception user clusters, you must first resize the admin cluster node memory from 16GB to 90GB.

### Admin cluster nodes when advanced clusters is enabled

The CPU and memory usage of the lifecycle components deployed in an admin cluster scale according to the number of total numbers of all nodes (The total number of nodes which includes admin cluster control plane nodes + all user cluster control plane nodes + worker nodes)

The following table describes the amount of admin cluster node CPU and memory required to run a large number of all nodes it manages:

Number of total nodes | Admin cluster node CPU | Admin cluster node memory  
---|---|---  
0 to 20 | 4 CPUs | 16GB  
21 to 100 | 8 CPUs | 16GB  
101 to 500 | 16 CPUs | 32GB  
  
For example, if there are 3 admin cluster nodes and each has 4 CPUs and 16GB memory, you can run one HA user cluster with 14 worker nodes. To create more than 20 advanced user clusters, each user cluster has more than 10 nodes, you must first resize the admin cluster node memory from 16GB to 32GB.

### GKE Hub

By default, you can register a maximum of 250 clusters with global memberships per fleet. To register more clusters in GKE Hub, you can submit a request to increase your quota in the Google Cloud console:

[Go to Quotas](https://console.cloud.google.com/apis/api/gkehub.googleapis.com/quotas)

For more information about cluster quotas based on membership settings, see [Allocation quotas](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/quotas#allocation_quotas).

## Running many nodes and pods in a user cluster

As you prepare to run many nodes and pods in a user cluster, perform the following steps when creating the user cluster.

### Pod CIDR block in the user cluster

The Pod CIDR block is the CIDR block for all Pods in a user cluster. It is configured via the `network.podCIDR` field in the `user-cluster.yaml`.

From this range, a smaller /24 block is assigned to each node. If you need an N nodes cluster, you must ensure this block is large enough to support N /24 blocks.

The following table describes the maximum number of nodes supported by different Pod CIDR block sizes:

Pod CIDR block size | Max number of nodes supported  
---|---  
/18 | 64  
/17 | 128  
/16 | 256  
/15 | 512  
  
The default Pod CIDR block is 192.168.0.0/16, which supports 256 nodes. For example, to create a cluster with 500 nodes, you must change the Pod CIDR block in the user cluster to use a /15 range.

### Service CIDR block in the user cluster

The Service CIDR block is the CIDR block for all Services in a user cluster. It is configured via the `network.serviceCIDR` field in the `user-cluster.yaml`.

The following table describes the maximum number of Services supported by different Service CIDR block sizes:

Service CIDR block size | Max number of Services supported  
---|---  
/21 | 2,048  
/20 | 4,096  
/19 | 8,192  
/18 | 16,384  
  
### User cluster control plane nodes

The memory usage of the user cluster control-plane components scales according to the number of nodes in the user cluster.

The following table gives the CPU and memory required by a user cluster control-plane node depending on the size of the user cluster:

Number of user cluster nodes | Control-plane node CPU | Control-plane node memory  
---|---|---  
0 to 20 | 3 CPUs | 5GB  
21 to 75 | 3 CPUs | 6GB  
76 to 250 | 4 CPUs | 8GB  
251 to 500 | 4 CPUs | 16GB  
  
For example, to create more than 250 nodes in a user cluster, you must use user cluster control plane nodes with at least 16GB of memory.

The user cluster control plane node spec can be changed via the `masterNode` field in the `user-cluster.yaml`.

#### Dataplane v2

For 500-node user clusters using Dataplane V2, we recommend 120 GB of memory and 32 CPU cores for the user cluster control plane nodes.

### Cloud Logging and Cloud Monitoring

[Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) help you track your resources.

The CPU and memory usage of the in-cluster agents deployed in a user cluster scale in terms of the number of nodes and Pods in a user cluster.

Cloud logging and monitoring components such as `prometheus-server` and `stackdriver-prometheus-sidecar` have different CPU and memory resource usage based on the number of nodes and the number of Pods. Before you scale up your cluster, [set the resources request and limit](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring) according to the estimated average usage of these components. The following table shows estimates for the average amount of usage for each component:

Number of nodes | Container name | Estimated CPU usage | Estimated memory usage  
---|---|---|---  
0 pods/node | 30 pods/node | 0 pods/node | 30 pods/node  
3 to 50 | prometheus-server | 100m | 390m | 650M | 1.3G  
stackdriver-prometheus-sidecar | 100m | 340m | 1.5G | 1.6G  
51 to 100 | prometheus-server | 160m | 500m | 1.8G | 5.5G  
stackdriver-prometheus-sidecar | 200m | 500m | 1.9G | 5.7G  
101 to 250 | prometheus-server | 400m | 2500m | 6.5G | 16G  
stackdriver-prometheus-sidecar | 400m | 1300m | 7.5G | 12G  
250 to 500 | prometheus-server | 1200m | 2600m | 22G | 25G  
stackdriver-prometheus-sidecar | 400m | 2250m | 65G | 78G  
  
Make sure you have nodes big enough to schedule the Cloud Logging and Cloud Monitoring components. One way to do this is to create a small cluster first, edit the Cloud Logging and Cloud Monitoring component resources according to the table above, [create a node pool](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/managing-node-pools) to accommodate the components, and then gradually scale up the cluster to a larger size.

You can choose to maintain a node pool just big enough for the monitoring and logging components to prevent other pods from being scheduled to the node pool. To do this, you must add the following [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to the node pool:
    
    
    taints:
      - effect: NoSchedule
        key: node-role.gke.io/observability

This prevents other components from being scheduled on the node pool and prevents user workloads from being evicted due to the monitoring components' resource consumption.

### Load Balancer

The Services discussed in this section refer to the Kubernetes Services with type LoadBalancer.

There is a limit on the number of nodes in your cluster, and on the number of Services that you can configure on your load balancer.

For bundled load balancing (Seesaw), there is also a limit on the number of health checks. The number of health checks depends on the number of nodes and the number of traffic local Services. A traffic local Service is a Service that has its externalTrafficPolicy set to `Local`.

The following table describes the maximum number of Services, nodes, and health checks for Bundled load balancing (Seesaw) and Integrated load balancing (F5):

| Bundled load balancing (Seesaw) | Integrated load balancing (F5)  
---|---|---  
Max Services | 500 | 250 2  
Max nodes | 500 | 250 2  
Max health checks | N + (L * N) <= 10K, where N is the number of nodes, and L is the number of traffic local services 1 | N/A 2  
  
1 For example, suppose you have 100 nodes and 99 traffic local Services. The number of health checks is 100 + (99 * 100) = 10,000, which is within the 10K limit.

2 Consult F5 for more information. This number is affected by factors such as your F5 hardware model number, virtual instance CPU/memory, and licenses.

## Auto-scaling system components

Google Distributed Cloud automatically scales the system components in user clusters according to the number of nodes without any need for you to change configurations. You can use the information in this section for resource planning.

**Warning:** The exact formulas are subject to change in a future Google Distributed Cloud release to accommodate changes in system component resource usage.

  * Google Distributed Cloud automatically performs vertical scaling by scaling the CPU and memory requests/limits of the following system components using [addon-resizer](https://github.com/kubernetes/autoscaler/tree/master/addon-resizer):

    * [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) is a Deployment running on cluster worker nodes that listens to the Kubernetes API server and generates metrics about the state of the objects. The CPU and memory request and limits scale based on the number of nodes.

The following table describes the resource requests/limits set by the system, given the number of nodes in a cluster:

Number of nodes | Approximate1 CPU request/limit (milli) | Approximate1 memory request/limit (Mi)  
---|---|---  
3 to 5 | 105 | 110  
6 to 500 | 100 + num_nodes | 100 + (2 * num_nodes)  
  
1 There is a margin of +-5% to reduce the number of component restarts during scaling.

For example, in a cluster with 50 nodes, the CPU request/limit are set to 150m/150m and the memory request/limit are set to 200Mi/200Mi. In a cluster with 250 nodes, the CPU request/limit are set to 350m/350m and the memory request/limit are set to 600Mi.

    * [metrics-server](https://github.com/kubernetes-sigs/metrics-server) is a deployment running on cluster worker nodes that is used by Kubernetes built-in autoscaling pipelines. The CPU and memory request and limits scale based on the number of nodes.

  * Google Distributed Cloud automatically performs horizontal scaling in both admin clusters and user clusters by scaling the number of replicas of the following system components:

    * [core-dns](https://github.com/coredns/coredns) is the DNS solution used for service discovery. It runs as a Deployment on user cluster worker nodes. Google Distributed Cloud automatically scales the number of replicas according to the number of nodes and CPU cores in the cluster. With each addition/deletion of 16 nodes or 256 cores, 1 replica is increased/decreased. If you have a cluster of `N` nodes and `C` cores, you can expect `max(N/16, C/256)` replicas.

    * [calico-typha](https://docs.projectcalico.org/reference/typha/overview) is a component for supporting Pod networking. It runs as a Deployment on user cluster worker nodes. Google Distributed Cloud automatically scales the number of calico-typha replicas based on the number of nodes in the cluster:

Number of nodes (N) | Number of calico-typha replicas  
---|---  
N = 1 | 1  
1 < N < 200 | 2  
N >= 200 | 3 or more  
    * [Istio ingress-gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/) is the component for supporting cluster ingress, and it runs as a Deployment on user cluster worker nodes. Depending on the amount of traffic ingress-gateway is handling, Google Distributed Cloud uses [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) to scale the number of replicas based on their CPU usage, with a minimum of 2 replicas and maximum of 5 replicas.

    * [konnectivity](https://github.com/kubernetes-sigs/apiserver-network-proxy) network proxy (KNP) provides a TCP-level proxy for egress from user cluster control-plane nodes. It tunnels user kube-apiserver egressing traffic that is destined to the user cluster nodes. Konnectivity agent runs as a Deployment on user cluster worker nodes. Google Distributed Cloud automatically scales the number of konnectivity agent replicas based on the number of nodes in the cluster.

Number of nodes (N) | Number of konnectivity agent replicas  
---|---  
1 <= N <= 6 | N  
6 < N < 10 | 6  
10 <= N < 100 | 8  
N >= 100 | 12 or more  



## Best practices

This section describes best practices for scaling your resources.

### Scale your cluster in stages

The creation of a Kubernetes node involves cloning the node OS image template into a new disk file, which is an I/O-intensive vSphere operation. There is no I/O isolation between the clone operation and workload I/O operations. If there are too many nodes being created at the same time, the clone operations take a long time to finish and may affect the performance and stability of the cluster and existing workloads.

Ensure that the cluster is scaled in stages depending on your vSphere resources. For example, to resize a cluster from 3 to 500 nodes, consider scaling it in stages from to 150 to 350 to 500, which helps reduce the load on vSphere infrastructure.

### Optimize etcd disk I/O performance

etcd is a key value store used as Kubernetes' backing store for all cluster data. Its performance and stability are critical to a cluster's health and are sensitive to disk and network I/O latency.

  * Optimize the I/O performance of the vSphere datastore used for the control-plane VMs by following these recommendations:

    * Follow the [etcd hardware requirements](https://etcd.io/docs/v3.4.0/op-guide/hardware/#disks).
    * Use SSD or all flash storage.
  * Latency of a few hundreds of milliseconds indicates a bottleneck on the disk or network I/O and may result in an unhealthy cluster. Monitor and set alert thresholds for the following etcd I/O latency metrics:

    * `etcd_disk_backend_commit_duration_seconds`
    * `etcd_disk_wal_fsync_duration_seconds`



### Optimize node boot disk I/O performance

Pods use ephemeral storage for their internal operations, like saving temporary files. Ephemeral storage is consumed by the container's writable layer, logs directory, and emptyDir volumes. Ephemeral storage comes from the node's file system, which is backed by the boot disk of the node.

As there is no storage I/O isolation on Kubernetes nodes, applications that consume extremely high I/O on their ephemeral storage can potentially cause node instability by starving system components like Kubelet and the docker daemon of resources.

Ensure that the I/O performance characteristics of the datastore on which the boot disks are provisioned can provide the right performance for the application's use of ephemeral storage and logging traffic.

### Monitor physical resource contention

Be aware of [vCPU to pCPU ratios](https://blogs.vmware.com/vsphere/2015/11/vcpu-to-pcpu-ratios-are-they-still-relevant.html) and [memory overcommitment](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html). A suboptimal ratio or memory contention at the physical hosts may cause VM performance degradation. You should monitor the physical resource utilization at host level and allocate enough resources to run your large clusters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
